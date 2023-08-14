import os
import sqlite3
from database_interaction import create_tables
from data_downloading.download_bhav_copy import download_bhav_copy
from data_processing.process_data import process_bhav_copy
from database_interaction.compute_average_prices import compute_average_prices
from database_interaction.create_tables import create_tables, insert_data

def main():
    # Download Bhav Copy files
    download_bhav_copy()

    file_path = "D:/vs_code_file/equity-data-automation-analysis/processed_data/"
    processed_dir = "processed_data"
    os.makedirs(processed_dir, exist_ok=True)
    process_bhav_copy(file_path)
    

    
    #Days for which equity data is not available
    invalid_days = [1, 2, 8, 9, 15, 16, 22, 23, 29, 30]
    
    db_file = 'equitydb.db'
    csv_folder = 'processed_data'
    month = '07'
    year = '23'

    conn = sqlite3.connect(db_file)

    # Create database tables
    create_tables(conn)

    #Itreating over the CSV files in the processed_data folder
    for day in range(1, 32):
        if(day not in invalid_days):
            day_str = str(day).zfill(2)
            # print(day_str)
            csv_file_path = os.path.join(csv_folder, f'EQ{day_str}{month}{year}.CSV')
            print(csv_file_path)
            date = f'{year}-{month}-{day_str}'
            if os.path.exists(csv_file_path):
                insert_data(conn, csv_file_path, date)
                print(f'Inserted data for {date}')

    conn.close()
    print("Data upload complete.")

    #computing average price for OPEN, HIGH, LOW, and CLOSE.
    compute_average_prices(db_file)

if __name__ == "__main__":
    main()
