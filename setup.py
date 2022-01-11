from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in manufacturing_overview/__init__.py
from manufacturing_overview import __version__ as version

setup(
	name="manufacturing_overview",
	version=version,
	description="Dashboard Overview for Sales Orders Items to be manufactured",
	author="CAnetzberger Design",
	author_email="admin@canetzberger.design",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
