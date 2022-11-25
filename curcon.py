from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror
import requests,json

APIKEY = "ENTER YOUR APIKEY HERE" # Get your Free API KEY from https://www.exchangerate-api.com/
url = f"https://v6.exchangerate-api.com/v6/{APIKEY}/latest/USD"
response = requests.get(f'{url}').json()
currencies = dict(response['conversion_rates'])

def concur():
    try:
        source = fromcurrencycombo.get()
        destination = tocurrencycombo.get()
        amount = amountentry.get()
        result = requests.get(f'https://v6.exchangerate-api.com/v6/{APIKEY}/pair/{source}/{destination}/{amount}').json()
        convertedresult = result['conversion_result']
        formattedresult = f'{amount} {source} = {convertedresult} {destination}'
        resultlabel.config(text=formattedresult)
        timelabel.config(text='Last Updated,' + result['time_last_update_utc'])

    except:
        showerror(title='Error', message='An error occurred!! Fill all required field or check your internet connection!!')

window = Tk()
window.geometry('310x340+500+200')
window.title('Currency Converter')
window.resizable(height=FALSE, width=FALSE)
primary = '#081F4D'
secondary = '#0083FF'
white = '#FFFFFF'
topframe = Frame(window, bg=primary, width=300, height=80)
topframe.grid(row=0,column=0)
namelabel = Label(topframe, text="Currency Converter", bg=primary,fg=white,pady=30,padx=24,justify=CENTER,font=('Poppins 18 bold'))
namelabel.grid(row=0,column=0)
bottomframe = Frame(window,width=300,height=250)
bottomframe.grid(row=1,column=0)
fromcurrencylabel = Label(bottomframe, text="FROM:",font=('Poppins 10 bold'),justify=LEFT)
fromcurrencylabel.place(x=5,y=10)
tocurrencylabel = Label(bottomframe,text="TO:",font=('Poppins 10 bold'),justify=RIGHT)
tocurrencylabel.place(x=160,y=10)
fromcurrencycombo = ttk.Combobox(bottomframe, values=list(currencies.keys()),width=14,font=('Poppins 9 bold'))
fromcurrencycombo.place(x=5, y=30)
tocurrencycombo = ttk.Combobox(bottomframe, values=list(currencies.keys()),width=14,font=('Poppins 9 bold'))
tocurrencycombo.place(x=160, y=30)
amountlabel = Label(bottomframe,text="AMOUNT:",font=('Poppins 10 bold'))
amountlabel.place(x=5,y=55)
amountentry = Entry(bottomframe,width=25,font=("Poppins 12 bold"))
amountentry.place(x=5,y=80)
resultlabel = Label(bottomframe,text='',font=('Poppins 12 bold'))
resultlabel.place(x=5,y=115)
timelabel = Label(bottomframe,text='',font=('Poppins, 8 bold'))
timelabel.place(x=5,y=135)
convertbtn = Button(bottomframe, text="CONVERT",bg=secondary,fg=white,font=('Poppins 10 bold'),command=concur)
convertbtn.place(x=5, y=165)
window.mainloop()
