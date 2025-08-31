livro1 = "O Senhor dos Anéis"
livro2 = "Harry Potter"
livro3 = "1984"

livros_disponiveis = [livro1, livro2, livro3]
livros_emprestados = []

informacoes_livros = {
    livro1: {"autor": "J.R.R. Tolkien", "ano": 1954},
    livro2: {"autor": "J.K. Rowling", "ano": 1997},
    livro3: {"autor": "George Orwell", "ano": 1949}
}

def mostrar_livros_disponiveis():
    print("📚 Livros disponíveis:")
    for livro in livros_disponiveis:
        print(f"- {livro}")

def emprestar_livro(nome_livro):
    if nome_livro in livros_disponiveis:
        livros_disponiveis.remove(nome_livro)
        livros_emprestados.append(nome_livro)
        print(f"✅ '{nome_livro}' foi emprestado com sucesso!")
        return True
    else:
        print(f"❌ '{nome_livro}' não está disponível para empréstimo")
        return False

def informacoes_completas(livro):
    if livro in informacoes_livros:
        info = informacoes_livros[livro]
        return f"Autor: {info['autor']}, Ano: {info['ano']}"
    else:
        return "Livro não encontrado no sistema"

def adicionar_livro(nome, autor="Desconhecido", ano=2000):
    livros_disponiveis.append(nome)
    informacoes_livros[nome] = {"autor": autor, "ano": ano}
    print(f"📖 '{nome}' foi adicionado ao sistema!")

def main():
    print("=== SISTEMA DE BIBLIOTECA ===")
    mostrar_livros_disponiveis()
    print()
    emprestar_livro("Harry Potter")
    print()
    mostrar_livros_disponiveis()
    print(f"Livros emprestados: {livros_emprestados}")
    print()
    info = informacoes_completas("1984")
    print(f"Informações sobre '1984': {info}")
    print()
    adicionar_livro("Dom Casmurro", "Machado de Assis", 1899)
    print()
    mostrar_livros_disponiveis()

if __name__ == "__main__":
    main()
