from tkinter import *
from PIL import ImageTk, Image
import requests

url = 'https://api.openweathermap.org/data/2.5/weather'
sifre = 'f3b0f70029662311da372fde8b7e90c8'
iconUrl = ' https://openweathermap.org/img/wn/{}@2x.png'


def getWeath(sehir):
    params = {'q': sehir, 'appid': sifre, 'lang': 'tr'}
    data = requests.get(url, params=params).json()
    if data:
        sehir = data['name'].title()
        ulke = data['sys']['country']
        derece = int(data['main']['temp'] - 273.15)
        icon = data['weather'][0]['icon']
        durum = data['weather'][0]['description']
        return (sehir, ulke, derece, icon, durum)


def main():
    sehir = sehirEkle.get()
    weather = getWeath(sehir)
    if weather:
        locationEkle['text'] = '{},{}'.format(weather[0], weather[1])
        dereceEkle['text'] = '{}°C'.format(weather[2])
        durumEkle['text'] = weather[4]
        icon = ImageTk.PhotoImage(Image.open(requests.get(iconUrl.format(weather[3]), stream=True).raw))
        iconEkle.configure(image=icon)
        iconEkle.image = icon


app = Tk()
app.geometry('350x500')
app.title('Hava Durumu')

sehirEkle = Entry(app, justify='center', font=('Calibri,40'))
sehirEkle.pack(fill=BOTH, ipady=15, padx=18, pady=20)
sehirEkle.configure(bg='beige')
sehirEkle.focus()

searchButton = Button(app, text='Arama', font=('Calibri,37'), command=main)
searchButton.pack()

iconEkle = Label(app)
iconEkle.pack()

locationEkle = Label(app, font=('Calibri', 40), fg='gray')
locationEkle.pack()

dereceEkle = Label(app, font=('Calibri', 50, 'bold'))
dereceEkle.pack()

durumEkle = Label(app, font=('Calibri', 20, 'bold'), fg='light blue')
durumEkle.pack()

app.mainloop()
