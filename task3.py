#Use the Weather API builder at https://open-meteo.com/en/docs to generate an API call for a city. 
# We are going to make use of the REQUESTS.Request method to retrieve this data and unpack it with 
# json.loads into a variable that we can use. Retrieve the data and present it in a more organized format. 
# You may use text output or a window using Tkinter. 
#Our goal is to format the result in a reasonably organized format.
import requests
import json
import tkinter as tk
import datetime as dt

#w = tk.Tk()
#w.title("weather API Builder")
#w.geometry('600x400')

class yes():
    def __init__(self) -> None:
        self.data()

    def data(self):
        weather = json.loads(requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m').text)
        timing = dt.datetime.now()
        y = str(timing)
        y = y.split(":")
        y.pop()[1]
        y.pop()[1]
        y = str(y)[2:-2]+":00"
        y = list(y)
        for i in y:
            if i == " ":
                y[y.index(i)] = "T"
        y = "".join(y)
        puns = weather["hourly"]["time"].index(y)
        temper = weather["hourly"]["temperature_2m"][puns]
        print(f"The temperature is {temper} degrees celius")
        return temper
        
y = yes()
#w.mainloop()