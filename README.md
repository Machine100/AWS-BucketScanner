AWS BUCKET SCANNER

This program looks for public AWS buckets.
A wordlist is used to generate possible bucket names.

For each possible name, an API call is made to the name's endpoint. A response from the endpoint with data
indicates the name exists publicly.

What I Learned:

Implementation of AWS API calls
Programatically access AWS services over their API.
Basic S3 API structure
Python
