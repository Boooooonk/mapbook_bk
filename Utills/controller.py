def get_user_info(users_data:list[dict]) -> None:
    for user in users_data:
        print(f'Twój znajomy: {user["name"]} z miejscowości: {user["location"]} opublikował {user["posts"]} postów.')

def add_user(users_data: list[dict]) -> None:
    tmp_name:str = str(input('Podaj imię: '))
    tmp_location:str = str(input('Podaj miejsce: '))
    tmp_posts = int(input('Podaj liczbę postów: '))
    users_data.append({'name': tmp_name, 'location': tmp_location, 'posts': tmp_posts})