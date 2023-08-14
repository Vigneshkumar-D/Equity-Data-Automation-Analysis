import os
import pandas as pd
import zipfile

# Directory containing downloaded Bhav Copy zip files
download_dir = "downloaded_files"

# Directory to save processed CSV files
processed_dir = "processed_data"

# Ensure the processed data directory exists
os.makedirs(processed_dir, exist_ok=True)

# Process Bhav Copy CSV files
def process_bhav_copy(csv_file_path):
    df = pd.read_csv(csv_file_path)
    return df

# Process each downloaded Bhav Copy ZIP file
for root, _, files in os.walk(download_dir):
    for file_name in files:
        if file_name.endswith(".zip"):
            zip_file_path = os.path.join(root, file_name)
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(root)  # Extract all contents of the ZIP file
                print(f"Extracted {file_name}")
            
            # Process each extracted CSV file
            for extracted_file_name in os.listdir(root):
                if extracted_file_name.endswith(".csv"):
                    extracted_csv_file_path = os.path.join(root, extracted_file_name)
                    processed_data = process_bhav_copy(extracted_csv_file_path)
                    processed_file_path = os.path.join(processed_dir, extracted_file_name.replace(".csv", "_processed.csv"))
                    processed_data.to_csv(processed_file_path, index=False)
                    print(f"Processed and saved {extracted_file_name}")
                
            
   
# Inform when data processing is complete
print("Data processing complete.")
