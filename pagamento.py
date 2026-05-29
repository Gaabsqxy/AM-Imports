from carrinho import show_cart
from estoque import decrease_stock
from utils import money, read_int, read_float, title, divider

PAYMENT_METHODS = {
    1: "Dinheiro",
    2: "Pix",
    3: "Cartão de Débito",
    4: "Cartão de Crédito",
}


def choose_payment():
    title("FORMA DE PAGAMENTO")
    for code, method in PAYMENT_METHODS.items():
        print(f"{code} - {method}")
    option = read_int("Escolha a forma de pagamento: ", 1, 4)
    return PAYMENT_METHODS[option]


def checkout(cart, customer, discount, register_sale):
    if not cart:
        print("Não é possível finalizar compra com carrinho vazio.")
        return False
    subtotal = sum(item["price"] * item["quantity"] for item in cart)
    discount_value = min(discount.get("value", 0.0), subtotal)
    total = subtotal - discount_value
    title("FINALIZAÇÃO DA COMPRA")
    show_cart(cart)
    print(f"Cliente: {customer['name'] if customer else 'Consumidor não identificado'}")
    print(f"Desconto: {money(discount_value)}")
    print(f"Total final: {money(total)}")
    method = choose_payment()
    change = 0.0
    if method == "Dinheiro":
        paid = read_float("Valor recebido: ", total)
        change = paid - total
        print(f"Troco: {money(change)}")
    confirm = input("Confirmar compra? (s/n): ").lower().strip()
    if confirm != "s":
        print("Compra cancelada.")
        return False
    for item in cart:
        decrease_stock(item["product_ref"], item["quantity"])
    sale = {
        "customer": customer["name"] if customer else "Consumidor não identificado",
        "items": [{"code": item["code"], "name": item["name"], "quantity": item["quantity"], "price": item["price"]} for item in cart],
        "subtotal": subtotal,
        "discount": discount_value,
        "total": total,
        "payment": method,
        "change": change,
    }
    register_sale(sale)
    print_receipt(sale)
    cart.clear()
    return True


def print_receipt(sale):
    title("RECIBO AM IMPORTS")
    print(f"Cliente: {sale['customer']}")
    print(f"Pagamento: {sale['payment']}")
    divider()
    for item in sale["items"]:
        total_item = item["price"] * item["quantity"]
        print(f"{item['quantity']}x {item['name']} - {money(total_item)}")
    divider()
    print(f"Subtotal: {money(sale['subtotal'])}")
    print(f"Desconto: {money(sale['discount'])}")
    print(f"Total: {money(sale['total'])}")
    if sale["payment"] == "Dinheiro":
        print(f"Troco: {money(sale['change'])}")
