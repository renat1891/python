import json

def save_to_json(data):
    with open("1.json", 'w') as file:
        json.dump(data, file, indent=4)

def load_from_json():
    try:
        with open("1.json", 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return [""]
    
data = load_from_json()
print("Current data:", data)

data[0] = input("Enter new value: ")

save_to_json(data)
print("Data saved.")
