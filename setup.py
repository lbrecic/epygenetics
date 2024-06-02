from setuptools import setup, find_packages

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
        "numpy",
        "pandas",
        "scikit-learn",
        "pyreadr"
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)
