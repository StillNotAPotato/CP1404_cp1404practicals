COLOUR_TO_CODE = {"CAROLINA BLUE": "#56a0d3", "CARROT ORANGE": "ed9121",
                  "CEDAR CHEST": "c95a49", "CELADON": "ace1af", "CELTIC BLUE": "246bce", "CELESTE": "b2ffff",
                  "CERULEAN BLUE": "#007ba7",
                  "CERULEAN FROST": "#6d9bc3", "CHARCOAL": "#36454f", "CHARTREUSE1": "#7fff00"}


def main():
    print(COLOUR_TO_CODE)
    colour_input = input("Name of colour: ").upper()
    while colour_input != "":
        if colour_input in COLOUR_TO_CODE:
            print(colour_input, "is", COLOUR_TO_CODE[colour_input])
        else:
            print("")
        colour_input = input("Name of colour: ").upper()


if __name__ == '__main__':
    main()
