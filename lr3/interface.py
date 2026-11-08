import os
import tkinter as tk

SKY = '#9bfaf0'
FONT = ('Courier New', 16, 'bold')

window = tk.Tk()
window.title('Keygen - Super Mario Bros. 3')


bg_img = tk.PhotoImage(file='background.png')

window.geometry(f'{bg_img.width()}x{bg_img.height()}')
window.resizable(False, False)

lbl_bg = tk.Label(window, image=bg_img)
lbl_bg.place(x=0, y=0)

frame = tk.Frame(window, bg=SKY, bd=4, relief='ridge')
frame.place(relx=0.5, rely=0.4, anchor='center')

lbl_title = tk.Label(frame, text='PRESS GENERATE', bg=SKY, fg='red', font=('Courier New', 20, 'bold'))
lbl_title.pack(padx=25, pady=(15, 5))


key = tk.StringVar(value='-- ------- --')

entry_key = tk.Entry(frame, textvariable=key, state='readonly', justify='center', font=FONT, width=16)
entry_key.pack(padx=25, pady=10)


btn_generate = tk.Button(frame, text='GENERATE', font=FONT, bg='#e45c10')
btn_generate.pack(padx=25, pady=5)


btn_music = tk.Button(frame, text='MUSIC: ON', font=('Courier New', 10, 'bold'))
btn_music.pack(padx=25, pady=(5, 15))
