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
import os, sys, itertools  
#from constants import *

GlobalClock = core.Clock() # Track time since experiment starts


################################################
############### Basic checks ###################
################################################
### Setting of sound driver stuff?
sd.default.device = 12 # Audigy ASIO driver for 16bit 48000HZ
sd.default.latency = ('low','low')
### check relative paths correct
_thisDir = os.path.abspath(os.path.dirname(__file__)))
os.chdir(_thisDir)

################################################
####### Collect experiment session info ########
################################################
#Exp name
expName = 'MeterSyntax'
#Define experiment info
expInfo = {'session':'001', 'participant':'001', 'order':1, 'handedness':'', 'gender':''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
# Create filename for data file (absolute path + name)
filename = _thisDir + os.sep + 'data/{0}'.format(expInfo['participant'])

################################################
################ Setup logfile #################
################################################
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DATA)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

################################################
################# Variables ####################
################################################
####====Auditory Stimuli====####
beat_stim, sd.default.samplerate = sf.read('pure_tone3.wav')
beat_inter, sd.default.samplerate = sf.read('tone_interruption.wav')
# setup window
win = visual.Window(fullscr=True,
                monitor='Laptop',
                units='deg',
                allowGUI=False)
# setup and load instructions text stimuli
# setup and load experimental text stimuli


################################################
########## Trial list construction #############
################################################


################################################
############## Run experiment ##################
################################################