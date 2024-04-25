from setuptools import setup, find_packages

setup(
    name='MetaMorf',
    version='0.1.0',
    description='A high-tech system for data processing, analysis, and modeling.',
    author='John Doe',
    author_email='john.doe@example.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'seaborn',
        'folium',
        'scikit-learn',
        'scipy',
        'tensorflow',
        'keras',
        'pytest',
        'coverage',
        'flake8',
        'black'
    ],
    tests_require=[
        'pytest',
        'coverage',
        'flake8',
        'black'
    ],
    entry_points={
        'console_scripts': [
            'metamorf = meta:main'
        ]
    }
)
