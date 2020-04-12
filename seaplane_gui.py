# Seaplane calculator with GUI
# By Jason VanDeventer

import tkinter as tk
from tkinter import ttk
import pprint as pp
import math
import os

if os.environ.get('DISPLAY', '') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')


# radius of Earth in kilometers
R = 6383.0


def calculate():
    first_text.delete(0, tk.END)
    first_city_text.delete(0, tk.END)
    second_city_text.delete(0, tk.END)

    if first_drop.get() in cities:
        code1 = cities[first_drop.get()]
        name1 = airport_names[code1]
    if code1 in latitudes:
        first_lat = latitudes[code1]
    if code1 in longitudes:
        first_lon = longitudes[code1]
    if second_drop.get() in cities:
        code2 = cities[second_drop.get()]
        name2 = airport_names[code2]
    if code2 in latitudes:
        second_lat = latitudes[code2]
    if code2 in longitudes:
        second_lon = longitudes[code2]

    lat1 = math.radians(float(first_lat))
    lon1 = math.radians(float(first_lon))
    lat2 = math.radians(float(second_lat))
    lon2 = math.radians(float(second_lon))

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * \
        math.cos(lat2) * math.sin(dlon / 2)**2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c

    # convert kilometers to nautical miles
    nmi = distance / 1.852

    first_text.insert(tk.END, str(round(nmi, 2)))
    first_city_text.insert(tk.END, name1)
    second_city_text.insert(tk.END, name2)


# Create window object
app = tk.Tk()
app.title('Seaplane Calculator')
app.geometry('600x300')
icon = tk.PhotoImage(file="airplane.png")
app.iconphoto(False, icon)

# dictionaries
cities = {'Atlanta': 'atl', 'Dallas': 'dfw', 'Tulsa': 'tul',
          'New York': 'jfk', 'Los Angeles': 'lax', 'London': 'lhr',
          'Chicago': 'ord', 'Seattle': 'sea', 'Paris': 'cdg',
          'Shanghai': 'pvg', 'Hong Kong': 'hkg', 'Tokyo': 'hnd',
          'Dubai': 'dxb', 'Beijing': 'pek', 'Sao Paulo': 'cgh'}
airport_names = {"atl": "Hartsfield-Jackson Atlanta International Airport",
                 "dfw": "DFW International Airport",
                 "jfk": "John F. Kennedy International Airport",
                 "lax": "Los Angeles International Airport",
                 "lhr": "London Heathrow Airport",
                 "ord": "O'Hare International Airport",
                 "sea": "Seattle-Tacoma International Airport",
                 "tul": "Tulsa International Airport",
                 "cdg": "Paris Charles de Gaulle Airport",
                 "pvg": "Shanghai Pudong International Airport",
                 "hkg": "Hong Kong International Airport",
                 "hnd": "Haneda Airport",
                 "dxb": "Dubai International Airport",
                 "pek": "Beijing Capital International Airport",
                 "cgh": "Sao Paulo Congonhas Airport"}
latitudes = {"atl": 33.6407, "dfw": 32.8998, "jfk": 40.6413,
             "lax": 33.9416, "lhr": 51.4700, "ord": 41.9742,
             "sea": 47.4502, "tul": 36.1988, "cdg": 49.0097,
             "pvg": 31.1443, "hkg": 22.3193, "hnd": 35.5494,
             "dxb": 25.2519, "pek": 40.0799, "cgh": -23.6278}
longitudes = {"atl": -84.4277, "dfw": -97.0403, "jfk": -73.7781,
              "lax": -118.4085, "lhr": -0.4543, "ord": -87.9073,
              "sea": -122.3088, "tul": -95.8839, "cdg": 2.5479,
              "pvg": 121.8083, "hkg": 114.1694, "hnd": 139.7798,
              "dxb": 55.3642, "pek": 116.6031, "cgh": -46.6542}

# first airport
first_airport_label = tk.Label(app, text='First City:',
                               font=('bold', 14), padx=10, pady=5)
first_airport_label.grid(column=0, row=5, sticky=tk.W)
first_drop = ttk.Combobox(app, values=sorted(cities.keys()))
pp.pprint(dict(first_drop))
first_drop.grid(column=1, row=5)
first_drop.current(0)

# airport name textboxes
first_city_text_label = tk.Label(app, text='Name of airport:',
                                 font=('bold', 14), padx=10, pady=5)
first_city_text_label.grid(column=0, row=10, sticky=tk.W)
first_city_text = ttk.Entry(app)
first_city_text.grid(column=1, row=10, sticky=tk.EW, ipadx=65)
second_city_text_label = tk.Label(app, text='Name of airport:',
                                  font=('bold', 14), padx=10, pady=5)
second_city_text_label.grid(column=0, row=20, sticky=tk.W)
second_city_text = ttk.Entry(app)
second_city_text.grid(column=1, row=20, columnspan=2, sticky=tk.EW)

# second airport
second_airport_label = tk.Label(app, text='Second City:',
                                font=('bold', 14), padx=10, pady=5)
second_airport_label.grid(column=0, row=15, sticky=tk.W)
second_drop = ttk.Combobox(app, values=sorted(cities.keys()))
pp.pprint(dict(second_drop))
second_drop.grid(column=1, row=15)
second_drop.current(0)

# create result textbox
first_text_label = tk.Label(app, text="Distance in nautical miles:",
                            font=('bold', 14))
first_text_label.grid(column=0, row=25, padx=10, pady=5)
first_text = ttk.Entry(app)
first_text.grid(column=1, row=25, padx=10, pady=5)

# create calculate button
button = tk.Button(app, text="Calculate Distance", command=calculate)
button.grid(column=0, row=30, padx=10, pady=5, columnspan=2, sticky=tk.EW)

# create quit button
button = tk.Button(app, text="Exit Program", command=app.quit)
button.grid(column=0, row=35, padx=10, pady=5, columnspan=2, sticky=tk.EW)

# Start program
app.mainloop()
