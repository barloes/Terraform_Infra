import boto3

# Boto Connection
ec2 = boto3.resource('ec2', 'ap-southeast-1')

def lambda_handler(event, context):
  # Filters

  # Filter stopped instances that should start
  instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])

  # Retrieve instance IDs
  instance_ids = [instance.id for instance in instances]

  # starting instances
  starting_instances = ec2.instances.filter(Filters=[{'Name': 'instance-id', 'Values': instance_ids}]).start()

  for instance in instance_ids:
    print("%s is starting"%(instance_ids))