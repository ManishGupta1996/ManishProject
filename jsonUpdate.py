import json



with open("data1.json", "r") as a_file:
    json_object = json.load(a_file)
    

json_object["sys"] = 100
json_object["dia"] = 80
json_object["puls"] = 95


with open("data1.json", "w") as a_file:
    json.dump(json_object, a_file)


print(json_object)
