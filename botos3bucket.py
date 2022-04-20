# using boto3 to create an aws s3 bucket
import boto3
client = boto3.client("s3")

# creating a public s3 bucket named newbucket421
response = client.create_bucket(
    ACL='public-read',
    Bucket='newbucket421',

)

print(response)
