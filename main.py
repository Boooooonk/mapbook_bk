users:list[dict] = [
    {'name': 'Bartlomiej', 'location': 'Krynki', 'posts': 500},
    {'name': 'Karol', 'location': 'Miedzyrzec Podlaski', 'posts': 700},
    {'name': 'Krystian', 'location': 'Zyrardow', 'posts': 200}
]

for user in users:
    print(f'Twój znajomy: {user["name"]} z miejscowości: {user["location"]} opublikował {user["posts"]} postów.')
