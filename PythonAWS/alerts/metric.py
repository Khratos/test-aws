
# Custom Metric for Disk Usage

import boto
import time
import datetime
import os


def main():
    cw = boto.connect_cloudwatch()
    md = boto.utils.get_instance_metadata()
    now = datetime.datetime.utcnow()
    stats = os.statvfs('/')

    total = float(stats.f_blocks * stats.f_bsize)
    available = float(stats.f_bavail * stats.f_bsize)
    percent_used = int(100 - 100 * (available / total))
    print (f'metric_disk_usage: %d' % percent_used)
    cw.put_metric_data(namespace='PAWS',
                       name='DiskUsage',
                       value=percent_used,
                       timestamp=now,
                       unit='Percent',
                       dimensions=[{'InstanceId': md['instance-id']}])
if __name__ == "__main__":
    main()
