def to_upper(words):
    result = []
    for i in words:
        i = i.upper()
        result.append(i)
    return result

#def to_upper(words):
    #result = []
    #for w in words:
        #result.append(w.upper())
    #return result

a = ["nora", "isabel", "einar"]

print(to_upper(a))