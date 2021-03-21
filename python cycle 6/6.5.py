f = open("F:\python\Book2.csv", "a")
import json
thisdict = {
"Fname":"Deepa",
"Lname":"Rose",
"Email":"deepa1819@gmail.com"
}
result = json.dumps(thisdict)
f.write(result)
f.close()
f = open("F:\python\Book2.csv", "r")
print(f.read())
