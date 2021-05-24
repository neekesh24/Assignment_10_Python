#Nikesh Kshetri, Assignment 10.1, 05/23/2021
#starting with OS module to create function that interact with operating system
import os
def main():
    #taking inputs inside of the main module
    directory = input("Please enter the directory that you want to save the file: ")
    fileName = input("Please enter the file name: ")
    name = input("Please enter your name: ")
    address = input("Please enter your address: ")
    phoneNumber = input("Please enter your phone number: ")

    #creating if/else method which will check if the directory exists
    if os.path.isdir(directory):
        #this step will create and open the file for writing
        write_file = open(os.path.join(directory,fileName), 'w')

        #this step writes the data with comma separated
        write_file.write(name+','+address+','+phoneNumber+'\n')

        #it closes once the writing is done
        write_file.close()

        #reading if the file is stored properly
        print("File information: ")
        readFile = open(os.path.join(directory,fileName),'r')
        for line in readFile:
            print(line)
            readFile.close()
    else:
        print("Sorry directory doesn't exists.")
main()