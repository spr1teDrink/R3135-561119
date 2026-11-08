import os
import random
import string
import sys
import pygame as pg
import interface
ALPHABET = string.ascii_uppercase


def generate_key():
    low = random.randint(1,24)
    high = random.randint(low+1,26)
    block1 = f'{low:02d}'    
    block3 = f'{high:02d}'
    letters = ALPHABET[low - 1:high]
    block2 = ''.join(random.choice(letters) for _ in range(7))
    return f'{block1} {block2} {block3}'



def random_stuff():
    left = random.randint(1, 26)
    right = random.randint(1, 26)
    middle = ''.join(random.choice(ALPHABET) for _ in range(7))
    return f'{left:02d} {middle} {right:02d}'


def roll(frame, final_key):
    if frame < 20:
        interface.key.set(random_stuff())
        interface.window.after(50, roll, frame + 1, final_key)
    else:
        interface.key.set(final_key)
        interface.btn_generate.config(state='normal')


def blink(visible=True):
    interface.lbl_title.config(fg= 'red' if visible else 'white')
    interface.window.after(500, blink, not visible)

music = True

def start_music():
    pg.mixer.init()
    pg.mixer.music.load('music.mp3')
    pg.mixer.music.set_volume(1)
    pg.mixer.music.play(-1)


def toggle_music():
    global music
    if music:
        pg.mixer.music.pause()
        interface.btn_music.config(text='MUSIC: OFF')
    else:
        pg.mixer.music.unpause()
        interface.btn_music.config(text='MUSIC: ON')
    music = not music


def on_generate():
    interface.btn_generate.config(state='disabled')
    roll(0, generate_key())                     


def on_close():
    pg.mixer.music.stop()
    interface.window.destroy()


interface.btn_generate.config(command=on_generate)
interface.btn_music.config(command=toggle_music)
interface.window.protocol('WM_DELETE_WINDOW', on_close)

start_music()
blink()
interface.window.mainloop()
