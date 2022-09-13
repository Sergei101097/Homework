def numer_numbers():
    myfile= open("numbers.txt","w")
    for new_file in range(1,5+1):
        myfile.write(str(new_file) + "\n")
numer_numbers()

def open_file_numbers ():
    myfile = open("numbers.txt","r")
    r = myfile.read()
    myfile.close()
    print(r)
open_file_numbers()