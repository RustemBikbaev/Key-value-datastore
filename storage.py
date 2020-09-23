import argparse
import json
import os
import tempfile

parser = argparse.ArgumentParser()
parser.add_argument("--key", type=str, help="the key by which the values are stored / received")
parser.add_argument("--value", type=str, help="the value to store")
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

def read_json_file(storage_path):
    if not os.path.exists(storage_path):
        return {}

    with open(storage_path, 'r') as file:
        data = file.read()
        if data:
            return json.loads(data)
        return {}
    
def write_to_json_file(storage_path, data):
    with open(storage_path, 'w') as f:
        f.write(json.dumps(data))
    
    
if (args.key!=None )&(args.value!=None):
    #Записываем value по key
    data_in_file = read_json_file(storage_path)
    
    #Если ключ найден в файле
    if args.key in data_in_file.keys():
        data_in_file.get(args.key)
        data_in_file[args.key].append(args.value)
        
    #Если ключа нет в файле
    else:
        data_in_file[args.key]=[args.value]
    
    write_to_json_file(storage_path, data_in_file)
    
elif (args.key != None )&(args.value == None):
    #Выводим value по key
    data_in_file = read_json_file(storage_path)
    
    #Вывод если ключ найден в файле
    if args.key in data_in_file.keys():
        print(', '.join(data_in_file.get(args.key)))
        
    #Вывод если ключа нет в файле
    else:
        print(None)