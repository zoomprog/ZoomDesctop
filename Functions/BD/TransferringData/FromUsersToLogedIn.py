from main import *


def FromUsersToLoggedIn(username, password):
    db = sqlite3.connect('database\contacts.db')
    coursor = db.cursor()
    coursor.execute(f"SELECT id FROM users WHERE firstname = '{username}' AND password = '{password}'")
    result = coursor.fetchone()

    if result is not None:
        user_id = result[0]

        coursor.execute(f"SELECT firstname, password, email FROM users WHERE id = {user_id}")
        result = coursor.fetchone()

        if result is not None:
            firstname, password, email = result

            coursor.execute(f"INSERT INTO LoggedIn (firstname, password, email) VALUES (?, ?, ?)", (firstname, password, email))
            db.commit()

            print("User logged in successfully!")
        else:
            print("User details not found!")
    else:
        print("User not found!")
    db.close()
