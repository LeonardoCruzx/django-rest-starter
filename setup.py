
import setuptools

with open('README.md', "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='django-rest-starter',
    version='0.0.16',
    url='https://github.com/LeonardoCruzx/django-rest-starter',
    author='Leonardo Cruz',
    author_email='leonardo.m.cruz0@gmail.com',
    description='Package to start a django with rest',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        
    ],
    python_requires='>=3.7',
)