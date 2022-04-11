import json
import requests

def menu():
    
    r=requests.get("http://saral.navgurukul.org/api/courses")
    with open("try.json","w") as file:
        co=json.loads(r.text)
        json.dump(co,file,indent=2) 
    with open("try.json","r") as file:
        var=json.load(file)
    # print(h)
    c=1
    lis=[]
    for i in co["availableCourses"]:
        print(c,i["name"],i["id"])
        lis.append(i["id"])
        c=c+1
    num=int(input("enter serial num"))
    x=0
    k=requests.get("http://saral.navgurukul.org/api/courses/"+str(lis[num ])+"/exercises")
    m=k.json()
    # print(m["content"])
    slug=[]
    for i in m["data"]:
        print(x,i["name"])
        slug.append(i["slug"])
        x+=1
    num1=int(input("enter slug num:"))
    l=requests.get("http://saral.navgurukul.org/api/courses/"+str(num)+"/exercise/getBySlug?slug="+slug[num1])
    n=l.json()
    print(n["content"])
    print("up: for all content")
    print("p: for previous content")
    print("n: for next content")
    print("again: for again")
    print("exit: for exit")
    d=0
    while d<len(slug):
        user=input("what u want::")
        if user=="up":
            cal=menu()
            print(cal["content"])
        elif user=="n":
            m=requests.get("http://saral.navgurukul.org/api/courses/"+str(num)+"/exercise/getBySlug?slug="+slug[num1+1])
            o=l.json()
            print(num1+1,o["content"])
        elif user=="p":
            m=requests.get("http://saral.navgurukul.org/api/courses/"+str(num)+"/exercise/getBySlug?slug="+slug[num1-1])
            z=l.json()
            print(num1-1,z["content"])
        user1=input("enter again or exit")
        if user1=="again":
            menu()
        else:
            break
        d+=1
menu()    



# import pprint
# pprint(stuff)


        
