#!/usr/bin/env python3
#chmod +x temp_sensor.py

# [START sheets_quickstart]
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import time, sys

import time
import smbus
import Adafruit_BBIO.GPIO as GPIO


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1nytQJZmAPP3sAD1jyL4Ix__gswq_vsJ2V9dkHYUuOXI'
SAMPLE_RANGE_NAME = 'A2'



bus = smbus.SMBus(2)  # Use i2c bus 2

sensor1 = 0x4a #temp1
sensor2 = 0x48 #temp2

def main():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            # creds = flow.run_local_server(port=0)
            creds = flow.run_console()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)
    
    
    while(1):
    
        temp = bus.read_byte_data(0x4a,0) #reading the temp from the sensor thata activated the alert
        temp = temp*9/5 +32 #converting to celicus
        temp2 = bus.read_byte_data(0x48,0) 
        temp2 = temp2*9/5 +32 
        
        sheet = service.spreadsheets()
        values = [ [time.time()/60/60/24+ 25569 - 5/24, temp, temp2]]
        body = {'values': values}
        result = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range=SAMPLE_RANGE_NAME,
                            valueInputOption='USER_ENTERED',
                            body=body
                            ).execute()

        
        time.sleep(4)
if __name__ == '__main__':
    main()
# [END sheets_quickstart]
