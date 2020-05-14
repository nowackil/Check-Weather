# Autor: Łukasz Nowacki vel banan
# Data: 13.05.2020

import tkinter as tk
from tkinter import font
import requests

HEIGHT = 500
WIDTH = 600

def test_function(entry):
    print("This is the entry:", entry)

# API 25b9ac8a8d36d792a5191157d68be0a0
# api.openweathermap.org/data/2.5/forecast?q={city name}&appid={your api key}

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'Miasto: %s \nZachmurzenie: %s \nTemperatura (°C): %s' % (name, desc, temp)
    except:
        final_str = 'Wystąpił problem z otrzymaniem informacji'

    return final_str

def get_weather(city):
    weather_key = '25b9ac8a8d36d792a5191157d68be0a0'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'appid': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)

root = tk.Tk()
root.title("Sprawdź pogodę")


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

backround_image = tk.PhotoImage(file='landscape.png')
backround_label = tk.Label(root, image=backround_image)
backround_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')


entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)


button = tk.Button(frame, text="Pogoda", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)



lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 18), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()
