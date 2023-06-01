import folium
import pandas as pd

df = pd.read_csv("Volcanoes.txt")
lat = list(df["LAT"])
lon = list(df["LON"])
name = list(df["NAME"])
fg = folium.FeatureGroup(name = "My map")
for i,j,k in zip(lat, lon, name):
    fg.add_child(folium.CircleMarker(location = [i,j], popup= k, radius = 4, fill_opacity = 0.8, fill_color = "red", color = "grey"))
fg.add_child(folium.GeoJson(data=open("world.json","r",encoding = "utf-8-sig").read())) 
map = folium.Map(location = [28.7041,77.1025], tiles = "Stamen Terrain", zoom_start=6)
map.add_child(fg)
map.save("Map.html")