import test
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
    passw = input("Entrer votre mot de passe : ")
    if login not in user_dict.keys():
        print("Données inexistantes veuillez réesayer")
        show_main_menu()

    elif passw not in dict_vault.keys():
        print("Erreur de mot de passe...")
    else:
        test.show_vault_menu(passw)

def create_user():
    """ create a new user"""
    loginc: str = input("Créer un nouveau pseudo : ")
    passw: str = input("Créer un nouveau mot de passe : ")
    if loginc not in user_dict.keys():
        dict_vault[passw] = []
        user_dict[loginc] = dict_vault
        print("Le login :", loginc, ", et le mot de passe :", passw, " ont bien été créer")
        test.show_vault_menu(passw)
    else:
        print("Ce login existe déja, veuillez réessayez")
        create_user()


def remove_user():
    login = input("Sélectionnez le login a supprimer : ")
    # del user_dict [d]
    if login in user_dict.keys():
        del user_dict[login]
        print("Le login ", login, " a bien été supprimer ")
    else:
        print("Ce login n'existe pas")
        remove_user()


def show_main_menu() -> None:
    """ Show the main menu """
    print("\n", " CODE-MOI ".center(20, "\U0001F600"))

    print("""#                                #
          \r#       1. Login                 #
          \r#       2. New user              #
          \r#       3. Remove user           #
#                                #
          \r#       0. Quit                  #
#                                #
##################################
    """)

    choice = ask("\U0001F607" " Your choice : ""\n")  # ask sends 0 numeric value

    match choice:
        case 0:
            print("\n", " MERCI A BIENTOT ".center(30, "\U0001F600"))
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

    dict_vaultitem: dict = {"amazon": ("jeremy22","666")}
    dict_vault: dict = {"1234": dict_vaultitem}
    user_dict = {"Jeremy": dict_vault}  # dictionnaire des login
    while True:
        show_main_menu()
