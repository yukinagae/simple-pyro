import codecs

from setuptools import find_packages, setup


install_requires = [
    'pyro-ppl',
]

test_requires = [
    'pytest',
]

setup(
    name='simple-pyro',
    version='0.0.1',
    description='A thin wrapper for Pyro - probabilistic modeling and inference',
    long_description=codecs.open('README.md', 'r', encoding='utf-8').read(),
    url='https://github.com/yukinagae',
    author='Yuki Nagae',
    author_email='yuki.nagae1130@gmail.com',
    keywords='machine learning statistics probabilistic programming bayesian modeling pyro pytorch',
    license='MIT License',
    packages=find_packages(),
    install_requires=install_requires,
    test_requires=test_requires,
)
