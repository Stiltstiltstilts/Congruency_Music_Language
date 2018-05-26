
#####################
#####==IMPORTS==#####
#####################

import os

def instImport(path):
    """
    instImport is a function for importing instruction text to be used in the experiment and does the required processing
        required inputs:
                        path: path of input file (as .txt)
        outputs: 
                        Variable with processed data as a list

    """
    # probably also write checks that the path points to a .txt and the outputName is a string

    with open(path, 'r') as f: #open file as object 
        processed_text = f.readlines()
    return processed_text

def sentencePreProcess(path):
    """
    stimPreProcess is a function for importing sentences from a text file, and then 1) making each sentence a list containing strings for each word, 
    and 2) converting underscores, which code for double words, into a space character within the string
        required inputs:
                        path: path of input file (as .txt)
        outputs: 
                        Variable with processed data as a list

    """
    temp2 = []
    with open(path, 'r') as f: #open stimuli file as object 
        rawText = f.readlines()
    # seperate the individual words and then turn underscore into spaces
    for n in range(0, len(rawText)):
        temp = rawText[n][:].split(' ')
        temp2.append(temp)
    #Get other info  
    # beat   
    if "2" in os.path.basename(path):
        beat_type = 'binary_beat'
    elif "3" in os.path.basename(path):
        beat_type = 'ternary_beat'
    # congruency
    if "cong" and not "incong" in os.path.basename(path):
        congruency = 'congruent'
    elif "incong" in os.path.basename(path):
        congruency = 'incongruent'
    #obj/sub
    if "Obj" in os.path.basename(path):
        extraction = 'object extracted'
    elif "Subj" in os.path.basename(path):
        extraction = 'subject extracted'
    else:
        extraction = 'other'
    temp = []
    temp3 = []
    for sentence in range(0, len(temp2)): # iterate sentences
        for word in range(0, len(temp2[sentence][:])): # iterate words
            temp.append(temp2[sentence][word].replace('_', ' '))
        stim_data = {'sent_stim':temp, 'beat_type':beat_type, 
                    'congruency':congruency, 'extraction': extraction, 'sent_number': sentence,}
        temp3.append(stim_data)
        temp = []

    return temp3

def probePreProcess(path):
    """
    instImport is a function for importing probes in txt file and outputting dictionary with probe and metadata
        required inputs:
                        path: path of input file (as .txt)
        outputs: 
                        Variable with processed data as a list of dictionaries

    """
    # probably also write checks that the path points to a .txt and the outputName is a string

    with open(path, 'r') as f: #open file as object 
        processed_text = f.readlines()
    #Get other info  
    # pos or neg   
    if "pos" and not "objpos" in os.path.basename(path):
        pos_neg = 'positive'
    elif "neg" and not "subneg" in os.path.basename(path):
        pos_neg = 'negative'
    elif "subneg" in os.path.basename(path): # relative clauses change which statement is correct based on obj or sub extracted
        pos_neg = "subneg_objpos"
    elif "subpos" in os.path.basename(path):
        pos_neg = "subpos_objneg"
    # main or relative claus
    if "MC" in os.path.basename(path):
        clause = 'main_clause'
    elif "RC" in os.path.basename(path):
        clause = 'relative_clause'
    else:
        clause = 'other'  

    final_output = []
    for n in range(len(processed_text)):
        temp = {'probe':processed_text[n],
                        'pos_neg': pos_neg,
                        'clause': clause,
                        'probe_n': n,}
        final_output.append(temp)
    return final_output


def takeSecond(elem):
    """ this is a function to pass as a key argument for sorting shit"""
    return elem[0]
