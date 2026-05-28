# Simulador de Loja de Roupas AM Imports

Projeto em Python para simular uma loja de roupas chamada AM Imports.

## Funcionalidades

- Menu principal
- Catálogo de produtos
- Busca de produtos
- Cadastro de clientes
- Carrinho de compras
- Controle de estoque
- Cupons e descontos automáticos
- Pagamento e checkout
- Recibo da compra
- Relatório de vendas
- Produtos com estoque baixo
- Efeito de digitação no terminal
- Limpeza de tela entre as opções do sistema

## Arquivos do projeto

```text
am-imports-simulador/
├── main.py
├── produtos.py
├── clientes.py
├── carrinho.py
├── estoque.py
├── descontos.py
├── pagamento.py
├── relatorios.py
├── utils.py
├── README.md
└── .gitignore
```

## Como executar

No terminal, entre na pasta do projeto e rode:

```bash
python main.py
```

## Modo rápido

Se quiser executar sem o efeito de digitação, use:

Windows PowerShell:

```bash
$env:AM_FAST_MODE="1"; python main.py
```

Linux/macOS:

```bash
AM_FAST_MODE=1 python main.py
```

## Branches sugeridas para o grupo

- feature/menu-principal
- feature/catalogo-produtos
- feature/cadastro-clientes
- feature/carrinho-compras
- feature/controle-estoque
- feature/descontos-promocoes
- feature/pagamento-checkout
- feature/relatorios-vendas
- feature/utils-validacoes

## Organização do grupo

Cada integrante deve trabalhar na sua própria branch, fazer commit, enviar para o GitHub e abrir Pull Request para a branch main.
