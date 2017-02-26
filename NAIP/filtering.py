import ee
import ee.mapclient

ee.Initialize()

lat = 46.80514
lng = -99.22023
lng_lat = ee.Geometry.Point(lng, lat)

collection = ee.ImageCollection('USDA/NAIP/DOQQ')
naip = collection.filterBounds(lng_lat)
naip_2015 = naip.filterDate('2015-01-01', '2015-12-31')

print(naip_2015.size().getInfo())
vis = {'bands': ['N', 'R', 'G']}
ee.mapclient.centerMap(lng, lat, 12)
ee.mapclient.addToMap(naip_2015,vis)


image = ee.Image('USDA/NAIP/DOQQ/m_4609915_sw_14_1_20100629')
ee.mapclient.centerMap(lng, lat, 12)
ee.mapclient.addToMap(image,vis)