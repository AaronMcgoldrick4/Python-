keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

print(dict(zip(keys, values)))

sampleDict = {
    "class":{
        "student":{
            "name":"Mike",
            "marks":{
                "physics":70,
                "history":80
            }
        }
    }
}

print(str(sampleDict["class"]["student"]["marks"]["history"]))

sampleDict2 = {
    "name": "Kelly",
    "age":25,
    "salary": 8000,
    "city": "New York"

}
sampleDict2.pop("name")
sampleDict2.pop("salary")

print(list(reversed(sampleDict2.items()))) 



