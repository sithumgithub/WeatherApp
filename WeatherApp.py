from doctest import master
import requests
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk
from PIL import ImageTk, Image

url = "https://weather.com/weather/today/l/2e7e4387ec7c77787780f685cf56e85c902235f12b815f56bccce92741840e89"

master = Tk()
master.title("Weather App")
master.config(bg= "white")

img = Image.open("E:/Projects/Weather new/logo.png")
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

def getWeather():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    location = soup.find('h1', class_="CurrentConditions--location--1YWj_").text
    temperature = soup.find('span', class_="CurrentConditions--tempValue--MHmYY").text
    weatherPrediction = soup.find('div', class_="CurrentConditions--phraseValue--mZC_p").text
    
    locationLabel.config(text=location)
    temperatureLabel.config(text=temperature)
    weatherPredictionLabel.config(text=weatherPrediction)

    temperatureLabel.after(60000,getWeather)
    master.update()

locationLabel = Label(master, font=("Calibri bold", 20), bg="white")
locationLabel.grid(row=0, sticky="N",padx=100)

temperatureLabel = Label(master, font=("Calibri bold", 70), bg="white")
temperatureLabel.grid(row=1, sticky="W",padx=40)

Label(master, image=img, bg="white").grid(row=1,sticky="E")
weatherPredictionLabel = Label(master, font=("Calibri bold",15),bg="white")
weatherPredictionLabel.grid(row=2,sticky="W", padx=40)

getWeather()

master.mainloop()

