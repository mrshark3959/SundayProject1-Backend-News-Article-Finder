from googlesearch import search


def main():
    print(
        "Welcome to News Term Finder, please input three terms you would like to search for in the news articles."
    )
    # take the quiries
    term1 = input("Enter first term: ")
    term2 = input("Enter second term: ")
    term3 = input("Enter third term: ")
    terms = [term1, term2, term3]
    search_terms(terms)


# make a function that searches for the terms
def search_terms(terms):
    query = " ".join(terms) + " news"
    results = []
    for j in search(query, num=5, stop=5, pause=2):
        results.append(j)
    title_printer(results)


# make a function that prompts the user for the titles
def title_printer(titles):
    print("Here are the top 5 news articles found:")
    for i, title in enumerate(titles):
        print(f"{i + 1}. {title}")


if __name__ == "__main__":
    main()
