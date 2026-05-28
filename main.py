from carrinho import add_item, cart_subtotal, remove_item, show_cart
from clientes import list_customers, register_customer
from descontos import apply_coupon, calculate_automatic_discount, show_discount_result
from estoque import low_stock_report
from pagamento import checkout
from produtos import PRODUCTS, find_product, list_products, search_products
from relatorios import register_sale, show_sales_report
from utils import clear_screen, enable_visual_mode, pause, read_int, title

enable_visual_mode()

cart = []
current_customer = None
current_discount = {"name": "Sem desconto", "value": 0.0, "description": "Nenhum desconto aplicado"}


def show_menu():
    title("AM IMPORTS - SIMULADOR DE LOJA")
    print("Sistema de vendas, estoque e carrinho".center(64))
    print()
    print("1 - Ver catálogo de produtos")
    print("2 - Buscar produto")
    print("3 - Cadastrar cliente")
    print("4 - Listar clientes")
    print("5 - Adicionar produto ao carrinho")
    print("6 - Remover produto do carrinho")
    print("7 - Ver carrinho")
    print("8 - Aplicar desconto")
    print("9 - Finalizar compra")
    print("10 - Relatório de vendas")
    print("11 - Produtos com estoque baixo")
    print("0 - Sair")


def handle_search():
    term = input("Digite nome ou categoria do produto: ")
    results = search_products(term)
    if results:
        list_products(results)
    else:
        print("Nenhum produto encontrado.")


def handle_add_to_cart():
    list_products()
    code = read_int("Código do produto: ")
    product = find_product(code)
    if not product:
        print("Produto não encontrado.")
        return
    quantity = read_int("Quantidade: ", 1)
    add_item(cart, product, quantity)


def handle_discount():
    global current_discount
    subtotal = cart_subtotal(cart)
    if subtotal <= 0:
        print("O carrinho está vazio.")
        return
    print("1 - Desconto automático")
    print("2 - Cupom")
    option = read_int("Escolha: ", 1, 2)
    if option == 1:
        current_discount = calculate_automatic_discount(subtotal)
    else:
        code = input("Digite o cupom: ")
        coupon = apply_coupon(subtotal, code)
        if not coupon["valid"]:
            print(coupon["description"])
            return
        current_discount = coupon
    show_discount_result(subtotal, current_discount)


def run():
    global current_customer, current_discount
    while True:
        clear_screen()
        show_menu()
        option = read_int("Escolha uma opção: ", 0, 11)
        clear_screen()
        if option == 1:
            list_products()
        elif option == 2:
            handle_search()
        elif option == 3:
            current_customer = register_customer()
        elif option == 4:
            list_customers()
        elif option == 5:
            handle_add_to_cart()
        elif option == 6:
            code = read_int("Código do produto para remover: ")
            remove_item(cart, code)
        elif option == 7:
            show_cart(cart)
        elif option == 8:
            handle_discount()
        elif option == 9:
            if checkout(cart, current_customer, current_discount, register_sale):
                current_discount = {"name": "Sem desconto", "value": 0.0, "description": "Nenhum desconto aplicado"}
        elif option == 10:
            show_sales_report()
        elif option == 11:
            low_stock_report(PRODUCTS)
        elif option == 0:
            print("Sistema encerrado. Obrigado por usar a AM Imports.")
            break
        pause()


if __name__ == "__main__":
    run()
