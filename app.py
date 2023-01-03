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
    if login not in user_dict.keys():
        create_user()
    passw = input("Entrer votre mot de passe : ")
    if passw not in user_dict.keys():
        print("Erreur de mot de passe...")




def create_user():
    loginc = input("Créer un nouveau Login : ")
    if loginc not in user_dict.keys():
        user_dict[loginc] = [] #creation du dictionnaire vide
        passw = input("Créer un nouveau mot de pass : ")
        user_dict[passw] = []
        print("Le login :",loginc,", et le mot de passe :",passw," ont bien été créer")
    else:
        print("Ce login existe déja, veuillez réessayez")
        create_user()


def remove_user():
    login = input("Sélectionnez le login a supprimer : ")
    #del user_dict [d]
    if login in user_dict.keys():
        del user_dict[login]
        print("Le login ",login," a bien été supprimer ")
    else:
        print("Ce login n'existe pas")
        remove_user()


def show_main_menu() -> None:
    """ Show the main menu """
    print("\n", " CODE-MOI ".center(20,"\U0001F600"))

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
            print("Choix invalide...")


if __name__ == '__main__':
    user_dict = {} #dictionnaire des login
    while True:
        show_main_menu()
