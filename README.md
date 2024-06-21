# Our New Server Is Broken!

My niece came in for an internship and changed some code in our most important production server.

The errors could be anywhere in both the server code and the dockerfile.

They force pushed to main and now it's broken?!

We need someone to come in and fix it!

## Instructions

### Build
`docker build . -t app`

### Run
`docker run -p 5678:5678 app`

### Evaluate
Send a curl request to the /get endpoint on localhost

## Success
A succesful fix should get the json data when calling the curl command

`[{"message":"Hello, World!"},{"status":"success"}]`

Create a branch, commit your solution and push it
