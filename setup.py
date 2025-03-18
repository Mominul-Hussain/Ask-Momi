from setuptools import setup, find_packages

setup(
    name='momi-cli',
    version='0.1.0',
    author='Mominul Hussain',
    author_email='hussainmominul786@gmail.com',
    description='A CLI tool to interact with AI powered',
    packages=find_packages(exclude=['tests']),  
    install_requires=[
        'requests',  # For making API calls
        'python-dotenv'  # For loading environment variables
    ],
    entry_points={
        'console_scripts': [
            'momi=momi.cli:main',  # Entry point for the CLI
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)