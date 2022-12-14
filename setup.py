import os

from setuptools import setup, find_packages
from infiq import get_version as get_package_version

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
REQUIREMENTS = open(os.path.join(os.path.dirname(__file__), 'requirements.txt')).read().splitlines()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='infiq',
    version=get_package_version(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=REQUIREMENTS,
    setup_requires=REQUIREMENTS,
    pyrobuf_modules='proto',
    license='APACHE 2.0',
    description='Some widgets collections fro the Django 4.0+',
    long_description=README,
    url='https://github.com/usalko/infiq',
    author='usalko',
    author_email='ivict@rambler.ru',
    maintainer='usalko',
    maintainer_email='ivict@rambler.ru',
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: AsyncIO',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet',
        'Development Status :: 4 - Beta',
    ],
)
