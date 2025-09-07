#!/usr/bin/env python3
import os
import sys
import pandas as pd
from datetime import datetime, time
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle

# Define the scopes required for Google Calendar API
SCOPES = ['https://www.googleapis.com/auth/calendar']

def convert_to_csv(file_path):
    """
    Convert Excel file to CSV if needed, otherwise return original path.
    """
    file_name, file_ext = os.path.splitext(file_path)
    
    if file_ext.lower() in ['.xls', '.xlsx']:
        print(f"Converting {file_path} to CSV format...")
        df = pd.read_excel(file_path)
        csv_path = f"{file_name}.csv"
        df.to_csv(csv_path, index=False)
        print(f"Converted to {csv_path}")
        return csv_path
    elif file_ext.lower() == '.csv':
        print(f"File {file_path} is already in CSV format.")
        return file_path
    else:
        raise ValueError(f"Unsupported file format: {file_ext}")

def get_google_calendar_service():
    """
    Get an authenticated Google Calendar API service
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
            
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credential.json', SCOPES)
            creds = flow.run_local_server(port=0, redirect_uri_trailing_slash=False)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service

def create_calendar_events(csv_file, date_col='Date', title_col='Topics', desc_col='Description'):
    """
    Create Google Calendar events from CSV file data.
    
    Parameters:
    - csv_file: Path to the CSV file
    - date_col: Column name for date information
    - title_col: Column name for event title
    - desc_col: Column name for event description
    """
    try:
        df = pd.read_csv(csv_file)
        
        required_cols = [date_col, title_col, desc_col]
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Missing required columns: {', '.join(missing_cols)}")
        
        if not pd.api.types.is_datetime64_any_dtype(df[date_col]):
            df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
        
        invalid_dates = df[df[date_col].isna()]
        if not invalid_dates.empty:
            print(f"Warning: {len(invalid_dates)} rows with invalid dates will be skipped")
            df = df.dropna(subset=[date_col])
        
        service = get_google_calendar_service()
        
        event_count = 0
        for _, row in df.iterrows():
            event_date = row[date_col].date()
            event_title = str(row[title_col])
            event_desc = str(row[desc_col]) if not pd.isna(row[desc_col]) else ""
            
            start_time = datetime.combine(event_date, time(8, 0))
            end_time = datetime.combine(event_date, time(9, 0))
            
            event = {
                'summary': event_title,
                'description': event_desc,
                'start': {
                    'dateTime': start_time.isoformat(),
                    'timeZone': 'IST',  
                },
                'end': {
                    'dateTime': end_time.isoformat(),
                    'timeZone': 'IST', 
                },
            }
            
            event = service.events().insert(calendarId='primary', body=event).execute()
            print(f"Created event: {event_title} on {event_date} - Event ID: {event['id']}")
            event_count += 1
            
        print(f"Successfully created {event_count} calendar events.")
        
    except Exception as e:
        print(f"Error creating calendar events: {str(e)}")
        raise

def main():
    if len(sys.argv) < 2:
        print("Usage: python csv_sheet_to_calender.py <file_path> [date_col] [title_col] [desc_col]")
        print("Default column names: 'date', 'topics', 'description'")
        sys.exit(1)
        
    file_path = sys.argv[1]
    
    date_col = sys.argv[2] if len(sys.argv) > 2 else 'Date'
    title_col = sys.argv[3] if len(sys.argv) > 3 else 'Topics'
    desc_col = sys.argv[4] if len(sys.argv) > 4 else 'Description'

    csv_file = convert_to_csv(file_path)
    
    create_calendar_events(csv_file, date_col, title_col, desc_col)
    
    if csv_file != file_path:
        print(f"Removing temporary CSV file: {csv_file}")
        os.remove(csv_file)

if __name__ == "__main__":
    main()
