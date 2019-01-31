

import boto3
s3 = boto3.client('s3')                                #instantiate a client connection to S3

#open a wordlist file using python's built in open() function
file = open('wordlist.txt')
print(file)                       #display the object's metadata?
print(file.name)                  #call a method on the open() object
wordlist=file.read().split('\n')  #call a method on the open() object to genearte the desired list. Newline characters are stripped.   
print(wordlist)                   

#need to clear the /n that was placed in the strings
#for i in wordlist:



#make API call (TBD) for each word
#record hits into a list

