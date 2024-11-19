from setuptools import setup, find_packages #type : ignore

setup(
    name='flowx_sdk', # The name of your package
    version='0.1', # Version of your package
    packages=find_packages(), # Automatically find all the packages
    install_requires=[ # Dependencies your package needs
        'requests', # Example dependency
    ],
    classifiers=[ # Optional classifiers for PyPI
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.6', # Specify the required Python version
)
