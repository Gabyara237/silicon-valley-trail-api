from cli.menus import welcome_menu

def run():
    choice = welcome_menu()

    if choice == 1:
        print("Login selected")
    elif choice == 2:
        print("Register selected")
    elif choice == 3:
        print("Play as Guest selected")
    elif choice == 4:
        print("View Rules selected")

if __name__ == "__main__":
    run()