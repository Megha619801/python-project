import mysql.connector


connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="root",
    password="<Megha@2024@>",
    autocommit=True,
    collation="utf8mb3_general_mysql500_ci"
    )

def get_airport_by_identity (identity):
    sql = "select * from airport where ident = {identity}"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    print(sql)
