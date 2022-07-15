import boto
def create_bucket(bucket_name):

    s3 = boto.connect_s3()

    bucket = s3.lookup(bucket_name)
    if bucket:
        print ('Bucket (%s) already exists' % bucket_name)
    else:
    # Let's try to create the bucket. This will fail if
    # the bucket has already been created by someone else.
    try:
        bucket = s3.create_bucket(bucket_name)
    except s3.provider.storage_create_error, e:
        print ('Bucket (%s) is owned by another user' % bucket_name)
    return bucket