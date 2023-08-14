import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def download_bhav_copy():
    # URL for the Bhav Copy files
    base_url = "https://www.bseindia.com/markets/marketinfo/BhavCopy.aspx"

    # Directory to save downloaded files
    download_dir = "downloaded_files"

    # Ensure the download directory exists
    os.makedirs(download_dir, exist_ok=True)

    # Function to download and save a file
    def download_file(url, file_path):
        response = requests.get(url)
        with open(file_path, 'wb') as file:
            file.write(response.content)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    start_date = datetime(2023, 7, 1)
    end_date = datetime(2023, 7, 31)

    # Iterate over each day in the month
    current_date = start_date
    while current_date <= end_date:
        formatted_date = current_date.strftime('%d%m%y')
        query_params = {
            "file": f"EQ_ISINCODE_{formatted_date}.zip",
            "ndm": current_date.strftime('%Y%m%d'),
            "ntm": current_date.strftime('%Y%m%d'),
        }

        response = requests.get(base_url, headers=headers, params=query_params)
        if response.status_code == 200:
            print(f"Web request successful for {current_date.strftime('%Y-%m-%d')}")
        else:
            print(f"Web request failed with status code {response.status_code} for {current_date.strftime('%Y-%m-%d')}")

        soup = BeautifulSoup(response.text, 'html.parser')
        download_link = f"https://www.bseindia.com/download/BhavCopy/Equity/EQ{formatted_date}_CSV.ZIP"
        
        print(f"Download link: {download_link}")
        file_name = f"EQ_ISINCODE_{formatted_date}.zip"
        file_path = os.path.join(download_dir, file_name)
        download_file(download_link, file_path)
        print(f"Downloaded {file_name}")

        current_date += timedelta(days=1)

    print("Download complete.")



