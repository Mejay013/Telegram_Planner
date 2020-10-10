from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class Event():
    def __init__(self):
        self.SCOPES = ['https://www.googleapis.com/auth/calendar']

    def сreate_creds(self):
        creds = None

        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
                
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)

            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        return(creds)

    def normal_date(self,date :str):
        bad_date = date.split('.')
        good_date = f'{bad_date[-1]}-{bad_date[0]}'
        return(good_date)

    def create_event(self,date,task_name, time_start, time_end):
        creds = self.сreate_creds()
        
        service = build('calendar', 'v3', credentials=creds)

        event = {
            'summary': task_name,
            'start': {
                'dateTime': f'2020-{self.normal_date(date)}T{time_start}:00',
                'timeZone': 'Europe/Moscow',
            },
            'end': {
                'dateTime': f'2020-{self.normal_date(date)}T{time_end}:00',
                'timeZone': 'Europe/Moscow',
            },
            }

        event = service.events().insert(calendarId='arseniy.kocharov012@gmail.com', body=event).execute()


if __name__ == '__main__':
    a = Event()
    a.create_event('13.10', 'Some event', '2020-10-12T09:00:00-12:30', '2020-10-12T09:00:00-13:30')