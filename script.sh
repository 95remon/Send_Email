#!/bin/bash

# API endpoint to send POST request
api_endpoint="http://<API_SERVER_IP>:5000/alert/<type_example>"

# Log file location
log_file="/path/to/logs.txt"

# Function to get the current date and time
get_datetime() {
    echo $(date +"%d-%m-%Y %H:%M:%S")
}


# Get the server's IP address and hostname
server_ip=$(hostname -I | awk '{print $1}')
hostname=$(hostname)
server_info="$server_ip ($hostname)"

# Add your needed Tasks and Commands to get the Data from machine



comment= "Data"

# Create JSON Object and add your Logic
json_data=$(cat <<EOF
{
    "receiver": "Type",
    "status": "firing",
    "alerts": [{
        "status": "firing",
        "labels": { },
        "annotations": {
            "Alert": "Example",
            "Server": "$server_info",
            "comment": "$comment"
        }
    }]
}
EOF
)

# Send POST request
sudo curl -X POST -H "Content-Type: application/json" -d "$json_data" "$api_endpoint"

echo " <Logs> " >> "$log_file"

