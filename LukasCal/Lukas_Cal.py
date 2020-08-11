# -*- coding: utf-8 -*-

from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import date
from datetime import datetime as dt
import datetime


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
SERVICE_ACCOUNT_FILE = '/var/www/piAppSwitcher/LukasCal/service.json'
# SERVICE_ACCOUNT_FILE = 'service.json'

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


def main():

    service = build('calendar', 'v3', credentials=credentials)

    # Call the Calendar API
    today = date.today()
    # tomorrow = datetime.datetime.utcnow() + datetime.timedelta(1)
    lastmidnight = (dt.combine(today, dt.min.time())).isoformat() + 'Z'
    # nextmidnight = (dt.combine(tomorrow, dt.min.time())).isoformat() + 'Z'
    # nowminus24 = (datetime.datetime.utcnow() - datetime.timedelta(hours=24)).isoformat() + 'Z'  # 'Z' indicates UTC time
    # print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='im87vdp823ct581abv0dce9s54@group.calendar.google.com',
                                          timeMin=lastmidnight,  # nowminus24,
                                          # timeMax=nextmidnight,
                                          maxResults=20, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    todays_events = []
    result = []

    if not events:
        return 'No upcoming events found.'
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        end = event['end'].get('dateTime', event['end'].get('date'))
        # Include only all-day events that are relevant to today
        if len(start) <= 10 and str(start).replace("-", "") <= \
           datetime.datetime.utcnow().strftime("%Y%m%d") <= str(end).replace("-", ""):
            todays_events.append(event['summary'])
        else:
            todays_events.append('***')

    for event in todays_events:
        if "Vacation" in event:
            result.append("Vacation")
        elif "Sleep Out" in event:
            result.append("SleepOut")
        else:
            result.append("")

    if "Vacation" in result and "SleepOut" in result:
        return 'AllDayOut'
    elif "Vacation" in result:
        return 'Vacation'
    elif "SleepOut" in result:
        return 'SleepOut'
    else:
        return 'School'


# if __name__ == '__main__':
#     main()


def L_Cal():
    return main()
