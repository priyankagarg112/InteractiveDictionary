import json
from difflib import get_close_matches

json_data = json.load(open("data.json"))

def meaning(key):
    key = key.lower()
    if key in json_data:
        return(json_data[key])
    elif get_close_matches(key,json_data.keys())[0]:
        ans=input("Did u mean this %s instead? if YES enter Y, if NO enter N "%get_close_matches(key,json_data.keys())[0])
        if ans=="Y":
            return(json_data[get_close_matches(key,json_data.keys())[0]])
        elif ans=="N":
            return("Sorry! We could not recognize the word.")
        else:
            return("Sorry! We did not get you.")

    else:
        return("NO such word exists. Please double check it")

key=input("Enter word to find the meaning: ")
print(meaning(key))
