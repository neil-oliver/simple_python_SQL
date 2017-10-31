import sqlite3
    
db = sqlite3.connect('books.db')

cursor = db.cursor()

def databaseSetup():
    global cursor

    #cursor.execute('DROP TABLE books') #uncomment this line after the first run of the program

    cursor.execute('CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER)')

    cursor.execute('INSERT INTO books(title, author, year) VALUES ("The Very Hungry Caterpillar", "Eric Carle", 1969)')
    cursor.execute('INSERT INTO books(title, author, year) VALUES ("Harry Potter and the Sorcerer’s Stone", "J.K. Rowling", 1998)')
    cursor.execute('INSERT INTO books(title, author, year) VALUES ("Dr. Seuss’s ABC", "Dr. Seuss", 1960)')
    cursor.execute('INSERT INTO books(title, author, year) VALUES ("Oh, the Places You’ll Go!", "Dr. Seuss", 1990)')
    cursor.execute('INSERT INTO books(title, author, year) VALUES ("Hop on Pop", "Dr. Seuss", 1963)')
    cursor.execute('INSERT INTO books(title, author, year) VALUES ("Harry Potter and the Prisoner of Azkaban", "J.K. Rowling", 1999)')

    db.commit()

#-----------------------------
#main code starts here
databaseSetup()
print("----------Welcome to the Big Book Database----------")
print("\n Please wait while we create this program...")

#Task 1: Create a database search for a book.
#Task 2: Create a favourites list that users can add books to. The favourites list should be stored in a text file.
#Task 3: Allow the users to recall and see their favourites list.
#Task 4: Create a menu system for users to be able to search / add / recall

#Extension task: Allow users to delete an item from the favourites list