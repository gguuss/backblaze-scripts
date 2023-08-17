# backblaze-scripts
A set of scripts for remotely managing backblaze from local network.

# Disclaimer
The web is riddled with articles about how this could get you hacked, 
restrict to your local network and use at your own risk. Don't use this.

# Setup
```
virtualenv env && source env/requirements
pip install -r requirements.txt
flask run 
```

# Testing
```
curl localhost:5000
curl localhost:5000/start
curl localhost:5000/stop
```

