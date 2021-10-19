# Copy Feature Layer out of ESRI Portal

from arcgis.gis import GIS
from arcgis.features import FeatureLayer

url_gis = # URL to AGOL or Portal
url_fl =  # URL for feature layer to download as feature class
user =  # AGOL or Portal username
pwd = # user password
fgdb = # path to file geodatabase
fc = # name of feature class

gis = GIS(url_gis, user, pwd)
fl = FeatureLayer(url_fl)
fs = fl.query()
fs.save(fgdb, fc)