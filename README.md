# Google-Contact-API
Google contact API integration

Ref Links: 

https://developers.google.com/people/v1/how-tos/authorizing

https://developers.google.com/people/quickstart/python

https://github.com/wittyhandle/go-google-contacts-api


Steps to Follow: 

Make Virtualenv

Run 

pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

Setup Google Credentials in Google Cloud Platform

https://console.cloud.google.com/

1. Create Project in Google Console
2. Enable required Google API and Services. For Eg: For contact API -> contact API and People API needs to be enabled

    - Go through API and Services -> Library -> Search and Enable  

3. Create OAuth2 Screen Consent

    - add test user emails
    - add scopes : Eg: Contact API

4. Create Oauth2 Credentials

    - Can create in Credntials menu -> Create OAuth2 creds
    - Choose Application type: web app/ android, etc. acc to requirement
    - complete setup and it generates : client_secret, client_id
    - download in working directory: OAuth2 json -> change filename to credentials.json  // Used in code;  Added in gitignore
    - Match redirect uri with port that of used in code

4. Need to Add Redirect URIs in Google Console
    - Credentials -> Choose Oauth2 credentials -> edit: Add in Redirect URIs 
    - Match redirect uri with port that of used in code

5. Run script

6. While running script, token.json is created for first time login/expiry or invalid, and for later uses the same token.json for refresh token  // saved through code; Added token.json in gitignore

7. After redirecting the final redirected URI with code and scope, it is completed and can find the resulting Contact API response
