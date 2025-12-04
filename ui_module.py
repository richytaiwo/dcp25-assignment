import tkinter as tk #base tk widgets
from tkinter import ttk #theme widgets
from tkinter import messagebox #for error messages

#main ui

def start_ui(conn, analysis_module):
    
    #create and display the main Tkinter UI window.

    #create main app window
    root = tk.Tk()
    root.title("ABC Tune Browser")        # Window title
    root.geometry("1100x650")             # Window size (width x height)


    #left sidebar

    sidebar = tk.Frame(root, width=220, bg="#f0f0f0")  #left panel container
    sidebar.pack(side="left", fill="y")                #attatch and stretch vertically

    tk.Label(
        sidebar,
        text="Books",
        bg="#f0f0f0",
        font=("Arial", 14)
    ).pack(pady=8)  #header

    #listbox showing numbers
    book_listbox = tk.Listbox(sidebar, width=20, font=("Arial", 12))
    book_listbox.pack(fill="y", expand=True, padx=8, pady=6)

    #load book numbers from database
    try:
        books = analysis_module.get_all_books(conn)
    except Exception as e:
        #error popup if fails
        messagebox.showerror("Database Error", f"Failed to load books: {e}")
        books = []
        
    #book numbers in sidebox
    for b in sorted(books):
        book_listbox.insert(tk.END, str(b))

    #main right area
    main_frame = tk.Frame(root)              #container for everything on the right
    main_frame.pack(side="right", fill="both", expand=True)

    #label on top that changes based on context
    header_label = tk.Label(main_frame, text="Select a book", font=("Arial", 16))
    header_label.pack(pady=8)
    
    
    #search bar
    
    search_frame = tk.Frame(main_frame)
    search_frame.pack(pady=4)

    tk.Label(search_frame, text="Search:").pack(side="left", padx=4)

    #input box for search teext
    search_entry = tk.Entry(search_frame, width=40)
    search_entry.pack(side="left", padx=4)
    

    #search
    
    def on_search():
        query = search_entry.get().strip()  #read and clean search
        if not query:
            return  #ignore empty searches
        
        #clear existing tables
        for item in tree.get_children():
            tree.delete(item)

        #use db query for each search
        try:
            tunes = analysis_module.search_tunes(conn, query)
        except Exception as e:
            messagebox.showerror("Search Error", f"{e}")
            return

        #update header for each search
        header_label.config(text=f"Search results for '{query}'")

        #matching tunes into treeview
        for t in tunes:
            tree.insert("", tk.END, values=(t["x"], t["title"], t["tune_type"], t["key"]))

    #search command acc showsw up
    tk.Button(search_frame, text="Search", command=on_search).pack(side="left", padx=4)
    
    #function referenced by button
    def show_all():
        for item in tree.get_children():
            tree.delete(item)
        header_label.config(text="All Tunes")
        tunes = analysis_module.get_all_tunes(conn)
        for t in tunes:
            tree.insert("", tk.END, values=(t["x"], t["title"], t["tune_type"], t["key"]))

    tk.Button(search_frame, text="Show All", command=show_all).pack(side="left", padx=4)

    #treeview display
        
    columns = ("X", "Title", "Type", "Key")  #table column names

    tree = ttk.Treeview(
        main_frame,
        columns=columns,
        show="headings"       #no blank first column
    )
    tree.pack(fill="both", expand=True, padx=8, pady=6)

    #set col headers and alignment
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="w")  #left aligned
        
    
    #book selection handler
        
    def on_book_select(event):
        #clear tree on each selection change
        for item in tree.get_children():
            tree.delete(item)

        sel = book_listbox.curselection()  #selected listbox index
        if not sel:
            return

        #text of selected items
        book_number = book_listbox.get(sel[0])
        header_label.config(text=f"Tunes in Book {book_number}")

        #tunes for that book
        try:
            tunes = analysis_module.get_tunes_by_book(conn, int(book_number))
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed: {e}")
            return

        #insert toons for that book
        for tune in tunes:
            tree.insert("", tk.END, values=(tune["x"], tune["title"], tune["tune_type"], tune["key"]))

    #bind listbox xselection event
    book_listbox.bind("<<ListboxSelect>>", on_book_select)
    

    #double click handler

    def show_tune_details(event):
        #find currently focused in treeview
        item = tree.focus()
        if not item:
            return

        #get the tunes x value
        x_value = tree.item(item)["values"][0]

        #load full tune details from db
        tune = analysis_module.get_tune_by_x(conn, x_value)
        if not tune:
            return

        #create popup window
        win = tk.Toplevel(root)
        win.title(f"Tune {x_value} Details")
        win.geometry("600x500")

        #title and header info
        tk.Label(win, text=tune["title"], font=("Arial", 16, "bold")).pack(pady=8)
        tk.Label(
            win,
            text=f"Type: {tune['tune_type']}    Key: {tune['key']}",
            font=("Arial", 12)
        ).pack()

        #text box containing full abc notation
        text = tk.Text(win, wrap="word", font=("Courier", 11))
        text.pack(fill="both", expand=True)
        text.insert("1.0", tune["notation"])  # Insert full notation at top

    #when double left click, tune detail popup
    tree.bind("<Double-1>", show_tune_details)

    #start the event loop
    root.mainloop()



#ui launch
def launch_ui(conn, analysis_module):
    
    #main.py can simply call launch_ui(). 
    start_ui(conn, analysis_module)
