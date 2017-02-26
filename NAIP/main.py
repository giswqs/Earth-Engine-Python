import ee
import ee.mapclient

ee.Initialize()

image = ee.Image('USDA/NAIP/DOQQ/m_3712213_sw_10_1_20140613')
ee.mapclient.centerMap(-122.466123, 37.769833, 17)
ee.mapclient.addToMap(image)