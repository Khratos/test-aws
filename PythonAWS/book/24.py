import boto
ec2 = boto.connect_ec2()
fp = open('key.pub')
material = fp.read()
fp.close()
key_pair = ec2.import_key_pair('key', material)