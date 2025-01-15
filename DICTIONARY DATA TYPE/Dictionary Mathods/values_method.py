myinfo={
    "name:":"kamalesh  kumar",
    "village:":"dhangaraha",
    "study":"MMDU ",
    "Roll no:":1323407,
    "deparment":"bca",
    "jayinfo":{            #nested dictionary
    "name:":"jayram kumar",
    "study:":"MMDU ",
    "Roll no:":1323409,
    "deparment:":"bca",

    }

    }

print(list(myinfo["jayinfo"]))# key values : nested dictionary ka output aayega 
print(list(myinfo.values()))#all keys output aayega
