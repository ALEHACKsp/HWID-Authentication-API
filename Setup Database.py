import sqlite3

db = sqlite3.connect('auth.db')
c = db.cursor()
c.execute("""CREATE TABLE hwids (
    hwid text
)""")
db.commit()
db.close()
print('Done')
input()