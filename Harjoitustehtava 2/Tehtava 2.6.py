import random
print(f"Kolmi numeroinen koodi:")
for i  in range(0,3):
    print (random.randint(0, 9), end="")
print(f"\nNelinumeroinen koodi:")
for i in range(0,4):
    print (random.randint(1, 6),end="")



from shutil import which
from tabnanny import check

import mysql.connector

db_connection = mysql.connector.connect(
         host='127.0.0.1', #host='localhost'
         port= 3306,
         database='detective_game2',
         user='heikki',
         password='pekka',
         autocommit=True
         )

'''
def start_location():
    # Empties locations tabel. Selects 5 random location from airport tabel and adds them to locations table,
    # selects one of the airports as starting airport.
    sql = (f'DELETE FROM game;')
    sql_1 = (f'ALTER TABLE game AUTO_INCREMENT= 1;')
    sql1= (f'DELETE FROM LOCATIONS;')
    sql1_1 = (f'ALTER TABLE locations AUTO_INCREMENT= 1;')
    sql2= (f'insert into locations(name, icao) SELECT name, ident FROM airport WHERE continent = "EU" and type = "large_airport" ORDER BY RAND() limit 5;')
    sql3= (f'insert into game(location) SELECT name FROM locations ORDER BY RAND() limit 1;')
    cursor = db_connection.cursor()
    cursor.execute(sql)
    cursor.execute(sql_1)
    cursor.execute(sql1)
    cursor.execute(sql1_1)
    cursor.execute(sql2)
    cursor.execute(sql3)
    db_connection.commit()
    return




start_location()


'''





def locations():
    sql = (f'SELECT icao, name FROM locations WHERE name NOT IN ;')
    cursor = db_connection.cursor()
    cursor.execute(sql)
    airports = cursor.fetchall()
    for airport in airports:
        print(f' Icao: {airport[0]}, {airport[1]}. ')
    return


locations()
'''
def is_location_current(destination):
    sql = (f'SELECT icao, FROM locations;')
    sql2 = (f'SELECT icao, FROM game;')
    cursor = db_connection.cursor()
    cursor.execute(sql)
    airports = cursor.fetchall()
    cursor.execute(sql2)
    your_airport = cursor.fetchall()
    if destination in airports and destination not in your_airport:
        return True

def fly():
    #print(f'You are currently at the {location_now()}.')
    print(locations())
    destination = input("Where would you like to fly next, use the Icao-code: ")
    if is_location_current(destination) == True:
        else:
'''





