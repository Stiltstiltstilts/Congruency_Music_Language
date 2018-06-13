#!/Users/Stilts/PsychoPyBuild/bin/python 
# -*- coding: utf-8 -*-

#####################
#####==IMPORTS==#####
#####################

import csv, os
import customFunctions as fun # my own function for preprocessing the text

#############################
#####==BASIC VARIABLES==#####
#############################

FGC = (1, 1, 1) #white
BGC = (0, 0, 0) #grey
TEXTSIZE = 42 #text size for stim (not instructions)
TEXTCORDS = (0, 0) #Centre of screen
beat_freq = 0.417 #2.4Hz
frameInterval = 0.0166667 #framerate.... CHECK THIS
sound_delay = .08 # 0.003 for processing command + .102 for soundcard/driver processing and sound coming out of earphones
trial_duration = 10 # seconds
probe_duration = 5 # seconds

_thisDir = os.path.abspath(os.path.dirname(__file__)) #change to local directory
os.chdir(_thisDir)

#####################
#####==STIMULI==#####
#####################

###===INSTRUCTIONS===###
part1Intro = fun.instImport('Stimuli/Instructions/Part1.txt')
part2Intro = fun.instImport('Stimuli/Instructions/Part2.txt')
part3Intro = fun.instImport('Stimuli/Instructions/Part3.txt')
bottom_text = fun.instImport('Stimuli/Instructions/bottom_text.txt')

###===SENTENCES===###
sub_ext_cong2 = fun.sentencePreProcess('Stimuli/Sentences/Subj_extracted_cong2.txt') 
sub_ext_cong3 = fun.sentencePreProcess('Stimuli/Sentences/Subj_extracted_cong3.txt')
sub_ext_incong2 = fun.sentencePreProcess('Stimuli/Sentences/Subj_extracted_incong2.txt')
sub_ext_incong3 = fun.sentencePreProcess('Stimuli/Sentences/Subj_extracted_incong3.txt')

obj_ext_cong2 = fun.sentencePreProcess('Stimuli/Sentences/Obj_extracted_cong2.txt') 
obj_ext_cong3 = fun.sentencePreProcess('Stimuli/Sentences/Obj_extracted_cong3.txt')
obj_ext_incong2 = fun.sentencePreProcess('Stimuli/Sentences/Obj_extracted_incong2.txt')
obj_ext_incong3 = fun.sentencePreProcess('Stimuli/Sentences/Obj_extracted_incong3.txt')

assorted_cong2 = fun.sentencePreProcess('Stimuli/Sentences/Assorted_cong2.txt')

prac_trials = fun.sentencePreProcess('Stimuli/Sentences/Practice_trials.txt')

###===PROBES===###
probe_mc_pos = fun.probePreProcess('Stimuli/Probes/MC_positive_probes.txt')
probe_mc_neg = fun.probePreProcess('Stimuli/Probes/MC_negative_probes.txt')
probe_rc_subpos_objneg = fun.probePreProcess('Stimuli/Probes/RC_subpos_objneg_probes.txt')
probe_rc_subneg_objpos = fun.probePreProcess('Stimuli/Probes/RC_subneg_objpos_probes.txt')
probe_ass_pos = fun.probePreProcess('Stimuli/Probes/Assorted_positive_probes.txt')
probe_ass_neg = fun.probePreProcess('Stimuli/Probes/Assorted_negative_probes.txt')

prac_probes = fun.probePreProcess('Stimuli/Probes/Practice_trial_probes.txt')

###===QUESTIONAIRE===###
gsi_part1 = fun.instImport('Stimuli/GSI_1-31.txt')
gsi_part2 = fun.instImport('Stimuli/GSI_32-38.txt')
gsi_part2_scales = [['0','1', '2', '3', '4-5', '6-9', '10+'],
                    ['0', '0.5', '1', '1.5', '2', '3-4', '5+'],
                    ['0', '1', '2', '3', '4-6', '7-10', '11+'], 
                    ['0', '0.5', '1', '2', '3', '4-6', '7+'], 
                    ['0', '0.5', '1', '2', '3-5', '6-9', '10+'], 
                    ['0', '1', '2', '3', '4', '5', '6+'],
                    ['0-15mins', '15-30mins', '30-60mins', '60-90mins', '2hrs', '2-3hrs', '4+hours']]
