from google.oauth2 import service_account
import pandas_gbq

def load(dataframe_assets, bookings_dataframe):
    credentials = service_account.Credentials.from_service_account_file('officebooking-project-7801c768d46d.json')

    pandas_gbq.to_gbq(dataframe_assets, 'Officebooking_dataset.d_asset', 'officebooking-project', credentials=credentials, if_exists='replace')
    pandas_gbq.to_gbq(bookings_dataframe, 'Officebooking_dataset.d_booking', 'officebooking-project', credentials=credentials, if_exists='replace')