import json
from pprint import pprint

with open('D:/Desktop/data.json', encoding='iso-8859-1') as f:
    data = json.load(f)

with open('D:/Desktop/layout.json', encoding='iso-8859-1') as f:
    model = json.load(f)

print("Loaded")
    
pprint(model)

def drill_json(a_json, a_model):
    for key in a_model:
        drill_object(a_json[key], a_model[key], key)

def drill_object(a_json, a_model, a_parentKey):
    type = a_model["type"]
    sqltype = a_model["sqltype"]
    count = len(a_model)
    if count > 2:
        for key in a_json:
            drill_object(a_json[key], a_model[key], key)
    elif sqltype == "tabel":
        if type == "jobject":
            drill_table_object(a_json, a_parentKey)
        else:
            drill_table_array(a_json, a_parentKey)

def drill_table_object(a_json, a_key):
    print("Table", a_key)
    for key in a_json:
        drill_row_object(a_json[key], key)

def drill_table_array(a_json, a_key):
    print("Tabel", a_key)
    for i in range(len(a_json)):
        if type(a_json[i]) == dict:
            drill_row_object(a_json[i], i)
        else:
            drill_row_array(a_json[i], i)

def drill_row_array(a_json, a_index):
    print("Id1 :", a_index)
    drill_row_object(a_json, "Col2")

def drill_row_object(a_json_obj, a_key):
    if type(a_json_obj) == dict:
        print("Col1 :", a_key)
        for key in a_json_obj:
            drill_row_object(a_json_obj[key], key)
    else:
        print(a_key, ":", a_json_obj)


















def drill_json2(a_data, a_model):
    for key in a_model:
        drill_object(a_data[key], a_model[key], key)
        
def drill_tabel_object2(a_data, a_key):
    print("Table:", a_key)
    for key in a_data:
        print("Row")
        drill_col_object(a_data[key], key, 1)

def drill_tabel_array2(a_data, a_key):
    print("Tabel:", a_key)
    for i in range(len(a_data)):
        print("Row")
        if type(a_data[i]) == dict:
            drill_col_object(a_data[i], i, 1)
        else:
            print("Col1:", i)
            drill_col_object(a_data[i], "Col 2", 2)

def drill_col_object2(a_data, a_key, a_level):
    if type(a_data) == dict:
        print("Col", a_level, ":", a_key)
        for key in a_data:
            drill_col_object(a_data[key], key, a_level + 1)
    else:
        print(a_key, ":", a_data)

def drill_object2(a_data, a_model, a_key):
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