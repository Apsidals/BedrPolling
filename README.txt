BEDR POLLING - SETUP INSTRUCTIONS
===================================

1. DROP YOUR FIREBASE KEY FILE
   - Take your downloaded Firebase key JSON file
   - Rename it to: firebase-key.json
   - Put a copy in: poll-service/firebase-key.json
   - Put a copy in: vote-service/firebase-key.json

2. MAKE SURE DOCKER DESKTOP IS RUNNING

3. OPEN A TERMINAL - run poll-service:
   cd poll-service
   docker build -t poll-service .
   docker run -p 5000:5000 -v ./firebase-key.json:/app/firebase-key.json poll-service

4. OPEN A SECOND TERMINAL - run vote-service:
   cd vote-service
   docker build -t vote-service .
   docker run -p 5001:5001 -v ./firebase-key.json:/app/firebase-key.json vote-service

5. OPEN THE APP
   Just open frontend/index.html in your browser. That's it!

NOTE: The firebase key file must be named exactly "firebase-key.json"
