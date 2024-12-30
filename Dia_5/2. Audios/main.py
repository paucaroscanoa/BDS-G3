from gtts import gTTS
import os

texto =input('Escribre un texto a convertir en audio :')
tts=gTTS(text=texto,lang='en')
filename='audio1.mp3'
tts.save(filename)
os.system(f'start{filename}')
