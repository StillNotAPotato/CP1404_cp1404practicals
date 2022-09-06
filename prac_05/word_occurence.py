def main():
    text_to_analyse = {}
    text = input("Text: ")
    # Text: this is a collection of words of nice words this is a fun thing it is
    words = text.split()
    for word in words:
        count = text_to_analyse.get(word, 0)
        text_to_analyse[word] = count + 1

    # display words and frequencies in alphabetical order
    words = list(text_to_analyse.keys())
    words.sort()

    maximum_length = max(len(word) for word in words)
    for word in words:
        print("{:{}} : {}".format(word, maximum_length, text_to_analyse[word]))

if __name__ == '__main__':
    main()
