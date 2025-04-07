from Utills.controller import get_user_info
from Utills.model import users


def main():
    while True:
        print('================Menu================')
        print('0 - Exit')
        print('1 - Get user info')
        print('====================================')
        choice = int(input('Podaj numer z menu: '))
        if choice == 0:
            break
        elif choice == 1:
            get_user_info(users)
            break


#if __name__ == "__main__":
#    main()

