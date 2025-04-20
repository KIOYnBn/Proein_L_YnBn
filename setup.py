from setuptools import setup, find_packages
from pkg_resources import parse_requirements

with open("requirements.txt", encoding="utf-8") as fp:
	install_requires = [str(requirement) for requirement in parse_requirements(fp)]

long_description = """
Until 2025-4-20, just acheived these functions
Model:bert_mask, print_tfreocrd, token, TFInputDataset
Data:read fasta, ELECTRA fragment, slice train and eval
"""

setup(
	name="Protein_L_YnBn",
	version="0.0.1",
	author="YnBn",
	author_email="twb72743075@126.com",
	description="some functions used frequently in protein deep learn model",
	long_description=long_description,
	license="MIT License",
	url="https://github.com/KIOYnBn/Proein_L_YnBn",
	
	classifiers=[
		"Development Status :: 3 - Alpha",
		"Intended Audience :: me",
		"Topic :: Software Development :: Deep Learn Model Tools",
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: All",
	],
	
	packages=find_packages(exclude='tests.'),
	install_requires=install_requires,
	entry_points={
		'console_scripts': [
			'test = test.help:main'
		]
	})
