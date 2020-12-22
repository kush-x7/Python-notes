file = open("filename.txt")   -->will open a file
contents =file.read()         -->will read content of the file
print(contents)               -->print the content
file.close()                  -->will close the file

     or

with open("filename.txt") as file:
    contents =file.read()         -->will read content of the file
    print(contents)               -->print the content


with open("filename.txt", mode="w") as file:   --> w means write (it will delete previous and write new line)
                                               --> a means append (ussi line ke age likh dega )
    file.write("my name is kush")
