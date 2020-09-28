# Modules
from tkinter import *
from tkinter import messagebox, colorchooser, ttk
from discord_webhook import DiscordWebhook, DiscordEmbed
import time, configparser




# Functions
def send_click():
	wh_url = wh_url_ph.get()
	wh_username = wh_username_ph.get()
	wh_avatar = wh_avatar_ph.get()

	if wh_username == "" and wh_avatar == "":
		webhook = DiscordWebhook(url=wh_url)
	elif wh_username != "" and wh_avatar == "":
		webhook = DiscordWebhook(url=wh_url, username=wh_username)
	elif wh_username == "" and wh_avatar != "":
		webhook = DiscordWebhook(url=wh_url, avatar_url=wh_avatar)
	elif wh_username != "" and wh_avatar != "":
		webhook = DiscordWebhook(url=wh_url, username=wh_username, avatar_url=wh_avatar)

	e_title = title_ph.get()
	e_desc = desc_ph.get()
	if color_ph.get() != "":
		e_color = int(color_ph.get(), 16)
	else:
		e_color = 0x000000
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
		messagebox.showerror('Error', 'There is an error in your data.')

def choose_color():
	color_ph.delete(0, "end")
	choosen_color = colorchooser.askcolor()
	color_ph.insert(0, choosen_color[1].lstrip('#'))
	color_ph.configure(bg=choosen_color[1])

def save_wh_info():
	config['WebHook']['wh_URL'] = wh_url_ph.get()
	config['WebHook']['wh_username'] = wh_username_ph.get()
	config['WebHook']['wh_avatar_URL'] = wh_avatar_ph.get()
	

	with open('data.ini', 'w') as cfg:
		config.write(cfg)



# Window
window = Tk()
window.title("Webhook Embed Sender v0.2.2")
window.geometry('500x300')

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Info')
tab_control.add(tab2, text='Webhook')
tab_control.add(tab3, text='Embed')



# Info menu
main_txt = Label(tab1, text="Webhook Embed Sender v0.2.2", font=("Calibri", 25))
main_txt.grid(column=0, row=0)
author_txt = Label(tab1, text="by FrachlitzStudio", font=("Calibri", 20))
author_txt.grid(column=0, row=1)



# Webhook configuring menu
main_txt = Label(tab2, text="Webhook configuring", font=("Arial Bold", 20))
main_txt.grid(column=1, row=0)

wh_url_text = Label(tab2, text="Webhook URL:", font=("Arial", 14))
wh_url_text.grid(column=0, row=1)
wh_url_ph = Entry(tab2, width=50)
wh_url_ph.grid(column=1, row=1)

wh_username_text = Label(tab2, text="Webhook Username:", font=("Arial", 14))
wh_username_text.grid(column=0, row=2)
wh_username_ph = Entry(tab2, width=50)
wh_username_ph.grid(column=1, row=2)

wh_avatar_text = Label(tab2, text="Webhook Avatar:", font=("Arial", 14))
wh_avatar_text.grid(column=0, row=3)
wh_avatar_ph = Entry(tab2, width=50)
wh_avatar_ph.grid(column=1, row=3)


send_btn = Button(tab2, text="Save", command=save_wh_info, width=32)
send_btn.grid(column=1, row=10)


config = configparser.ConfigParser()
config.read("data.ini")

wh_url_ph.insert(0, config['WebHook']['wh_URL'])
wh_username_ph.insert(0, config['WebHook']['wh_username'])
wh_avatar_ph.insert(0, config['WebHook']['wh_avatar_url'])



# Embed configuring menu
title_txt = Label(tab3, text="Embed configuring", font=("Arial Bold", 20))
title_txt.grid(column=1, row=0)

title_text = Label(tab3, text="Title:", font=("Arial", 14))
title_text.grid(column=0, row=1)
title_ph = Entry(tab3, width=50)
title_ph.grid(column=1, row=1)

desc_text = Label(tab3, text="Description:", font=("Arial", 14))
desc_text.grid(column=0, row=2)
desc_ph = Entry(tab3, width=50)
desc_ph.grid(column=1, row=2)

color_btn = Button(tab3, text="Pick color", command=choose_color, width=10)
color_btn.grid(column=0, row=3)
color_ph = Entry(tab3, width=50)
color_ph.grid(column=1, row=3)

author_text = Label(tab3, text="Author Name:", font=("Arial", 14))
author_text.grid(column=0, row=4)
author_ph = Entry(tab3, width=50)
author_ph.grid(column=1, row=4)

author_icon_text = Label(tab3, text="Author Icon URL:", font=("Arial", 14))
author_icon_text.grid(column=0, row=5)
author_icon_ph = Entry(tab3, width=50)
author_icon_ph.grid(column=1, row=5)

footer_text = Label(tab3, text="Footer:", font=("Arial", 14))
footer_text.grid(column=0, row=6)
footer_ph = Entry(tab3, width=50)
footer_ph.grid(column=1, row=6)

timestamp_text = Label(tab3, text="Timestamp:", font=("Arial", 14))
timestamp_text.grid(column=0, row=7)
chk_state = BooleanVar()
chk_state.set(False)
timestamp_ph = Checkbutton(tab3, text="True", var=chk_state)
timestamp_ph.grid(column=1, row=7)


send_btn = Button(tab3, text="Send!", fg="green", command=send_click, width=16)
send_btn.grid(column=1, row=10)



# Main loop
tab_control.pack(expand=1, fill='both')  
window.mainloop()