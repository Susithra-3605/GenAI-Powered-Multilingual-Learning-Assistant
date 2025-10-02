# Deployment Notes

## Backend
1. Install dependencies: `pip install fastapi uvicorn transformers pymongo`
2. Start server: `uvicorn backend.app.main:app --reload`

## Mobile App
1. Install dependencies: `npm install`
2. Run app: `npx react-native run-android` or `npx react-native run-ios`

## MongoDB
- Make sure MongoDB is running locally.
