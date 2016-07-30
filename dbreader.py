import sqlite3

conn = sqlite3.connect('/tmp/petfeeder.db')

curs = conn.cursor()

print curs.execute("SELECT * from entries where pet_name='Romeo'").fetchall()

#curs.execute("INSERT INTO entries VALUES (1,'Romeo')")
#conn.commit()

print curs.execute('SELECT * FROM entries;').fetchall()

def open_db():
	pass

def show_entries_table():
	return

def add():
	pass