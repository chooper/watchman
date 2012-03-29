from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='Watchman',
      version=version,
      description="Framework to monitor a [generic] value and trigger actions based on that value.",
      long_description="""\
Edit""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='ZIP',
      author='Charles Hooper',
      author_email='chooper@plumata.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
