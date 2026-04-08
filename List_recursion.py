def printlist(gatecs):
    for i in gatecs:
        if isinstance(i, list):
                printlist(i)        # using recursion now to avoid more loops

                              
        else:                                 
                print(i)


gatecs = [] 
for i in gatecs:
    gatecs = input("Enter the list! ")
printlist(gatecs)