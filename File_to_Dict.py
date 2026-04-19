with open(r"C:\Users\ibrah\OneDrive\Desktop\ibrahim.txt","r") as fr:
    lines = fr.readlines()
    


    for i in lines:
        i = i.lower()



length = len(lines)

for i in range(length):
    lines[i] = lines[i].lower()

#print(lines[0])

#for i in range(length):
    #lines[i] = lines.replace("\n", "")

unchars = ['\n','.',",",","]
for i in range(length):
    for j in unchars:
        lines[i] = lines[i].replace(j, " ")

#print(lines)

singlestr = ""
for i in range(length):
    singlestr = singlestr + lines[i] + " "

#print(singlestr)

words = singlestr.split()
print(words)
print(len(words))

dict = {}


for i in words:
    if i in dict:
        dict[i] += 1     # iterate through the words if present in words increase its value 
    
    else:
        dict[i] = 1

print(dict)


for i in dict:
    print(i, ":" , dict[i])