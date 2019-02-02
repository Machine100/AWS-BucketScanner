

import boto3
import botocore
s3 = boto3.client('s3')                                #instantiate a client connection to S3

#open a wordlist file using python's built in open() function
file = open('wordlist.txt')
print(file)                       #display the object's metadata?
print(file.name)                  #call a method on the open() object
words=file.read().split('\n')  #call a method on the open() object to genearte the desired list. Newline characters are stripped.   
#print(words)                   

for i in words:     bucket = s3.Bucket('word')     exists = true     try:
s3.meta.client.head_bucket('name')     

except botocore.exceptions.ClientError as e:         
	# if a client error is thrown, then check that it was a 404 error
	# if it was a 404 error, then the bucket does not exist
	error_code = e.response['Error']['Code']         
	if error_code == '404':
		exists=false

#for i in wordlist:



#make API call (TBD) for each word
#record hits into a list

