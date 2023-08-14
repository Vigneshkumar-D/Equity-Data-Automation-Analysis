import sqlite3

def compute_average_prices(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    def compute_average(query, label):
        cursor.execute(query)
        average_prices = cursor.fetchall()

        print(f"Stock-wise average {label} prices for July 2023:")
        for row in average_prices:
            print(f"{row[0]}: {row[1]}")

        print("\n")

    query_open = '''
        SELECT SC_NAME, AVG(OPEN) AS avg_open
        FROM stocks_data
        GROUP BY SC_NAME;
    '''
    compute_average(query_open, "OPEN")

    query_high = '''
        SELECT SC_NAME, AVG(HIGH) AS avg_high
        FROM stocks_data
        GROUP BY SC_NAME
    '''
    compute_average(query_high, "HIGH")

    query_low = '''
        SELECT SC_NAME, AVG(LOW) AS avg_low
        FROM stocks_data
        GROUP BY SC_NAME;
    '''
    compute_average(query_low, "LOW")

    query_close = '''
        SELECT SC_NAME, AVG(CLOSE) AS avg_close
        FROM stocks_data
        GROUP BY SC_NAME;
    '''
    compute_average(query_close, "CLOSE")

    conn.close()

if __name__ == "__main__":
    db_file = 'equitydb.db'
    compute_average_prices(db_file)
