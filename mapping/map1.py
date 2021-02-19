import folium
import pandas

map = folium.Map(location =[38.58, -99.09], zoom_start=5, tiles = 'Stamen Terrain')
fga = folium.FeatureGroup(name='Volcanoes')
fgb = folium.FeatureGroup(name='Population')
data = pandas.read_csv('Volcanoes.txt')
html = """<h4>Volcano information:</h4>
Height: %s m
"""
def color(x):
    if x < 1500:
        return 'green'
    elif x >= 1500 and x < 2500:
        return 'orange'
    else:
        return 'red'


for i in range(data.shape[0]):
    iframe = folium.IFrame(html=html % str(str(data["ELEV"].iloc[i])+" m"), width=200, height=100)
    fga.add_child(folium.Marker(location=[data.LAT[i], data.LON[i]], popup=folium.Popup(iframe), icon=folium.Icon(color=color(int(data["ELEV"].iloc[i])))))


fgb.add_child(folium.GeoJson(data = open('world.json', 'r', encoding='utf-8-sig').read(), style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000 else 'orange' if 40000000 <= x['properties']['POP2005'] <= 70000000 else 'red'}))
map.add_child(fga)
map.add_child(fgb)
map.add_child(folium.LayerControl())
map.save('Map1.html')
