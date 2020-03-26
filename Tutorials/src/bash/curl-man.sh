# e.g. test REST API
curl https://www.google.com/

curl http://localhost:5000

curl http://localhost:5000/json-test

# extra info
curl -i http://localhost:5000/json-test

# post up or del info
curl http://localhost:5000/methods
#You sent a GET request

# simulate submitting form data to the same URL
curl -d "first=Adama&last=Jimenez" http://localhost:5000/methods
#You sent a POST request




