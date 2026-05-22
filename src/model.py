import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split


def _calendar_features(df):
    monthly = df.groupby("month", as_index=False)["claim_amount"].sum()
    monthly["month_date"] = pd.to_datetime(monthly["month"])
    monthly["year"] = monthly["month_date"].dt.year
    monthly["month_num"] = monthly["month_date"].dt.month
    return monthly


def run_model(df):
    m = _calendar_features(df)

    X = m[["year", "month_num"]]
    y = m["claim_amount"]

    if len(m) < 4:
        print("Not enough monthly data for forecasting model.")
        return None

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )

    model = Ridge()
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)

    results = X_test.copy()
    results["actual_claim_amount"] = y_test.values
    results["predicted_claim_amount"] = preds
    results["mae"] = mae

    results.to_csv("reports/claim_forecast_results.csv", index=False)

    print(f"Healthcare claim forecasting MAE: {mae:.2f}")

    return model