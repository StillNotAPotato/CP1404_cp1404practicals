import wikipedia

def main():
    page_title = input("Page title: ")
    while input() != " ":
        print(wikipedia.search(page_title))
        print(wikipedia.summary(page_title))
        page_title = input("Page title: ")
        wikipedia.page(page_title, auto_suggest=True)
    try:
        page_title = wikipedia.summary("Page Title")
    except wikipedia.DisambiguationError as e:
        print(e.options)

if __name__ == '__main__':
    main()