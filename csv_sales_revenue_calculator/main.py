# Calculate Revenue and Generate a CSV

import csv

def calculate_revenue(csv_file, output_file):
    revenue = {}

    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            product = row["Product"]
            sales = int(row["Quantity"]) * float(row["Price"])
            revenue[product] = revenue.get(product, 0) + sales

    with open(output_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["Product", "Total Revenue"])
        for product, total in revenue.items():
            writer.writerow([product, total])

calculate_revenue("sales.csv", "revenue.csv")
