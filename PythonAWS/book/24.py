import boto
ec2 = boto.connect_ec2()
fp = open('mykey.pub')
material = fp.read()
fp.close()
key_pair = ec2.import_key_pair('root@ip-172-31-28-165.ec2.interna', material)