"""Setuptool for python stack matcher."""
import setuptools
import stack_matchers

setuptools.setup(
    name=stack_matchers.__title__,
    version=stack_matchers.__version__,
    author=stack_matchers.__author__,
    author_email=stack_matchers.__email__,
    description=stack_matchers.__summary__,
    long_description=open("README.rst", "r").read(),
    long_description_content_type='text/x-rst',
    license=stack_matchers.__license__,
    url=stack_matchers.__uri__,
    packages=setuptools.find_packages(),
    zip_safe=False,
    install_requires=['PyHamcrest>=1.9.0',
                      'boto3>=1.10.35',
                      'botocore>=1.13.35']
)
