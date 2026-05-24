def printtuple(mytuple,indent = True, level = 0):
    for i in mytuple:
        if isinstance(i, tuple):
                printtuple(i,indent,level + 1) 
        else:
                if indent:
                        for j in range(level):
                         print("\t", end = " ")

                                                                
                print(i)

nested = (
    (1,(2),(3,3,4)),
    (8,9,10),
    (11,(1,(1,2,(8,9,10),75),3,4),12,13)
)

printtuple(nested,True,2)

