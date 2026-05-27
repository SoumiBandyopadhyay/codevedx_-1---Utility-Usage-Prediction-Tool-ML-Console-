import pandas as pd

FILE_PATH = "../data/usage_data.csv"

def add_data():
    month = int(input("Enter month: "))
    units = int(input("Enter units used: "))
    bill = int(input("Enter bill amount: "))

    new_data = pd.DataFrame({
        "month": [month],
        "units_used": [units],
        "bill_amount": [bill]
    })

    new_data.to_csv(FILE_PATH, mode='a', header=False, index=False)

    print("Data added successfully!")

def view_data():
    df = pd.read_csv(FILE_PATH)
    print(df)

def update_data():
    df = pd.read_csv(FILE_PATH)

    month = int(input("Enter month to update: "))

    if month in df["month"].values:
        units = int(input("New units used: "))
        bill = int(input("New bill amount: "))

        df.loc[df["month"] == month, "units_used"] = units
        df.loc[df["month"] == month, "bill_amount"] = bill

        df.to_csv(FILE_PATH, index=False)

        print("Data updated!")
    else:
        print("Month not found!")
