import json

# some string
x = '{"name":"Harsh", "age":20, "city":"New York"}'

# parse x
y = json.loads(x)

print(y["age"])

# to make a dict json compatible

det = {
    "name": "Harsh",
    "friends": ["bittu", "Sunil", "Vishal"],
    "Items": ("kutta", "billi")
}

p = json.dumps(det)     # Now p can be used as a json
print(p)
