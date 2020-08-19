#!/usr/bin/env python3

import argparse
from s3resource import S3Resource


# This file contains the app's entry-point and the logic to accept and build a resource object (like s3resource)
# while also processing the command line args.
# The ResourceFactory class (below) accepts any type of resource object just by adding it to the conditional.
# For instance, it currently accepts the only resource type available ('s3resource'), but if in the future, we wanted
# to expand this tool to work with EC2 instances (or any other API addressable service), we could easily add a new
# resource class extended from awsresource::AwsResource and enforce ResourceFactory to only accept
# isinstance(awsresrouce).
# If we wanted to extend the tool to a multi-cloud-provider environment, we could easily add an abstract Resource class
# and extend awsresource::AwsResource and gcpresource::GcpResource and azureresource::AzureResource with their own
# respective resource modules/classes.  Since they all would extend from the superclass of Resource, we could easily
# enforce object-specific parameters within ResourceFactory just by requiring the object be an instance of the
# superclass (Resource).  This is not currently done for simplicity's sake but is easily accomplished with few lines of
# additional code all without changing the overall application in any meaningful way.

def init(args):
    resource = ResourceFactory.get_resource(args.resource.lower())
    resource_object = resource.build_bucket_object(args.unit.lower())
    if args.format == 'object':
        print(resource_object)
    else:
        format_output(resource_object)


def format_output(resource_object):
    for bucket in resource_object:
        print('Bucket Name: ' + str(bucket))
        print('Bucket Creation Date: ' + str(resource_object[bucket]['created_date']))
        print('Number of Objects: ' + str(resource_object[bucket]['number_of_objects']))
        print('Total Size of Objects: ' + str(resource_object[bucket]['size_of_all_objects']))
        print('Last Modified Object Date: ' + str(resource_object[bucket]['latest_modified_date']) + "\n")


class ResourceFactory:
    @staticmethod
    def get_resource(resource):
        try:
            if resource == "s3":
                return S3Resource()
            raise AssertionError("No such resource type.")
        except AssertionError as _e:
            print(_e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Object Analyzer Tool")
    parser.add_argument("-u", "--unit", default="b", type=str,
                        help="Display the size of objects in the specified units.  Options are b=bytes (default), "
                             "kb=kilobytes, mb=megabytes, gb=gigabytes")
    parser.add_argument("-r", "--resource", type=str, default='S3', help="The resource type.  Default is 'S3'.")
    parser.add_argument('-f', '--format', type=str, default='pretty', help="The formatted output.  Options are "
                                                                           "pretty=pretty format (default) or "
                                                                           "object=object format.")
    args = parser.parse_args()

    init(args)
