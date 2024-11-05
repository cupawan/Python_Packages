from setuptools import setup, find_packages

setup(
    name='cu_packages',
    version='0.1',                  
    packages=find_packages(),
    install_requires=[
        'PyYAML','garminconnect', 'pytz', 'requests','stravalib', 'pandas', 'googlemaps', 'tabulate', 'folium', 'polyline'
    ],
    author='Pawan Kumar',
    author_email='pavan11896@gmail.com',
    description='',
    url='',
)
