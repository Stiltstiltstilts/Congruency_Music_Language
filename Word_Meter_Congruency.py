#!/Users/Stilts/PsychoPyBuild/bin/python

################################################
################# Imports ######################
################################################
from psychopy import core, visual, logging, gui, event, parallel, prefs, data
import soundfile as sf
import sounddevice as sd
prefs.general['audioLib'] = ['sounddevice']
from numpy.random import random, randint, normal, shuffle
from psychopy import sound
import os
import sys
import itertools
from constants import *

GlobalClock = core.Clock()  # Track time since experiment starts

"""
################################################
############### Basic checks ###################
################################################
# Setting of sound driver stuff?
sd.default.device = 12 # Audigy ASIO driver for 16bit 48000HZ
sd.default.latency = ('low','low')
# check relative paths correct
_thisDir = os.path.abspath(os.path.dirname(__file__))
os.chdir(_thisDir)

################################################
####### Collect experiment session info ########
################################################
# Exp name
expName = 'MeterSyntax'
# Define experiment info
expInfo = {'session':'001', 'participant':'001',
    'order':1, 'handedness':'', 'gender':''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName,
                      date=data.getDateStr(),)
if dlg.OK == False:
    core.quit()  # user pressed cancel

# Create filename for data file (absolute path + name)
filename = _thisDir + os.sep + 'data/{0}'.format(expInfo['participant'])

################################################
################ Setup logfile #################
################################################
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DATA)
# this outputs to the screen, not a file
logging.console.setLevel(logging.WARNING)

################################################
################# Variables ####################
################################################

####====Auditory Stimuli====####
beat_stim, sd.default.samplerate = sf.read('pure_tone3.wav')
beat_inter, sd.default.samplerate = sf.read('tone_interruption.wav')
# setup window

win = visual.Window(fullscr=True,
                monitor='Laptop',  ### can I set this up in the constants file?
                units='deg',
                allowGUI=False)
# setup and load instructions text stimuli
# setup and load experimental text stimuli
"""

################################################
########## Trial list construction #############
################################################
############ main sentences ############
main_conditions = [sub_ext_cong2, sub_ext_incong2, obj_ext_cong2, obj_ext_incong2,
                 sub_ext_cong3, sub_ext_incong3, obj_ext_cong3,  obj_ext_incong3]  # first half binary second half ternary
nSentences = len(sub_ext_cong2) # should write an exception error check thing to check that all main conditions have same length...
main_sentence_chunk_size = int(nSentences / len(main_conditions)) # chunk: how many sentences per condition
main_condition_index = list(range(len(main_conditions))) * main_sentence_chunk_size # list of indexes for main_conditions, length of nProbes
shuffle(main_condition_index)  # randomise
main_condition_list = [ (i, main_conditions[main_condition_index[i]][i]) for i in range(nSentences) ] #create list of tuples containing [0]index and [1] probes, in original order

############ main probes ############
main_probes = [probe_mc_pos, probe_mc_neg,
               probe_rc_subpos_objneg, probe_rc_subneg_objpos]
nProbes = len(probe_mc_pos) # how many probes
main_probe_chunk_size = int(nProbes / len(main_probes)) # chunk: how many sentences per probe
main_probe_index = list(range(len(main_probes))) * main_probe_chunk_size # list of indexes for main_probes, length of nProbes
shuffle(main_probe_index) # randomise
main_probe_list = [ (i, main_probes[main_probe_index[i]][i]) for i in range(nProbes) ] #create list of tuples containing [0]index and [1] probes, in original order

trial_list = []  # initialising

############ Assorted sentences ############
assorted_condition_list = [ (i, assorted_cong2[i]) for i in range(len(assorted_cong2)) ] 

############ Assorted probes ############
assorted_probes = [probe_ass_neg, probe_ass_pos]
n_ass_probes = len(probe_ass_neg)
assorted_probe_chunk_size = int(n_ass_probes / len(assorted_probes))
assorted_probe_index = list(range(len(assorted_probes))) * assorted_probe_chunk_size
shuffle(assorted_probe_index)
assorted_probe_list = [ (i,assorted_probes[assorted_probe_index[i]][i]) for i in range(len(assorted_cong2)) ] 

############ Combining stuff ############
main_trials = [ {**main_condition_list[i][1], **main_probe_list[i][1]} for i in range(len(main_condition_list)) ]
assorted_trials = [ {**assorted_condition_list[i][1], **assorted_probe_list[i][1]} for i in range(len(assorted_condition_list)) ]
all_trials = main_trials
all_trials.extend(assorted_trials)
shuffle(all_trials)

################################################
############## Run experiment ##################
################################################
