from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='object-analyzer',
    version='1.0.1',
    description='A command line tool to gather AWS S3 information.',
    long_description=long_description,
    long_description_content_type='text/plain',
    url='https://github.com/realmarkcross/object-analyzer.git',
    author='Mark Cross',
    author_email='markkcross@gmail.com',
    package_dir={'': 'object-analyzer'},
    packages=find_packages(where='object-analyzer'),
    python_requires='>=3.5, <4',
    install_requires=['boto3'],
    entry_points={
        'console_scripts': [
            'main=main:main',
        ],
    },
)