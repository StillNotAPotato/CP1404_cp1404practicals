def main():
    name = str(input("Enter name: "))
    MENU_STRING = "(H)ello\n(G)oodbye\n(Q)uit"
    print(MENU_STRING)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "H":
            print("Hello " + name)
        elif choice == "G":
            print("Goodbye " + name)
        else:
            print("Invalid choice")
        print(MENU_STRING)
        choice = input(">>>").upper()
    print("Finished")


main()




