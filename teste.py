with open('login.txt') as f:
    mylist = [line.rstrip('\n') for line in f]

print(mylist)

for i in mylist:
    login = i.split(',')
    print (login)
