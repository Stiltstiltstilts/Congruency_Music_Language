#!/usr/bin/env python2

################################################
################# Imports ######################
################################################
from psychopy import core, visual, logging, gui, event, parallel, prefs, data
import sounddevice as sd
import soundfile as sf
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
print(os.path.join(os.path.dirname(__file__), '..'))
print(os.path.abspath(os.path.dirname(__file__)))
### Check port info IF EEG
    #port = parallel.ParallelPort(address=0xd050) 
    #port.setData(0)    

################################################
####### Collect experiment session info ########
################################################
#Exp name
#Define experiment info
#prompt user for info
# Add DateTime stamp
# Create filename

################################################
################ Setup logfile #################
################################################


################################################
################# Variables ####################
################################################
# setup Auditory sounds
# setup window
# setup and load instructions text stimuli
# setup and load experimental text stimuli


################################################
########## Trial list construction #############
################################################


################################################
############## Run experiment ##################
################################################