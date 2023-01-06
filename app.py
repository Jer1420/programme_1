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

def remove_item():

    print("occupé")


def add_new_item(password_user: str):

    name_item: str = input("Entrer le nom : ")
    login_item: str = input("Pseudo : ")
    password_item: str = input("Mot de passe : ")
    if name_item not in dict_vaultitem.keys():
        dict_vaultitem[name_item] = {name_item: (login_item, password_item)}
        dict_vault[password_item] = {password_item: dict_vaultitem}
        dict_main = {login_item: dict_vault}
        print(
            "Le nom: ",
            password_item,
            "\nLe login :",
            login_item,
            "\nLe mot de passe :",
            password_item,
            "\nOnt bien été créer",
        )
        show_vault_menu()
    else:
        print("Ce nom existe déja, veuillez réessayez")
        add_new_item()


def change_item():

    # todo modifie l'element demander
    print("occupé")


def search_item():

    # todo cherche l'element demander et l affiche
    print("occupé")

def do_login():
    login = input("Entrer votre Login : ")
    passw = input("Entrer votre mot de passe : ")
    if login not in user_dict.keys():
        print("Données inexistantes veuillez réesayer")
        show_main_menu()

    elif passw not in dict_vault.keys():
        print("Erreur de mot de passe...")
    else:
        show_vault_menu()


def create_user():
    """create a new user"""
    loginc: str = input("Créer un nouveau pseudo : ")
    passw: str = input("Créer un nouveau mot de passe : ")
    if loginc not in user_dict.keys():
        dict_vault[passw] = []
        user_dict[loginc] = dict_vault
        print(
            "Le login :", loginc, ", et le mot de passe :", passw, " ont bien été créer"
        )
        show_vault_menu()
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
    """Show the main menu"""
    print("\n", " CODE-MOI ".center(20, "\U0001F600"))

    print(
        """#                                #
          \r#       1. Login                 #
          \r#       2. New user              #
          \r#       3. Remove user           #
#                                #
          \r#       0. Quit                  #
#                                #
##################################
    """
    )

    choice = ask("\U0001F607" " Your choice : " "\n")  # ask sends 0 numeric value

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


def show_vault_menu():
    """Menu du coffre fort"""
    print("\n", " BIENVENU CHER TOI ".center(25, "\U0001F600"))

    print(
        """#                                #
          \r#       1. Add item              #
          \r#       2. Remove item           #
          \r#       3. Change item           #
          \r#       4. Search item           #
#                                #
          \r#       0. Quit                  #
#                                #
##################################
    """
    )

    choice = ask("\U0001F607" " Your choice: " "\n")

    match choice:
        case 0:
            print("\n", " MERCI A BIENTOT ".center(30, "\U0001F600"))
            exit()
        case 1:
            add_new_item()
        case 2:
            remove_item()
        case 3:
            change_item()
        case 4:
            search_item()
        case _:
            print("Choix invalide...")

if __name__ == "__main__":

    dict_vaultitem: dict = {"amazon": ("jeremy22", "666")}
    dict_vault: dict = {"1234": dict_vaultitem}
    user_dict = {"Jeremy": dict_vault}  # dictionnaire des login
    while True:
        show_main_menu()