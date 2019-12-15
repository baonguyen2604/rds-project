from .command import Command
import mysql.connector

class Ls(Command):

    name = "List"
    
    def __init__(self, args=None):
        self.path = args.path
        self.name = args.name
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database='filesystem'
        )

    # Connect to our mysql db to collect metadata, without having to contact volume
    def run(self):
        cursor = self.mydb.cursor()
        cursor.execute("USE filesystem")
        cursor.execute("Select * from %s where path LIKE '%s%%'" % (self.name, self.path))
        result = cursor.fetchall()
        message = ''
        for x in result:
            message+= str(x) + "\n"
        return message


        
