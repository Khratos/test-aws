#Configuring SNS for CloudWatch Alarms
import boto3
sns = boto3.connect_sns()
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

#TEST
 
 #Creating a CloudWatch Alarm
# import boto3
# cw = boto3.connect_cloudwatch()
# my_metrics = cw.list_metrics(dimensions={'InstanceId':'i-76894c16'})
# my_metrics[
#     Metric:DiskReadOps, Metric:NetworkOut, Metric:NetworkIn, Metric:DiskReadBytes,
#     Metric:CPUUtilization, Metric:DiskWriteBytes, Metric:DiskWriteOps]
# metric = my_metrics[4]
# metric
# Metric:CPUUtilization
# alarm = metric.create_alarm(name='CPUAlarm', comparison='>', threshold=80.0, 
# period=60,
# evaluation_periods=2, statistic='Average',
# alarm_actions=['arn:aws:sns:us-east-1:084307701560:paws_cloudwatch'],
# ok_actions=['arn:aws:sns:us-east-1:084307701560:paws_cloudwatch'])
# alarm
# MetricAlarm:CPUAlarm[CPUUtilization(Average) GreaterThanThreshold 80.0]
# alarm.set_state('ALARM', 'Testing my alarm', '100')
# True

# alarm.describe_history()