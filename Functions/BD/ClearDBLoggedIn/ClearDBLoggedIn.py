from main import *


def ClearDBLoggedIn():
    db = sqlite3.connect('database\contacts.db')
    coursor = db.cursor()
    coursor.execute(f"DELETE FROM LoggedIn;")
    db.commit()
    db.close()
    print('Данные очищены')
