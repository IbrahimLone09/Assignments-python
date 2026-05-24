def printlist(gatecs):
    for i in gatecs:
        if isinstance(i, list):
                printlist(i)        # using recursion now to avoid more loops

                              
        else:                                 
                print(i)


gatecs = ['ADA' , ['CLR', 'SS' ,[12]], 'DM', ['RS','SH']]
printlist(gatecs)