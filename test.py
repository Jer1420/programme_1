import app
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

    # type and assign
    name_item: str = input("nom:")
    login_item : str = input("pseudo:")
    password_item : str = input("mot de passe:")
    # vérifie si la donnée exist déjà
    if name_item not in app.dict_vaultitem.keys():
        app.dict_vaultitem[name_item] = (login_item,password_item)
        app.dict_vault[password_user: app.dict_vaultitem]
    else:
        print("Cet élément exist déjà!")

def change_item():


# todo modifie l'element demander
    print("occupé")

def search_item():


# todo cherche l'element demander et l affiche
    print("occupé")

def show_vault_menu(passw: str):
    """Menu du coffre fort"""
    print("\n", " BIENVENU CHER TOI ".center(25, "\U0001F600"))

    print("""#                                #
          \r#       1. Add item              #
          \r#       2. Remove item           #
          \r#       3. Change item           #
          \r#       4. Search item           #
#                                #
          \r#       0. Quit                  #
#                                #
##################################
    """)

    choice = ask("\U0001F607" " Your choice: ""\n")

    match choice:
        case 0:
            print("\n", " MERCI A BIENTOT ".center(30, "\U0001F600"))
            exit()
        case 1:
            add_new_item(passw)
        case 2:
            remove_item()
        case 3:
            change_item()
        case 4:
            search_item()
        case _:
            print("Choix invalide...")
