# Equity Data Automation and Analysis

This project automates the process of downloading Bhav Copy files (equity data) from the BSE India website for the month of July 2023. It also uploads these files into an SQL database and performs data analysis on the uploaded data.

## Project Overview

The project consists of the following main components:

1. **Data Downloading**: Automated downloading of Bhav Copy files (equity data) for the month of July 2023 from the [BSE India Website](https://www.bseindia.com/markets/marketinfo/BhavCopy.aspx).

2. **Data Uploading**: The downloaded files are uploaded into an SQL database. All the equity files for July 2023 are stored in a single table along with their respective dates.

3. **Data Analysis**: The project runs queries on the SQL database to compute the stock-wise average opening, high, low, and closing prices for the month of July 2023.

4. **Performance Optimization**: The README also provides suggestions on how to reduce the response time of the database queries.

## How to Use

1. **Environment Setup**: Make sure you have Python installed. You can set up a virtual environment for this project to manage dependencies.

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

2. **Dependencies**: Install the required Python libraries by running `pip install -r requirements.txt`.

3. **Data Downloading**: The data downloading script automatically downloads the Bhav Copy files for the specified month and year.

4. **Data Uploading**: The `create_tables.py` script creates tables in the database to store the downloaded equity data files. It also uploads the data from the processed CSV files.

5. **Data Analysis**: Run the queries provided in the `data_analysis.sql` file to compute the stock-wise average opening, high, low, and closing prices for the month of July 2023.

## Note

Due to technical issues with unzipping the downloaded files, the project utilized manually downloaded files for the analysis. I apologize for any inconvenience caused.

Feel free to explore and modify the project to suit your specific needs!

## Contact

For any questions or feedback, please contact [vigneshkumar.d2797@gmail.com](mailto:vigneshkumar.d2797@gmail.com).
