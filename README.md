

This is a program that looks for buckets on the internet that are marked public. 

A wordlist is used to generate probable bucket names.

For each word, an API call is made to the bucket endpoint. A response from the API with data
indicates that a bucket exists and is marked as public.

It should be remembered that just because this scanner finds data, that is not an indication of a security hole.
Many public buckets at AWS are meant to be public.
