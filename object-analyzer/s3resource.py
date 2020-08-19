import boto3
from awsresource import AwsResource


# This class extends from AwsResource class, so that future AWS services can easily be added with a simple
# class addition.

class S3Resource(AwsResource):

    def __init__(self):
        super().__init__()
        self.resource = boto3.resource('s3')
        self.buckets = self.resource.buckets.all()

    def build_bucket_object(self, unit_of_measure):
        bucket_info = {}
        for bucket in self.buckets:
            bucket_info[bucket.name] = {}
            bucket_info[bucket.name]['created_date'] = bucket.creation_date

            total_object_size = 0
            total_object_count = 0
            latest_modified_date = ""
            bucket = self.resource.Bucket(bucket.name)
            for object_key in bucket.objects.all():
                total_object_count += 1
                total_object_size += object_key.size
                if str(object_key.last_modified) > str(latest_modified_date):
                    latest_modified_date = object_key.last_modified
            bucket_info[bucket.name]['number_of_objects'] = total_object_count
            bucket_info[bucket.name]['latest_modified_date'] = latest_modified_date

            formatted_object = S3Resource.format_unit_of_measure(total_object_size, unit_of_measure)
            bucket_info[bucket.name]['size_of_all_objects'] = formatted_object

        return bucket_info

    @staticmethod
    def format_unit_of_measure(size_of_object, desired_unit_of_measure):
        if desired_unit_of_measure == 'kb':
            size_of_object *= 1.0 / 1024
        elif desired_unit_of_measure == 'mb':
            size_of_object *= 1.0 / 1024 / 1024
        elif desired_unit_of_measure == 'gb':
            size_of_object *= 1.0 / 1024 / 1024 / 1024
        else:
            return size_of_object

        return size_of_object
