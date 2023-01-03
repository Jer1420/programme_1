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

def add_new_item():
    # todo ajoute un nouvelle element dans le coffre
    """ create a new user"""
    name_item: str = input("Créer un nouveau nom: ")
    login_item: str = input("Créer un nouveau pseudo: ")
    passw_item: str = input("Créer un nouveau mot de passe: ")
    if login_item not in user_dict.keys():
        dict_vault_item[passw_item] = []
        user_dict_item[login_item] = dict_vault_item
        dict_vault_all = {name_item: (login_item, passw_item)}
        print("Le nom:",name_item,", le login:", login_item, ", et le mot de passe:", passw_item, " ont bien été créer")
        print(dict_vault_all)


def change_item():


# todo modifie l'element demander
    print("occupé")

def search_item():


# todo cherche l'element demander et l affiche
    print("occupé")

def show_vault_menu():
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
            add_new_item()
        case 2:
            remove_item()
        case 3:
            change_item()
        case 4:
            search_item()
        case _:
            print("Choix invalide...")



if __name__ == '__main__':

    dict_vault_item: dict= {}
    user_dict_item: dict= {}
    dict_all: dict = {}
    dict_vault: dict = {}
    dict_vaultitem: dict = {}
    user_dict = {}  # dictionnaire des login
    while True:
        show_vault_menu()