

import boto3
s3 = boto3.client('s3')                                #nstantiate a client connection to S3

response = s3.list_buckets()
print('<---rcvd from s3.list_buckets()---', response)  #response comes in as a dict

response2 = response['Buckets']                        #from key 'Buckets', extract a list
print('<---rcvd the Buckets key---', response2)

print('These are the buckets in your account:')        #display key 'Name' for each item in that list 
for item in response2:                                 #these are the bucketnames for the account configured
	print(item['Name'])                                #under the pc's AWS console configuration.

  

	  
##call s3 to list current buckets
#response = s3.list_buckets()

#get list of bucket names
#buckets = [bucket['Name'] for bucket in response['Buckets']]

#print('Bucket List: %s' % buckets)                  
