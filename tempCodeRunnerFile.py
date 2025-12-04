from parser_module import load_abc_files, load_abc_file, parse_all_tunes

from database_module import save_tunes_to_db, create_connection

import sqlite3 # used to open db connectiion manually
import analysis_module #query finctions used by ui

from ui_module import launch_ui

all_tunes = []  #hold all tunes across al books

#loads abc files and returns list of filepath abd bookfoldername
for filepath, book in load_abc_files('abc_books'):

    #read the abc file line by line
    lines = load_abc_file(filepath)

    #paarse all tunes found in this file into structured dictionaries
    file_tunes = parse_all_tunes(lines)

    #process each tune parrsed from this file
    for tune in file_tunes:

        #convert book folder name into intt if possible
        try:
            tune_book = int(book)  #folder 3 = integer 3
        except:
            tune_book = book       #fallback if folder name isnt number

        #keep book in tune directory
        tune['book'] = tune_book

        #add tune to main list
        all_tunes.append(tune)

#how many tunes were found
print(f"Parsed {len(all_tunes)} tunes across all books.")


#save parsed tunes to sqlite db

save_tunes_to_db(all_tunes, db_name="tunes.db")
print("Saved tunes to tunes.db")


#open db connection and launch ui 

#create connection to db
conn = sqlite3.connect("tunes.db")

#launch ui
launch_ui(conn, analysis_module)