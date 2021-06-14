"""
This file provides examples on how to download/upload data from/to our S3
bucket using the telluslabs.s3 package that has already been included in the
requirements (pip install telluslabs). This package has more functions that
what is shown below and you can explore the main file here:
https://github.com/indigo-ag/shared/blob/master/telluslabs/s3.py
"""

from pathlib import Path

import pandas as pd
from telluslabs.s3 import S3Path, download_file, upload_df, upload_file

# Local paths
PROJECT_DIR = Path(__file__).resolve().parents[2]
FILENAME = "test_file.csv"
LOCAL_PATH = PROJECT_DIR / "data"
LOCAL_FILE_PATH = LOCAL_PATH / FILENAME

# S3 path
S3_BUCKET = "indigo.soil-carbon-science"
S3_FILE_PATH = f"template/data/{FILENAME}"  # This one has to be a string
S3_FILE_LOCATION = S3Path(S3_BUCKET, S3_FILE_PATH)

# UPLOADS EXAMPLES
# Uploading a dataframe to the S3 bucket:
df = pd.read_csv(LOCAL_FILE_PATH)
upload_df(df, S3_FILE_LOCATION)

# Uploading a file to the S3 bucket:
upload_file(
    bucket=S3_BUCKET, key=S3_FILE_PATH, local_path=LOCAL_FILE_PATH,
)

# DOWNLOADS EXAMPLES
# Downloading data as a temporary file from the S3 bucket:
if S3_FILE_LOCATION.exists():
    with S3_FILE_LOCATION.download() as local:
        df = pd.read_csv(local)
        print(df.head())

# Download the same data permanently on your local machine:
download_file(bucket=S3_BUCKET, key=S3_FILE_PATH, target_dir=LOCAL_PATH)
