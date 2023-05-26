firstnum = 100
first_string = 'blahblah'
first_bool = False
first_array = ['one','two','three','four']
second_array = [1,2,3,4]

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

for string in first_array:
    print(string)

for num in second_array:
    print('look at this number ',num)

def static_greeting():
    print('hello dale')

static_greeting()

def dynamic_greeting(arg):
    print('hello',arg)

dynamic_greeting('sally')
dynamic_greeting('bob')
dynamic_greeting('bill')