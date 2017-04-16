import ee
import ee.mapclient

ee.Initialize()

fromFT = ee.FeatureCollection('ft:1CLldB-ULPyULBT2mxoRNv7enckVF0gCQoD2oH7XP')
polys = fromFT.geometry()
centroid = polys.centroid()
lng, lat = centroid.getInfo()['coordinates']
# print("lng = {}, lat = {}".format(lng, lat))
# ee.mapclient.centerMap(lng, lat, 10)
# ee.mapclient.addToMap(fromFT)

count = fromFT.size().getInfo()
ee.mapclient.centerMap(lng, lat, 10)

for i in range(2, 2 + count):
    fc = fromFT.filter(ee.Filter.eq('system:index', str(i)))
    ee.mapclient.addToMap(fc)