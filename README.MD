# Data Centric Programming Assignment 2025

- [Assignment Brief](assignment.md)

Name: Richard Taiwo

Student Number: C24375003

# Screenshots
[TEST] (images/Screenshot 2025-12-04 115539.png)
# Description of the project
This assignment shows the whole data centric programming pipeline using Python, going from structured text files provided to us, to storing in a database, using data analysis tools and creating an interface that is easy to use.

My aim in this assignment is to:
-Recursively load the ABC files from the multiple folders given.
-Parse their contents into structures Python dictionaries.
-Keep the results in a SQLite database.
-Load the data using Pandas for analysis.
-Create a UI using TKinter for interacting, searching and browsing.

My application lets individuals search for tunes by book, by titlle, type, kep and see the full ABC notation in a window that pops up when the user double clicks. The system uses parsing, data modelling, storage, analytics and a UI, which completes all the goals I was aiming for.
# Instructions for use
As long as the abc_books directory has one more more files in either the 1 or 2 folder, my application will run smoothly.

### To run the main application, open terminal and type:
python main.py
This script will load and parse the ABC files, put the parsed tunes into tunes.db and opens the Tkinter UI.
or just click the run button on VSCode.

### To navigate the UI:
The left sidebar has all the folders found in the abc_books. directory. Clicking a book will allow you to load all of the tunes from that book.
The search bar allows youto search by title, the tune type or musical key, it is not case sensitive.
Double clicking a tune will open another popup that shows the title, type, key and full abc notation.

### To exit the program:
Close the Tkinter window.
# How it works:
My assignment has four major parts that allows it to work.

## 1. File loading and parsing
This was added in my parser_module.py file

### Recursive File Discovery
My base_dir goes through all of the abc_books directory using the os.walk function, catching all of the .abc files and getting their book number from their parent folder.

### ABC File Reading
load_abc_file scans each file with latin-1 encoding to keep different characters used in older tunes.

### Tune Parsing
All tunes begin with an X: line, so a tune is parsed into a dictionary with the tune index, which is the X, the title, alternate title, tune type, key and notation.
parse_all_tunes() oricesses the complere files, and catches tune boundaries, calling parse_tune() to change each tune to a dictionary.

## 2. Database Storage
This was added in database_module.py

I created my tables in SQLITE using standard table format.

### Saving Tunes
save_tunes_to_db() drops and remakes the entire database, making sure that the loading is smooth each time. It goes through every parsed tune dictionary and puts them into SQLite.

## 3. Data Loading and Analysis
This was added in analysis_module.py

### Pandas Integration
load_tunes_df() loads the entire tunes table into a dataframe.

### Analysis Functions
I created this module to include functions that will help me list all the books, get the tunes by the book, get all the tunes, look for tunes through their title, key or type and getting full tune info.

## 4. Interactive UI.
I added this in ui_module.py

### Tkinter UI
The Ui has:
-A left sidebar, which gives a list of books
-A search bar, which has search and show all buttons.
-A main table which displays the tunes
-A popup window that opens on double clicks to give the full tune details.

When a user selects a book, the query executes and tunes are shown.
When a user searches something, the results update dynamically.
When a user double clicks a tune, it opens a popup windown with extra details.

# List of files in the project

| Files | Source |
|-----------|-----------|
| main.py | Self written |
| parser_module.py | Modified from [https://docs.python.org/3/library/os.html#os.walk]() |
| database_module.py | Self written |
| analysis_module.py | Self written |
| ui_module.py | Modified from [https://youtu.be/TuLxsvK4svQ?si=01X3-PQtxnZCcwTV]() |
| build_database.py | Modified from [https://sqlite.org/docs.html]() |
| abc__books/ | Provided dataset |

# References
* https://docs.python.org/3/library/os.html#os.walk
* https://youtu.be/TuLxsvK4svQ?si=01X3-PQtxnZCcwTV
* https://sqlite.org/docs.html 

# What I am most proud of in the assignment
The part of this assignment I am most proud of is the data pipeline I created from scratch.

This project needed me to understand the text notation format, parse data that was provided to me, create a relational schema, create a storage, analysis interfact and create a UI that works alongside the database.

I believe each section can be completed on its own, however the harder part is putting them all into one application that actually works.
I am proud of my final result because it loads the tunes, stores them and has an interactive interface, exactly as the assignment brief said.

# What I learned

This assignment helped me understand application design alot.

## 1. Building and managing databases

I learned how to design schemas, drop and recreate tables and map Python dictionaries into SQL rows. I feel like I properly understand SQLite and the workflow thanks to this project.

## 2. Using Pandas for Analysis

Even though it was quite easy in this project, loading a database into a dataframe feels alot easier for me now.

## 3. UI Programming

Using Tkinter made me learn about how to layout my screen, how to create pop windows and how to bind events to other events. This assignment helped me learn how to crreate a Python app that is interactive.


