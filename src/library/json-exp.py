import json

def json_to_string():
    data = {'name': 'nanbei', 'age': 18}
    print(json.dumps(data))

def string_to_json():
    str = '{"name": "John", "age": 30, "city": "New York"}'
    print(json.loads(str))

def read_json_file():
    with open("example.json", "r", encoding='utf-8') as f:
        res = json.loads(f.read())
        print(type(res), res)

def write_json():
    dict = {"name": "Jane", "age": 25, "city": "Paris"}
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(dict, file)

if __name__ == '__main__':
    # json_to_string()
    # string_to_json()
    # write_json()
    read_json_file()