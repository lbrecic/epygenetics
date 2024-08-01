from setuptools import find_packages, setup

setup(
    name='epygenetics',
    version='0.0.0',
    packages=find_packages(),
    description='',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Luka Brečić',
    author_email='luka.brecic3@gmail.com',
    url='https://github.com/lbrecic/epygenetics',
    install_requires=[
        # List your package dependencies here
        "setuptools",
        "numpy",
        "pandas",
        "pandas-stubs",
        "pyreadr",
        "scipy",
        "mypy",
        "flake8",
        "isort",
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
    entry_points={
        'console_scripts': [
            'epygenetics = epygenetics.main:main',
            'analysis = epygenetics.analysis:main',
        ],
    },
)
