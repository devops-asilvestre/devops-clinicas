# aws_utils/aws_services/report/sns_report_metrics.py
"""
Script para analisar o arquivo de log (logs/app.log) e gerar métricas
de duração média das operações SNS.
"""

import re
from collections import defaultdict

LOG_FILE = "logs/app.log"

def parse_log(file_path: str):
    metrics = defaultdict(list)
    pattern = re.compile(r"em ([0-9]+\.[0-9]+)s")
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            match = pattern.search(line)
            if match:
                if "listagem de tópicos" in line:
                    op = "list_topics"
                elif "tópico criado" in line:
                    op = "create_topic"
                elif "tópico excluído" in line:
                    op = "delete_topic"
                elif "mensagem publicada" in line:
                    op = "publish_message"
                elif "assinatura criada" in line:
                    op = "subscribe"
                elif "assinatura removida" in line:
                    op = "unsubscribe"
                else:
                    op = "outros"
                metrics[op].append(float(match.group(1)))
    return metrics

def generate_report(metrics: dict):
    print("=== Relatório de Métricas SNS ===")
    for op, durations in metrics.items():
        avg = sum(durations)/len(durations) if durations else 0
        print(f"{op}: {len(durations)} execuções, média {avg:.2f}s")

if __name__ == "__main__":
    metrics = parse_log(LOG_FILE)
    generate_report(metrics)
