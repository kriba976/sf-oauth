#Strings
host = "www.successfactors.com"
entity = "PerPerson"

url = f"{host}/{entity}"
##print(url)

#Lists
a="1,2,3,4,5"
b=a.split(",")
#print(b[0])

b.append("6")
#print(b)

#Dictionaries
user1 = {"name": "John", "age": 30, "city": "New York"}
#print(user["name"])

user1["age"]=31
user1["city"]="Los Angeles"
user1["name"]="Jane"
print(user1["name"])

user2 = {"name": "Alice", "age": 25, "city": "Chicago"}
print(user2["name"])

user=[user1, user2]
print (user)
