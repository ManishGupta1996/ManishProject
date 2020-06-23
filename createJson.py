import json

hr=[98,98,94,96]
temp=[100,99,96]
dictionary ={ 
    "heartrate" : hr, 
    "oxygen" : temp, 

}
  
# Serializing json  
json_object = json.dumps(dictionary, indent = 2) 
  
# Writing to sample.json 
with open("data1.json", "w") as outfile: 
    outfile.write(json_object)


