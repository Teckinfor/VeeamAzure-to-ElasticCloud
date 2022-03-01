#!/bin/python3

import requests, json, urllib3, time, sys, os


NO_TOKEN = {"Error":"Impossible to get an authorization"}

def get_authorization(config:dict) :
    url = 'https://' + config["IP"] + '/api/oauth2/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'grant_type':'Password','Username':config["username"],'password':config["password"]}

    try :
        authorization = requests.post(url, data=data, headers=headers, verify=False)
        if authorization.status_code == 200 :
            authorization_json = authorization.json()
        else :
            print(authorization)
            return NO_TOKEN
    except :
        return NO_TOKEN

    return authorization_json["access_token"]

def get_job_collection_logs(config:dict, token:str):
    headers = {"Authorization": "Bearer " + token}
    url = 'https://' + config["IP"] + '/api/v3/jobSessions?Limit=100'
    response = requests.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        response_json = response.json()
        return response_json

def get_config() :
    file = open("config.json")
    config = json.load(file)
    file.close()
    return config 

def generate_config () :
    config =   {
                    "username":os.getenv("VEEAM_USERNAME"),
                    "password":os.getenv("VEEAM_PASSWORD"),
                    "IP":os.getenv("VEEAM_HOST")
                }
    
    return config

def add_log(outfile, event) :
    final_log = {}

    try :
        final_log["@timestamp"] = event["executionStopTime"]
        final_log["executionStartTime"] = event["executionStartTime"]
        final_log["executionStopTime"] = event["executionStopTime"]
    except :
        final_log["@timestamp"] = event["executionStartTime"]
        final_log["executionStartTime"] = event["executionStartTime"]
        final_log["executionStopTime"] = ""

    final_log["message"] = event["type"] + ": " + event["status"]
    final_log["type"] = event["type"]
    final_log["localizedType"] = event["localizedType"]

    final_log["status"] = event["status"]
    final_log["id"] = event["id"]

    json_object = json.dumps(final_log)

    outfile.write(json_object)
    outfile.write("\n")







if __name__ == "__main__" :

    urllib3.disable_warnings()

    if len(sys.argv) > 1 :
        config = generate_config()

    else :
        config = get_config()

    while(True) :

        token = get_authorization(config)

        if token != NO_TOKEN :
            logs = get_job_collection_logs(config, token)
            log_file = logs["results"]

            try :
                outfile = open('/var/log/veeam.log', 'r')
                lst = {}
                lines = outfile.readlines()
                for line in lines :
                    line = json.loads(line)
                    for event in log_file :
                        if line["id"] == event["id"] :
                            lst[event["id"]] = line["status"]
                outfile.close()

            except :
                no_error = "OK"

            with open("/var/log/veeam.log", "a") as outfile:

                for event in log_file :

                    if event["id"] not in lst.keys():
                        add_log(outfile, event)

                    elif lst[event["id"]] != event["status"]:
                        add_log(outfile, event)
                        
        time.sleep(30)