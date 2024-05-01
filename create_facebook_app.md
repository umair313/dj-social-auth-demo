## Creating App

Here are the instructions re-written with emojis and easy wording for a GitHub README:

- 📝 Log in to [Meta Developers](https://developers.facebook.com/apps/)
- 🆕 Click on Create App
- ✅ Select `Authenticate and request data from users with Facebook Login` and click `Next`.
- 🎮 Answer the question Are you building a game? with Yes or No, then click Next
-📋 Provide the following details:
  - App Name 📚
  - App Contact Email ✉️
  - 🔑 Click Next and enter your password
- ⚙️ From the app dashboard, click Customize this app and add the email permission
- 🌐 Open Basic App Settings, fill in the required information, set the site URL as http://localhost:8000/, review the details, and click Save
- 🔍 Open API Explorer by navigating to Review -> Testing -> Open Graph API Explorer
- 📩 In Explorer, under permissions, select email and click Generate Access Token. After the token is generated, click Submit - you should see your ID, email, and username
- 📝 Note: If you don't see the email in test mode, try using an account with Professional Mode disabled (used for Content Creators on Facebook). If Professional Mode is enabled, you won't see the email in testing until you publish your app.

- ### ⚙️ Set the APP ID and secret in the backend and frontend accordingly