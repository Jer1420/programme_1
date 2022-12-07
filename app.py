def ask(prompt: str) -> int:
    """
    Prompts user to make a choice
    :param prompt: prompt Text
    :return: an integer
    """
    ch: str = ""
    while not ch.isdigit():
        ch = input(prompt)
    return int(ch)


def do_login():
    login = input("Entrer votre Login : ")


def create_user():
    loginc = input("Entrer votre Login : ")
    #psw = input("Entrer votre mot de passe : ")
    if loginc not in user_dict.keys():
        user_dict[loginc] = []
    else:
        print("Ce login existe déja.")

def remove_user():
    pass


def show_main_menu() -> None:
    """ Show the main menu """
    print("PASSMAN - a PASSword MANager".center(100, '#'))

    print("""
          \r1. Login
          \r2. New user
          \r3. Remove user

          \r0. Quit
    """)

    choice = ask("Your choice: ")  # ask sends 0 numeric value

    match choice:
        case 0:
            exit()
        case 1:
            do_login()
        case 2:
            create_user()
        case 3:
            remove_user()
        case _:
            print("Invalide choice. Try again")


if __name__ == '__main__':
    user_dict = {}
    while True:
        show_main_menu()
