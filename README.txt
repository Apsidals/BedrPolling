## Tools
Software Used:
Google Cloud
Firebase
# adsfasdfadsf
## Languages:
HTML
JS
CSS
Python
Dockerfile

Link to our website: [https://bedrpolling.web.app/](https://bedrpolling.web.app/)

## Creating the app
To access google cloud and firebase, just search them up in google and you should have access to our projects. Their called “first project” and “BedrPolling” respectively. Firebase might have sent an invitation on gmail that you have to check. 

## Database
For Firebase, to create a new application from scratch, you need to go to this link: [https://console.firebase.google.com/u/0/](https://console.firebase.google.com/u/0/)

1. Click on Create a new Firebase project and follow the instructions
- Once you get to your project, expand the sidebar and click on “databases & storage”
- Create a Firestore NoSQL database, and follow the steps once again. We used all default settings.
- Once the database is created, go back to the `Sidebar -> Settings -> Service accounts -> Generate a new private key`. It should download a JSON file, the contents of which you will use in your environment variables. 

## Cloud Service
For each of the microservice backends, you need to create a Google Cloud account [https://console.cloud.google.com/welcome/](https://console.cloud.google.com/welcome/) and click on “deploy an application.” Go through these steps:
1. Connect the GitHub repository to the application
- Under the "Build configuration", use the Dockerfile for whichever microservice you are making this for. Ex: If I'm setting this up for the voting service, then I would use Dockerfile.vote
- Select "allow public access" for authentication
- Set the region to US East Virginia
- Set the maximum number of instances on whatever you want (ours is set to 3)
- Expand the "Containers, Networking, Security" section
- Scroll down and select the tab "Variables & Secrets"
- Make an environment variable with these settings:
- Name: `GOOGLE_CREDENTIALS`
- Value will be whatever your Firestore credentials are in the JSON file
- Deploy this 3 times, one for polling, one for voting, one for stats. Remember to change the Dockerfile each time and also add the environment variable. 

Once your microservices are working, we need to host the static webpages on Firebase.

Open a terminal and run these commands
```
npm install -g firebase-tools
firebase login
```
Log in with your credentials
'cd' into the project folder where you pulled the git repo
`firebase init hosting`
Which project: the name of the project of the Firebase project you created for the database
Public directory: frontend
Single page app: `N`
Set up automatic builder with GitHub: `N`
Overwrite index.html: `N`
`firebase deploy --only hosting`
You have to run the deploy command every time you make a change to the frontend, or you can enable the automatic builder with the GitHub setting above
