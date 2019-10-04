from setuptools import setup

setup(
	name='clickgen',
	version='0.1',
	py_modules=['yena'],
	install_requires=[
		'Click',
	],
	entry_points='''
		[console_scripts]
		clickgen=yena:cli
	'''
)
