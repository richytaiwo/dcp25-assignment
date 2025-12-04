# Data Centric Programming Assignment 2025

- [Assignment Brief](assignment.md)

Name: Richard Taiwo

Student Number: C24375003

# Screenshots

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

To run the main application, open terminal and type:
python main.py
This script will load and parse the ABC files, put the parsed tunes into tunes.db and opens the Tkinter UI.
or just click the run button on VSCode.

To navigate the UI:
The left sidebar has all the folders found in the abc_books. directory. Clicking a book will allow you to load all of the tunes from that book.
The search bar allows youto search by title, the tune type or musical key, it is not case sensitive.
Double clicking a tune will open another popup that shows the title, type, key and full abc notation.

To exit the program:
Close the Tkinter window.
# How it works:
My assignment has four major parts that allows it to work.

File loading and parsing
# List of files in the project

| Files | Source |
|-----------|-----------|
| main.py | Self written |
| test.py | Modified from [reference]() |
| test.py | From [reference]() |

# References
* Item 1
* Item 2

# What I am most proud of in the assignment

Bla bla bla

# What I learned

Bla bla bla

## Below is how to use Markdown. You can delete this:

## This is how to markdown text:

This is *emphasis*

This is a bulleted list

- Item
- Item

This is a numbered list

1. Item
1. Item

This is a [hyperlink](http://bryanduggan.org)

# Headings
## Headings
#### Headings
##### Headings

This is code:

```Java
public void render()
{
	ui.noFill();
	ui.stroke(255);
	ui.rect(x, y, width, height);
	ui.textAlign(PApplet.CENTER, PApplet.CENTER);
	ui.text(text, x + width * 0.5f, y + height * 0.5f);
}
```

So is this without specifying the language:

```
public void render()
{
	ui.noFill();
	ui.stroke(255);
	ui.rect(x, y, width, height);
	ui.textAlign(PApplet.CENTER, PApplet.CENTER);
	ui.text(text, x + width * 0.5f, y + height * 0.5f);
}
```

This is an image using a relative URL:

![An image](images/p8.png)

This is an image using an absolute URL:

![A different image](https://bryanduggandotorg.files.wordpress.com/2019/02/infinite-forms-00045.png?w=595&h=&zoom=2)

This is a youtube video:

[![YouTube](http://img.youtube.com/vi/J2kHSSFA4NU/0.jpg)](https://www.youtube.com/watch?v=J2kHSSFA4NU)

This is a table:

| Heading 1 | Heading 2 |
|-----------|-----------|
|Some stuff | Some more stuff in this column |
|Some stuff | Some more stuff in this column |
|Some stuff | Some more stuff in this column |

|Some stuff | Some more stuff in this column |

