#Configuring SNS for CloudWatch Alarms
import boto
sns = boto.connect_sns()
sns.create_topic('paws_cloudwatch')
{
    u'CreateTopicResponse': {u'ResponseMetadata': {u'RequestId': u'73721b87da0e-11e0-99a4-59769425d805'},
    u'CreateTopicResult': {u'TopicArn': 
    u'arn:aws:sns:useast-1:084307701560:paws_cloudwatch'}}
}
topic_arn = _['CreateTopicResponse']['CreateTopicResult']['TopicArn']

topic_arn 
u'arn:aws:sns:us-east-1:084307701560:paws_cloudwatch'

sns.subscribe(topic_arn, 'email', 'suemail@email.org')
{
    u'SubscribeResponse':{u'SubscribeResult': {u'SubscriptionArn': u'pending confirmation'},
    u'ResponseMetadata': {u'RequestId': u'd4a846fd-da0e-11e0-bcf1-37db33647dea'}}
} 


 

