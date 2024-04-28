from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='muhammad-waleed',
    author_email='waleednaveed962@gmail.com',
    install_requires=["langchain","streamlit","pypdf"],
    packages=find_packages()
)