import pandas as pd
from src.utils import read_raw

def load_and_clean():
    df = read_raw()

    df = df.drop_duplicates()

    df["service_date"] = pd.to_datetime(df["service_date"])

    df = df[df["claim_amount"] > 0]
    df = df[df["patient_age"] > 0]

    df["length_of_stay"] = df["length_of_stay"].fillna(0)
    df["denied_flag"] = df["denied_flag"].fillna(0).astype(int)
    df["readmission_30d"] = df["readmission_30d"].fillna(0).astype(int)
    df["ed_visit_flag"] = df["ed_visit_flag"].fillna(0).astype(int)

    df["month"] = df["service_date"].dt.to_period("M").astype(str)
    df["weekday"] = df["service_date"].dt.day_name()
    df["is_weekend"] = df["service_date"].dt.weekday >= 5

   
    return df