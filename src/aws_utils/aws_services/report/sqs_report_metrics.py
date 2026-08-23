# aws_utils/aws_services/report/sqs_report_metrics.py
"""
Script para analisar o arquivo de log (logs/app.log) e gerar métricas
de duração média das operações SQS.
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
                if "listagem de filas" in line:
                    op = "list_queues"
                elif "fila criada" in line:
                    op = "create_queue"
                elif "fila excluída" in line:
                    op = "delete_queue"
                elif "mensagem enviada" in line:
                    op = "send_message"
                elif "mensagens recebidas" in line:
                    op = "receive_message"
                elif "mensagem excluída" in line:
                    op = "delete_message"
                else:
                    op = "outros"
                metrics[op].append(float(match.group(1)))
    return metrics

def generate_report(metrics: dict):
    print("=== Relatório de Métricas SQS ===")
    for op, durations in metrics.items():
        avg = sum(durations)/len(durations) if durations else 0
        print(f"{op}: {len(durations)} execuções, média {avg:.2f}s")

if __name__ == "__main__":
    metrics = parse_log(LOG_FILE)
    generate_report(metrics)
