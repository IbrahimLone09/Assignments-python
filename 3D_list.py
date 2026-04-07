def printlist(gatecs):
    for i in gatecs:
        if isinstance(i, list):              # funaction to check if "i" is a list also or not                        
                for j in i:                  #  "j" iterates over "i"
                    if isinstance(j,list):
                            for k in j:      #  "k" iterates over "j"
                                print(k)           

                    else:
                            print(j)         # if "j" is not a list print "j"
                    
        else:
                print(i)

gatecs = ['ADA' , ['CLR', 'SS' ,[12]], 'DM', ['RS','SH']]      # 3D list 
printlist(gatecs)
            