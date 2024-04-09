# Using json.dumps() without Spaces in Python

import json

employee = {
    'name': 'Bobby',
    'age': 30,
    'salary': 100,
}

# 👉️ default separators are (', ', ': ')

# ✅ JSON string without spaces

json_str = json.dumps(employee, separators=(',', ':'))
print(json_str)  # 👉️ '{"name":"Bobby","age":30,"salary":100}'

# -----------------------------------------------

# ✅ JSON string with spaces only between keys and values
json_str = json.dumps(employee, separators=(',', ': '))
print(json_str)  # ✅ '{"name": "Bobby","age": 30,"salary": 100}'

# -----------------------------------------------

# ✅ JSON string with spaces only between key-value pairs

json_str = json.dumps(employee, separators=(', ', ':'))
print(json_str)  # ✅ '{"name":"Bobby", "age":30, "salary":100}'