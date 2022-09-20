def main():
    filenames = ["Away In A Manger.txt",
                 "SilentNight.txt",
                 "O little town of bethlehem.TXT",
                 "ItIsWell (oh my soul).txt, "
                 "The_Lord_is_King.jpg",
                 "file no extension"]

    for filename in filenames:
        fixed_filename = get_fixed_filename(filename)
        print(fixed_filename)


# convert a1 to use song objects

def get_fixed_filename(filename_extension):
    data = filename_extension.split(".")
    filename = data[0]
    length_of_name = len(filename)
    index = 1
    while index < length_of_name:
        current_character = filename[index]
        previous_character = filename[index - 1]
        if current_character.isupper() and previous_character.isalpha():
            # filename = filename.replace(current_character, " " + current_character) # replacing with a whitespace
            filename = filename[:index] + " " + filename[index:]  # inserting a whitespace
            length_of_name += 1
            index += 1  # _N index is now at _ +=1 -> N
        index += 1
    print(filename.strip())
    if len(data) == 2:
        filename = filename.strip().title() + "." + data[1].lower()
    return filename.replace(" ", "_")


if __name__ == '__main__':
    main()
