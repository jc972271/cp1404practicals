import wikipedia

search = input("Search: ")

while search.strip() != "":
    try:
        page = wikipedia.page(search)
        print(page.title)
        print(page.summary)
        print(page.url)
    except wikipedia.exceptions.PageError:
        print(f"Page id {search} does not match any pages. Try another id!")
    except wikipedia.exceptions.DisambiguationError:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(wikipedia.search(search, results=5))
    search = input("Search: ")

def temp_fuction():
    pages = wikipedia.search(search, results=3)
    for i, page in enumerate(pages):
        print(f"{i}. {page}")
    page_index = int(input("Please choose a page (enter number): "))