import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read() 

setup(
    name = "django-qna",
    version = "0.1",
    license = "Apache 2.0",
    description = "Small qna app for Django",
    long_description = read("README"),
    url = "https://github.com/bazukas/django-qna",
    author = "Azat Khasanshin",
    author_email = "azatkhasanshin@gmail.com",
    packages = find_packages("src"),
    package_dir = {"": "src"},
    install_requires = ["setuptools"],
    classifiers = [
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache License 2.0',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
