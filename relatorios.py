from collections import Counter
from utils import money, title, divider

SALES = []


def register_sale(sale):
    SALES.append(sale)


def show_sales_report():
    title("RELATÓRIO DE VENDAS")
    if not SALES:
        print("Nenhuma venda registrada.")
        return
    total_sales = sum(sale["total"] for sale in SALES)
    total_discounts = sum(sale["discount"] for sale in SALES)
    print(f"Quantidade de vendas: {len(SALES)}")
    print(f"Total vendido: {money(total_sales)}")
    print(f"Total em descontos: {money(total_discounts)}")
    divider()
    counter = Counter()
    for sale in SALES:
        for item in sale["items"]:
            counter[item["name"]] += item["quantity"]
    print("Produtos mais vendidos:")
    for name, quantity in counter.most_common():
        print(f"{name}: {quantity} unidade(s)")
