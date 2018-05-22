#!/Users/Stilts/PsychoPyBuild/bin/python 
# -*- coding: utf-8 -*-

#####################
#####==IMPORTS==#####
#####################

import csv, os
import textPreProcess as txt

#############################
#####==BASIC VARIABLES==#####
#############################

FGC = (-1, -1, -1) #black
BGC = (0, 0, 0) #grey
TEXTSIZE = 42 #text size for stim (not instructions)
TEXTCORDS = (0, 0) #Centre of screen
TRIALREPEATS = 1 # each trial last for approx 35seeconds 
beatFreq = 0.417 #2.4Hz
frameInterval = 0.0166667 #framerate.... CHECK THIS
soundDelay = .105 # 0.003 for processing command + .102 for soundcard/driver processing and sound coming out of earphones

_thisDir = os.path.abspath(os.path.dirname(__file__)) #change to local directory
os.chdir(_thisDir)

#Instruction durations
condition_duration = 3 #duration for condition instructions prior to each trial
eye_duration = 2 #duration for prompt to close eyes

#####################
#####==STIMULI==#####
#####################

###===INSTRUCTIONS===###
# Part 1
with open('Stimuli/Instructions/Part1.txt', 'r') as f: #open stimuli file as object 
    part1Intro = f.readlines()
# Part 2
with open('Stimuli/Instructions/Part2.txt', 'r') as f: #open stimuli file as object 
    part2Intro = f.readlines()   

###===EXPERIMENTAL WORDS===###
# Subject extracted congruent binary
sub_ext_cong2 = []
with open('Stimuli/Subj_extracted_cong2.txt', 'r') as f: #open stimuli file as object 
    rawText = f.readlines()
# seperate the individual words and then turn underscore into spaces
for n in range(0, len(rawText)):
    temp = rawText[n][:].split(' ')
    sub_ext_cong2.append(temp)
temp = []
temp2 = []
for k in range(0, len(sub_ext_cong2)):
    for m in range(0, len(sub_ext_cong2[k][:])):
        temp.append(sub_ext_cong2[k][m].replace('_', ' '))
    temp2.append([temp])
    temp = []
sub_ext_cong2 = temp2

ControlWords = [] #create empty list for processed words
for n in range(0,len(d)):
    sen = d[n][0].split(' ') #going one line at a time spliting the sentence into seperate words
    ControlWords.append(sen)
###===BINARY===###
with open('WordList_Binary.txt', 'r') as f: #open stimuli file as object
    reader = csv.reader(f, delimiter='\t')
    d = list(reader)

BinaryWords = [] #create empty list for processed words
for n in range(0,len(d)):
    sen = d[n][0].split(' ') #going one line at a time spliting the sentence into seperate words
    BinaryWords.append(sen)
###===TERNARY===###
with open('WordList_Ternary.txt', 'r') as f: #open stimuli file as object
    reader = csv.reader(f, delimiter='\t')
    d = list(reader)

TernaryWords = [] #create empty list for processed words
for n in range(0,len(d)):
    sen = d[n][0].split(' ') #going one line at a time spliting the sentence into seperate words
    TernaryWords.append(sen)



