import os
import glob
import zipfile
import numpy as np
import time
import datetime
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
import numpy as np
import imaplib
import email
import pathlib
import xlwings as xw
from collections.abc import Iterable
import xlrd
import requests
import zipfile
import xml.etree.ElementTree as ET
from openpyxl.utils.exceptions import InvalidFileException
import requests
import time
import os
import glob
import re
import pandas as pd
import datetime
import csv
from io import BytesIO
import zipfile
import xml.etree.ElementTree as ET
from io import BytesIO
import re
from email.header import decode_header
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from selenium.common.exceptions import TimeoutException
import shutil
import magic
import os
import glob
import openpyxl
import gspread
from google.oauth2.service_account import Credentials
from googleapiclient.http import MediaIoBaseDownload
import io
import pandas
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import threading
import json
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from google.cloud import bigquery
from google.oauth2 import service_account
from google.cloud import storage
from google.auth.exceptions import DefaultCredentialsError, RefreshError
import google.api_core.exceptions
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
from googleapiclient.http import MediaIoBaseDownload

# directory_path = r'C:\\Users\\shash\\Desktop\\py\\'

def merge_csv_files(directory_path, file_patterns):
    """
    Reads multiple CSV files based on patterns, merges them,
    and adds a 'source_type' column indicating the origin of the data.

    Args:
        directory_path (str): The local path where the CSV files are stored.
        file_patterns (dict): A dictionary mapping a source identifier 
                              (e.g., 'product', 'display') to a glob pattern 
                              for files (e.g., 'product_*.csv').

    Returns:
        pandas.DataFrame: A single merged DataFrame, or None if no files are found.
    """
    all_data = []

    for source_type, pattern in file_patterns.items():
        # Construct the full search path using os.path.join for cross-OS compatibility
        search_path = os.path.join(directory_path, pattern)
        
        # Use glob to find all files matching the pattern
        file_list = glob.glob(search_path)
        
        print(f"--- Found {len(file_list)} files for source '{source_type}'.")

        for file_path in file_list:
            try:
                # Read the CSV file into a temporary DataFrame
                df = pd.read_csv(file_path)
                
                # Add the new column indicating the source type
                df['source_type'] = source_type
                
                # Append the DataFrame to the list
                all_data.append(df)
                
                print(f"  > Successfully read and tagged: {os.path.basename(file_path)}")
                
            except Exception as e:
                print(f"  ! ERROR reading {os.path.basename(file_path)}: {e}")
                
    if not all_data:
        print("No data found to merge.")
        return None

    # Concatenate all DataFrames in the list into one master DataFrame
    merged_df = pd.concat(all_data, ignore_index=True)
    
    return merged_df

# --- Configuration ---

# 1. DEFINE THE DIRECTORY where your CSV files are located
# NOTE: Replace 'C:\path\to\your\local\data' with your actual directory path
DATA_DIR = r'C:\\Users\\shash\\Desktop\\py\\' 

# 2. DEFINE THE FILE PATTERNS and their corresponding labels (source_type)
# This assumes files related to 'product' look like 'product_jan.csv'
# and files related to 'display' look like 'display_feb.csv'.
FILE_MAPPING = {
    'product': 'product_*.csv',  # Matches any file starting with 'product_' and ending in '.csv'
    'display': 'display_*.csv',  # Matches any file starting with 'display_' and ending in '.csv'
    'other': 'other_*.csv'       # You can add more categories as needed
}

# --- Execution ---

if __name__ == "__main__":
    
    # 1. Run the merge function
    final_df = merge_csv_files(DATA_DIR, FILE_MAPPING)

    if final_df is not None:
        # 2. Display the result summary
        print("\n--- MERGE COMPLETE ---")
        print(f"Total Rows Merged: {len(final_df)}")
        print("First 5 rows of the merged data:")
        print(final_df.head())
        
        # 3. Optional: Save the merged data to a new CSV file
        merged_file_path = os.path.join(DATA_DIR, 'merged_data.csv')
        final_df.to_csv(merged_file_path, index=False)
        print(f"\nSaved merged data to: {merged_file_path}")