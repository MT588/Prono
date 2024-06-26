import datetime
import os
import csv

def load_data(file_path):
    data = []  # Initialize an empty list to store the data
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = list(csv.reader(csvfile, delimiter=';'))  # Convert to list
        for row in reader:
            # Combine row[2] and row[3] to form a complete datetime string
            datetime_str = f"{row[2]} {row[3]}"
            # Parse the combined string into a datetime object
            date_obj = datetime.datetime.strptime(datetime_str, '%b %d, %Y %H:%M')
            # Format the datetime object into a more readable string format
            formatted_date = date_obj.strftime('%a %b %d, %Y %H:%M')
            # Replace the date and time strings in the row with the formatted date string
            new_row = row[:1] + [formatted_date] + row[4:]  # Adjust the row to include the formatted date string
            data.append(new_row)  # Append the modified row to the data list

    return data

data = load_data('PlayerData/MOD_Invulblad prono Bol EK2024.csv')
print(data)