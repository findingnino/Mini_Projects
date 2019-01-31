import folium

map = folium.Map(location = [40.0757384,-74.4041622], zoom_start=10)

map.save("map2.html")
#map.save("map2.png") #doesn't seem to work, file is corrupted???