from binary_movie_tree import MovieBinaryTree


def main():
    tree = MovieBinaryTree()
    
    tree.add_movie("The Shawshank Redemption", "Drama", 9.3, 1994)
    tree.add_movie("The Godfather", "Crime", 9.2, 1972)
    tree.add_movie("The Godfather: Part II", "Crime", 9.0, 1974)
    tree.add_movie("The Dark Knight", "Action", 9.0, 2008)
    tree.add_movie("12 Angry Men", "Drama", 8.9, 1957)
    tree.add_movie("Schindler's List", "Biography", 8.9, 1993)
    tree.add_movie("The Lord of the Rings: The Return of the King", "Adventure", 8.9, 2003)
    tree.add_movie("Pulp Fiction", "Crime", 8.9, 1994)
    tree.add_movie("The Lord of the Rings: The Fellowship of the Ring", "Adventure", 8.8, 2001)
    tree.add_movie("Forrest Gump", "Drama", 8.8, 1994)
    tree.add_movie("The Good, the Bad and the Ugly", "Western", 8.8, 1966)
    tree.add_movie("Inception", "Action", 8.7, 2010)
    tree.add_movie("The Lord of the Rings: The Two Towers", "Adventure", 8.7, 2002)
    tree.add_movie("Fight Club", "Drama", 8.7, 1999)
    tree.add_movie("Star Wars: Episode V - The Empire Strikes Back", "Action", 8.7, 1980)
    tree.add_movie("The Matrix", "Action", 8.7, 1999)
    tree.add_movie("Goodfellas", "Biography", 8.7, 1990)
    tree.add_movie("Seven Samurai", "Adventure", 8.6, 1954)
    tree.add_movie("Se7en", "Crime", 8.6, 1995)
    tree.add_movie("City of God", "Crime", 8.6, 2002)
    tree.add_movie("The Silence of the Lambs", "Crime", 8.6, 1991)
    tree.add_movie("It's a Wonderful Life", "Drama", 8.6, 1946)
    tree.add_movie("Life Is Beautiful", "Comedy", 8.6, 1997)
    tree.add_movie("Star Wars: Episode IV - A New Hope", "Action", 8.6, 1977)
    tree.add_movie("Saving Private Ryan", "Drama", 8.5, 1998)
    tree.add_movie("The Green Mile", "Crime", 8.5, 1999)
    tree.add_movie("Interstellar", "Adventure", 8.5, 2014)
    tree.add_movie("Spirited Away", "Animation", 8.5, 2001)
    tree.add_movie("Parasite", "Comedy", 8.5, 2019)
    tree.add_movie("Léon: The Professional", "Crime", 8.5, 1994)
    tree.add_movie("The Usual Suspects", "Crime", 8.5, 1995)
    tree.add_movie("Harakiri", "Action", 8.5, 1962)
    tree.add_movie("The Lion King", "Animation", 8.5, 1994)
    tree.add_movie("The Pianist", "Biography", 8.5, 2002)
    tree.add_movie("Gladiator", "Action", 8.5, 2000)
    tree.add_movie("Back to the Future", "Adventure", 8.5, 1985)
    tree.add_movie("The Departed", "Crime", 8.5, 2006)
    tree.add_movie("Whiplash", "Drama", 8.5, 2014)
    tree.add_movie("The Intouchables", "Biography", 8.5, 2011)
    tree.add_movie("The Prestige", "Drama", 8.5, 2006)
    tree.add_movie("The Lives of Others", "Drama", 8.5, 2006)
    tree.add_movie("Memento", "Mystery", 8.4, 2000)
    tree.add_movie("American History X", "Drama", 8.4, 1998)
    tree.add_movie("The Shining", "Drama", 8.4, 1980)
    tree.add_movie("Apocalypse Now", "Drama", 8.4, 1979)
    tree.add_movie("The Great Dictator", "Comedy", 8.4, 1940)
    tree.add_movie("The Sting", "Comedy", 8.3, 1973)
    tree.add_movie("The Dark Knight Rises", "Action", 8.3, 2012)
    tree.add_movie("Alien", "Horror", 8.4, 1979)
    tree.add_movie("The Bridge on the River Kwai", "Adventure", 8.2, 1957)
    tree.add_movie("Django Unchained", "Drama", 8.4, 2012)
    tree.add_movie("WALL·E", "Animation", 8.4, 2008)
    tree.add_movie("The Lives of Others", "Drama", 8.5, 2006)
    tree.add_movie("The Godfather: Part III", "Crime", 7.6, 1990)
    tree.add_movie("The Social Network", "Biography", 7.7, 2010)
    tree.add_movie("The Martian", "Adventure", 8.0, 2015)
    tree.add_movie("The Big Lebowski", "Comedy", 8.1, 1998)
    tree.add_movie("The Princess Bride", "Adventure", 8.1, 1987)
    tree.add_movie("Scarface", "Crime", 8.3, 1983)
    tree.add_movie("Die Hard", "Action", 8.2, 1988)
    tree.add_movie("A Clockwork Orange", "Crime", 8.3, 1971)
    tree.add_movie("The Truman Show", "Comedy", 8.1, 1998)
    tree.add_movie("Jurassic Park", "Adventure", 8.1, 1993)
    tree.add_movie("The Sixth Sense", "Drama", 8.1, 1999)
    tree.add_movie("Prisoners", "Crime", 8.1, 2013)
    tree.add_movie("There Will Be Blood", "Drama", 8.2, 2007)
    tree.add_movie("No Country for Old Men", "Crime", 8.1, 2007)
    tree.add_movie("Blade Runner", "Action", 8.1, 1982)
    tree.add_movie("Lock, Stock and Two Smoking Barrels", "Comedy", 8.1, 1998)

    while True:
        print(f"\nSelecione uma operação:\n")
        print("1. Pesquisar filmes por gênero")
        print("2. Pesquisar filmes por título")
        print("3. Pesquisar filmes por classificação")
        print("4. Adicionar filme")
        print("5. Remover filme")
        print("6. Recomendar filmes")
        print("0. Sair")

        choice = input(f"\nEscolha uma opção:")

        if choice == "1":
            genre = input("Digite o gênero que deseja pesquisar: ")
            movies = tree.search_movies_by_genre(tree.root, genre)
            if movies:
                print("Filmes encontrados:")
                for movie in movies:
                    print(movie.title, "-", movie.genre, "-", movie.rating, "-", movie.year)
            else:
                print("Nenhum filme encontrado para este gênero.")


        elif choice == "2":
            title = input("Digite o título do filme que deseja pesquisar: ")
            title_cased = title.title()
            
            movie = tree.search_movies_by_title(tree.root, title_cased)
            if movie:
                print("Filme encontrado:")
                print(movie.title, "-", movie.genre, "-", movie.rating, "-", movie.year)
            else:
                print("Filme não encontrado.")

        elif choice == "3":
            rating = float(input("Digite a classificação mínima desejada: "))
            movies = tree.search_movies_by_rating(tree.root, rating)
            if movies:
                print("Filmes recomendados:")
                for movie in movies:
                    print(movie)
            else:
                print("Nenhum filme recomendado encontrado para os critérios fornecidos.")
        
        elif choice == "4":
            title = input("Digite o título do filme: ")
            genre = input("Digite o gênero do filme: ")
            rating = float(input("Digite a classificação do filme: "))
            year = int(input("Digite o ano de lançamento do filme: "))
            tree.add_movie(title, genre, rating, year)
            print("Filme adicionado com sucesso!")

        elif choice == "5":
            title = input("Digite o título do filme que deseja remover: ")
            movie = tree.search_movies_by_title(tree.root, title)
            if movie:
                tree.remove_movie_by_title(tree.root, title)
                print("Filme removido com sucesso!")
            else:
                print("Filme não encontrado.")

        elif choice == "6":

            rating = float(input("Digite a classificação mínima desejada para a recomendação: "))
            genre = input("Digite o gênero para filtrar (ou deixe em branco para não filtrar por gênero): ")
            start_year = input("Digite o ano inicial para filtrar (ou deixe em branco para não filtrar por ano): ")
            end_year = input("Digite o ano final para filtrar (ou deixe em branco para não filtrar por ano): ")
            start_year = int(start_year) if start_year else None
            end_year = int(end_year) if end_year else None

            movies = tree.recommend_movies(tree.root, genre, rating, start_year, end_year)

            if movies:
                print("Filmes recomendados:")
                for movie in movies:
                    print(movie)
            else:
                print("Nenhum filme recomendado encontrado para os critérios fornecidos.")

        elif choice == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
