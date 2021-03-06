import boto
def bucket_du(bucket_name):

    s3 = boto.connect_s3()
    total_bytes = 0
    bucket = s3.lookup(bucket_name)
    if bucket:
        for key in bucket:
            total_bytes += key.size
    else:
        print(f'Warning: bucket %s was not found!', bucket_name)
    return total_bytes
