# This super/abstract class provides a way to create any number of resource classes (like s3resource or ec2resource)
# and have the ResourceFactory (in main.py) enforce object types for its incoming parameters based on whether the
# parameter objects are derived and instanced from this class.

class AwsResource:
    def __init__(self):
        pass

