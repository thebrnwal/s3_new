import boto3


bucket_name = input(Enter Bucket Name :)

client = boto3.client('s3')
response = client.get_bucket_acl(Bucket=bucket_name)
print = (response)

if "'Permission': 'FULL_CONTROL" in str(response):
	print("Full control")

elif "'Permission': 'READ'}" in str(response):
	print("Read Access")

elif "'Permission': 'WRITE'}" in str(response):
	print("WRITE Access")

elif "'Permission': 'READ_ACP'}" in str(response):
	print("READ_ACP")

elif "'Permission': 'WRITE_ACP'}" in str(response):
	print("WRITE_ACP")