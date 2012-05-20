from setuptools import setup, find_packages

setup(
    name="django-imperavi",
    version="0.1.0",
    author="Vasyl Stanislavchuk",
    author_email="vasyl.stanislavchuk@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    description="A django application that contains a widget to render a" \
        "form field as beautiful Imperavi WYSIWYG editor http://redactorjs.com/",
    license="MIT License",
    keywords="django admin widget imperavi",
    platforms=['any'],
    install_requires=[
        "django >= 1.3.0",
        "sorl-thumbnail >= 11.12",
    ],
    url="https://github.com/vasyabigi/django-imperavi",
)
