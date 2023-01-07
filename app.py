


def remove_user():
    login = input("Sélectionnez le login a supprimer : ")
    # del user_dict [d]
    if login in user_dict.keys():
        del user_dict[login]
        print("Le login ", login, " a bien été supprimer ")
    else:
        print("Ce login n'existe pas")
        show_main_menu()



def create_user():
    """create a new user"""
    user_dict : dict
    loginc: str = input("Créer un nouveau pseudo : ")
    passw: str = input("Créer un nouveau mot de passe : ")
    for i in range(len(user_list)):
        user_dict = user_list[i]
        keys:list = list(user_dict.keys())
        if loginc == keys[0]:
            print("Ce login existe déja, veuillez réessayez")
            create_user()

    # création du nouvel utilisateur
    user_list.append({loginc:{passw:{"":("","")}}})
    print("Votre compte a bien été créer, merci")
    show_vault_menu(loginc,passw)


def remove_item():
    print("occupé")


def change_item():
    # todo modifie l'element demander
    print("occupé")


def search_item(user_password:str):
    # récupère tout les keys du dict_vaultItem lier a l'utilisateur
    list_name : list = dict_vault[user_password]
    # affiche la liste de nom de chaque petit coffre (VaultItem)
    print(list_name)
    # demande a l'user d'
    answer : str = input("choisir:")
    # affiche les données de l'élément choisi par l'utilisateur
    data_item : tuple = dict_vaultItem[answer]
    print(f"nom:{answer} pseudo:{data_item[0]} mot de passe:{data_item[1]}")
    input("quitté (oui/non):")
    show_vault_menu(user_password)

def add_new_item(loginc:str , passw : str)->None:
    name_item: str = input("Entrer le nom : ")
    login_item: str = input("Pseudo : ")
    password_item: str = input("Mot de passe : ")
    list_name : list = dict_vault[user_password]
    if name_item not in list_name:
        dict_vault[user_password] = name_item
        dict_vaultItem[name_item] = (login_item,password_item)
        print(
            "Le nom: ",
            password_item,
            "\nLe login :",
            login_item,
            "\nLe mot de passe :",
            password_item,
            "\nOnt bien été créer",
        )
        show_vault_menu(user_password)

    else:
        print("Ce nom existe déja, veuillez réessayez")
        add_new_item(user_password)


def show_vault_menu(loginc : str,passw:str)->None:
    """
    Menu du coffre fort
    :param loginc:
    :param passw:
    :return:
    """
    print("\n", " BIENVENU CHER TOI ".center(25, "\U0001F600"))

    print(
        """#                                #
          \r#       1. Add item              #
          \r#       2. Remove item           #
          \r#       3. Change item           #
          \r#       4. Search item           #
#                                #
          \r#       0. Back                  #
#                                #
##################################
    """
    )

    choice = ask("\U0001F607" " Your choice: " "\n")

    match choice:
        case 0:
            print("\n", " MERCI A BIENTOT ".center(30, "\U0001F600"))
            show_main_menu()
        case 1:
            add_new_item(loginc,passw)
        case 2:
            remove_item(loginc,passw)
        case 3:
            change_item(loginc,passw)
        case 4:
            search_item(loginc,passw)
        case _:
            print("Choix invalide...")


def do_login():
    login = input("Entrer votre Login : ")
    passw = input("Entrer votre mot de passe : ")
    for i in range (len(user_list)):
        user_dict : dict = user_list[i]
        list_login : list = list(user_dict.keys())
        if login == list_login[0]:
            vault_dict: dict = user_dict[login]
            list_vault: list = list(vault_dict.keys())
            if passw == list_vault[0]:
                print("Bienvenu")
                show_vault_menu(login, passw)

    print("Les données entrer sont incorrecte")
    show_main_menu()

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


if __name__ == "__main__":
    user_list : list = [{"Adrien":{"2310":{"Amazon":("Adrien23","1245")}}}]
    while True:
        show_main_menu()
