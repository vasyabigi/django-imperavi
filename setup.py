import os
from setuptools import setup, find_packages

README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.rst')
description = "A django application that contains a widget to render a \
    form field as beautiful Imperavi WYSIWYG editor http://redactorjs.com/"

if os.path.exists(README_PATH):
    long_description = open(README_PATH).read()
else:
    long_description = description

setup(
    name="django-imperavi",
    version="0.1.2",
    author="Vasyl Stanislavchuk",
    author_email="vasyl.stanislavchuk@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    description=description,
    long_description=long_description,
    license="MIT License",
    keywords="django admin widget imperavi",
    platforms=['any'],
    install_requires=[
        "django",
        "sorl-thumbnail >= 11.12",
    ],
    url="https://github.com/vasyabigi/django-imperavi",
)
