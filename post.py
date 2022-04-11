import json
import requests
r=requests.post("http://saral.navgurukul.org/api/courses")
h=r.json()
with open("post.json","w") as file:
    json.dump(h,file,indent=2)