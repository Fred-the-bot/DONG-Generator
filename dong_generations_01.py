from playsound import playsound
import time
import random
import keyboard
i=0
x = random.randrange(300, 900)
while (True):
    x=x*10
    i=i+1
    if (i==x):
        i=0
        x = random.randrange(300, 900)
        playsound('C:/Users/frede/PycharmProjects/DONG_generator/dong.mp3')
    if (keyboard.is_pressed('shift')):
        playsound('C:/Users/frede/PycharmProjects/DONG_generator/dong.mp3')
    time.sleep(0.1)
