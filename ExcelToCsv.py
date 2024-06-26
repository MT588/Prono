import os
import csv

def read_csv_data(file_path):
    data = []
    start_row = 9
    end_row = 44
    max_columns = 9

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for i, row in enumerate(reader):
            if start_row <= i <= end_row:
                # Extract only the first 9 columns from the current row
                data.append(row[:max_columns])

    return data

def write_csv_data(file_path, data):
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:  # Removed space in 'w '
        writer = csv.writer(csvfile, delimiter=';')
        for row in data:
            writer.writerow(row)

# Example usage
file_path = 'unfilteredExcel/Invulblad prono Bol EK2024.csv'
extracted_data = read_csv_data(file_path)

new_file_path = 'PlayerData/MOD_Invulblad prono Bol EK2024.csv'
write_csv_data(new_file_path, extracted_data)
