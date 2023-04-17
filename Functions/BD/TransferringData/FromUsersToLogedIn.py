from main import *
from database.DB import client, db, coll, collLoggedIn

def FromUsersToLoggedIn(username, password):
    # выбор коллекции


    # поиск пользователя по имени и паролю
    result = coll.find_one({"firstname": username, "password": password})

    if result is not None:
        user_id = result["_id"]

        # получение данных пользователя
        result = coll.find_one({"_id": user_id}, {"firstname": 1, "password": 1, "email": 1})

        if result is not None:
            firstname = result["firstname"]
            password = result["password"]
            email = result["email"]

            # добавление пользователя в коллекцию LoggedIn
            collLoggedIn.insert_one({"firstname": firstname, "password": password, "email": email})

            print("User logged in successfully!")
        else:
            print("User details not found!")
    else:
        print("User not found!")
























    # db = sqlite3.connect('database\contacts.db')
    # coursor = db.cursor()
    # coursor.execute(f"SELECT id FROM users WHERE firstname = '{username}' AND password = '{password}'")
    # result = coursor.fetchone()
    #
    # if result is not None:
    #     user_id = result[0]
    #
    #     coursor.execute(f"SELECT firstname, password, email FROM users WHERE id = {user_id}")
    #     result = coursor.fetchone()
    #
    #     if result is not None:
    #         firstname, password, email = result
    #
    #         coursor.execute(f"INSERT INTO LoggedIn (firstname, password, email) VALUES (?, ?, ?)", (firstname, password, email))
    #         db.commit()
    #
    #         print("User logged in successfully!")
    #     else:
    #         print("User details not found!")
    # else:
    #     print("User not found!")
    # db.close()
