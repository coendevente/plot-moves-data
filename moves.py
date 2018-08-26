import pandas as pd
from gmplot import gmplot


if __name__ == '__main__':
    places = pd.read_csv('data/places.csv')
    lat = places['Latitude']
    lon = places['Longitude']
    dates = places['Date']

    startdate = min(dates[0])

    gmap = gmplot.GoogleMapPlotter(lat[0], lon[0], 13)
    for i in range(len(lat)):

        color = '#FF0000'
        gmap.marker(lat[i], lon[i], color)
    gmap.draw("my_map_no_routes.html")

    gmap.plot(lat, lon, '#afdb6c', size=40, marker=False, alpha=.5)
    gmap.draw("my_map.html")