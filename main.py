from extract import extract
from transform import transform
from load import load

if __name__ == "__main__":
    dataframe_workplace, dataframe_bookings = extract()
    d_asset_dataframe, d_bookings_dataframe = transform(dataframe_workplace, dataframe_bookings)
    load(d_asset_dataframe, d_bookings_dataframe)