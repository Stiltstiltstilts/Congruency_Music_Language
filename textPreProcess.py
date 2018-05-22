
"""
instImport is a function for importing instruction text to be used in the experiment and does the required processing
    required inputs:
                    path: path of input file (as .txt)
    outputs: 
                    Variable with processed data as a list

"""
def instImport(path):
    # probably also write checks that the path points to a .txt and the outputName is a string

    with open(path, 'r') as f: #open file as object 
        processed_text = f.readlines()
    return processed_text

"""
stimPreProcess is a function for importing sentences from a text file, and then 1) making each sentence a list containing strings for each word, 
and 2) converting underscores, which code for double words, into a space character within the string
    required inputs:
                    path: path of input file (as .txt)
    outputs: 
                    Variable with processed data as a list

"""

def stimPreProcess(path):
    temp2 = []
    with open(path, 'r') as f: #open stimuli file as object 
        rawText = f.readlines()
    # seperate the individual words and then turn underscore into spaces
    for n in range(0, len(rawText)):
        temp = rawText[n][:].split(' ')
        temp2.append(temp)
    temp = []
    temp3 = []
    for sentence in range(0, len(temp2)):
        for word in range(0, len(temp2[sentence][:])):
            temp.append(temp2[sentence][word].replace('_', ' '))
        temp3.append(temp)
        temp = []
    return temp3
