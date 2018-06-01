#!/Users/Stilts/PsychoPyBuild/bin/python

################################################
################# Imports ######################
################################################
from psychopy import core, visual, logging, gui, event, prefs, data
import pyo
prefs.general['audioLib'] = ['pyo']
from psychopy import sound
from numpy.random import random, randint, normal, shuffle
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import os
import sys
#import itertools
import numpy as np
from constants import *

GlobalClock = core.Clock()  # Track time since experiment starts

################################################
############### Basic checks ###################
################################################
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
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName,)
if dlg.OK == False:
    core.quit()  # user pressed cancele
expInfo['date'] = data.getDateStr()

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
binary_beat = sound.Sound('binary_beat.wav', secs=-1)
binary_beat.setVolume(1)
ternary_beat = sound.Sound('ternary_beat.wav', secs=-1)
ternary_beat.setVolume(1)

# setup window
win = visual.Window(fullscr=True,
                monitor='Laptop',  
                units='deg',
                allowGUI=False)

trialClock = core.Clock()

# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

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
all_trials = data.TrialHandler(trialList = all_trials, nReps = 1, method = 'random', extraInfo = expInfo, name = 'all_trials') 
thisTrial = all_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

################################################
############## Run experiment ##################
################################################
try: 
    # Set up variables and trial objects etc
    message1 = visual.TextStim(win, pos=[0,+3], color=FGC, alignHoriz='center', name='topMsg', text="placeholder") 
    message2 = visual.TextStim(win, pos=[0,-3], color=FGC, alignHoriz='center', name='bottomMsg', text="placeholder") 
    fixation = visual.TextStim(win,  pos=[0,0], color=FGC, alignHoriz='center', text="+")
    endMessage = visual.TextStim(win,  pos=[0,0], color=FGC, alignHoriz='center', text="The end!")
    space_cont = visual.TextStim(win, pos=[0,0], color=FGC, text="Press space to continue")
    introText = visual.TextStim(win, pos=[0,0], color=FGC, text="Placeholder")
    word_stim_list = []
    for i in range(15): # setting up text_stimuli objects... 15 is the most words in the sent_stims
            exec( '{} = visual.TextStim(win, pos=[0,0], color=FGC, text="placeholder")'.format('word' + '_' + str(i+1)) ) # create text objects
            exec( 'word_stim_list.extend([{}])'.format(str('word' + '_' + str(i+1))) ) # putting them in word_stim_list
    probe_text = visual.TextStim(win, pos=[0,+3], color=FGC, alignHoriz='center', name='top_probe', text="placeholder")
    probe_text_lower = visual.TextStim(win, pos=[0,-3], color=FGC, alignHoriz='center', name='bottom_probe', text="yes or no?")
    clock = core.Clock()
    routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
    endExpNow = False  # flag for 'escape' or other condition => quit the exp

    # ========================== #
    # ==== START EXPERIMENT ==== #
    # ========================== #

    # ===== INSTRUCTIONS ====== #
    counter = 0
    while counter < len(part1Intro):
        if part1Intro[counter] == "sound":
            #sd.play(beat_inter)
            core.wait(5)
            #sd.stop()
        else:
            message1.setText(part1Intro[counter])
            if counter == 0:
                message2.setText(bottom_text[0])
            elif counter in range(1, (len(part1Intro) - 1)):
                message2.setText(bottom_text[1])
            else: 
                message2.setText(bottom_text[2])
        #display instructions and wait
        message1.draw()
        message2.draw() 
        win.logOnFlip(level=logging.EXP, msg='Display Instructions%d'%(counter+1))
        win.flip()
        #check for a keypress
        thisKey = event.waitKeys()
        if thisKey[0] in ['q','escape']:
            core.quit()
        elif thisKey[0] == 'backspace':
            counter -= 1
        else:
            counter += 1

    # ===== TRIALS ====== #
    for trial in all_trials:  
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        probe_resp = event.BuilderKeyResponse()
        probe_cont_resp = event.BuilderKeyResponse()

        # initialize trial components list
        trialComponents = []

        # add auditory stimuli component
        if beat_type == 'binary_beat':
            beat_stim = binary_beat
        elif beat_type == 'ternary_beat':
            beat_stim = ternary_beat
        trialComponents.extend([beat_stim]) # add beat stim to trialComponents list

        # add text stimuli components
        for i in range(len(sent_stim)): # for i in range(len(trial['sent_stim'])):
            exec('trialComponents.extend([{}])'.format('word' + '_' + str(i+1)))
            word_stim_list[i].setText(sent_stim[i])
            
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        #routineTimer.add(trial_duration) # need to add the amount of time for the trial
        # update component parameters for each repeat
        # keep track of which components have finished
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        t = 0
        trialClock.reset()  # clock
        frameN = -1
        # -------Start Routine "trial"-------
        while continueRoutine: # and routineTimer.getTime() > 0
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            
            # start/stop beat_stim   
            if t >= 0.0 + sound_delay and beat_stim.status == NOT_STARTED:
                # keep track of start time/frame for later
                beat_stim.tStart = t
                beat_stim.frameNStart = frameN  # exact frame index
                beat_stim.play()  # start the sound (it finishes automatically)
            frameRemains = 0.0 + sound_delay + trial_duration - win.monitorFramePeriod * 0.75  # most of one frame period left
            if beat_stim.status == STARTED and t >= frameRemains:
                beat_stim.stop()  # stop the sound (if longer than duration)
            
            # iterate through sentence text stimuli     
            for word_index in range(len(sent_stim)):
                if t >= word_index * beat_freq and word_stim_list[word_index].status == NOT_STARTED:
                    # keep track of start time/frame for later
                    word_stim_list[word_index].tStart = t
                    word_stim_list[word_index].frameNStart = frameN  # exact frame index
                    word_stim_list[word_index].setAutoDraw(True)
                frameRemains = (beat_freq * word_index) + beat_freq - win.monitorFramePeriod * 0.75  # most of one frame period left
                if word_stim_list[word_index].status == STARTED and t >= frameRemains:
                    word_stim_list[word_index].setAutoDraw(False)

            # display probe text
            if t >= len(sent_stim) * beat_freq and probe_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                probe_text.tStart = t
                probe_text.frameNStart = frameN  # exact frame index
                probe_text.setAutoDraw(True)
            frameRemains = (beat_freq * len(trial['sent_stim'])) + probe_duration - win.monitorFramePeriod * 0.75  # most of one frame period left
            if probe_text.status == STARTED and t >= frameRemains:
                probe_text.setAutoDraw(False)

            # check for response keys for probe
            if t >= (len(sent_stim) * beat_freq) and probe_resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                probe_resp.tStart = t
                probe_resp.frameNStart = frameN  # exact frame index
                probe_resp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(probe_resp.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = (len(sent_stim) * beat_freq) + probe_duration - win.monitorFramePeriod * 0.75  # most of one frame period left
            if probe_resp.status == STARTED and t >= frameRemains:
                probe_resp.status = STOPPED
            if probe_resp.status == STARTED:
                theseKeys = event.getKeys(keyList=['y', 'n'])
                
                # log response etc:
                if len(theseKeys) > 0:  # at least one key was pressed
                    probe_resp.keys = theseKeys[-1]  # just the last key pressed
                    probe_resp.rt = probe_resp.clock.getTime()
                    # was this 'correct'?
                    if (probe_resp.keys == "y") and ( (pos_neg == 'positive') or (pos_neg == 'subneg_objpos' and clause == 'relative_clause' and extraction == 'object extracted') ):
                        probe_resp.corr = 1
                    else:
                        probe_resp.corr = 0

            # display "press space to continue text"
            if t >= (len(sent_stim) * beat_freq) + probe_duration and space_cont.status == NOT_STARTED:
                # keep track of start time/frame for later
                space_cont.tStart = t
                space_cont.frameNStart = frameN  # exact frame index
                space_cont.setAutoDraw(True)
                # keyboard checking is just starting
                win.callOnFlip(probe_cont_resp.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
                if probe_cont_resp.status == STARTED:
                    theseKeys = event.getKeys(keyList=['space'])
                    if "space" in theseKeys:
                        space_cont.setAutoDraw(False)
                        continueRoutine = False

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        beat_stim.stop()  # ensure sound has stopped at end of routine
        #thisExp.nextEntry()
        core.wait(1)

finally:
    win.close()
    