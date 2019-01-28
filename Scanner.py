

import boto3
s3 = boto3.client('s3')

response = s3.list_buckets()
print('----dict rcvd from s3.list_buckets()---->', response)        #response comes in as a dict

for key in response:    
	print(key, '<----key from list_buckets')         #Buckets will return a list

pails = response['Buckets']  #extract data on a single key which will yield a list
print('----list rcvd the Buckets key---->', pails)

print('----These are the buckets in your account:--->')
for item in pails:
	print(item['Name'])

  

	                    
