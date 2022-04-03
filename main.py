from PIL import *
from tkinter import *
import  requests

from PIL import Image,ImageTk
from PIL.Image import Resampling
#106edcd6fa82d98c793c451f1aed09d0
# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
def open_image(icon):
    size=int(f2.winfo_height()*0.25)
    img=ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size,size)))


def format_response(weather):
    try:

        city=weather['name']
        condition=weather['weather'][0]['description']
        temprature=weather['main']['temp']
        fstr='City:%s\n Condition:%s \n Temprature:%s'%(city,condition,temprature)
    except:
        fstr='Sorry we cannot recognize it'
    return fstr



def gwt(city):
    key='106edcd6fa82d98c793c451f1aed09d0'
    url='https://api.openweathermap.org/data/2.5/weather'
    para={'APPID':key,'q':city,'units':'imperial'}
    respone=requests.get(url,para)
    # print(respone.json())
    weather=respone.json()
    # print(weather['name'])
    # print(weather['weather'][0]['description'])
    # print(weather['main']['temp'])
    res['text']=format_response(weather)
    icon=weather['weather'][0]['icon']
    open_image(icon)
    wicon.delete('all')
    wicon.create_image(0,0,anchor='nw',image=img)
    wicon.image=img



root=Tk()
root.title("Weather recognization")
root.geometry("600x500")
img=Image.open('index.jpg')
img=img.resize((600,500),Image.ANTIALIAS)
pic=ImageTk.PhotoImage(img)
lbl=Label(root,image=pic).place(x=0,y=0,width=600,height=500)
title=Label(lbl,text='Earth includes over 2,00,000 cities',fg='green',background='powder blue',font=('times new roman',18,'bold'))
title.place(x=100,y=14)
f1=Frame(lbl,background="#281E50",bd=5)
f1.place(x=60,y=50,width=450,height=50)
txt=Entry(f1,font=('times new roman',25),width=17)
txt.grid(row=0,column=0,sticky=W)
b1=Button(f1,text='Get Weather',fg='black',font=('times new roman',16,'bold'),command=lambda :gwt(txt.get()))
b1.grid(row=0,column=1,padx=10)
f2=Frame(lbl,background="#281E50",bd=5)
f2.place(x=60,y=130,width=450,height=300)
res=Label(f2,font=40,background='white',justify=LEFT,anchor='nw')
res.place(relwidth=1,relheight=1)
wicon=Canvas(res,background='white',bd=0,highlightthickness=0)
wicon.place(relx=.75,rely=0,relheight=.5,relwidth=1)


root.mainloop()