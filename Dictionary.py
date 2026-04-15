s1 = {
    'name': "zainab",
    "rank" : "99",
    "inst" : "IITB"
}
 

print(s1)

print(s1['name'])  #keys allow you to index the data items directly using strings which are interpretable and relative
              


s1["batch"] = "cse"
print(s1["batch"])

print(s1.keys())          # it will list all the keys of our dict and printing them

for i in s1:
    print(i , s1[i])  #printing one by one keys and their pairs



s2 = {
    "name" : "samin",
    "rank" :  "101",
    "inst" : "IITD"

}

gq = [s1,s2]          #converting dictionary s1 and s2 into list


print(gq)


for i in gq:                #now traversing over the list one by one key value pairs
    if isinstance(i,dict):
        for j in i:
            print(j, i[j])

    else:
        print(i)