# Function Imports
from __future__ import division
from psychopy import core, visual, event
from random import shuffle, randint
from random import shuffle

# User-defined variables
colours = {'red':'v', 'blue':'b', 'green':'n', 'yellow':'m'} #{Text colour:Response key}
word_duration = 2
fix_duration_range = (1000,2000) # needs to be in milliseconds
iti_duration = 2
text_height = 1 # In degrees
text_colour = 'white'
text_font = 'Arial'
vb_offset = 0.01 #vertical blank
n_trials = 3
allowed_keys = [x for x in colours.values()]
response_duration = 4



# Trial list construction
congruent_list = [{'condition':'Congruent',
                    'word':colour.upper(), 
                    'colour':colour} for colour in colours] * (len(colours) * (len(colours) -1))
incongruent_list = [{'condition':'Incongruent',
                        'word':colour.upper(),
                        'colour':i_colour}
                        for i_colour in colours
                        for colour in colours
                        if i_colour != colour] * len(colours)
neutral_list = [{'condition':'Neutral',
                'word':'X' * len(colour_word),
                'colour':colour}
                for colour_word in colours
                for colour in colours] * (len(colours) -1)
                
trial_list =  congruent_list + incongruent_list + neutral_list
shuffle(trial_list)


# Start the experiment
try: 
    win = visual.Window(fullscr=False,
                    monitor='Laptop',
                    color='black',
                    units='deg',
                    allowGUI=False)
    word = visual.TextStim(win, text='dummy', color= 'Red', height=1, font='Arial')
    fixation = visual.TextStim(win, text='+', color='white', height=1, font='Arial')
    intro = visual.TextStim(win, text='press space', color= 'Red', height=1, font='Arial')
    start_response = []
    intro.draw()
    win.flip()
    
    core.wait(1)
    
    with open('log.txt', 'w') as log_file:
        log_file.write('Trial/t' +
                       'Condition/t' +
                       'Word/t' +
                       'Colour/t' +
                       'Response/t' +
                       'Accuracy/t' +
                       'RT/t' + '\n')
    
        for trial in trial_list[:n_trials]:
            response = None
            # Set fixation jitter
            fix_duration = randint(*fix_duration_range) / 1000 #asterisk does unpacking: takes one variable and splits it
        
            # Present fixation cross
            fixation.draw()
            fixation_onset = win.flip()
            visual.TextStim(win, text=trial['word'], color=trial['colour'], height=1, font='Arial').draw() #stroop stim
            while core.getTime() < (fixation_onset + fix_duration - vb_offset) : pass
            #Present word_duration
            word.color = trial['colour']
            word.text = trial['word']
            word.draw()
            word_onset = win.flip()
            fixation.draw()
            event.clearEvents()
            while core.getTime() < (word_onset + word_duration - vb_offset) : 
                if not response:
                    response = event.getKeys(timeStamped = True, keyList=allowed_keys)
            if not response: #only do this if no response
                win.flip()
                fixation.draw()
                while core.getTime() < (word_onset + response_duration):
                    response = event.waitKeys(maxWait=response_duration, timeStamped = True, keyList=allowed_keys)
                    if response:
                        break
            print(response)
        
            #Present fixation cross
            iti_onset = win.flip()
            if response:
                key_pressed, rt = response [0] #unpacking
                rt -= word_onset # rt minues word onset
                acc = int(key_pressed == colours[trial['colour']])
            else: 
                key_pressed = acc = rt = ''
            log_file.write('\t'.join( [str(trial_num+1),
                            trial['condition'],
                            trial['word'],
                            trial['colour'],
                            key_pressed,
                            str(acc),
                            str(rt)]) + '\n')
            log_file.flush()
            while core.getTime() < (iti_onset + iti_duration - vb_offset) : pass
        else:
            core.wait(2)
        
        

finally:
    win.close()




