# aws_utils/aws_services/report/rds_report_metrics.py
"""
Script para analisar o arquivo de log (logs/app.log) e gerar métricas
de duração média das operações RDS.
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
                if "listagem de instâncias RDS" in line:
                    op = "list_instances"
                elif "instância RDS criada" in line:
                    op = "create_instance"
                elif "instância RDS excluída" in line:
                    op = "delete_instance"
                elif "instância RDS iniciada" in line:
                    op = "start_instance"
                elif "instância RDS parada" in line:
                    op = "stop_instance"
                elif "descrição da instância RDS" in line:
                    op = "describe_instance"
                elif "backup da instância RDS" in line:
                    op = "backup_instance"
                else:
                    op = "outros"
                metrics[op].append(float(match.group(1)))
    return metrics

def generate_report(metrics: dict):
    print("=== Relatório de Métricas RDS ===")
    for op, durations in metrics.items():
        avg = sum(durations)/len(durations) if durations else 0
        print(f"{op}: {len(durations)} execuções, média {avg:.2f}s")

if __name__ == "__main__":
    metrics = parse_log(LOG_FILE)
    generate_report(metrics)
