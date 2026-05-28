from utils import money, title

COUPONS = {
    "AM10": {"type": "percent", "value": 0.10, "description": "10% de desconto"},
    "AM20": {"type": "percent", "value": 0.20, "description": "20% de desconto"},
    "FRETE50": {"type": "fixed", "value": 50.00, "description": "R$ 50,00 de desconto"},
}


def calculate_automatic_discount(subtotal):
    if subtotal >= 500:
        return {"name": "Desconto automático", "value": subtotal * 0.08, "description": "8% em compras acima de R$ 500,00"}
    if subtotal >= 300:
        return {"name": "Desconto automático", "value": subtotal * 0.05, "description": "5% em compras acima de R$ 300,00"}
    return {"name": "Sem desconto", "value": 0.0, "description": "Nenhum desconto automático aplicado"}


def apply_coupon(subtotal, code):
    coupon = COUPONS.get(code.upper().strip())
    if not coupon:
        return {"valid": False, "code": code, "value": 0.0, "description": "Cupom inválido"}
    if coupon["type"] == "percent":
        value = subtotal * coupon["value"]
    else:
        value = min(coupon["value"], subtotal)
    return {"valid": True, "code": code.upper().strip(), "value": value, "description": coupon["description"]}


def show_discount_result(subtotal, discount):
    title("DESCONTO")
    print(f"Subtotal: {money(subtotal)}")
    print(f"Desconto: {money(discount['value'])}")
    print(f"Descrição: {discount['description']}")
    print(f"Total final: {money(max(subtotal - discount['value'], 0))}")
