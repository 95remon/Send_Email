# Python Flask API to send Emails
This Repo is just for documentation it needs your modification to be executed. 

## API Host Server

- prerequisite:

    1. Python3 - pip3 - (Flask-exchangelib)
    2. 24/7 working server

- Check the "app.py" file for the code and you can implement your logic and parse the JSON object recived and display the needed information in the HTML body which will be send in the Email

- you can add Config file for the api where you can make mutiple types of alert and build your own logic for each type of them and make different content also for each one (it is up to you and the business need)

- after implement your logic you can run this python file

```bash
./app.py
```

## The source server/servers (It depends on your needs)

- this is the server you need to get info from (it might be the same API server)

- prerequisite:

    1. (curl) package installed 
    2. Opened connection between 2 servers the sourse (current server) and the Distination (Api Server) on port 5000 as implemented in code (you can also change if you want to)

- Check the script.sh file and implement your own logic and collect the data from the server and save it in variables and build a JSON object as in code, and perform a post curl command and send the json object to the api end-point.

- make a cronetab for this script (for example each 5 min) to execute your logic and send email if something upnormal happens or configer it as you want and the business logic.