import os # walking directories and file paths

#look for all .abc files in a directory

def load_abc_files(base_dir):
    """
    Recursively find all .abc files under base_dir.
    Returns a list of tuples: (filepath, book_folder_name)
    """
    abc_files = []  # collect filepath, book pairs
    
    
    #os.walk checks every folder, subfolder and file starting from base dir
     for root, dirs, files in os.walk(base_dir):

        for file in files:
            # look for files that end with abc only
            if file.endswith('.abc'):
                # create the paths: /root/subfolder/file.abc
                filepath = os.path.join(root, file)

                # book identifier is the name of the folder containing the ABC file
                book = os.path.basename(os.path.dirname(filepath))

                # save
                abc_files.append((filepath, book))

    return abc_files #return list of filess