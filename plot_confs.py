from geopy.geocoders import Nominatim
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import pickle

# Visualize how top tier conferences move

class citylocs():
    cities = {}
    geolocator = Nominatim(user_agent="MyApp")
    def __init__(self):
        try:
            with open('cities.pickle', 'rb') as cache:
                self.cities = pickle.load(cache)
                cache.close()
        except:
            self.cities = {}
    
    def get_loc(self, city):
        if city not in self.cities:
            loc = self.geolocator.geocode(city, timeout=None)
            if loc == None:
                print('City {} not found'.format(city))
            self.cities[city] = (loc.address, loc.latitude, loc.longitude)
            with open('cities.pickle', 'wb') as cache:
                pickle.dump(self.cities, cache)
                cache.close()
        print(self.cities[city])
        return self.cities[city]

cl = citylocs()

def get_locs(cities):
    lats = []
    lons = []
    city_names = []
    for city in cities:
        loc = cl.get_loc(city)
        lats.append(loc[1])
        lons.append(loc[2])
        city_names.append(city)
    return (lats, lons, city_names)

def add_locs(fig, cities, col, name):
    lats, lons, cities = get_locs(cities)
    fig.add_trace(go.Scattergeo(
        lat = lats,
        lon = lons,
        hoverinfo = 'text',
        text = cities,
        name = name,
        mode = 'markers',
        marker = dict(
            size = 5,
            color = col,
            line = dict(
                width = 3,
                color = col
            )
        )))

    for i in range(len(cities)-1):
        fig.add_trace(
            go.Scattergeo(
                lat = [lats[i], lats[i+1]],
                lon = [lons[i], lons[i+1]],
                mode = 'lines',
                line = dict(width = 2, color = col),
                showlegend = False,
                hoverinfo = 'skip',
            )
        )


usenix_sec_cities = [
    'San Diego, USA',      # 2014
    'Washington, D.C., USA', # 2015
    'Austin, USA',        # 2016
    'Vancouver, Canada',  # 2017
    'Baltimore, USA',     # 2018
    'Santa Clara, USA',   # 2019
    # virtual
    # virtual
    'Boston, USA',        # 2022
    'Anaheim, USA',       # 2023
    'Philadelphia, USA',  # 2024
]

ndss_cities = [
    'San Diego, USA'
]

oakland_cities = [
    'Berkeley, USA',      # 2014
    'San Jose, USA',      # 2015
    'San Jose, USA',      # 2016
    'San Jose, USA',      # 2017
    'San Francisco, USA', # 2018
    'San Francisco, USA', # 2019
    'San Francisco, USA', # 2020
    'San Francisco, USA', # 2021
    'San Francisco, USA', # 2022
    'San Francisco, USA', # 2023
    'San Francisco, USA', # 2024
]

ccs_cities = [
    'Scottsdale, USA',    # 2014
    'Denver, USA',        # 2015
    'Vienna, Austria',    # 2016
    'Dallas, USA',        # 2017
    'Toronto, Canada',    # 2018
    'London, UK',         # 2019
    # virtual
    # virtual
    'Los Angeles, USA',   # 2022
    'Copenhagen, Denmark', # 2023
    'Salt Lake City, USA', # 2024
]

micro_cities = [
    'Davis, USA',         # 2014
    'Cambridge, UK',      # 2015
    'Waikiki, USA',       # 2016
    'Taipei, Taiwan',     # 2017
    'Boston, USA',        # 2018
    'Fukuoka, Japan',     # 2019
    'Columbus, USA',      # 2020
    # 'virtual'
    # 'virtual'
    'Chicago, USA',       # 2022
    'Toronto, Canada',    # 2023
    'Austin, USA',        # 2024
]

isca_cities = [
    'Minneapolis, USA',   # 2014
    'Portland, USA',      # 2015
    'Seoul, South Korea', # 2016
    'Toronto, Canada',    # 2017
    'Los Angeles, USA',   # 2018
    'Phoenix, USA',       # 2019
    # virtual
    # virtual
    'New York, USA',      # 2022
    'Orlando, USA',       # 2023
    'Buenos Aires, Argentina', # 2024
]

asplos_cities = [
    'Salt Lake City, USA',# 2014
    'Istanbul, Turkey',   # 2015
    'Atlanta, USA',       # 2016
    "Xi'an, China",       # 2017
    'Williamsburg, USA',  # 2018
    'Providence, USA',    # 2019
    #virtual
    # virtual
    'Lausanne, Switzerland', # 2022
    'Vancouver, Canada',  # 2023
    'San Diego, USA',     # 2024
]

sosp_cities = [
    'Monterey, USA',      # 2015
    'Shanghai, China',    # 2017
    'Huntsville, Canada', # 2019
    # virtual
    'Koblenz, Germany',   # 2023
]

osdi_cities = [
    'Broomfield, USA',    # 2014
    'Savannah, USA',      # 2016
    'Carlsbad, USA',      # 2018
    # virtual 2020
    # virtual 2021
    'Carlsbad, USA',      # 2022
    'Boston, USA',        # 2024
]

fse_cities = [
    'Hong Kong, China',   # 2014
    'Bergamo, Italy',     # 2015
    'Seattle, USA',       # 2016
    'Paderborn, Germany', # 2017
    'Lake Buena Vista, FL, USA', # 2018
    'Tallinn, Estonia',   # 2019
    # virtual
    'Athens, Greece',     # 2021
    'Singapore',          # 2022
    'San Francisco, USA', # 2023
    'Porto de Galinhas, Brazil', # 2024
]

icse_cities = [
    'Hyderabad, India',   # 2014
    'Florence, Italy',    # 2015
    'Austin, USA',        # 2016
    'Buenos Aires, Argentina', # 2017
    'Gothenburg, Sweden', # 2018
    'Montreal, Canada',   # 2019
    'Seoul, South Korea', # 2020
    'Madrid, Spain',      # 2021
    'Pittsburgh, USA',    # 2022
    'Melbourne, Australia', # 2023
    'Lisbon, Portugal',   # 2024
]

fig = go.Figure()

add_locs(fig, usenix_sec_cities, 'rgb(139, 0, 0)', 'USENIX SEC') # Dark Red
add_locs(fig, ndss_cities, 'rgb(204, 85, 0)', 'ISOC NDSS') # Burnt Orange
add_locs(fig, oakland_cities, 'rgb(210, 43, 43)', 'IEEE SSP') # Cadmium Red
add_locs(fig, ccs_cities, 'rgb(210, 4, 45)', 'ACM CCS') # Cherry


# Architecture
add_locs(fig, micro_cities, 'rgb(34, 139, 34)', 'MICRO') # Forest Green
add_locs(fig, isca_cities, 'rgb(76, 187, 23)', 'ISCA') # Kelly Green

# Systems
add_locs(fig, asplos_cities, 'rgb(0, 71, 171)', 'ASPLOS') # Cobald Blue
add_locs(fig, sosp_cities, 'rgb(0, 0, 139)', 'SOSP') # Dark Blue
add_locs(fig, osdi_cities, 'rgb(63, 0, 255)', 'OSDI') # Indigo

# SE
add_locs(fig, fse_cities, 'rgb(255, 191, 0)', 'FSE') # Amber
add_locs(fig, icse_cities, 'rgb(253, 218, 13)', 'ICSE') # Cadmium Yellow

fig.update_layout(
    title_text = 'Conference Locations for Security/Architecture/Systems/Software Engineering: From 2014 to 2024',
    #showlegend = True,
    #autosize=True,
    geo = dict(
#        scope = 'north america',
#        projection_type = 'azimuthal equal area',
        projection_rotation=dict(
            lat=0,
            lon=-115
        ),
        showland = True,
        landcolor = 'rgb(243, 243, 243)',
        countrycolor = 'rgb(204, 204, 204)',
    ),
)

fig.show()
fig.write_html('conf_locs.html')