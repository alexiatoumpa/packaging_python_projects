from setuptools import setup, find_packages

setup(
	name = "myproject",
	version = "1.0",
	description = "An example Python package.",
	packages = ["myproject", "myproject/pack1", "myproject/pack2"],
	install_requires = ["setuptools>=61.0",
	],
	classifiers = [
			"Programming Language :: Python :: 3",
			"License :: OSI Approved :: MIT License",
	],
)
