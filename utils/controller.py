def get_user_info(users_date: list)->None:
    for user in users_date:
        print(f'Twój znajmoy {user["name"]} z miejscowości  {user["Location"]} opublikował {user["Posts"]}')




def add_user(users_date: list) -> None:
    new_name: str = input('Podaj imię nowego znajomego: ')
    new_location: str = input('Podaj skąd pochodzi nowy znajomy: ')
    new_posts: int = int(input('Podaj liczbę postów: '))
    users_date.append({'name': new_name, 'Location': new_location, 'Posts': new_posts}, )



def remove_user(users_date: list) -> None:
    user_name: str = input('Kogo chcesz usunąć: ')
    for user in users_date:
        if user['name'] == user_name:
            users_date.remove(user)
