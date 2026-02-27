import json
from movie_tree.binary_movie_tree import MovieBinaryTree
from colorama import Fore, Style, init

def main():
    init(autoreset=True)

    tree = MovieBinaryTree()
    
    try:
        with open("database/movies.json", "r") as file:
            data = json.load(file)
            for movie_data in data["movies"]:
                tree.add_movie(movie_data["title"], movie_data["genre"], movie_data["rating"], movie_data["year"])
    except FileNotFoundError:
        print(f"{Fore.RED}Arquivo 'movies.json' não encontrado.")

    while True:
        print(f"\n{Fore.YELLOW}Selecione uma operação:\n")
        print(f"{Fore.CYAN}1. Pesquisar filmes por gênero")
        print(f"{Fore.CYAN}2. Pesquisar filmes por título")
        print(f"{Fore.CYAN}3. Pesquisar filmes por classificação")
        print(f"{Fore.CYAN}4. Adicionar filme")
        print(f"{Fore.CYAN}5. Remover filme")
        print(f"{Fore.CYAN}6. Recomendar filmes")
        print(f"{Fore.RED}0. Sair")

        choice = input(f"\n{Fore.GREEN}Escolha uma opção: ")

        if choice == "1":
            genre = input("Digite o gênero que deseja pesquisar: ")
            movies = tree.search_movies(tree.root, "genre", genre)
            if movies:
                print(f"\n{Fore.YELLOW}Filmes encontrados:\n")
                for movie in movies:
                    print(f"{Fore.GREEN}{movie.title} - {movie.genre} - {movie.rating} - {movie.year}")
            else:
                print(f"{Fore.RED}Nenhum filme encontrado para este gênero.")

        elif choice == "2":
            title = input("Digite o título do filme que deseja pesquisar: ")
            title_cased = title.title()
            
            movies = tree.search_movies(tree.root, "title", title_cased)
            if movies:
                print(f"\n{Fore.YELLOW}Filme encontrado:\n")
                for movie in movies:
                    print(f"{Fore.GREEN}{movie.title} - {movie.genre} - {movie.rating} - {movie.year}")
            else:
                print(f"{Fore.RED}Filme não encontrado.")

        elif choice == "3":
            rating = float(input("Digite a classificação mínima desejada: "))
            movies = tree.search_movies(tree.root, "rating", rating)
            if movies:
                print(f"\n{Fore.YELLOW}Filmes recomendados:\n")
                for movie in movies:
                    print(f"{Fore.GREEN}{movie.title} - {movie.genre} - {movie.rating} - {movie.year}")
            else:
                print(f"{Fore.RED}Nenhum filme recomendado encontrado para os critérios fornecidos.")
        
        elif choice == "4":
            title = input("Digite o título do filme: ")
            genre = input("Digite o gênero do filme: ")
            rating = float(input("Digite a classificação do filme: "))
            year = int(input("Digite o ano de lançamento do filme: "))
            tree.add_movie(title, genre, rating, year)
            print(f"{Fore.GREEN}Filme adicionado com sucesso!")

        elif choice == "5":
            title = input("Digite o título do filme que deseja remover: ")
            movies = tree.search_movies(tree.root, "title", title)
            if movies:
                tree.remove_movie(tree.root, "title", title)
                print(f"{Fore.GREEN}Filme removido com sucesso!")
            else:
                print(f"{Fore.RED}Filme não encontrado.")

        elif choice == "6":
            rating = float(input("Digite a classificação mínima desejada para a recomendação: "))
            genre = input("Digite o gênero para filtrar (ou deixe em branco para não filtrar por gênero): ")
            start_year = input("Digite o ano inicial para filtrar (ou deixe em branco para não filtrar por ano): ")
            end_year = input("Digite o ano final para filtrar (ou deixe em branco para não filtrar por ano): ")
            start_year = int(start_year) if start_year else None
            end_year = int(end_year) if end_year else None

            movies = tree.recommend_movies(tree.root, genre, rating, start_year, end_year)

            if movies:
                print(f"\n{Fore.YELLOW}Filmes recomendados:\n")
                for movie in movies:
                    print(f"{Fore.GREEN}{movie}")
            else:
                print(f"{Fore.RED}Nenhum filme recomendado encontrado para os critérios fornecidos.")

        elif choice == "0":
            print(f"{Fore.CYAN}Saindo...")
            break

        else:
            print(f"{Fore.RED}Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()