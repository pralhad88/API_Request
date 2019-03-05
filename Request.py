import os.path 
from os import path
import json
import requests

exists = path.exists("./courses.json")

if (exists):
    with open("courses.json") as file:
        var = json.load(file)
else:
    data = requests.get("http://saral.navgurukul.org/api/courses").text
    with open("courses.json", "w+") as file:
        file.write(data)
        var = json.loads(data)


def list_of_cources():
    j = 0
    for i in var["availableCourses"]:
        j+=1
        print(j, i['name'])



def details_of_cource():
    while True:
        print("..........Welcome to Navgurukul saral Portfolio and Learn basic Programming Languges..........")
        print("..............The list of course is given below...........................")
        print(" ")
        print(list_of_cources())
        print("...........................")
        user = int(input("Enter your courses number that you want to learn:- "))
        k = 0
        for j in var["availableCourses"]:
            k+=1
            if user == k :
                print (j['name'])
                print('')
                req = requests.get("http://saral.navgurukul.org/api/courses/"+str(j["id"])+"/exercises").text
                dic = json.loads(req)
                
                while True:
                    k = 0
                    for i in dic['data']:
                        k+=1
                        print (k, i['name'])
                    print('')
                    
                    n = int(input("Enter topic number that's you want to learn:- "))
                    print("")
                    
                    s = 0
                    for p in dic['data']:
                        s+=1
                        if n == s:
                            cource_data = requests.get("http://saral.navgurukul.org/api/courses/"+ str(j["id"]) + "/exercise/getBySlug?slug=" + p["slug"]).text
                            data_type = json.loads(cource_data)
                            print("Topic name:- " + data_type['name'])
                            print("")
                            print(data_type["content"].strip('\n'))
                            print('-------------------------------------------------')
                    
                    user = input ("If you want to learn next topic then press any key or type 'exit' to leave the cource:- ")
                    
                    if user == 'exit':
                        break

        print("")
        user = input("If you want to learn another cource then press any key or 'exit' to terminat the cource:- ")
        
        if user == "exit":
            print("")
            print("-----Thank you for visiting to Navgurukul Study Portfolio---------")
            break

details_of_cource()
