from utils import title, divider


def available_quantity(product, cart=None):
    cart = cart or []
    reserved = sum(item["quantity"] for item in cart if item["code"] == product["code"])
    return product["stock"] - reserved


def has_stock(product, quantity, cart=None):
    return available_quantity(product, cart) >= quantity


def decrease_stock(product, quantity):
    if product["stock"] >= quantity:
        product["stock"] -= quantity
        return True
    return False


def low_stock_report(products, limit=5):
    title("PRODUTOS COM ESTOQUE BAIXO")
    low_stock = [product for product in products if product["stock"] <= limit]
    if not low_stock:
        print("Nenhum produto com estoque baixo.")
        return
    print(f"{'Código':<8} {'Produto':<30} {'Estoque':<8}")
    divider()
    for product in low_stock:
        print(f"{product['code']:<8} {product['name']:<30} {product['stock']:<8}")
