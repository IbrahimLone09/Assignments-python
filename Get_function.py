IITS = {
"IITB"  : "Get rank to 1 to 99",
"IITD"  : "Get rank 100 to 200",
"IITM"  : "Get rank 200 to 300"
}
msg = input("Enter your favt IIT! ").upper()
output = ""
words = msg.split()
for i in words:
    output = IITS.get(i)   

print(output)
