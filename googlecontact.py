from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/contacts']


def main():
    """Shows basic usage of the People API.
    Prints the name of the first 10 connections.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            
        '''
            # this worked ref github: https://github.com/wittyhandle/go-google-contacts-api
            
            following params required for Auth Code:
            
            CLIENT_ID = <client_id > // used from credentials.json
            REDIRECT_URI = <redirect uri> "http://localhost:42047" // used from credentials.json
            SCOPE = <list of scopes>
            access_type = offline
            response_type = code
            
            # used for auth code
            # https://accounts.google.com/o/oauth2/v2/auth?client_id=<client_id>&redirect_uri=<redirect_url>&scope=https://www.googleapis.com/auth/contacts&access_type=offline&response_type=code
            
            # redirects to Account choose; redirect uri, client id is taken from credentials.json
             
            https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?client_id=<client id>&redirect_uri=<redirect_uri>&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcontacts&access_type=offline&response_type=code&flowName=GeneralOAuthFlow
            
            Generates the URI with Auth Code Eg:
            
            https://www.googleapis.com/oauth2/v4/token?code=<generated_auth_code>&redirect_uri=<redirect_uri>&client_id=<client_id>&client_secret=<client_secret>&grant_type=authorization_code
            
            this generates access token, refresh token; for the first time it stores token.json and later uses the same for refresh token
            
        '''
            
        creds = flow.run_local_server(port=42047) # match port according to redirect uri for localhost
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('people', 'v1', credentials=creds)

        # Call the People API
        print('List 10 connection names')
        results = service.people().connections().list(
            resourceName='people/me',
            pageSize=10,
            personFields='names,emailAddresses').execute()
        connections = results.get('connections', [])

        for person in connections:
            names = person.get('names', [])
            if names:
                name = names[0].get('displayName')
                print(name)
    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()

# http: // localhost: 42047 /?code = 4/0AX4XfWgZTo1A7eGOReI6jERpg787drXOvzuLR3x0dfNzHV6pRmN2ILi4RwVtePrnTowJGA & scope = https: // www.googleapis.com/auth/contacts

# curl - v - XPOST https: // www.googleapis.com/oauth2/v4/token? - d code = <authorization code > -d redirect_uri = <redirect url > -d client_id = <client_id > -d client_secret = <client_secret > -d grant_type = authorization_code
