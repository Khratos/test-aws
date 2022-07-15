import boto
def create_bucket(bucket_name):

    s3 = boto.connect_s3()

    bucket = s3.lookup(bucket_name)
    if bucket:
        print (f'Bucket (%s) already exists', bucket_name)
    else:
        try:
            bucket = s3.create_bucket(bucket_name)
        except s3.provider.storage_create_error as e:
            print (f'Bucket (%s) is owned by another user'.bucket_name)
    return bucket