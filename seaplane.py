import math

# radius of Earth in kilometers
R = 6383.0

# create input for first airport and set as first_airport
first_airport = input("Please input the three letter code for \
an airport: ").lower()
airport_names = {"atl": "Hartsfield-Jackson Atlanta International Airport",
                 "dfw": "DFW International Airport",
                 "jfk": "John F. Kennedy International Airport",
                 "lax": "Los Angeles International Airport",
                 "lhr": "London Heathrow Airport",
                 "ord": "O'Hare International Airport",
                 "sea": "Seattle-Tacoma International Airport",
                 "tul": "Tulsa International Airport",
                 "cgd": "Paris Charles de Gaulle Airport",
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

keepGoing = True
while(keepGoing):
    if first_airport in latitudes:
        first_lat = latitudes[first_airport]
        first_lon = longitudes[first_airport]
        airport1 = airport_names[first_airport]
        keepGoing = False
    else:
        print("Invalid airport code.")
        first_airport = input("Please input the three letter code for \
an airport: ").lower()

# create input for second airport and set as second_airport
second_airport = input("Please input the three letter code for \
a second airport: ").lower()

keepGoing = True
while(keepGoing):
    if second_airport in latitudes:
        second_lat = latitudes[second_airport]
        second_lon = longitudes[second_airport]
        airport2 = airport_names[second_airport]
        keepGoing = False
    else:
        print("Invalid airport code.")
        second_airport = input("Please input the three letter code for a \
second airport: ").lower()

# calculate distance between first_airport and second_airport
lat1 = math.radians(float(first_lat))
lon1 = math.radians(float(first_lon))
lat2 = math.radians(float(second_lat))
lon2 = math.radians(float(second_lon))

dlon = lon2 - lon1
dlat = lat2 - lat1

a = math.sin(dlat / 2)**2 + math.cos(lat1) * \
    math.cos(lat2) * math.sin(dlon / 2)**2

c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

# distance in kilometers
distance = R * c

# convert kilometers to miles
mi = distance / 1.609
# convert kilometers to nautical miles
nmi = distance / 1.852

# display distance
print(airport1 + " and " + airport2 + " are " + str(round(distance, 2)) + " \
kilometers apart.")
print("They are " + str(round(mi, 2)) + " miles apart and " +
      str(round(nmi, 2)) + " nautical miles apart.")
