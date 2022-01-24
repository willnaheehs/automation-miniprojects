import sys
import clipboard
import json

SAVED_DATA = 'clipboard.json'

def save_items(filepath, data): #writes json file
    with open(filepath, 'w') as f: #make new json file. if file already exist, overide it (w)
        json.dump(data, f) #take 'data' as python dictionary and makes it json format

def load_json(filepath): #reads the json data
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            return data
    except:
        return{}

if len(sys.argv) == 2: #number of commands passed after python3 multiclipboard.py
    command = sys.argv[1]
    data = load_json(SAVED_DATA)

    if command == 'save':
        key = input("Enter a key: ")
        data[key] = clipboard.paste() #grabs what is copied and saves it to dictionary
        save_items(SAVED_DATA, data) #saves item to json file
        print('Data Saved')
    elif command == 'load':
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print('Data copied to clipboard')
        else:
            print("key does not exist")
    elif command == 'list':
        print (data)
    else:
        print('unknown command')
else:
    print("please pass exactly one command")