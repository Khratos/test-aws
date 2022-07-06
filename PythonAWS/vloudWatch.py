

 


 #A Simple User-Data Script
 >>> from ec2_launch_instance import launch_instance
 >>> script = """#!/bin/sh
 ... echo "Hello World. The time is now $(date -R)!" | tee /root/output.txt
 ... """
 >>> instance, cmdshell = launch_instance(user_data=script)
 Security Group: paws already authorized
 waiting for instance
 .
 .
 .
  done
 SSH Connection refused, will retry in 5 seconds
 >>> cmdshell.shell()
 __| __|_ )
 _| ( / Amazon Linux AMI
 ___|\___|___|
 See /usr/share/doc/system-release/ for latest release notes.
 No packages needed for security; 1 packages available
 [ec2-user@domU-12-31-39-00-E4-53 ~]# sudo su
 [ec2-user@domU-12-31-39-00-E4-53 ~]# cd /root
 [ec2-user@domU-12-31-39-00-E4-53 ~]# ls
 output.txt
 [ec2-user@domU-12-31-39-00-E4-53 ~]# cat output.txt
 Hello World. The time is now Wed, 21 Sep 2011 23:53:51 +0000!
 [ec2-user@domU-12-31-39-00-E4-53 ~]# exit
 [ec2-user@domU-12-31-39-00-E4-53 ~]$ logout
 *** EOF
 >>> instance.terminate()
 >>>
 
 
