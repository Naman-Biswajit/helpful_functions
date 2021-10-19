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


# ArcPy Field Mappings Example
def select_and_save_nearby_features(out_featureset, map_index_length, user_selected_layers):
    # Create buffer that's 2x the size of the `map_index_length`
    temp_length = float(map_index_length.split()[0]) * 2
    buffer_size = temp_length * 1609  # need to convert to meters, buffer won't respond to `Miles` as a unit
    arcpy.Buffer_analysis(out_featureset, directory_gdb + "\\_Working\\selected_line_buffered", buffer_size,
                          dissolve_option="ALL")

    for l in user_selected_layers:
        l_path = str(sde_directory_gdb + "\\" + l['fd'] + "\\" + l['fc'])

        temp_selected_features = arcpy.SelectLayerByLocation_management(
            in_layer=l_path,
            overlap_type="INTERSECT",
            select_features=directory_gdb + "\\_Working\\selected_line_buffered",
            selection_type="NEW_SELECTION"
        )

        fields_to_keep = l["fields_to_keep"]

        mapS = arcpy.FieldMappings()  # create an empty field mapping object
        # for each field, create an individual field map, and add it to the field mapping object
        for field in fields_to_keep:
            map = arcpy.FieldMap()
            map.addInputField(temp_selected_features, field)
            mapS.addFieldMap(map)

        newCopy = arcpy.FeatureClassToFeatureClass_conversion(temp_selected_features, directory_gdb + "\\" + l['fd'] + "\\", l['fc'], "#", mapS)

        fc_name = str(l["fc"])
        if fc_name == "Switches" or fc_name == "Substations":
            arcpy.AddField_management(directory_gdb + "\\" + l['fd'] + "\\" + l['fc'], "SYM_ROTATION", "DOUBLE")
        elif fc_name in ["Access_Barriers", "Access_Roads", "SC_Gate_Locations", "Special_Considerations"]:
            arcpy.AddField_management(directory_gdb + "\\" + l['fd'] + "\\" + l['fc'], "ROTATION", "DOUBLE")
            #  These specific feature classes need a 'ROTATION' field added to them

    print("done")
    return True