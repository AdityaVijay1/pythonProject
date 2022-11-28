SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
words=[]
text = "?name=Bob&age=99&day=Wed"
text = text[1:].split('&')
print(text)
for i in range(0, len(text)):
    print(text[i])
    text[i] = tuple(text[i].split('='))
for i in text:
    a,b=i
    if a.isdigit():
        a=int(a)
    if b.isdigit():
        b=int(b)
    i=(a,b)
    words.append(i)
name = "?name=Bob&age=99&day=Wed"

names = name.split("&")
for i in range(0, len(names)):
    names[i] = names[i].lstrip("?")
    names[i] = names[i].split("=")
    for j in range(0, len(names[i])):
        if names[i][j].isdigit():
            names[i][j] = int(names[i][j])
    names[i] = tuple(names[i])


print(names)
print(text)
print(words)


