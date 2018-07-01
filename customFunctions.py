
#####################
#####==IMPORTS==#####
#####################

import os
import numpy as np
from psychopy import core, visual, event, data, logging
#from constants import *

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

def sentencePreProcess(path, congruency=None, beat_type=None, extraction=None):
    """
    stimPreProcess is a function for importing sentences from a text file, and then 1) making each sentence a list containing strings for each word, 
    and 2) converting underscores, which code for double words, into a space character within the string
        required inputs:
                        path: path of input file (as .txt)
                        congruency: 'congruent' or 'incongruent'
                        beat_type: 'binary_beat' or 'ternary_beat'
                        extraction: 'subject' or 'object'
        outputs: 
                        Variable with processed data as a list

    """
    temp2 = []
    with open(path, 'r') as f: #open stimuli file as object 
        rawText = f.readlines()
    # seperate the individual words and then turn underscore into spaces
    for n in range(0, len(rawText)):
        temp = rawText[n][:].replace('\n', '') # getting rid of the line break thing
        temp = temp.split(' ') # splitting the sentence up by spaces
        temp2.append(temp)
    temp = []
    temp3 = []
    for sentence in range(0, len(temp2)): # iterate sentences
        for word in range(0, len(temp2[sentence][:])): # iterate words
            word_stim = temp2[sentence][word].replace('_', ' ') # cleaning off the underscore and turning it into space
            temp.append(word_stim) 
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
    if "positive" in os.path.basename(path):
        pos_neg = 'positive'
    elif "negative" in os.path.basename(path):
        pos_neg = 'negative'
    elif "subneg" in os.path.basename(path): # relative clauses change which statement is correct based on obj or sub extracted
        pos_neg = 'subneg_objpos'
    elif "subpos" in os.path.basename(path):
        pos_neg = 'subpos_objneg'
    else:
        pos_neg = None
    # main or relative clause
    if "MC" in os.path.basename(path):
        clause = 'main_clause'
    elif "RC" in os.path.basename(path):
        clause = 'relative_clause'
    else:
        clause = 'other'  

    final_output = []
    for n in range(len(processed_text)):
        temp = {'probe':processed_text[n].replace('\n', ''),
                        'pos_neg': pos_neg,
                        'clause': clause,
                        'probe_n': n,}
        final_output.append(temp)
    return final_output

def customHanning(M, floor):
    """ 
    this is a function to create a custom hanning window with a non-zero floor, specified by the variable 'floor'
    for example M = 0.2 means creating a hanning window with values between .2 and 1
    """
    a = 0.5 + 0.5*floor
    b = 0.5 - 0.5*floor
    M = int(M)
    custom_hanning_window = [a - b*np.cos(2 * x * np.pi /(M-1)) for x in range(M)]

    return custom_hanning_window

def instructionDelivery(text_list, bottom_text):
    """
    etc

    """
    counter = 0
    while counter < len(text_list):
        message1.setText(text_list[counter])
        if counter == 0:
            message2.setText(bottom_text[0])
        elif counter in range(1, (len(text_list) - 1)):
            message2.setText(bottom_text[1])
        else: 
            message2.setText(bottom_text[2])
        #display instructions and wait
        message1.draw()
        message2.draw() 
        win.logOnFlip(level=logging.EXP, msg='Display Instructions{}'.format(counter+1))
        win.flip()
        #check for a keypress
        thisKey = event.waitKeys()
        if thisKey[0] in ['q','escape']:
            core.quit()
        elif thisKey[0] == 'backspace':
            counter -= 1
        else:
            counter += 1
