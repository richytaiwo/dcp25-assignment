import os # walking directories and file paths

#look for all .abc files in a directory

def load_abc_files(base_dir):
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

#load contents into abc file

def load_abc_file(filename):
    with open(filename, 'r', encoding='latin-1') as f:
        lines = f.readlines()  # read file into list of lines
    return lines


#parse a single tunes abc lines into structured directory

def parse_tune(tune_lines):
    #default tune structure
    tune = {
        'X': None,
        'title': None,
        'alt_title': None,
        'tune_type': None,
        'key': None,
        'notation': '\n'.join(tune_lines)  #store full text as one big string
    }

    title_count = 0  #track how many ts weve counted
    
    #process tune line by line
    for line in tune_lines:
        line = line.strip()  #trail space/ newline removal
        
        #x is the tune index
        if line.startswith('X:'):
            tune['X'] = line[2:].strip()

        #t is the primary or alt title
        elif line.startswith('T:'):
            title_count += 1

            if title_count == 1:
                tune['title'] = line[2:].strip()      # First T: is main title
            elif title_count == 2:
                tune['alt_title'] = line[2:].strip()  # Second T: is alt title

        #r is the tune type
        elif line.startswith('R:'):
            tune['tune_type'] = line[2:].strip()

        #k is the musical key
        elif line.startswith('K:'):
            tune['key'] = line[2:].strip()

    return tune  #completed tune directory

#parse entire abc file with alot of tunes

def parse_all_tunes(lines):
    tunes = []   # Final list of parsed tunes
    current = [] # Accumulates lines belonging to the current tune

    for line in lines:
        
        #if new tune header starts with x start a new block
            #if creating a tune, start a new one
            if current:
                tunes.append(parse_tune(current))
                current = []

            #start capturing lines for new tunes
            current.append(line)

        #if in a tune block
        elif current:
            
            #blank line means end of tune
            if line.strip() == '':
                tunes.append(parse_tune(current))  #finish tune
                current = []                      #reset for next tune
            else:
                current.append(line)  #still in same tune

    #iff file ended without a final blank line, add last tune
    if current:
        tunes.append(parse_tune(current))

    return tunes  #return list of parsed tune directories