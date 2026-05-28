from utils import ask_non_empty, title, divider

CUSTOMERS = []


def register_customer():
    title("CADASTRO DE CLIENTE")
    name = ask_non_empty("Nome: ")
    phone = ask_non_empty("Telefone: ")
    email = input("E-mail: ").strip()
    customer = {
        "id": len(CUSTOMERS) + 1,
        "name": name,
        "phone": phone,
        "email": email,
    }
    CUSTOMERS.append(customer)
    print(f"Cliente {name} cadastrado com sucesso.")
    return customer


def list_customers():
    title("CLIENTES CADASTRADOS")
    if not CUSTOMERS:
        print("Nenhum cliente cadastrado.")
        return
    print(f"{'ID':<5} {'Nome':<25} {'Telefone':<18} {'E-mail'}")
    divider()
    for customer in CUSTOMERS:
        print(f"{customer['id']:<5} {customer['name']:<25} {customer['phone']:<18} {customer['email']}")


def find_customer(customer_id):
    for customer in CUSTOMERS:
        if customer["id"] == customer_id:
            return customer
    return None
