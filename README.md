AWS BUCKET SCANNER

This is a program that looks for buckets on the internet that are marked public. 


A wordlist is used to generate probable bucket names.

For each word, an API call is made to the bucket endpoint. A response from the API with data
indicates that a bucket exists and is marked as public.

Because this scanner finds data, this is not an indication of a security hole.
Many public buckets at AWS are meant to be public.


What I Learned
implementation of AWS API calls
Programatically access AWS services over their API.
basic S3 API structure
Python
