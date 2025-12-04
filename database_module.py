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
    
    #saves lsit of tune directories to the database
    
def save_tunes_to_db(tunes, db_name="tunes.db"):
    """
    Saves a list of parsed tune dictionaries into the SQLite database.
    Recreates the table before inserting anything to guarantee schema matches.
    """
    conn = sqlite3.connect(db_name)  #open db file
    cursor = conn.cursor()           #cursor for sql inject

    #makes sure tunes table exist and was just created
    create_tunes_table(conn)

    #loop each parsed tune dictionary and put into db
    for tune in tunes:

        #extract values using .get or do none if missing
        book = tune.get("book")

        #checking case
        x_val = tune.get("X") or tune.get("x")

        #try changing X to integer
        try:
            x_val = int(x_val) if x_val is not None else None
        except:
            #fail then just leave it
            pass

        #standard tune fields
        title = tune.get("title")
        alt_title = tune.get("alt_title")
        tune_type = tune.get("tune_type")
        key = tune.get("key")
        notation = tune.get("notation")  #all of abc tune

        #put the tune into db table
        cursor.execute(
            "INSERT INTO tunes (book, x, title, alt_title, tune_type, key, notation) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (book, x_val, title, alt_title, tune_type, key, notation)
        )

    conn.commit()  #commit all instered rows into disk
    conn.close()   #close db connection