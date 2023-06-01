import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def has_space(w):
    if w.__contains__(" "):
        if w.upper().startswith("EC ") or w.upper().startswith("EU "):
            w = w[:3].upper()+w[3:]
            return w

def has_shape(w):
    if w.__contains__(" "):
        if w.upper().startswith("EU "):
            w = w[:3].upper()+w[3:]
            return w

def dictionary(w): 
    w = w.lower()
    if w in data:
        return (data[w])
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif has_space(w) in data:
        return data[get_close_matches(has_space(w),data.keys()[0])]
    elif has_shape(w) in data:
        return data[get_close_matches(has_shape(w),data.keys()[0])]              
    elif len(get_close_matches(w,data.keys()))>0:
        ch=input("Do you mean %s instead? If yes press Y and for No press N :  " % get_close_matches(w,data.keys())[0])
        if ch == 'Y' or ch == 'y':
            return data[get_close_matches(w,data.keys())[0]]
        elif ch == 'N' or ch == 'n':
            return "This word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."            
    else:
        return "This word doesn't exist. Please double check it." 

word = input("Enter a word: ") 
output = dictionary(word)
if type(output) == 'list':
    for item in output:
        print(item)
else:
    print(output)