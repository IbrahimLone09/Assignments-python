gatecs = ['ADA' , ['CLR', 'SS'], 'DM', ['RS','SH']]     # A simple "2D" list 
print(len(gatecs))
print(gatecs)
for i in gatecs:
      if isinstance(i, list):    # Function to check if "i" is also a list
            for j in i:
                  print(j)
      else:
            print(i)
print(gatecs[1][0])
print(gatecs[1][1])
        