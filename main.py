users: list= [
    {'name': 'Julia', 'Location': 'Ząbki', 'Posts': 10},
    {'name': 'Julia', 'Location': 'Sokółka', 'Posts': 20},
    {'name': 'Klaudia', 'Location': 'Warszawa', 'Posts': 15},
    {'name': 'Marcin', 'Location': 'Grudziądz', 'Posts': 1000},
    {'name': 'Mateusz', 'Location': 'Lublin', 'Posts': 100},
]





def get_user_info(users_date: list)->None:
    for user in users_date:
        print(f'Twój znajomy {user['name']} z miejscowości {user["Location"]} opublikował {user["Posts"]}')


print(f'Witaj {users[0]['name']}')
get_user_info(users[1:])







