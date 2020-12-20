import mysql.connector
from Models.Users import Users

mydb = mysql.connector.connect(
  host="localhost",
  user="WeeklyPlans_admin",
  password="WeeklyPlans",
  database="WeeklyPlans"
)
mycursor = mydb.cursor()


def add_User(user: Users):
    sql = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
    val = (user.name, user.email, user.password)
    mycursor.execute(sql, val)
    mydb.commit()


def initial_execution():
    mycursor.execute("CREATE TABLE users (name VARCHAR(255), email VARCHAR(255), password VARCHAR(255))")


if __name__ == "__main__":
    initial_execution()
