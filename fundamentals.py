firstnum = 100
first_string = 'blahblah'
first_bool = False
print(first_bool)
print(firstnum)
print(first_string)

if(firstnum > 10):
    print('that is larger than ten')
else:
    print('that is not larger than 10')    

if(firstnum < 0 and first_bool == True):
    print('negative and true')
elif(firstnum > 0 and first_bool == False):
    print('positive and false')
elif(firstnum > 100 or first_bool == True):
    print('large or true')
else:
    print('i dont know')
