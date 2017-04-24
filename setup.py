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
          'pyhamcrest',
      ])
