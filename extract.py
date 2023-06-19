import pandas as pd
from sqlalchemy import create_engine

def extract():
    engine =  create_engine('postgresql+psycopg2://postgres:Officebooking1@127.0.0.1/FinalPOC_db')

    connection = engine.connect()

    dataframe_workplaces = pd.read_sql("SELECT * FROM workplaces", connection)
    dataframe_bookings = pd.read_sql("SELECT * FROM bookings", connection)

    connection.close()

    return dataframe_workplaces, dataframe_bookings