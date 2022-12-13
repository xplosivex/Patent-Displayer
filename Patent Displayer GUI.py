from tkinter import *
from tkinter import messagebox
import random
import math
import ctypes
import json
import requests
from bs4 import BeautifulSoup
f = open('config_the_goodman.json')
loaded_configuration = json.load(f) #Loads the config file into a varible
counter = 0


    
window = Tk()
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1) #Gets screen resoultion
screenres_half = str(math.ceil(screensize[0] / 2)) +"x" + str(math.ceil(screensize[1] / 2)) # divides user screen resoultion by 2

window.geometry(str(screenres_half))
window.title("Goodman Experience V2.1.1")
window.configure(bg=loaded_configuration["background_color"])
window.iconbitmap("goodmanicon.ico")
#bg = PhotoImage(file = "goodmanimage.png")

window_label = Label(window,bg=loaded_configuration["background_color"],font=("Onyx", 45),wraplength=math.ceil(screensize[0] / 2))#window created to put text on
window_label.pack(expand=True)# who the fuck knows what the pack command does 
window_label2 = Label(window,bg=loaded_configuration["background_color"],font=("Onyx", 25),wraplength=math.ceil(screensize[0] / 1.5))
window_label2.pack(expand=True)
window_label3 = Label(window,bg=loaded_configuration["background_color"],font=("Ariel", 12),wraplength=math.ceil(screensize[0] / 2))
window_label3.pack()
def GetRandomPatent():#000
    url = "https://patents.google.com/patent/US" + str(random.randint(1,8000000))
    print("Url: ",url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    h1_selected = soup.find('h1').text
    patentdiv = h1_selected.replace("- Google Patents","").split(" - ")
    case_number = patentdiv[0]
    patent_title = patentdiv[1]
    patent_list = []
    patent_list.append(case_number.replace("\n",""))
    patent_list.append(patent_title.replace("\n","").replace("       ",""))
    
    
    return patent_list

def on_closing():
    if messagebox.askokcancel("The Choice of a lifetime", "Are you sure you want to exit the Goodman experience"):
        window.destroy()
        
def update():
    try:
        window_text = GetRandomPatent()
        window_time = math.ceil(len(window_text[1]) * 1000 / 6.5)
        print("determined delay: ",window_time)
        window_label['text'] = window_text[1] #this sets the text for the window
        global counter
        if "apparatus" in window_text[1].lower():
            counter = counter + 1 
        window_label2['text'] = "apparatus has been said this many times: " + str(counter)
        window_label3['text'] = window_text[0]
        window.after(window_time, update) # run itself again after 1000 ms updating the text
 # run itself again after 1000 ms updating the text
    except:
        window_label['text'] = "HORRIBLE THINGS HAVE BROKE THE CODE" #this sets the text for the window
        window_label2['text'] = "HORRIBLE THINGS HAVE BROKE THE CODE"
        window_label3['text'] = "HORRIBLE THINGS HAVE BROKE THE CODE"
        window.after(1000, update)
# run first time
update()
window.protocol("WM_DELETE_WINDOW", on_closing) #this hooks into the window to know when it's being closed
window.mainloop()
