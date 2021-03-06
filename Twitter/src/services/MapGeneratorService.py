"""Map Generator Service

This script allows the user to put a pin on a map based on coordinates
using the folium library using the json file named "tweets_info.json"
that must be included in a folder "data". Every pin will have a popup
when the user clicks on it and will contain different information
about a tweet.

This tool accepts just json files

This script requires that `folium` be installed within the Python
environment you are running this script in.

This file can also be imported as a module and contains the following
functions:

    * mark_on_map - marks the pin on the map
    * generate_map - populates the map with in information from the
    json file
"""
import json

import folium as folium

"""
    Global settings
"""
map = folium.Map(location=[45, 0], zoom_start=2, tiles='cartodbdark_matter')
tooltip = "Click for more info"


def mark_on_map(info, hashtag):
    """
    Marks the pin on the map with the additional information: author,
    date and content

    Parameters
    ----------
    :param info:
        The list that contains the coordinates and other information
        needed to be plotted on the map
    :type info: list
    :param hashtag:
        the used hashtag
    :type hashtag: str

    :return: None
    """
    if info["coordinates"][0] != 0 or info["coordinates"][1] != 0:
        folium.Marker([info["coordinates"][0], info["coordinates"][1]],
                      popup=folium.Popup(
                          html='<style type="text/css" scoped> .leaflet-popup-content-wrapper { width: 250px }</style>'
                               f'<h5><strong>{info["author"]}\'s tweet</strong></h5>'
                               f'<h6>Using the hashtag: <strong>#{hashtag}</strong></h6>'
                               f'<a href="https://twitter.com/twitter/status/{info["id_str"]}"> Click to '
                               f'see the tweet</a> '
                               f'</br>'
                               f'<small>'
                               f'Created on: {info["date"]["day"]}.{info["date"]["month"]}.{info["date"]["year"]}'
                               f'</small> '
                      ),
                      tooltip=tooltip,
                      icon=folium.Icon(icon="globe", color="lightblue")).add_to(map)


def generate_map(hashtag: str, nr_tweets: int):
    """
    Populates the map with in information from the json file. The
    generated file will be located in a folder named "data" and it
    will contain the map html

    :param hashtag:
        the raw hashtag from the user
    :type hashtag: str
    :param nr_tweets:
        the maximum number of tweets
    :type nr_tweets: int

    :return: None
    """
    with open("./data/tweets_info.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        for chunk in data["info"]:
            mark_on_map(chunk, hashtag)
        map.save(f"../data/{hashtag}{nr_tweets}_map.html")

