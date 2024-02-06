# BestFriendsProj.PY: This app can add/remove names in a lsit
__author__  = "Artem Tsvietkov"
__version__ = "1.0.0"
__email__   = "artem.tsvietkov@elev.ga.ntig.se"

from colors import bcolors
import os

os.system('cls')

# Show names in list
names = []
def show_list(friend_list):
    print(bcolors.BLUE + "ꑭ"*11)
    print(bcolors.YELLOW + "Frineds in your list: ")
    for name in friend_list:
        print(bcolors.YELLOW + name)


# Add name to list
def add_name(friend_list):
    friend = input("Write in a name you want to add to your list: ")
    friend_list.append(friend)
    print(bcolors.BLUE + {friend} + bcolors.GREEN + "has been successfully added to your list.")

# Remove name from list
def remove_name(friend_list):
    friend = input("Write in the name you want to delete: ")
    if friend in friend_list:
        friend_list.remove(friend)
        print(f"{friend} has been successfully removed from your list.")
    else:
        print(f"{friend} is not in your list. Check if there are some spelling misstakes.")

while True:
    print(bcolors.BLUE + "ꑭ"*11)
    print(bcolors.YELLOW + "Your choice is:")
    print(bcolors.BLUE + "1. Add name")
    print(bcolors.BLUE + "2. Remove name")
    print(bcolors.YELLOW + "3. Show list")
    print(bcolors.YELLOW + "4. Close the program")
    print(bcolors.BLUE + "ꑭ"*11)
    user_choice = input(bcolors.BLUE + "What do you" + bcolors.YELLOW +" want to choose? " + bcolors.DEFAULT)

    if user_choice == "1":
        add_name(names)
    elif user_choice == "2":
        remove_name(names)
    elif user_choice == "3":
        show_list(names)
    elif user_choice == "4":
        break
    else:
        print(bcolors.RED + bcolors.BOLD + "You've made a misstake. Try again choosing between 1-4" + bcolors.DEFAULT)


