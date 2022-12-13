def read_data():
    f = open("names.txt", 'r')
    count = 0
    s = f.read()
    x = s.split()
    for i in x:
        if i == "Darth":
            count +=1
    print(str(count)+" "+"times")

read_data()
