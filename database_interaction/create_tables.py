import sqlite3
import csv

def create_tables(conn):
    # Connect to SQLite database using context manager
        cursor = conn.cursor()
        # Create the table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS stocks_data (
                date DATE,
                SC_CODE TEXT,
                SC_NAME TEXT,
                SC_GROUP TEXT,
                SC_TYPE TEXT,
                OPEN REAL,
                HIGH REAL,
                LOW REAL,
                CLOSE REAL,
                LAST REAL,
                PREVCLOSE REAL,
                NO_TRADES INTEGER,
                NO_OF_SHRS INTEGER,
                NET_TURNOV REAL,
                TDCLOINDI REAL
            )
        ''')

        print("Table 'stocks_data' created successfully.")

def insert_data(conn, csv_file_path, date):
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip header
        for row in csv_reader:
            query = '''
                INSERT INTO stocks_data
                (date, SC_CODE, SC_NAME, SC_GROUP, SC_TYPE, OPEN, HIGH, LOW, CLOSE, LAST, PREVCLOSE, NO_TRADES, NO_OF_SHRS, NET_TURNOV, TDCLOINDI)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            '''
            cursor = conn.cursor()
            cursor.execute(query, [date] + row)
            conn.commit()

        print("Data inserted into table 'stocks_data'.")