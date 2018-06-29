from distutils.core import setup

from setuptools import find_packages

REQUIRED_PYTHON = (3, 6, 5)

requirements = ['pytest']

setup(
    name='python project template',
    version='0.1',
    author='Ike Tohru',
    author_email='rokujyouhitomajp@gmail.com',
    url='',
    description='',
    long_description='',
    classifiers=[],
    license='',
    python_requires='>={}.{}.{}'.format(*REQUIRED_PYTHON),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=requirements,
    zip_safe=False,
)
