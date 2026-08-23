# aws_utils/aws_services/report/stepfunctions_report_metrics.py
"""
Script para analisar o arquivo de log (logs/app.log) e gerar métricas
de duração média das operações Step Functions.
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
                if "listagem de state machines" in line:
                    op = "list_state_machines"
                elif "state machine criada" in line:
                    op = "create_state_machine"
                elif "state machine excluída" in line:
                    op = "delete_state_machine"
                elif "execução iniciada" in line:
                    op = "start_execution"
                elif "execução descrita" in line:
                    op = "describe_execution"
                elif "listagem de execuções" in line:
                    op = "list_executions"
                else:
                    op = "outros"

                metrics[op].append(float(match.group(1)))
    return metrics

def generate_report(metrics: dict):
    print("=== Relatório de Métricas Step Functions ===")
    for op, durations in metrics.items():
        avg = sum(durations)/len(durations) if durations else 0
        print(f"{op}: {len(durations)} execuções, média {avg:.2f}s")

if __name__ == "__main__":
    metrics = parse_log(LOG_FILE)
    generate_report(metrics)
