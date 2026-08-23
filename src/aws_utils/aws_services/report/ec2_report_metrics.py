# aws_utils/aws_services/report/ec2_report_metrics.py
"""
Script para analisar o arquivo de log (logs/app.log) e gerar métricas
de duração média das operações EC2.
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
                if "listagem de instâncias EC2" in line:
                    op = "list_instances"
                elif "instância EC2 criada" in line:
                    op = "create_instance"
                elif "instância iniciada" in line:
                    op = "start_instance"
                elif "instância parada" in line:
                    op = "stop_instance"
                elif "instância terminada" in line:
                    op = "terminate_instance"
                elif "descrição da instância" in line:
                    op = "describe_instance"
                else:
                    op = "outros"

                metrics[op].append(float(match.group(1)))
    return metrics

def generate_report(metrics: dict):
    print("=== Relatório de Métricas EC2 ===")
    for op, durations in metrics.items():
        avg = sum(durations)/len(durations) if durations else 0
        print(f"{op}: {len(durations)} execuções, média {avg:.2f}s")

if __name__ == "__main__":
    metrics = parse_log(LOG_FILE)
    generate_report(metrics)
