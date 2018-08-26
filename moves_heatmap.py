import pandas as pd
from gmplot import gmplot
import numpy as np


if __name__ == '__main__':
    places = pd.read_csv('data/places.csv')
    lat = places['Latitude']
    lon = places['Longitude']
    dates = places['Date']

    gmap = gmplot.GoogleMapPlotter(lat[0], lon[0], 5)
    gmap.heatmap(lat, lon, radius=10, maxIntensity=10)
    gmap.draw("my_map_heatmap.html")
