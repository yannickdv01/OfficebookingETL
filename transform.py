import pandas as pd

def transform(dataframe_workplaces, dataframe_bookings):
    dataframe_workplaces.fillna('')
    dataframe_bookings.fillna('')

    subset_dataframe_workplaces = dataframe_workplaces[["id", "tags", "seats", "zone_id", "parent_workplace_id", "category_id", "workspace_id", "map_x_coord"]]
    subset_dataframe_workplaces.rename(columns={'id':'asset_id', 'tags':'labels', 'seats':'capacity', 'zone_id':'occ_capacity', 'parent_workplace_id':'parent_asset', 'category_id':'category', 'workspace_id':'main_category', 'map_x_coord':'coords'}, inplace = True)
    d_asset_dataframe = subset_dataframe_workplaces.astype({'asset_id':'int', 'labels':'str', 'capacity':'int', 'occ_capacity':'int', 'parent_asset': 'int', 'category': 'str', 'main_category': 'str', 'coords': 'str'})

    subset_dataframe_bookings = dataframe_bookings[['attendants', 'user_id', 'canceled_at', 'id']]
    subset_dataframe_bookings['canceled'] = False
    subset_dataframe_bookings.loc[subset_dataframe_bookings['canceled_at'] != None, 'canceled'] = True
    subset_dataframe_bookings.rename(columns={'id':'booking_id', 'user_id':'booked_by', 'attendants':'booking_users'}, inplace=True)
    print(list(subset_dataframe_bookings.columns.values))
    d_bookings_dataframe = subset_dataframe_bookings.astype({'booking_users': 'str', 'booked_by': 'int', 'canceled_at': 'str'})

    return d_asset_dataframe, d_bookings_dataframe