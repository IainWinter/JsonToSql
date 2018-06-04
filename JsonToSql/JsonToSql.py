import json
from pprint import pprint

with open('D:/Desktop/data.json', encoding='iso-8859-1') as f:
    data = json.load(f)

with open('D:/Desktop/layout.json', encoding='iso-8859-1') as f:
    model = json.load(f)

print("Loaded")
    
pprint(model)

def drill_json(a_data, a_model):
    for key in a_model:
        drill_object(a_data[key], a_model[key], key)

def drill_tabel_object(a_data, a_key):
    print("Table:", a_key)
    for key in a_data:
        drill_col_object(a_data[key], key)

def drill_tabel_array(a_data, a_key):
    print("Tabel:", a_key)
    for i in range(len(a_data)):
        drill_col_object(a_data[i], i)

def drill_col_object(a_data, a_key):
    if type(a_data) == dict:
        print("Col1:", a_key)
        for key in a_data:
            drill_col_object(a_data[key], key)
    else:
        print(a_key, ":", a_data)

def drill_object(a_data, a_model, a_key):
    type = a_model["type"]
    sqltype = a_model["sqltype"]
    count = len(a_model)
    if count > 2:
        for key in a_data:
            drill_object(a_data[key], a_model[key], key)
    if sqltype == "tabel":
        if type == "jobject":
            drill_tabel_object(a_data, a_key)
        else:
            drill_tabel_array(a_data, a_key)

drill_json(data, model)