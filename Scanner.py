

import boto3
import botocore
s3client = boto3.client('s3')           #instantiate a client connection to S3
s3resource = boto3.resource('s3')       #instantiate a resource connection to S3
file = open('wordlist.txt')             #open a wordlist file using python's built in open() function
print(file)                             #display the object's metadata?
print(file.name)                        #call a method on the open() object
words=file.read().split('\n')           #call a method on the open() object to genearte the desired list. Newline characters are stripped.   
#print(words)                   

for word in words:
	exists = True 
	try:
		s3resource.meta.client.head_bucket(Bucket=word)     #This is the official way to check if a bucket exists
	except botocore.exceptions.ClientError as e:            #Which is to say go through the resource object.
		error_code = e.response['Error']['Code']            #This snippet copied from official docs.    
		if error_code == '404': 
			exists=False
	print ('Bucket', word,':', exists) 




#make API call (TBD) for each word
#record hits into a list

