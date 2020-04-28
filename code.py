# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:49:29 2020

@author: user
"""

import pyaudio
import webbrowser as wb
import speech_recognition as sr
r1=sr.Recognizer()
r2=sr.Recognizer()
r3=sr.Recognizer()
with sr.Microphone() as source:
    print("speak now")
    print("how may i help you")
    audio=r3.listen(source)
if 'edureka' in r2.recognize_google(audio):
    r2=sr.Recognizer()
    url='htts://www.edureka.co/'
    with sr.Microphone() as source:
        print('search your querry')
        audio=r2.listen(source)
    try:
        get=r2.recognize_google(audio)
        print(get)
        wb.get().open_new(url+get)
    except sr.UnknownValueError:
        print('error')
    except sr.RequestError as e:
        print('failed '.format(e))
if 'video' in r1.recognize_google(audio):
    r1=sr.Recognizer()
    url='htts://www.edureka.co/'
    with sr.Microphone() as source:
        print('search your querry')
        audio=r1.listen(source)
    try:
        get=r1.recognize_google(audio)
        print(get)
        wb.get().open_new(url+get)
    except sr.UnknownValueError:
        print('error')
    except sr.RequestError as e:
        print('failed '.format(e))
                
        
