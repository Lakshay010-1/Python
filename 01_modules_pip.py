# In terminal Python uses REPL(Read Evaluate Print Loop).  
# Module - Module is a file containing code written by somebody else (usually) which can be imported and used in our programs.
# PIP    - Pip is the package manager for python. You can use pip to install a module on your system.

# os module
# Usuage
import os
# Specify the Directory you want to list
directory_path='/'

# Use os module and list all files and directories in the specified path
contents=os.listdir(directory_path)

# Print each file and directory name
for item in contents:
      print(item)


# pyttsx3 Module
# Installation Command
# pip install pyttsx3
 
# Usage
import pyttsx3
engine = pyttsx3.init()
engine.say("I Can Do this all Day...")
engine.runAndWait()

# Changing Voice , Rate and Volume 
""" 
import pyttsx3
engine = pyttsx3.init() # object creation

# RATE
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate


# VOLUME
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

# VOICE
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()

# Saving Voice to a file
# On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.save_to_file('Hello World', 'test.mp3')
engine.runAndWait()

"""