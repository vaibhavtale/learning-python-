course = 'Python for begginers'

another = course[:]
print(another)
print(course)
print(course[0:3])


course = "Python's course course for begginers"

print(course)
print(course[1])

course = 'Python course for "Begginers"'

print(course)
print(course[-4])
print(len(course))

long = '''
        learn the things from basics wich you are not good at, bring a little shame, you are'nt even able to solve a basic calculation of 5th standard .. ya but 'j zal te zal' I really want to change myself deep within my heart, i will really learn all those concepts from basics to pro and also by learning such exciting and important concepts not only helps me to grow a problem solving mindset but also at the same time it opens up so many new opportunities for you...
'''

print(long)

# exercise

name = 'Jennifer'

print(name[1:-1])

# String formatting

first = 'Mosh'
last = 'Hamedani'

message = first + ' [' + last + '] is the best Programming teacher i have ever seen.'
print(message)

msg = f'{first} [ {last} ] is one the cool teacher for coding.'
print(msg)

sen = "python learning for begginers."

print(sen.replace('python', 'django'))

# use of "in" and 'find' to find the presence of string in string...

print('Python' in sen)
print(sen.find('for'))

n = input("your name please")
print('hii' + n)
























