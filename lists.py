# s3_buckets_list = ["bucker-1", "bucket-2", "bucket-3"]
# s3_buckets_list.append("bucket-4")
# s3_buckets_list.append("bucket-5")

# print(s3_buckets_list)

ec2_instances = ["t2.micro", "t2.small", "t2.medium", "t2.large", "t2.xlarge", "t2.2xlarge"]
print(ec2_instances)
print(len(ec2_instances))

new-list = ec2_instances([0:4])
print(len(ec2_instances))

ec2_instances.remove("t2.micro")
ec2_instances.remove("t2.small")    
print(ec2_instances)
print(len(ec2_instances))