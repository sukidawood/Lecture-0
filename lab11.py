import sqlite3
import base64
import webbrowser
conn = sqlite3.connect("week11.db")
c = conn.cursor()
def promptNumber():
    while True:
        try:
            x = int(input("Pick a number between 1 and 24 (or q to quit): "))
            if x > 0 and x < 25:
                c.execute("SELECT link from Lab10 where id = %s" % x)
                link = c.fetchone()
                # print(link[0])
                decoded = base64.b64decode(link[0]).decode('utf-8')
                # print(decoded)
                webbrowser.open(decoded)
                city = input("What is the name of the city? ")
                country = input("What is the name of the country? ")
                c.execute("UPDATE Lab10 SET city = '%s', country = '%s' WHERE id = '%d'" % (city, country, x))
                conn.commit()
                break

        except ValueError:
                print("Quit")
                break
