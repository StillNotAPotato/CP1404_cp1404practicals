def main():
    pass
    text = input("Text: ")
    text_to_analyse = {}
    # Text: this is a collection of words of nice words this is a fun thing it is
    word = text.split()
    for word in text:     #
        # print(text)
        count = text_to_analyse.get(text, 0)
        text_to_analyse[text] = count + 1

    text = list(text_to_analyse.keys())
    text.sort()

    for text in text_to_analyse:
        maximum_length = max(len(word) )
        print("{{}} : {}".format(text, maximum_length, text_to_analyse[text]))

if __name__ == '__main__':
    main()
