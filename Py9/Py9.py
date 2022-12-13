#names
def read_data():
    f = open("names.txt", 'r')
    count = 0
    s = f.read()
    x = s.split()
    for i in x:
        if i == "Darth":
            count +=1
    print("Darth - " + str(count)+" "+"times")

    for i in x:
        if i == "Luke":
            count +=1
    print("Luke - " + str(count)+" "+"times")

    for i in x:
        if i == "Lea":
            count +=1
    print("Lea - " + str(count)+" "+"times")
read_data()

#category
