import os
import sys
import pandas as pd
import boto3
import dotenv
from botocore.exceptions import NoCredentialsError

def upload_files_to_s3(folder_path,bucket_name):
    """
    Upload CSV files directly to S3.
    Convert all XLS/XLSX worksheets in folder to CSV and upload to S3.
    """
    s3_client = boto3.client("s3")

    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder_path, filename)
            try:
                s3_client.upload_file(file_path, bucket_name, filename)
                print(f"Uploaded {filename} directly to S3 bucket {bucket_name}")
            except NoCredentialsError:
                print("AWS Credentials not available.")
            except Exception as e:
                print(f"Error uploading {filename}: {str(e)}")
        elif filename.endswith(".xls") or filename.endswith(".xlsx"):
            file_path = os.path.join(folder_path, filename)
            try:
                xls = pd.ExcelFile(file_path)

                for sheet_name in xls.sheet_names:
                    df = pd.read_excel(file_path,sheet_name=sheet_name)

                    csv_filename = f"{os.path.splitext(filename)[0]}_{sheet_name}.csv"
                    temp_csv_path = os.path.join(folder_path, csv_filename)

                    df.to_csv(temp_csv_path, index=False)

                    # Upload the CSV file to S3
                    try:
                        s3_client.upload_file(temp_csv_path, bucket_name, csv_filename)
                        print(f"Uploaded {csv_filename} to S3 bucket {bucket_name}")

                    except NoCredentialsError:
                        print("AWS Credentials not available.")
                    except Exception as e:
                        print(f"Error uploading {csv_filename}: {str(e)}")            

                    if os.path.exists(temp_csv_path):
                        os.remove(temp_csv_path)
                        print(f"Removed temporary file {temp_csv_path}")

            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <folder_path>")
        sys.exit(1)

    folder = sys.argv[1]

    dotenv.load_dotenv()
    bucket = os.getenv("AWS_BUCKET_NAME")
    access_key = os.getenv("AWS_ACCESS_KEY_ID")
    secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    region = os.getenv("AWS_REGION", "us-east-1") 

    if not all([bucket, access_key, secret_key]):
        print("AWS credentials or bucket name not set in environment variables.")
        sys.exit(1)

    boto3.setup_default_session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region
    )
    upload_files_to_s3(folder, bucket)