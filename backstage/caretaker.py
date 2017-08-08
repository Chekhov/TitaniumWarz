
def reader():
    file = open("lists.txt", 'r')
    string = ["["]
    for line in file.readlines():
        k = "'"+line.strip("\n") + "',"
        string.append(k)
    string.append("]")
    print ("".join(string))

reader()