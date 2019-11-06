# -*- coding: utf-8 -*-
"""
Author: Leonardo Laipelt dos Santos

Lab: Large Scale Hydrology research group - UFRGS\Brazil
"""

import folium
import ee
import webbrowser

class Map(object):
    def __init__(self,center=[0, 0],zoom=3):
        self._map = folium.Map(location=center,zoom_start=zoom)
        return

    def addLayer_Image(self,img,visParams,name):
         map_id = ee.Image(img.visualize(**visParams)).getMapId()
         tile_url_template = "https://earthengine.googleapis.com/map/{mapid}/{{z}}/{{x}}/{{y}}?token={token}"
         mapurl = tile_url_template.format(**map_id)
         folium.WmsTileLayer(mapurl,layers=name,name=name).add_to(self._map)
         return
     
    def addLayer_Point(self,long_tower, lat_tower):
        folium.Marker([lat_tower,long_tower], popup='<i>Tower</i>').add_to(self._map)
        return
    
    def addLayer_Polygon(self,geometry,Name):
        bounds_geometry = geometry.getInfo()
        folium.GeoJson(data = bounds_geometry,name = Name,
                       style_function=lambda feature: {
                               'fillColor': 'red',
                               'color' : 'red',
                               'weight' : 1,
                               'fillOpacity' : 0.3,
                               }).add_to(self._map)
        return

    def add_LayerControl(self):
         self._map.add_child(folium.map.LayerControl())
         return
    
    def Open(self):
        self._map.save('Map.html')
        return webbrowser.open('Map.html')
    
    