"""Teste público e isolado de narração pt-BR para vídeo institucional.
Não recebe nem publica dados de funcionários ou código privado do aplicativo.
"""
import asyncio
import json
import subprocess
from pathlib import Path

import edge_tts

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "saida"
OUT.mkdir(parents=True, exist_ok=True)
TEXTO = (ROOT / "roteiro-publico.txt").read_text(encoding="utf-8").strip()
VOZ = "pt-BR-AntonioNeural"
ARQUIVO = OUT / "mc_segurancas_narracao_ptbr.mp3"


async def gerar():
    # Uma unica locucao continua para evitar emendas e cortes secos.
    comunicacao = edge_tts.Communicate(
        text=TEXTO, voice=VOZ, rate="-8%", pitch="-1Hz", volume="+0%"
    )
    await comunicacao.save(str(ARQUIVO))


def verificar():
    if not ARQUIVO.is_file() or ARQUIVO.stat().st_size < 20000:
        raise RuntimeError("Nao foi gerado um arquivo de voz MP3 valido")
    cmd = [
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(ARQUIVO),
    ]
    duracao = float(subprocess.check_output(cmd, text=True).strip())
    if not 60 <= duracao <= 240:
        raise RuntimeError(f"Duracao da voz inesperada: {duracao:.1f}s")
    info = {
        "voz": VOZ,
        "idioma": "pt-BR",
        "duracao_segundos": round(duracao, 2),
        "tamanho_bytes": ARQUIVO.stat().st_size,
        "roteiro_caracteres": len(TEXTO),
        "gerador": "edge-tts",
        "uso": "video institucional MC Segurancas",
    }
    (OUT / "verificacao.json").write_text(
        json.dumps(info, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(info, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    asyncio.run(gerar())
    verificar()
