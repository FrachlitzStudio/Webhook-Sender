# Modules
from tkinter import *
from tkinter import messagebox, colorchooser, ttk
from discord_webhook import DiscordWebhook, DiscordEmbed
import time


# Functions
def send_click():
	wh_url = wh_url_ph.get()
	wh_username = wh_username_ph.get()
	if wh_username == "":
		webhook = DiscordWebhook(url=wh_url)
	else:
		webhook = DiscordWebhook(url=wh_url, username=wh_username)
	e_title = title_ph.get()
	e_desc = desc_ph.get()
	e_color = int(color_ph.get(), 16)
	e_author = author_ph.get()
	e_author_icon = author_icon_ph.get()
	e_footer = footer_ph.get()
	embed = DiscordEmbed(title=e_title, description=e_desc, color=e_color)
	embed.set_author(name=e_author, icon_url=e_author_icon)
	embed.set_footer(text=e_footer)
	if chk_state.get() == True:
		embed.set_timestamp()
	webhook.add_embed(embed)
	response = webhook.execute()
	if str(response) == "<Response [400]>":
		messagebox.showerror('Error', 'There is an error in your embed data.')

def choose_color():
	color_ph.delete(0, "end")
	choosen_color = colorchooser.askcolor()
	color_ph.insert(0, choosen_color[1].lstrip('#'))
	color_ph.configure(bg=choosen_color[1])



# Window
window = Tk()
window.title("Webhook Embed Sender")
window.geometry('500x300')

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Webhook')
tab_control.add(tab2, text='Embed')


# Webhook configuring GUI
main_txt = Label(tab1, text="Webhook configuring", font=("Arial Bold", 20))
main_txt.grid(column=1, row=0)

wh_url_text = Label(tab1, text="Webhook URL:", font=("Arial", 14))
wh_url_text.grid(column=0, row=1)
wh_url_ph = Entry(tab1, width=50)
wh_url_ph.grid(column=1, row=1)

wh_username_text = Label(tab1, text="Webhook Username:", font=("Arial", 14))
wh_username_text.grid(column=0, row=2)
wh_username_ph = Entry(tab1, width=50)
wh_username_ph.grid(column=1, row=2)


# Embed configuring GUI
title_txt = Label(tab2, text="Embed configuring", font=("Arial Bold", 20))
title_txt.grid(column=1, row=0)

title_text = Label(tab2, text="Title:", font=("Arial", 14))
title_text.grid(column=0, row=1)
title_ph = Entry(tab2, width=50)
title_ph.grid(column=1, row=1)

desc_text = Label(tab2, text="Description:", font=("Arial", 14))
desc_text.grid(column=0, row=2)
desc_ph = Entry(tab2, width=50)
desc_ph.grid(column=1, row=2)

color_btn = Button(tab2, text="Pick color", command=choose_color, width=10)
color_btn.grid(column=0, row=3)
color_ph = Entry(tab2, width=50)
color_ph.grid(column=1, row=3)

author_text = Label(tab2, text="Author Name:", font=("Arial", 14))
author_text.grid(column=0, row=4)
author_ph = Entry(tab2, width=50)
author_ph.grid(column=1, row=4)

author_icon_text = Label(tab2, text="Author Icon URL:", font=("Arial", 14))
author_icon_text.grid(column=0, row=5)
author_icon_ph = Entry(tab2, width=50)
author_icon_ph.grid(column=1, row=5)

footer_text = Label(tab2, text="Footer:", font=("Arial", 14))
footer_text.grid(column=0, row=6)
footer_ph = Entry(tab2, width=50)
footer_ph.grid(column=1, row=6)

timestamp_text = Label(tab2, text="Timestamp:", font=("Arial", 14))
timestamp_text.grid(column=0, row=7)
chk_state = BooleanVar()
chk_state.set(False)
timestamp_ph = Checkbutton(tab2, text="True", var=chk_state)
timestamp_ph.grid(column=1, row=7)


# Send btn
send_btn = Button(tab2, text="Send!", fg="green", command=send_click, width=16)
send_btn.grid(column=1, row=10)


# Main loop
tab_control.pack(expand=1, fill='both')  
window.mainloop()