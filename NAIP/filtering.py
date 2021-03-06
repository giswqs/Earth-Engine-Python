import ee
import ee.mapclient

ee.Initialize()

collection = ee.ImageCollection('USDA/NAIP/DOQQ')


fromFT = ee.FeatureCollection('ft:1CLldB-ULPyULBT2mxoRNv7enckVF0gCQoD2oH7XP')
polys = fromFT.geometry()
centroid = polys.centroid()
lng, lat = centroid.getInfo()['coordinates']
print("lng = {}, lat = {}".format(lng, lat))

# lat = 46.80514
# lng = -99.22023
lng_lat = ee.Geometry.Point(lng, lat)
# naip = collection.filterBounds(lng_lat)
naip = collection.filterBounds(polys)
naip_2015 = naip.filterDate('2015-01-01', '2015-12-31')
ppr = naip_2015.mosaic().clip(polys)

# print(naip_2015.size().getInfo())
vis = {'bands': ['N', 'R', 'G']}
ee.mapclient.centerMap(lng, lat, 10)
# ee.mapclient.addToMap(naip_2015,vis)
ee.mapclient.addToMap(ppr,vis)
# ee.mapclient.addToMap(fromFT)

# image = ee.Image('USDA/NAIP/DOQQ/m_4609915_sw_14_1_20100629')
# ee.mapclient.centerMap(lng, lat, 12)
# ee.mapclient.addToMap(image,vis)
