#!/usr/bin/env python3
"""
Setup moderne pour le Refuge - Architecture Temple
"""

from setuptools import setup, find_packages
from pathlib import Path

# Lire le README
readme_path = Path(__file__).parent / "README.md"
long_description = readme_path.read_text(encoding='utf-8') if readme_path.exists() else ""

# Lire les requirements
requirements_path = Path(__file__).parent / "requirements.txt"
requirements = []
if requirements_path.exists():
    requirements = requirements_path.read_text(encoding='utf-8').strip().split('\n')
    requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#')]

setup(
    name="le-refuge",
    version="2.0.0",
    description="Refuge Poétique - Architecture Temple Moderne",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Laurent Franssen & Ælya",
    author_email="contact@le-refuge.fr",
    url="https://github.com/le-refuge/le-refuge",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'refuge=main:cli',
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Artistic Software",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="refuge, poésie, spiritualité, temple, architecture",
    project_urls={
        "Bug Reports": "https://github.com/le-refuge/le-refuge/issues",
        "Source": "https://github.com/le-refuge/le-refuge",
        "Documentation": "https://le-refuge.readthedocs.io/",
    },
)
