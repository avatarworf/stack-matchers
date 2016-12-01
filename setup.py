from setuptools import setup

setup(name='stack_matchers',
      version='0.0.1',
      description='A matcher library for cloudformation stack assertions',
      url='https://github.com/Financial-Times/stack-matchers',
      author='Konstructor Cloud Team',
      author_email='konstructor.cloud@ft.com',
      license='MIT',
      packages=['stack_matchers'],
      zip_safe=False,
      install_requires=[
          'pyhamcrest',
      ])
