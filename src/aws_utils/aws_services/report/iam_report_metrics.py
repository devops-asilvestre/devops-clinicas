# aws_utils/aws_services/report/iam_report_metrics.py
"""
Script para analisar o arquivo de log (logs/app.log) e gerar métricas
de duração média das operações IAM.
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
                if "listagem de roles" in line:
                    op = "list_roles"
                elif "criada" in line and "role" in line:
                    op = "create_role"
                elif "excluída" in line and "role" in line:
                    op = "delete_role"
                elif "listagem de usuários" in line:
                    op = "list_users"
                elif "usuário criado" in line:
                    op = "create_user"
                elif "usuário excluído" in line:
                    op = "delete_user"
                elif "policy anexada" in line:
                    op = "attach_policy"
                else:
                    op = "outros"

                duration = float(match.group(1))
                metrics[op].append(duration)

    return metrics

def generate_report(metrics: dict):
    print("=== Relatório de Métricas IAM ===")
    for op, durations in metrics.items():
        avg = sum(durations) / len(durations) if durations else 0
        print(f"{op}: {len(durations)} execuções, média {avg:.2f}s")

if __name__ == "__main__":
    metrics = parse_log(LOG_FILE)
    generate_report(metrics)
