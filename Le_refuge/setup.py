"""
Configuration du package refuge.
"""

from setuptools import setup, find_packages

setup(
    name="refuge",
    version="0.1.0",
    description="Un espace poétique où les cycles naturels et émotionnels s'entremêlent",
    author="Le Refuge",
    packages=find_packages(),
    install_requires=[
        "python-dateutil>=2.8.2",
        "typing-extensions>=4.0.0"
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
) 