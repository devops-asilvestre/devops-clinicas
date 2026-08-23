# aws_utils/aws_services/s3_report_metrics.py
"""
Script para analisar o arquivo de log (logs/app.log) e gerar métricas
de duração média das operações S3.
"""

import re
from collections import defaultdict

LOG_FILE = "logs/app.log"

def parse_log(file_path: str):
    metrics = defaultdict(list)

    # Regex para capturar mensagens de fim com duração
    pattern = re.compile(r"em ([0-9]+\.[0-9]+)s")

    # Abrir com fallback de encoding
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            match = pattern.search(line)
            if match:
                # Identificar operação pelo texto
                if "listagem de buckets" in line:
                    op = "list_buckets"
                elif "criado" in line and "Bucket" in line:
                    op = "create_bucket"
                elif "Upload" in line:
                    op = "upload_file"
                elif "Download" in line:
                    op = "download_file"
                elif "Objeto" in line and "excluído" in line:
                    op = "delete_file"
                elif "Bucket" in line and "excluído" in line:
                    op = "delete_bucket"
                else:
                    op = "outros"

                # Captura duração
                duration = float(match.group(1))
                metrics[op].append(duration)

    return metrics

def generate_report(metrics: dict):
    print("=== Relatório de Métricas S3 ===")
    for op, durations in metrics.items():
        avg = sum(durations) / len(durations) if durations else 0
        print(f"{op}: {len(durations)} execuções, média {avg:.2f}s")

if __name__ == "__main__":
    metrics = parse_log(LOG_FILE)
    generate_report(metrics)
