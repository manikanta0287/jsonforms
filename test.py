from ast import alias
import os, json

dir = "/home/xelpmoc/Documents/Mailer/whatsapp"

files = os.listdir(dir)

def addAlias():
    for filename in files:
        if filename.endswith("json"):   
            f = open(filename)
            print(filename)

            data = json.load(f)

            fields = data["data"]

            i = 1
            for field in fields:
                _alias =  str(field["page"]) + "_" +   str(i)
                field["alias"] = _alias
                
                i += 1
            f.close()


            f = open(filename, "w")
            f.write(str({"data" : fields}))
            f.close()

def testjson():
    for filename in files:
        if filename.endswith("json"):
            try:
                f = open(filename)
                data = json.load(f)
                f.close()
                if data != None:
                    print("OK:", filename)
            except:
                print("error:"  ,filename )

    print("all files tested")

testjson()