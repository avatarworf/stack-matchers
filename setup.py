from setuptools import setup

setup(name='stack_matchers',
      version='0.0.2',
      description='A matcher library for CloudFormation stack assertions',
      url='https://github.com/Financial-Times/stack-matchers',
      author='Cloud Enablement',
      author_email='cloud.enablement@ft.com',
      license='MIT',
      packages=['stack_matchers'],
      zip_safe=False,
      install_requires=[
          'PyHamcrest==1.9.0',
          'boto3==1.6.16',
          'botocore==1.9.16'
      ])
