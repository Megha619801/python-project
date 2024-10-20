#Q.no.1
import mysql.connector

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = '121100',
    autocommit = True,
    collation = 'utf8mb3_general_mysql500_ci'
)

def retrieve_airport(icao_code):
    airport_sql = f'select name, municipality from airport where ident = "{icao_code}";'
    airport_cursor = connection.cursor()
    airport_cursor.execute(airport_sql)
    result = airport_cursor.fetchall()
    if airport_cursor.rowcount >0:
        for row in result:
            print(f'The airport with {icao_code} is {row[0]} in {row[1]}')
    return

icao_input = input('What is the ICAO code you are looking for? - ').upper()
retrieve_airport(icao_input)

#Q.no.2
import mysql.connector

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = '121100',
    autocommit = True,
    collation = 'utf8mb3_general_mysql500_ci'
)
def airport_type(area_code):
    type_sql = f'select name, type from airport where iso_country = "{area_code}" order by type;'
    airport_type_cursor = connection.cursor()
    airport_type_cursor.execute(type_sql)
    result = airport_type_cursor.fetchall()
    print('Airport name, Type of airport')
    closed = 0
    large = 0
    small = 0
    medium = 0
    heliport = 0
    if airport_type_cursor.rowcount > 0:
        for row in result:
            print(f'{row[0]},{row[1]}')
            if row[1] == "closed":
                closed += 1
            elif row[1] == "large_airport":
                large += 1
            elif row[1] == "small_airport":
                small += 1
            elif row[1] == "heliport":
                heliport += 1
            elif row[1] == "medium_airport":
                medium +=1
    return large, small, medium, heliport, closed

def country(country_code):
    country_sql = f'select country.name from country where iso_country = "{country_code}";'
    country_cursor = connection.cursor()
    country_cursor.execute(country_sql)
    result = country_cursor.fetchall()
    country = result[0][0]
    return country

area = input('Type in the area code: ').upper()
airport_type(area)
large, small, medium, heliport, closed = airport_type(area)
print(f'{country(area)} has {large} large airports, {medium} medium airports, {small} small airports, {heliport} heliports, and {closed} closed airports.')

#Q.no.3
import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = '121100',
    autocommit = True,
    collation = 'utf8mb3_general_mysql500_ci')

def coordinate(icao_code):
    cor_sql = f'select latitude_deg, longitude_deg from airport where ident = "{icao_code}";'
    cor_cursor = connection.cursor()
    cor_cursor.execute(cor_sql)
    result_cor = cor_cursor.fetchall()
    if cor_cursor.rowcount >0:
        latitude = result_cor[0][0]
        longitude = result_cor[0][1]
    else:
        latitude = None
        longitude = None
    return latitude, longitude

def airport_name(icao_code):
    airport_sql =f'select name from airport where ident = "{icao_code}";'
    airport_cursor = connection.cursor()
    airport_cursor.execute(airport_sql)
    result_airport = airport_cursor.fetchall()
    if airport_cursor.rowcount > 0:
        airport_name = result_airport[0][0]
    else:
        airport_name = None
    return airport_name

icao_input1 = input('Please enter ICAO of airport number 1: ').upper()
icao_input2 = input('Please enter ICAO of airport number 2: ').upper()
airport1 = coordinate(icao_input1)
airport2 = coordinate(icao_input2)
airport_name1 = airport_name(icao_input1)
airport_name2 = airport_name(icao_input2)

if airport_name1 == None or airport_name2 == None:
    print('Invalid ICAO code, please try again')
else:
    print(f'The distance between {(airport_name(icao_input1))} and {airport_name(icao_input2)} is: {distance.distance(airport1, airport2).km:.3f}km')
