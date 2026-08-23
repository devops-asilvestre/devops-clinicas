# aws_utils/aws_services/report/cloudformation_report_metrics.py
"""
Script para analisar o arquivo de log (logs/app.log) e gerar métricas
de duração média das operações CloudFormation.
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
                if "listagem de stacks" in line:
                    op = "list_stacks"
                elif "stack criada" in line:
                    op = "create_stack"
                elif "stack atualizada" in line:
                    op = "update_stack"
                elif "stack excluída" in line:
                    op = "delete_stack"
                elif "descrição da stack" in line:
                    op = "describe_stack"
                else:
                    op = "outros"
                metrics[op].append(float(match.group(1)))
    return metrics

def generate_report(metrics: dict):
    print("=== Relatório de Métricas CloudFormation ===")
    for op, durations in metrics.items():
        avg = sum(durations)/len(durations) if durations else 0
        print(f"{op}: {len(durations)} execuções, média {avg:.2f}s")

if __name__ == "__main__":
    metrics = parse_log(LOG_FILE)
    generate_report(metrics)
