import sqlite3 #sqlite for interacting with .db files

#create or open connection to database

def create_connection(db_name="tunes.db"):
    """
    Create a connection to the SQLite database.
    If the database file does not exist, SQLite will create it.
    """
    conn = sqlite3.connect(db_name)  #open or create db file
    return conn #return active connection object


#create tune tables from scratch drop and create

def create_tunes_table(conn):
    """
    Drops the 'tunes' table if it exists and recreates it with the schema
    expected by the rest of the application.
    """
    cursor = conn.cursor()  #cursor does sql cmds

    #remove table if already exists so we have a clean schema
    cursor.execute("DROP TABLE IF EXISTS tunes")
    conn.commit()  #save changes to db

    #create fresh tunes column with lowercase names
    cursor.execute("""
        CREATE TABLE tunes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique ID for each row
            book INTEGER,       -- Book number (derived from folder name)
            x INTEGER,          -- Tune index (X: field)
            title TEXT,         -- Primary tune title
            alt_title TEXT,     -- Secondary title (optional)
            tune_type TEXT,     -- Type (Reel, Jig, etc.)
            key TEXT,           -- Musical key
            notation TEXT       -- Full ABC notation as a string
        )
    """)
    conn.commit()  #save changes after creating