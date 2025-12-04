import sqlite3 #sqlite to interact with db file
import pandas as pd #read csv data and insert into db

#name of the SQLite database file being rebuilt
DB_NAME = "tunes.db"

#name of csv file with parsed tune data
CSV_FILE = "tunes.csv"

#open connection to sql lite database and creates a file iof doesnt exist
conn = sqlite3.connect(DB_NAME)

#create cursor object to execute sql commands
cursor = conn.cursor()

#removes old tunes table to rebuild it
cursor.execute("DROP TABLE IF EXISTS tunes")

#creates new tunes table with columns
cursor.execute("""
CREATE TABLE tunes (
    X INTEGER,        -- Tune index number (X:)
    title TEXT,        -- Primary tune title
    tune_type TEXT,    -- Type (reel, jig, hornpipe, etc.)
    key TEXT,          -- Musical key (D, G, Em, etc.)
    book INTEGER       -- The book number this tune belongs to
)
""")

#read csv file into pandas dataframe
df = pd.read_csv(CSV_FILE)

# insert dataframe into sqlite table, if exist, dataframe rows inserted into new table
# index=false stops insertion of dataframe index as column
df.to_sql("tunes", conn, if_exists="append", index=False)

#save all changes to db file
conn.commit()

#close db connection cleanly
conn.close()

#confirmation that everything completed successfully
print("Database rebuilt successfully!")