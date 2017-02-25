#!/usr/bin/env python
"""Display an image given its ID."""

import ee
import ee.mapclient

ee.Initialize()
image = ee.Image('srtm90_v4')
vis_params = {'min': 0, 'max': 3000}
ee.mapclient.addToMap(image, vis_params,"mymap")
