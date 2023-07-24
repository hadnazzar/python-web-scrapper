import os
import pandas as pd
import camelot

def extract_pdf_data(pdf_file):
    # Extract data from the PDF using camelot-py
    tables = camelot.read_pdf(pdf_file, flavor="stream")

    # Process extracted tables
    data_list = []
    for table in tables:
        # Convert each table to a Pandas DataFrame
        df = table.df

    # Save the extracted data to a CSV file
    df = pd.DataFrame(data_list)
    csv_file = "extracted_data.csv"
    df.to_csv(csv_file, index=False)
    print(f"Extracted data saved to {csv_file}.")

if __name__ == "__main__":
    target_pdf = "sample.pdf"  # Replace with the path to your target PDF file
    extract_pdf_data(target_pdf)