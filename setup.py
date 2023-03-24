from setuptools import setup, find_packages

setup(
    name='quickquery',
    version='0.1.0',
    description='api',
    author='Miguel Perez',
    author_email='maperez.r93@gmail.com',
    url='https://github.com/maperezrf/api_django.git',
    packages=find_packages(),
    install_requires=[
        'django==3.2',
        'djangorestframework==3.13',
        'django-filter'
    ],
)
