from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ebooks/__init__.py
from ebooks import __version__ as version

setup(
	name="ebooks",
	version=version,
	description="PDFs",
	author="Saba Fdal",
	author_email="sabafadl.rowad@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
