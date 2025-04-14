users: list[dict] = [
    {'name': 'Bartlomiej', 'location': 'Krynki', 'posts': 500},
    {'name': 'Karol', 'location': 'Miedzyrzec Podlaski', 'posts': 700},
    {'name': 'Krystian', 'location': 'Zyrardow', 'posts': 200}
]

def update_user(users_data:list[dict])->None:
    user_name=input('Podaj imię użytkownika do zmodyfikowania: ')
    for user in users_data:
        if user["name"] == user_name:
            user['name'] = input('Podaj nowe imię: ')
            user['location'] = input('Podaj nową lokalizację: ')
            user['posts'] = input('Podaj nową liczbę postow: ')

update_user(users)
print(users)
