import os
import time
import boto
import boto.manage.cmdshell
def launch_instance(ami='ami-7341831a',
instance_type='t1.micro',
key_name='paws',
key_extension='.pem',
key_dir='~/.ssh',
group_name='paws',
ssh_port=22,
cidr='0.0.0.0/0',
tag='paws',
user_data=None,
cmd_shell=True,
login_user='ec2-user',
ssh_passwd=None):

    cmd = None
    # Create a connection to EC2 service.
    # You can pass credentials in to the connect_ec2 method explicitly
    # or you can use the default credentials in your ~/.boto config file
    # as we are doing here.
    ec2 = boto.connect_ec2()
    # Check to see if specified keypair already exists.
    # If we get an InvalidKeyPair.NotFound error back from EC2,
    # it means that it doesn't exist and we need to create it.
    try:
        key = ec2.get_all_key_pairs(keynames=[key_name])[0]
    except ec2.ResponseError as e:
        if e.code == 'InvalidKeyPair.NotFound':
            print( 'Creating keypair: %s' % key_name )
            # Create an SSH key to use when logging into instances.
            key = ec2.create_key_pair(key_name)
            # AWS will store the public key but the private key is
            # generated and returned and needs to be stored locally.
            # The save method will also chmod the file to protect
            # your private key.
            key.save(key_dir)
        else:
            raise
    # Check to see if specified security group already exists.
    # If we get an InvalidGroup.NotFound error back from EC2,
    # it means that it doesn't exist and we need to create it.
    try:
        group = ec2.get_all_security_groups(groupnames=[group_name])[0]
    except ec2.ResponseError as e:
        if e.code == 'InvalidGroup.NotFound':
            print( 'Creating Security Group: %s' % group_name )
    # Create a security group to control access to instance via SSH.
            group = ec2.create_security_group(group_name,
            'A group that allows SSH access')
        else:
            raise
            # Add a rule to the security group to authorize SSH traffic
            # on the specified port.
    try:
        group.authorize('tcp', ssh_port, ssh_port, cidr)
    except ec2.ResponseError as e:
        if e.code == 'InvalidPermission.Duplicate':
            print( 'Security Group: %s already authorized' % group_name )
        else:
            raise
  
    # Now start up the instance. The run_instances method
    # has many, many parameters but these are all we need
    # for now.
    reservation = ec2.run_instances(ami,
    key_name=key_name,
    security_groups=[group_name],
    instance_type=instance_type,
    user_data=user_data)
    # Find the actual Instance object inside the Reservation object
    # returned by EC2.
    instance = reservation.instances[0]
    # The instance has been launched but it's not yet up and
    # running. Let's wait for its state to change to 'running'.
    print( 'waiting for instance' )
    while instance.state != 'running':
        print ('.' )
        time.sleep(5)
        instance.update()
    print( 'done' )
    # Let's tag the instance with the specified label so we can
    # identify it later.
    instance.add_tag(tag)
    # The instance is now running, let's try to programmatically
    # SSH to the instance using Paramiko via boto CmdShell.
    if cmd_shell:
        key_path = os.path.join(os.path.expanduser(key_dir),
        key_name+key_extension)
        cmd = boto.manage.cmdshell.sshclient_from_instance(instance,
        key_path,
        user_name=login_user)
    return(instance, cmd)