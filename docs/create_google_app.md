
Login to Google Cloud console and create/select project.
Navigate to `OAuth consent screen` select User Type External if you are not under organization.
click on create and on next page provide all the required app details
save and continue 
click on `add or remove scopes` select email, profile, openid and click on UPdate.
click on save and continue.
in Next step add test users for testing.
click on save and continue.
Review the details and click on back to dashboard

Now Open Credentials click on Create Credentials -> OAuth client ID.
set application type to web application
set name


Add following in both Authorized JavaScript origins
and Authorized redirect URIs


http://localhost
http://localhost:8000
http://localhost:8000/
http://localhost:3000
http://localhost:3000/

click on save and save copy client id and client secret.
