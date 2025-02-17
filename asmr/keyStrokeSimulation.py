import pygame
from pynput import keyboard 

#initialize pygame mixer for sound
pygame.mixer.init()

#load the mechanical keyboard sound
click_sound = "key.wav" #make sure that sound file is in same file as py file

#track pressed keys to avoid repeated sounds on long press
pressed_keys = set()

def play_sound():
    try:
        pygame.mixer.Sound(click_sound).play()
    except Exception as e:
        print("Sound error:", e)

def key_press(key):
    if key not in pressed_keys:
        pressed_keys.add(key)
        play_sound()

def key_release(key):
    if key in pressed_keys:
        pressed_keys.remove(key)

#listen for keyboard evevnts
with keyboard.Listener(on_press=key_press, on_release=key_release) as listener:
    listener.join()

