from Utills.controller import get_user_info, add_user, remove_user, update_user
from Utills.model import users


def main():
    while True:
        print('================Menu================')
        print('0 - Exit')
        print('1 - Get user info')
        print('2 - Add user')
        print('3 - Remove user')
        print('4 - Update user')
        print('====================================')

        choice = int(input('Podaj numer z menu: '))
        if choice == 0:
            break
        elif choice == 1:
            get_user_info(users)
        elif choice == 2:
            add_user(users)
        elif choice == 3:
            remove_user(users)
        elif choice == 4:
            update_user(users)

if __name__ == "__main__":
    main()
