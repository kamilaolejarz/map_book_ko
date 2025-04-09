def get_user_info(users_date: list)->None:
    for user in users_date:
        print(f'Twój znajmoy {user["name"]} z miejscowości  {user["Location"]} opublikował {user["Posts"]}')