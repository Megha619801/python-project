# import pyttsx3
# engine = pyttsx3.init()
#
# """ RATE"""
# rate = engine.getProperty('rate')
# print (rate)
# engine.setProperty('rate', 125)
#
#
# """VOLUME"""
# volume = engine.getProperty('volume')
# print (volume)                          #printing current volume level
# engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
#
# """VOICE"""
# voices = engine.getProperty('voices')       #getting details of current voice
# #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
# engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
#
# engine.say("Hello, My name is Mahi Mahato.")
# engine.say('My current speaking rate is ' + str(rate))
# engine.runAndWait()
# engine.stop()
#
# """Saving Voice to a file"""
# engine.save_to_file('Hello World', 'test.mp3')
# engine.runAndWait()


import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()

import pyttsx3
engine