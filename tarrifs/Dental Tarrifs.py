import pandas as pd

# Load the .xls file
file_path = r"tarrifs\(20121228024246 PM) 2013 Momentum Health Rates - Health Practitioners.xls.xlsx"
df = pd.read_excel(file_path,header=2)
while True:
    search_value = int(input("search for a tarrif code: "))  # Replace with the actual tariff code you are searching for
    filtered_df = df[df["Tariff code"] == search_value]

    # Print the found rows
    if not filtered_df.empty:
        print(filtered_df)
    elif search_value == 'q' :
        break
    else:
        print(f"No rows found with Tariff code: {search_value}")




