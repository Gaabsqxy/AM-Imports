from estoque import has_stock, available_quantity
from utils import money, title, divider


def add_item(cart, product, quantity):
    if not has_stock(product, quantity, cart):
        print(f"Estoque insuficiente. Disponível: {available_quantity(product, cart)}")
        return False
    for item in cart:
        if item["code"] == product["code"]:
            item["quantity"] += quantity
            print("Quantidade atualizada no carrinho.")
            return True
    cart.append({
        "code": product["code"],
        "name": product["name"],
        "price": product["price"],
        "quantity": quantity,
        "product_ref": product,
    })
    print("Produto adicionado ao carrinho.")
    return True


def remove_item(cart, code):
    for item in cart:
        if item["code"] == code:
            cart.remove(item)
            print("Produto removido do carrinho.")
            return True
    print("Produto não encontrado no carrinho.")
    return False


def show_cart(cart):
    title("CARRINHO DE COMPRAS")
    if not cart:
        print("Carrinho vazio.")
        return
    print(f"{'Código':<8} {'Produto':<28} {'Qtd.':<6} {'Preço':<12} {'Total':<12}")
    divider()
    for item in cart:
        total = item["price"] * item["quantity"]
        print(f"{item['code']:<8} {item['name']:<28} {item['quantity']:<6} {money(item['price']):<12} {money(total):<12}")
    divider()
    print(f"Subtotal: {money(cart_subtotal(cart))}")


def cart_subtotal(cart):
    return sum(item["price"] * item["quantity"] for item in cart)


def clear_cart(cart):
    cart.clear()
