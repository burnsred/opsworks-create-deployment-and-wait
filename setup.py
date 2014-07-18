from setuptools import setup

setup(
    name='create-opsworks-deployment-and-wait',
    version='0.0.1',
    packages=['opsworks_create_deployment_and_wait',],
    scripts=['bin/opsworks-create-deployment-and-wait'],
    include_package_data=True,
    license='MIT License',
    author='Michael Bertolacci',
    author_email='michael@burnsred.com.au',
    url='',
    install_requires=['boto==2.31.1'],
    long_description=open('README.md').read(),
)