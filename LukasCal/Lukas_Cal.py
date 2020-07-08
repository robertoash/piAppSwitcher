# -*- coding: utf-8 -*-

from google.oauth2 import service_account
from googleapiclient.discovery import build
import datetime


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
SERVICE_ACCOUNT_FILE = '/var/www/piAppSwitcher/LukasCal/service.json'

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """

    service = build('calendar', 'v3', credentials=credentials)

    # Call the Calendar API
    nowminus24 = (datetime.datetime.utcnow() - datetime.timedelta(hours=24)).isoformat() + 'Z'  # 'Z' indicates UTC time
    # print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='im87vdp823ct581abv0dce9s54@group.calendar.google.com',
                                          timeMin=nowminus24,
                                          maxResults=1, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    next_events_start = []
    next_events_end = []

    if not events:
        return 'No upcoming events found.'
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        end = event['end'].get('dateTime', event['end'].get('date'))
        # Include only all-day events
        if len(start) <= 10:
            next_events_start.append([start, event['summary']])
            next_events_end.append([end, event['summary']])

    if str(next_events_start[0][0]).replace("-", "") <= datetime.datetime.utcnow().strftime("%Y%m%d") <= str(next_events_end[0][0]).replace("-", ""):
        return 'Vacation'
    else:
        return 'Not'


# if __name__ == '__main__':
#     main()


def L_Cal():
    return main()
