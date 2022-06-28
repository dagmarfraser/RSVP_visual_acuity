#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.1),
    on June 28, 2022, at 19:08
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLatencyMode'] = '0'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.1'
expName = 'rsvp_EEG_VA'  # from the Builder filename that created this script
expInfo = {'SONA_number': '', 'Age': '', 'Gender': ''}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['SONA_number'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\zdats\\OneDrive\\Documents\\masters research project\\psychoPY_project\\rsvp_EEG_VA\\rsvp_EEG_VA_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 720], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='deg')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "loading_stimuli"
loading_stimuliClock = core.Clock()

# Initialize components for Routine "instruc_practice"
instruc_practiceClock = core.Clock()
text_instructions1 = visual.TextStim(win=win, name='text_instructions1',
    text='',
    font='Arial',
    units='deg', pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "instruc_practise_2"
instruc_practise_2Clock = core.Clock()
text_instructions2 = visual.TextStim(win=win, name='text_instructions2',
    text='',
    font='Arial',
    units='deg', pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "set_variables_template"
set_variables_templateClock = core.Clock()
previous_target_letter = 'A'
instruc_repeat_template = 'This is the initial template generation part of this visual acuity test. Please cover your RIGHT eye with your hand so that you are looking through your LEFT eye only.\n\n Press ENTER when you are ready to continue.'

# Initialize components for Routine "set_instruc_template"
set_instruc_templateClock = core.Clock()

# Initialize components for Routine "instruc_start_template"
instruc_start_templateClock = core.Clock()
text_repeat_template = visual.TextStim(win=win, name='text_repeat_template',
    text='',
    font='Arial',
    units='deg', pos=(0, 0), height=0.5, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
key_resp_10 = keyboard.Keyboard()

# Initialize components for Routine "instruc_block_template"
instruc_block_templateClock = core.Clock()
new_block_text = "This is the start of a new block."
text_2 = visual.TextStim(win=win, name='text_2',
    text=new_block_text,
    font='Arial',
    units='deg', pos=(0, 0), height=0.5, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "rsvp_setup_template"
rsvp_setup_templateClock = core.Clock()
letters = ['C','D','H','K','N','F','R','S','V','Z']

# Initialize components for Routine "instruc_trial"
instruc_trialClock = core.Clock()
ENTER_2 = visual.TextStim(win=win, name='ENTER_2',
    text='Press SPACE BAR when ready',
    font='Arial',
    units='deg', pos=[0,-0.3], height=1.0, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixation_text = visual.TextStim(win=win, name='fixation_text',
    text='+',
    font='Arial',
    units='deg', pos=(0, 0), height=1.0, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "stream"
streamClock = core.Clock()
stimuli = visual.TextStim(win=win, name='stimuli',
    text='',
    font='Arial',
    units='deg', pos=(0, 0), height=1.0, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "question"
questionClock = core.Clock()
Recog_text = visual.TextStim(win=win, name='Recog_text',
    text='What letter did you see?\n\nPlease type only the letter and nothing else\n',
    font='Arial',
    units='deg', pos=[0,3], height=0.5, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
textbox = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),units='deg',     letterHeight=0.5,
     size=(2,2), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor='white', borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox',
     autoLog=True,
)
click_text = visual.TextStim(win=win, name='click_text',
    text='click here to continue',
    font='Arial',
    units='deg', pos=[0,-3], height=1.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
click = visual.Rect(
    win=win, name='click',units='deg', 
    width=(12, 2)[0], height=(12, 2)[1],
    ori=0.0, pos=(0, -3), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor=None,
    opacity=0.0, depth=-4.0, interpolate=True)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "set_variables"
set_variablesClock = core.Clock()
instruc_repeat = 'This is the first part of the visual acuity test. Please cover your RIGHT eye with your hand so that you are looking through your LEFT eye only.\n\n Press ENTER when you are ready to continue.'

# Initialize components for Routine "set_instruc"
set_instrucClock = core.Clock()

# Initialize components for Routine "instruc_start_exp"
instruc_start_expClock = core.Clock()
text_repeat = visual.TextStim(win=win, name='text_repeat',
    text='',
    font='Arial',
    units='deg', pos=(0, 0), height=0.5, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "instruc_block"
instruc_blockClock = core.Clock()
new_block_text = "This is the start of a new block."
text_start_blocks = visual.TextStim(win=win, name='text_start_blocks',
    text=new_block_text,
    font='Arial',
    units='deg', pos=(0, 0), height=0.5, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "rsvp_setup"
rsvp_setupClock = core.Clock()
letters = ['C','D','H','K','N','F','R','S','V','Z']

# Initialize components for Routine "instruc_trial"
instruc_trialClock = core.Clock()
ENTER_2 = visual.TextStim(win=win, name='ENTER_2',
    text='Press SPACE BAR when ready',
    font='Arial',
    units='deg', pos=[0,-0.3], height=1.0, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixation_text = visual.TextStim(win=win, name='fixation_text',
    text='+',
    font='Arial',
    units='deg', pos=(0, 0), height=1.0, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "stream"
streamClock = core.Clock()
stimuli = visual.TextStim(win=win, name='stimuli',
    text='',
    font='Arial',
    units='deg', pos=(0, 0), height=1.0, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "question"
questionClock = core.Clock()
Recog_text = visual.TextStim(win=win, name='Recog_text',
    text='What letter did you see?\n\nPlease type only the letter and nothing else\n',
    font='Arial',
    units='deg', pos=[0,3], height=0.5, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
textbox = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),units='deg',     letterHeight=0.5,
     size=(2,2), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor='white', borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox',
     autoLog=True,
)
click_text = visual.TextStim(win=win, name='click_text',
    text='click here to continue',
    font='Arial',
    units='deg', pos=[0,-3], height=1.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
click = visual.Rect(
    win=win, name='click',units='deg', 
    width=(12, 2)[0], height=(12, 2)[1],
    ori=0.0, pos=(0, -3), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor=None,
    opacity=0.0, depth=-4.0, interpolate=True)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "loading_stimuli"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
loading_stimuliComponents = []
for thisComponent in loading_stimuliComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
loading_stimuliClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "loading_stimuli"-------
while continueRoutine:
    # get current time
    t = loading_stimuliClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=loading_stimuliClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in loading_stimuliComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "loading_stimuli"-------
for thisComponent in loading_stimuliComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "loading_stimuli" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruc_practice"-------
continueRoutine = True
# update component parameters for each repeat
instructions_1 = "Thank you for taking part in this study.\n\nIn the following trials, your task will be to recognise a letter presented within a series of numbers, known as a stream. Each trial will begin with a fixation cross + which indicates the centre of the screen where the next stream will appear. \n\nOnce the stream has been presented, you will be asked to enter the letter that you saw. If you did not see a letter, please leave the field blank.\n\n \n\nOnce you have read and understood these instructions please press “ENTER” to continue."
text_instructions1.setText(instructions_1)
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
instruc_practiceComponents = [text_instructions1, key_resp_4]
for thisComponent in instruc_practiceComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruc_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruc_practice"-------
while continueRoutine:
    # get current time
    t = instruc_practiceClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruc_practiceClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_instructions1* updates
    if text_instructions1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_instructions1.frameNStart = frameN  # exact frame index
        text_instructions1.tStart = t  # local t and not account for scr refresh
        text_instructions1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_instructions1, 'tStartRefresh')  # time at next scr refresh
        text_instructions1.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['return'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruc_practiceComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruc_practice"-------
for thisComponent in instruc_practiceComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()
# the Routine "instruc_practice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruc_practise_2"-------
continueRoutine = True
# update component parameters for each repeat
instructions_2 = "The letters and numbers presented in the streams will vary in size from trial to trial. We expect there to be trials in which you cannot recognise the letter in the stream. \n\nThis experiment consists of two parts. In the first part, we will ask you to cover your RIGHT eye, so that you are looking through your LEFT eye. Vice versa for the second part. If you wish to leave the experiment at any point, please communicate this to the experimenter.\n\nOnce you have read and understood these instructions please press 'ENTER' to continue."
text_instructions2.setText(instructions_2)
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
instruc_practise_2Components = [text_instructions2, key_resp_5]
for thisComponent in instruc_practise_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruc_practise_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruc_practise_2"-------
while continueRoutine:
    # get current time
    t = instruc_practise_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruc_practise_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_instructions2* updates
    if text_instructions2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_instructions2.frameNStart = frameN  # exact frame index
        text_instructions2.tStart = t  # local t and not account for scr refresh
        text_instructions2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_instructions2, 'tStartRefresh')  # time at next scr refresh
        text_instructions2.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['return'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruc_practise_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruc_practise_2"-------
for thisComponent in instruc_practise_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.nextEntry()
# the Routine "instruc_practise_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "set_variables_template"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
set_variables_templateComponents = []
for thisComponent in set_variables_templateComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
set_variables_templateClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "set_variables_template"-------
while continueRoutine:
    # get current time
    t = set_variables_templateClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=set_variables_templateClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in set_variables_templateComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "set_variables_template"-------
for thisComponent in set_variables_templateComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "set_variables_template" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
eyes_template = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('eyes_template.csv'),
    seed=None, name='eyes_template')
thisExp.addLoop(eyes_template)  # add the loop to the experiment
thisEyes_template = eyes_template.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEyes_template.rgb)
if thisEyes_template != None:
    for paramName in thisEyes_template:
        exec('{} = thisEyes_template[paramName]'.format(paramName))

for thisEyes_template in eyes_template:
    currentLoop = eyes_template
    # abbreviate parameter names if possible (e.g. rgb = thisEyes_template.rgb)
    if thisEyes_template != None:
        for paramName in thisEyes_template:
            exec('{} = thisEyes_template[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "set_instruc_template"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    set_instruc_templateComponents = []
    for thisComponent in set_instruc_templateComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    set_instruc_templateClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "set_instruc_template"-------
    while continueRoutine:
        # get current time
        t = set_instruc_templateClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=set_instruc_templateClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in set_instruc_templateComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "set_instruc_template"-------
    for thisComponent in set_instruc_templateComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    instruc_repeat_template = instruc_repeat_template
    
    if previous_target_letter != 'A':
        instruc_repeat_template = 'This is the second part of the templating phase. Please cover your LEFT eye with your hand so that you are looking through your RIGHT eye only.\n\n Press ENTER when you are ready to continue.'
    # the Routine "set_instruc_template" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "instruc_start_template"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_repeat_template.setText(instruc_repeat_template)
    key_resp_10.keys = []
    key_resp_10.rt = []
    _key_resp_10_allKeys = []
    # keep track of which components have finished
    instruc_start_templateComponents = [text_repeat_template, key_resp_10]
    for thisComponent in instruc_start_templateComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instruc_start_templateClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instruc_start_template"-------
    while continueRoutine:
        # get current time
        t = instruc_start_templateClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instruc_start_templateClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_repeat_template* updates
        if text_repeat_template.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_repeat_template.frameNStart = frameN  # exact frame index
            text_repeat_template.tStart = t  # local t and not account for scr refresh
            text_repeat_template.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_repeat_template, 'tStartRefresh')  # time at next scr refresh
            text_repeat_template.setAutoDraw(True)
        
        # *key_resp_10* updates
        if key_resp_10.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_10.frameNStart = frameN  # exact frame index
            key_resp_10.tStart = t  # local t and not account for scr refresh
            key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
            key_resp_10.status = STARTED
            # keyboard checking is just starting
            key_resp_10.clock.reset()  # now t=0
        if key_resp_10.status == STARTED:
            theseKeys = key_resp_10.getKeys(keyList=['return'], waitRelease=False)
            _key_resp_10_allKeys.extend(theseKeys)
            if len(_key_resp_10_allKeys):
                key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
                key_resp_10.rt = _key_resp_10_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instruc_start_templateComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instruc_start_template"-------
    for thisComponent in instruc_start_templateComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_10.keys in ['', [], None]:  # No response was made
        key_resp_10.keys = None
    eyes_template.addData('key_resp_10.keys',key_resp_10.keys)
    if key_resp_10.keys != None:  # we had a response
        eyes_template.addData('key_resp_10.rt', key_resp_10.rt)
    # the Routine "instruc_start_template" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "instruc_block_template"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    instruc_block_templateComponents = [text_2]
    for thisComponent in instruc_block_templateComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instruc_block_templateClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instruc_block_template"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = instruc_block_templateClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instruc_block_templateClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instruc_block_templateComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instruc_block_template"-------
    for thisComponent in instruc_block_templateComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    trials_template = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditions_template.csv'),
        seed=None, name='trials_template')
    thisExp.addLoop(trials_template)  # add the loop to the experiment
    thisTrials_template = trials_template.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_template.rgb)
    if thisTrials_template != None:
        for paramName in thisTrials_template:
            exec('{} = thisTrials_template[paramName]'.format(paramName))
    
    for thisTrials_template in trials_template:
        currentLoop = trials_template
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_template.rgb)
        if thisTrials_template != None:
            for paramName in thisTrials_template:
                exec('{} = thisTrials_template[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "rsvp_setup_template"-------
        continueRoutine = True
        # update component parameters for each repeat
        length=15
        iNum = 0
        
        tar_pos=randint(6, 9)
        # fill stream with numbers
        rsvp_list=[]
        while len(rsvp_list) != length:
            iNum = randint(1,9)
            if not rsvp_list:
                rsvp_list.append(iNum)
            elif iNum != rsvp_list[-1]:
                rsvp_list.append(iNum)
        
        shuffle(letters)
        Critical = letters[0]
        while Critical == previous_target_letter:
            shuffle(letters)
            Critical = letters[0]
        previous_target_letter = Critical
        rsvp_list[tar_pos]=Critical
        rsvpSize = stimulus_size
        counterTrial = 0
        # keep track of which components have finished
        rsvp_setup_templateComponents = []
        for thisComponent in rsvp_setup_templateComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rsvp_setup_templateClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rsvp_setup_template"-------
        while continueRoutine:
            # get current time
            t = rsvp_setup_templateClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rsvp_setup_templateClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rsvp_setup_templateComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rsvp_setup_template"-------
        for thisComponent in rsvp_setup_templateComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "rsvp_setup_template" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "instruc_trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        ENTER_2.setHeight(0.5)
        key_resp_3.keys = []
        key_resp_3.rt = []
        _key_resp_3_allKeys = []
        # keep track of which components have finished
        instruc_trialComponents = [ENTER_2, key_resp_3]
        for thisComponent in instruc_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        instruc_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "instruc_trial"-------
        while continueRoutine:
            # get current time
            t = instruc_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=instruc_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ENTER_2* updates
            if ENTER_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                ENTER_2.frameNStart = frameN  # exact frame index
                ENTER_2.tStart = t  # local t and not account for scr refresh
                ENTER_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ENTER_2, 'tStartRefresh')  # time at next scr refresh
                ENTER_2.setAutoDraw(True)
            
            # *key_resp_3* updates
            waitOnFlip = False
            if key_resp_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.tStart = t  # local t and not account for scr refresh
                key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_3_allKeys.extend(theseKeys)
                if len(_key_resp_3_allKeys):
                    key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                    key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in instruc_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "instruc_trial"-------
        for thisComponent in instruc_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "instruc_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "fixation"-------
        continueRoutine = True
        routineTimer.add(0.700000)
        # update component parameters for each repeat
        fixation_text.setHeight(1)
        # keep track of which components have finished
        fixationComponents = [fixation_text]
        for thisComponent in fixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fixation"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = fixationClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixationClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_text* updates
            if fixation_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_text.frameNStart = frameN  # exact frame index
                fixation_text.tStart = t  # local t and not account for scr refresh
                fixation_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_text, 'tStartRefresh')  # time at next scr refresh
                fixation_text.setAutoDraw(True)
            if fixation_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_text.tStartRefresh + 0.7-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_text.tStop = t  # not accounting for scr refresh
                    fixation_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation_text, 'tStopRefresh')  # time at next scr refresh
                    fixation_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fixation"-------
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # set up handler to look after randomisation of conditions etc
        template_loop = data.TrialHandler(nReps=length, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='template_loop')
        thisExp.addLoop(template_loop)  # add the loop to the experiment
        thisTemplate_loop = template_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTemplate_loop.rgb)
        if thisTemplate_loop != None:
            for paramName in thisTemplate_loop:
                exec('{} = thisTemplate_loop[paramName]'.format(paramName))
        
        for thisTemplate_loop in template_loop:
            currentLoop = template_loop
            # abbreviate parameter names if possible (e.g. rgb = thisTemplate_loop.rgb)
            if thisTemplate_loop != None:
                for paramName in thisTemplate_loop:
                    exec('{} = thisTemplate_loop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "stream"-------
            continueRoutine = True
            # update component parameters for each repeat
            thisItem=rsvp_list[counterTrial]
            
            stimuli.setText(thisItem)
            stimuli.setHeight(rsvpSize)
            # keep track of which components have finished
            streamComponents = [stimuli]
            for thisComponent in streamComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            streamClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "stream"-------
            while continueRoutine:
                # get current time
                t = streamClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=streamClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *stimuli* updates
                if stimuli.status == NOT_STARTED and frameN >= 0.0:
                    # keep track of start time/frame for later
                    stimuli.frameNStart = frameN  # exact frame index
                    stimuli.tStart = t  # local t and not account for scr refresh
                    stimuli.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(stimuli, 'tStartRefresh')  # time at next scr refresh
                    stimuli.setAutoDraw(True)
                if stimuli.status == STARTED:
                    if frameN >= (stimuli.frameNStart + 7):
                        # keep track of stop time/frame for later
                        stimuli.tStop = t  # not accounting for scr refresh
                        stimuli.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(stimuli, 'tStopRefresh')  # time at next scr refresh
                        stimuli.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in streamComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "stream"-------
            for thisComponent in streamComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            counterTrial +=1
            
            # the Routine "stream" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed length repeats of 'template_loop'
        
        
        # ------Prepare to start Routine "question"-------
        continueRoutine = True
        # update component parameters for each repeat
        textbox.reset()
        textbox.setText('')
        click_text.setHeight(0.5)
        # setup some python lists for storing info about the mouse
        mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        questionComponents = [Recog_text, textbox, click_text, click, mouse]
        for thisComponent in questionComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        questionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "question"-------
        while continueRoutine:
            # get current time
            t = questionClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=questionClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Recog_text* updates
            if Recog_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Recog_text.frameNStart = frameN  # exact frame index
                Recog_text.tStart = t  # local t and not account for scr refresh
                Recog_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Recog_text, 'tStartRefresh')  # time at next scr refresh
                Recog_text.setAutoDraw(True)
            
            # *textbox* updates
            if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textbox.frameNStart = frameN  # exact frame index
                textbox.tStart = t  # local t and not account for scr refresh
                textbox.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
                textbox.setAutoDraw(True)
            
            # *click_text* updates
            if click_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                click_text.frameNStart = frameN  # exact frame index
                click_text.tStart = t  # local t and not account for scr refresh
                click_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(click_text, 'tStartRefresh')  # time at next scr refresh
                click_text.setAutoDraw(True)
            
            # *click* updates
            if click.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                click.frameNStart = frameN  # exact frame index
                click.tStart = t  # local t and not account for scr refresh
                click.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(click, 'tStartRefresh')  # time at next scr refresh
                click.setAutoDraw(True)
            # *mouse* updates
            if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(click)
                            clickableList = click
                        except:
                            clickableList = [click]
                        for obj in clickableList:
                            if obj.contains(mouse):
                                gotValidClick = True
                                mouse.clicked_name.append(obj.name)
                        if gotValidClick:  
                            continueRoutine = False  # abort routine on response
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in questionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "question"-------
        for thisComponent in questionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_template.addData('textbox.text',textbox.text)
        trials_template.addData('textbox.started', textbox.tStartRefresh)
        trials_template.addData('textbox.stopped', textbox.tStopRefresh)
        probe = Critical
        pptResponse = textbox.text
        if pptResponse.upper() == probe:
            pptAns = 1
        else:
            pptAns = 0
        
        trials_template.addData('target', probe)
        trials_template.addData('correct', pptAns)
        # store data for trials_template (TrialHandler)
        # the Routine "question" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_template'
    
# completed 1.0 repeats of 'eyes_template'


# ------Prepare to start Routine "set_variables"-------
continueRoutine = True
# update component parameters for each repeat
previous_target_letter = 'A'
# keep track of which components have finished
set_variablesComponents = []
for thisComponent in set_variablesComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
set_variablesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "set_variables"-------
while continueRoutine:
    # get current time
    t = set_variablesClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=set_variablesClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in set_variablesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "set_variables"-------
for thisComponent in set_variablesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "set_variables" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
both_eyes = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('eyes.csv'),
    seed=None, name='both_eyes')
thisExp.addLoop(both_eyes)  # add the loop to the experiment
thisBoth_eye = both_eyes.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBoth_eye.rgb)
if thisBoth_eye != None:
    for paramName in thisBoth_eye:
        exec('{} = thisBoth_eye[paramName]'.format(paramName))

for thisBoth_eye in both_eyes:
    currentLoop = both_eyes
    # abbreviate parameter names if possible (e.g. rgb = thisBoth_eye.rgb)
    if thisBoth_eye != None:
        for paramName in thisBoth_eye:
            exec('{} = thisBoth_eye[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "set_instruc"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    set_instrucComponents = []
    for thisComponent in set_instrucComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    set_instrucClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "set_instruc"-------
    while continueRoutine:
        # get current time
        t = set_instrucClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=set_instrucClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in set_instrucComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "set_instruc"-------
    for thisComponent in set_instrucComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    instruc_repeat = instruc_repeat
    
    if previous_target_letter != 'A':
        instruc_repeat = 'This is the second part of the visual acuity test. Please cover your LEFT eye with your hand so that you are looking through your RIGHT eye only.\n\n Press ENTER when you are ready to continue.'
    # the Routine "set_instruc" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "instruc_start_exp"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_repeat.setText(instruc_repeat)
    key_resp_8.keys = []
    key_resp_8.rt = []
    _key_resp_8_allKeys = []
    # keep track of which components have finished
    instruc_start_expComponents = [text_repeat, key_resp_8]
    for thisComponent in instruc_start_expComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instruc_start_expClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instruc_start_exp"-------
    while continueRoutine:
        # get current time
        t = instruc_start_expClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instruc_start_expClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_repeat* updates
        if text_repeat.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text_repeat.frameNStart = frameN  # exact frame index
            text_repeat.tStart = t  # local t and not account for scr refresh
            text_repeat.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_repeat, 'tStartRefresh')  # time at next scr refresh
            text_repeat.setAutoDraw(True)
        
        # *key_resp_8* updates
        if key_resp_8.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_8.frameNStart = frameN  # exact frame index
            key_resp_8.tStart = t  # local t and not account for scr refresh
            key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
            key_resp_8.status = STARTED
            # keyboard checking is just starting
            key_resp_8.clock.reset()  # now t=0
        if key_resp_8.status == STARTED:
            theseKeys = key_resp_8.getKeys(keyList=['return'], waitRelease=False)
            _key_resp_8_allKeys.extend(theseKeys)
            if len(_key_resp_8_allKeys):
                key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
                key_resp_8.rt = _key_resp_8_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instruc_start_expComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instruc_start_exp"-------
    for thisComponent in instruc_start_expComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instruc_start_exp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    blocks = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('nblocks.csv'),
        seed=None, name='blocks')
    thisExp.addLoop(blocks)  # add the loop to the experiment
    thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    for thisBlock in blocks:
        currentLoop = blocks
        # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
        if thisBlock != None:
            for paramName in thisBlock:
                exec('{} = thisBlock[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "instruc_block"-------
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        instruc_blockComponents = [text_start_blocks]
        for thisComponent in instruc_blockComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        instruc_blockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "instruc_block"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = instruc_blockClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=instruc_blockClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_start_blocks* updates
            if text_start_blocks.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                text_start_blocks.frameNStart = frameN  # exact frame index
                text_start_blocks.tStart = t  # local t and not account for scr refresh
                text_start_blocks.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_start_blocks, 'tStartRefresh')  # time at next scr refresh
                text_start_blocks.setAutoDraw(True)
            if text_start_blocks.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_start_blocks.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    text_start_blocks.tStop = t  # not accounting for scr refresh
                    text_start_blocks.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_start_blocks, 'tStopRefresh')  # time at next scr refresh
                    text_start_blocks.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in instruc_blockComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "instruc_block"-------
        for thisComponent in instruc_blockComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # set up handler to look after randomisation of conditions etc
        trials = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('conditions.csv'),
            seed=None, name='trials')
        thisExp.addLoop(trials)  # add the loop to the experiment
        thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        for thisTrial in trials:
            currentLoop = trials
            # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
            if thisTrial != None:
                for paramName in thisTrial:
                    exec('{} = thisTrial[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "rsvp_setup"-------
            continueRoutine = True
            # update component parameters for each repeat
            length=15
            iNum = 0
            
            tar_pos=randint(6, 9)
            # fill stream with numbers
            rsvp_list=[]
            while len(rsvp_list) != length:
                iNum = randint(1,9)
                if not rsvp_list:
                    rsvp_list.append(iNum)
                elif iNum != rsvp_list[-1]:
                    rsvp_list.append(iNum)
            
            shuffle(letters)
            Critical = letters[0]
            while Critical == previous_target_letter:
                shuffle(letters)
                Critical = letters[0]
            previous_target_letter = Critical
            rsvp_list[tar_pos]=Critical
            rsvpSize = stimulus_size
            counterTrial = 0
            # keep track of which components have finished
            rsvp_setupComponents = []
            for thisComponent in rsvp_setupComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            rsvp_setupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "rsvp_setup"-------
            while continueRoutine:
                # get current time
                t = rsvp_setupClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=rsvp_setupClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in rsvp_setupComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "rsvp_setup"-------
            for thisComponent in rsvp_setupComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "rsvp_setup" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "instruc_trial"-------
            continueRoutine = True
            # update component parameters for each repeat
            ENTER_2.setHeight(0.5)
            key_resp_3.keys = []
            key_resp_3.rt = []
            _key_resp_3_allKeys = []
            # keep track of which components have finished
            instruc_trialComponents = [ENTER_2, key_resp_3]
            for thisComponent in instruc_trialComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            instruc_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "instruc_trial"-------
            while continueRoutine:
                # get current time
                t = instruc_trialClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=instruc_trialClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ENTER_2* updates
                if ENTER_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    ENTER_2.frameNStart = frameN  # exact frame index
                    ENTER_2.tStart = t  # local t and not account for scr refresh
                    ENTER_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ENTER_2, 'tStartRefresh')  # time at next scr refresh
                    ENTER_2.setAutoDraw(True)
                
                # *key_resp_3* updates
                waitOnFlip = False
                if key_resp_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_3.frameNStart = frameN  # exact frame index
                    key_resp_3.tStart = t  # local t and not account for scr refresh
                    key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                    key_resp_3.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_3.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
                    _key_resp_3_allKeys.extend(theseKeys)
                    if len(_key_resp_3_allKeys):
                        key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                        key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in instruc_trialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "instruc_trial"-------
            for thisComponent in instruc_trialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "instruc_trial" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "fixation"-------
            continueRoutine = True
            routineTimer.add(0.700000)
            # update component parameters for each repeat
            fixation_text.setHeight(1)
            # keep track of which components have finished
            fixationComponents = [fixation_text]
            for thisComponent in fixationComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "fixation"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = fixationClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=fixationClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fixation_text* updates
                if fixation_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixation_text.frameNStart = frameN  # exact frame index
                    fixation_text.tStart = t  # local t and not account for scr refresh
                    fixation_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation_text, 'tStartRefresh')  # time at next scr refresh
                    fixation_text.setAutoDraw(True)
                if fixation_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixation_text.tStartRefresh + 0.7-frameTolerance:
                        # keep track of stop time/frame for later
                        fixation_text.tStop = t  # not accounting for scr refresh
                        fixation_text.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(fixation_text, 'tStopRefresh')  # time at next scr refresh
                        fixation_text.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in fixationComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "fixation"-------
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            # set up handler to look after randomisation of conditions etc
            rsvp_loop = data.TrialHandler(nReps=length, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='rsvp_loop')
            thisExp.addLoop(rsvp_loop)  # add the loop to the experiment
            thisRsvp_loop = rsvp_loop.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisRsvp_loop.rgb)
            if thisRsvp_loop != None:
                for paramName in thisRsvp_loop:
                    exec('{} = thisRsvp_loop[paramName]'.format(paramName))
            
            for thisRsvp_loop in rsvp_loop:
                currentLoop = rsvp_loop
                # abbreviate parameter names if possible (e.g. rgb = thisRsvp_loop.rgb)
                if thisRsvp_loop != None:
                    for paramName in thisRsvp_loop:
                        exec('{} = thisRsvp_loop[paramName]'.format(paramName))
                
                # ------Prepare to start Routine "stream"-------
                continueRoutine = True
                # update component parameters for each repeat
                thisItem=rsvp_list[counterTrial]
                
                stimuli.setText(thisItem)
                stimuli.setHeight(rsvpSize)
                # keep track of which components have finished
                streamComponents = [stimuli]
                for thisComponent in streamComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                streamClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "stream"-------
                while continueRoutine:
                    # get current time
                    t = streamClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=streamClock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *stimuli* updates
                    if stimuli.status == NOT_STARTED and frameN >= 0.0:
                        # keep track of start time/frame for later
                        stimuli.frameNStart = frameN  # exact frame index
                        stimuli.tStart = t  # local t and not account for scr refresh
                        stimuli.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(stimuli, 'tStartRefresh')  # time at next scr refresh
                        stimuli.setAutoDraw(True)
                    if stimuli.status == STARTED:
                        if frameN >= (stimuli.frameNStart + 7):
                            # keep track of stop time/frame for later
                            stimuli.tStop = t  # not accounting for scr refresh
                            stimuli.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(stimuli, 'tStopRefresh')  # time at next scr refresh
                            stimuli.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in streamComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "stream"-------
                for thisComponent in streamComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                counterTrial +=1
                
                # the Routine "stream" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
            # completed length repeats of 'rsvp_loop'
            
            
            # ------Prepare to start Routine "question"-------
            continueRoutine = True
            # update component parameters for each repeat
            textbox.reset()
            textbox.setText('')
            click_text.setHeight(0.5)
            # setup some python lists for storing info about the mouse
            mouse.clicked_name = []
            gotValidClick = False  # until a click is received
            # keep track of which components have finished
            questionComponents = [Recog_text, textbox, click_text, click, mouse]
            for thisComponent in questionComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            questionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "question"-------
            while continueRoutine:
                # get current time
                t = questionClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=questionClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Recog_text* updates
                if Recog_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Recog_text.frameNStart = frameN  # exact frame index
                    Recog_text.tStart = t  # local t and not account for scr refresh
                    Recog_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Recog_text, 'tStartRefresh')  # time at next scr refresh
                    Recog_text.setAutoDraw(True)
                
                # *textbox* updates
                if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    textbox.frameNStart = frameN  # exact frame index
                    textbox.tStart = t  # local t and not account for scr refresh
                    textbox.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
                    textbox.setAutoDraw(True)
                
                # *click_text* updates
                if click_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    click_text.frameNStart = frameN  # exact frame index
                    click_text.tStart = t  # local t and not account for scr refresh
                    click_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(click_text, 'tStartRefresh')  # time at next scr refresh
                    click_text.setAutoDraw(True)
                
                # *click* updates
                if click.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    click.frameNStart = frameN  # exact frame index
                    click.tStart = t  # local t and not account for scr refresh
                    click.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(click, 'tStartRefresh')  # time at next scr refresh
                    click.setAutoDraw(True)
                # *mouse* updates
                if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse.frameNStart = frameN  # exact frame index
                    mouse.tStart = t  # local t and not account for scr refresh
                    mouse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                    mouse.status = STARTED
                    mouse.mouseClock.reset()
                    prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
                if mouse.status == STARTED:  # only update if started and not finished!
                    buttons = mouse.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            try:
                                iter(click)
                                clickableList = click
                            except:
                                clickableList = [click]
                            for obj in clickableList:
                                if obj.contains(mouse):
                                    gotValidClick = True
                                    mouse.clicked_name.append(obj.name)
                            if gotValidClick:  
                                continueRoutine = False  # abort routine on response
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in questionComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "question"-------
            for thisComponent in questionComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials.addData('textbox.text',textbox.text)
            trials.addData('textbox.started', textbox.tStartRefresh)
            trials.addData('textbox.stopped', textbox.tStopRefresh)
            probe = Critical
            pptResponse = textbox.text
            if pptResponse.upper() == probe:
                pptAns = 1
            else:
                pptAns = 0
            
            trials_template.addData('target', probe)
            trials_template.addData('correct', pptAns)
            # store data for trials (TrialHandler)
            # the Routine "question" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'trials'
        
    # completed 1.0 repeats of 'blocks'
    
# completed 1.0 repeats of 'both_eyes'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
