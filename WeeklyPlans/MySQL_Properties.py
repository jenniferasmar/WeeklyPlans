import mysql.connector
from Models.Users import Users

mydb = mysql.connector.connect(
  host="localhost",
  user="WeeklyPlans_admin",
  password="WeeklyPlans",
  database="WeeklyPlans"
)
my_cursor = mydb.cursor()


def add_user(user: Users):
    sql = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
    val = (user.name, user.email, user.password)
    my_cursor.execute(sql, val)
    mydb.commit()


def get_users():
    my_cursor.execute("SELECT * FROM users")
    users = my_cursor.fetchall()
    return users


def get_user_by_email(email):
    users = get_users()
    for x in users:
        if x[2] == email:
            return x


def initial_execution():
    my_cursor.execute("CREATE TABLE users (name VARCHAR(255), email VARCHAR(255), password VARCHAR(255))")


if __name__ == "__main__":
    initial_execution()
