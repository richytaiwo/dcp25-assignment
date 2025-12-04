import sqlite3 #peovides db connection and sql execution
import pandas as pd #loading tables into dataframes

def load_tunes_df(db_name="tunes.db"):
    #load full tunes table into a Pandas DataFrame for analysis or debugging.
    conn = sqlite3.connect(db_name)     #open connection to the sqlite db file
    df = pd.read_sql("SELECT * FROM tunes", conn)  #read table into dataframe
    conn.close()                        #close db connection
    return df                           #return dataframe

#existing function

def get_all_books(conn):
    #return a list of all distinct book numbers found in the database.
    cursor = conn.cursor()  #create cursor for sql cmds
    cursor.execute("SELECT DISTINCT book FROM tunes ORDER BY book")  
    #unique book numbers sorted

    rows = cursor.fetchall()  #fetch all rows returned
    #[(1,), (2,), (3,), ...]

    #get book number
    return [row[0] for row in rows if row[0] is not None]
    #filter out none entries

def get_tunes_by_book(conn, book_number):
    #all tunes that belong to a specific book.
    cursor = conn.cursor()  #new cursor for sql

    #query tunes match book nummber, sorted by x number
    cursor.execute(
        "SELECT x, title, tune_type, key FROM tunes WHERE book=? ORDER BY x",
        (book_number,)  #pass arguments as a tuple to prevent sql inject
    )
    
    rows = cursor.fetchall()   #get all matching tunes

    #concert tuples into dictionaries
    return [
        {"x": r[0], "title": r[1], "tune_type": r[2], "key": r[3]}
        for r in rows
    ]

def get_all_tunes(conn):
    #Return all tunes in the database
    cursor = conn.cursor()  #new sql cursor

    cursor.execute(
        "SELECT x, title, tune_type, key FROM tunes ORDER BY title"
    )  #query everything in alphabetical order

    rows = cursor.fetchall()  #all result rows

    #change each row into dictionary for ui
    return [
        {"x": r[0], "title": r[1], "tune_type": r[2], "key": r[3]}
        for r in rows
    ]



def search_tunes(conn, term):
    cursor = conn.cursor()  #build cursor

    like = f"%{term}%"      #sql search
    #search across 3 columns
    cursor.execute("""
        SELECT x, title, tune_type, key
        FROM tunes
        WHERE title LIKE ? OR tune_type LIKE ? OR key LIKE ?
        ORDER BY title
    """, (like, like, like))  #search inputs 3 times
    rows = cursor.fetchall()  #get matching tunes

    #convert sql rows into dicts
    return [
        {"x": r[0], "title": r[1], "tune_type": r[2], "key": r[3]}
        for r in rows
    ]



def get_tune_by_x(conn, x_value):
    #fetch a single tune by its X
    cursor = conn.cursor()  #new cursor for query
    # query for tune with x identifier
    cursor.execute("""
        SELECT x, title, tune_type, key, notation
        FROM tunes
        WHERE x=?
    """, (x_value,))  #pass argument 

    r = cursor.fetchone()  #get single result row

    if not r:
        return None  #if no tune, return none instead of crashing

    #return as dictionary
    return {
        "x": r[0],
        "title": r[1],
        "tune_type": r[2],
        "key": r[3],
        "notation": r[4]
    }
