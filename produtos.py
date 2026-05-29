from utils import money, title, divider

PRODUCTS = [
    {"code": 101, "name": "Camiseta Oversized AM", "category": "Camisetas", "size": "M", "price": 89.90, "stock": 12},
    {"code": 102, "name": "Camiseta Basic Premium", "category": "Camisetas", "size": "G", "price": 69.90, "stock": 18},
    {"code": 201, "name": "Calça Cargo Importada", "category": "Calças", "size": "42", "price": 179.90, "stock": 8},
    {"code": 202, "name": "Calça Jeans Slim", "category": "Calças", "size": "40", "price": 159.90, "stock": 10},
    {"code": 301, "name": "Vestido Midi Elegance", "category": "Vestidos", "size": "P", "price": 199.90, "stock": 6},
    {"code": 302, "name": "Vestido Casual AM", "category": "Vestidos", "size": "M", "price": 149.90, "stock": 9},
    {"code": 401, "name": "Jaqueta Puffer Importada", "category": "Jaquetas", "size": "G", "price": 289.90, "stock": 5},
    {"code": 501, "name": "Tênis Street White", "category": "Tênis", "size": "39", "price": 249.90, "stock": 7},
    {"code": 601, "name": "Boné AM Imports", "category": "Acessórios", "size": "Único", "price": 59.90, "stock": 15},
]


def list_products(products=None):
    products = products or PRODUCTS
    title("CATÁLOGO AM IMPORTS")
    print(f"{'Código':<8} {'Produto':<28} {'Categoria':<14} {'Tam.':<6} {'Preço':<12} {'Estoque':<8}")
    divider()
    for product in products:
        print(f"{product['code']:<8} {product['name']:<28} {product['category']:<14} {product['size']:<6} {money(product['price']):<12} {product['stock']:<8}")


def find_product(code):
    for product in PRODUCTS:
        if product["code"] == code:
            return product
    return None


def search_products(term):
    term = term.lower().strip()
    return [product for product in PRODUCTS if term in product["name"].lower() or term in product["category"].lower()]
