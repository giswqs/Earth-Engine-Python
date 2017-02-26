import ee
import ee.mapclient

ee.Initialize()

fromFT = ee.FeatureCollection('ft:1CLldB-ULPyULBT2mxoRNv7enckVF0gCQoD2oH7XP')
# print(fromFT.getInfo())


collection = ee.ImageCollection('LANDSAT/LC8_L1T_TOA')

path = collection.filterBounds(fromFT)

images = path.filterDate('2016-05-01', '2016-10-31')
print(images.size().getInfo())

median = images.median()

lat = 46.80514
lng = -99.22023
lng_lat = ee.Geometry.Point(lng, lat)
ee.mapclient.centerMap(lng, lat, 12)
vis = {'bands': ['B5', 'B4', 'B3'], 'max': 0.3}
ee.mapclient.addToMap(median,vis)
ee.mapclient.addToMap(fromFT)