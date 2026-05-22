import pandas as pd


def patient_risk_segments(df):
    now = df["service_date"].max() + pd.Timedelta(days=1)

    patient_df = df.groupby("patient_id").agg(
        recency=("service_date", lambda x: (now - x.max()).days),
        frequency=("claim_id", "count"),
        total_claim_amount=("claim_amount", "sum"),
        avg_claim_amount=("claim_amount", "mean"),
        readmission_count=("readmission_30d", "sum"),
        ed_visit_count=("ed_visit_flag", "sum"),
        avg_los=("length_of_stay", "mean")
    ).reset_index()

    def assign_segment(row):
        if row["readmission_count"] > 0 or row["ed_visit_count"] >= 2:
            return "High Risk"
        elif row["total_claim_amount"] >= patient_df["total_claim_amount"].quantile(0.75):
            return "High Cost"
        elif row["frequency"] >= 3:
            return "Frequent Utilizer"
        else:
            return "Low Risk"

    patient_df["patient_segment"] = patient_df.apply(assign_segment, axis=1)
    return patient_df


def run_rfm(df):
    segment_df = patient_risk_segments(df)
    segment_df.to_csv("reports/patient_segments.csv", index=False)
    return segment_df