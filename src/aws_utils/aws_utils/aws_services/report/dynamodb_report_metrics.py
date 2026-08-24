# aws_utils/aws_services/report/dynamodb_report_metrics.py
"""
Script para analisar o arquivo de log (logs/app.log) e gerar métricas
de duração média das operações DynamoDB.
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
                if "listagem de tabelas" in line:
                    op = "list_tables"
                elif "tabela criada" in line:
                    op = "create_table"
                elif "tabela excluída" in line:
                    op = "delete_table"
                elif "item inserido" in line:
                    op = "put_item"
                elif "item recuperado" in line:
                    op = "get_item"
                elif "item atualizado" in line:
                    op = "update_item"
                elif "item excluído" in line:
                    op = "delete_item"
                elif "query executada" in line:
                    op = "query_items"
                else:
                    op = "outros"

                duration = float(match.group(1))
                metrics[op].append(duration)

    return metrics

def generate_report(metrics: dict):
    print("=== Relatório de Métricas DynamoDB ===")
    for op, durations in metrics.items():
        avg = sum(durations) / len(durations) if durations else 0
        print(f"{op}: {len(durations)} execuções, média {avg:.2f}s")

if __name__ == "__main__":
    metrics = parse_log(LOG_FILE)
    generate_report(metrics)
