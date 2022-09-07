import boto3                                                                                        
import sys                                                                                                                                                                                                    

#bucket_name = input("Enter Bucket Name : ")                                                            

client = boto3.clinet('s3')                                                                                                                                                                                    

with open(sys.argv[1], 'r') as file:                                                                      
    for bucket_name in file:                                                                                
        response = client.get_bucket_acl(Bucket=bucket_name)                                                    
        print("start testing {}").format(bucket_name)                                                        
        if "'Permission': 'FULL_CONTROL" in str(response):                          
            print ("Full control")                                                  
        elif "'Permission': 'READ'}" in str(response):      
            print ("Read Access")          
        elif "'Permission': 'WRITE'}" in str(response):  
            print ("WRITE Access")          
        elif "'Permission': 'READ_ACP'}" in str(response):          
            print ("READ_ACP")        
        elif "'Permission': 'WRITE_ACP'}" in str(response):          
            print ("WRITE_ACP")                          
        else:                                
            print("bucket not found")