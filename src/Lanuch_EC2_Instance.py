import boto3

ec2 = boto3.resource('ec2')
'''
instance = ec2.create_instances(
    ImageId = 'ami-0b0b075706e19de29',
    MinCount = 1,
    MaxCount =1,
    InstanceType = 't2.micro')

print(instance[0].id)
'''
instance_id = 'i-00cd13acb9bde955a'
instance = ec2.Instance(instance_id)
response = instance.terminate()
print(response)
