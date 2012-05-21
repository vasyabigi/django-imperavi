from setuptools import setup, find_packages

setup(
    name="django-imperavi",
    version="0.1.5dev",
    author="Vasyl Stanislavchuk",
    author_email="vasyl.stanislavchuk@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    description="A django application that contains a widget to render a \
        form field as beautiful Imperavi WYSIWYG editor http://redactorjs.com/",
    long_description=open('README.txt', 'r').read(),
    license="MIT License",
    keywords="django admin widget imperavi",
    platforms=['any'],
    install_requires=[
        "django",
        "PIL",
        "sorl-thumbnail >= 11.12",
    ],
    url="https://github.com/vasyabigi/django-imperavi",
)
