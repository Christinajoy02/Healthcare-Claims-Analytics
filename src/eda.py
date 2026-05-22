import matplotlib.pyplot as plt


def run_eda(df):
    # 1. Monthly Claim Amount Trend
    monthly = df.groupby("month", as_index=False)["claim_amount"].sum()

    plt.figure()
    plt.plot(monthly["month"], monthly["claim_amount"])
    plt.xticks(rotation=45)
    plt.title("Monthly Claim Amount Trend")
    plt.tight_layout()
    plt.savefig("reports/monthly_claim_amount.png")
    plt.close()

    # 2. Claim Amount by Department
    dept = df.groupby("department", as_index=False)["claim_amount"].sum()

    plt.figure()
    plt.bar(dept["department"], dept["claim_amount"])
    plt.xticks(rotation=45)
    plt.title("Claim Amount by Department")
    plt.tight_layout()
    plt.savefig("reports/claim_by_department.png")
    plt.close()

    # 3. Length of Stay vs Claim Amount
    plt.figure()
    plt.scatter(df["length_of_stay"], df["claim_amount"])
    plt.xlabel("Length of Stay")
    plt.ylabel("Claim Amount")
    plt.title("Length of Stay vs Claim Amount")
    plt.tight_layout()
    plt.savefig("reports/los_vs_claim_amount.png")
    plt.close()