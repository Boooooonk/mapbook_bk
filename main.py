from Utills.controller import get_user_info, add_user
from Utills.model import users


def main():
    while True:
        print('================Menu================')
        print('0 - Exit')
        print('1 - Get user info')
        print('2 - Add user')
        print('====================================')

        choice = int(input('Podaj numer z menu: '))
        if choice == 0:
            break
        elif choice == 1:
            get_user_info(users)
            break
        elif choice == 2:
            add_user(users)

if __name__ == "__main__":
    main()
