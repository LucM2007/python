import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="login"
)

mycursor = mydb.cursor()
to_do = input("do you want to login or sign up?")
if to_do == "login":
  username = input("what is your username?").lower()
  password = input("what is your password?")
  sql = "SELECT * FROM user WHERE name = %s AND password = %s"
  val = (username, password)
  mycursor.execute(sql, val)
  result = mycursor.fetchall()
  if result:
    mydb.commit()
    print("you have logged in")
  else:
    print("wrong username or password")
if to_do == "signup":
  username = input("what is your username?")
  password = input("what is your password?")
  sql = "INSERT INTO login (name, password) VALUES (%s, %s)"
  val = (username, password)
  mycursor.execute(sql, val)
  mydb.commit()
  print("you have signed up")


mycursor.close()