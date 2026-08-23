# aws_utils/aws_services/report/lambda_report_metrics.py
"""
Script para analisar o arquivo de log (logs/app.log) e gerar métricas
de duração média das operações Lambda.
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
                if "listagem de funções Lambda" in line:
                    op = "list_functions"
                elif "função Lambda criada" in line:
                    op = "create_function"
                elif "função Lambda atualizada" in line:
                    op = "update_function_code"
                elif "função invocada" in line:
                    op = "invoke_function"
                elif "função excluída" in line:
                    op = "delete_function"
                else:
                    op = "outros"

                metrics[op].append(float(match.group(1)))
    return metrics

def generate_report(metrics: dict):
    print("=== Relatório de Métricas Lambda ===")
    for op, durations in metrics.items():
        avg = sum(durations)/len(durations) if durations else 0
        print(f"{op}: {len(durations)} execuções, média {avg:.2f}s")

if __name__ == "__main__":
    metrics = parse_log(LOG_FILE)
    generate_report(metrics)
