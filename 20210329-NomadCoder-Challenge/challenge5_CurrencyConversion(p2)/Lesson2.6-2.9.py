"""
2.6 - extract data from html
1. Make soup
2. You can use the find_all("")
ex:
results = soup.find_all("div", {"class: "classname"})
3. Extracting
- for result in results:
    print(result.find("div",{"class":"title"}))
: title has anchor inside. 
4. Use .string
- print(title.find("a).string)
- anchor = title.find("a)[title] - you can get the attribute and within the attribute - title property.
- after you are sure that this is going to work you can unify different lines of code with .
ex:
title = result.find(("div", {"class": "title"}}.find("a")["title"]

2.7