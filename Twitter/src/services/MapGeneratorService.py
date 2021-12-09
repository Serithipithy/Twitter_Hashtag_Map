import json

import folium as folium

map = folium.Map(location=[45, 0], zoom_start=2, tiles='cartodbdark_matter')
tooltip = "Click for more info"


def mark_on_map(info):
    if info["coordinates"][0] != 0 or info["coordinates"][1] != 0:
        folium.Marker([info["coordinates"][0], info["coordinates"][1]],
                      popup=folium.Popup(
                          html='<style type="text/css" scoped> .leaflet-popup-content-wrapper { width: 250px }</style>'
                               f'<h5><strong>{info["author"]}\'s tweet</strong></h5>'
                               f'</br>'
                               f'<small>Created on: {info["date"]["day"]}.{info["date"]["month"]}.{info["date"]["year"]}</small>'
                               f'</br>'
                               f'<h6><strong>{info["text"]}</strong></h6>',
                      ),
                      tooltip=tooltip,
                      icon=folium.Icon(icon="globe", color="lightblue")).add_to(map)


def generate_map():
    with open("./data/tweets_info.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        for chunk in data["info"]:
            mark_on_map(chunk)
        map.save("../data/tweets_map.html")
