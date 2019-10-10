import os
import click
from pathlib import Path

def curate(lst, thing):
        lst = [words.strip() for words in lst.split(',')]
        if thing not in lst:
                lst.append(thing)
        return lst


intro_txt ="""
     _/_/_/  _/  _/            _/          _/_/_/                     
 _/        _/        _/_/_/  _/  _/    _/          _/_/    _/_/_/    
_/        _/  _/  _/        _/_/      _/  _/_/  _/_/_/_/  _/    _/   
_/        _/  _/  _/        _/  _/    _/    _/  _/        _/    _/    
 _/_/_/  _/  _/    _/_/_/  _/    _/    _/_/_/    _/_/_/  _/    _/    
-----------------------------------------------------------------

Click is a Python package for creating beautiful command line interfaces
in a composable way with as little code as necessary. It's the "Command
Line Interface Creation Kit". It's highly configurable but comes with 
sensible defaults out of the box.

ClickGen is a Command line Application that helps in curating a Click
development directory/enviornment. 
                
                
                
                """
click.echo(intro_txt)
@click.command()

@click.option('--name', prompt ='Application Name', default ='Ap1',
                help ='The Name of the Application')
@click.option('--version', prompt ='Application Version', default ='1.0',
                help ='The Version of the Application')
@click.option('--pymods', prompt ='Modules in Application', default ='main',
                help ='The Name of modules to be used by the Application')
@click.option('--requires', prompt ='Packages required (other that click)', default ='Click',
                help ='The Name of the python packages required for this  Application')
def cli(name, version, pymods, requires):
        """
        Generates Basic Click development Enviornment
        ----------------------------------------------
        
        """
        
        click.echo(" (1/3) Processing Input Data.. ")
        pymods = curate(pymods, 'main')
        requires = curate(requires, 'Click')


        click.echo(" (2/3) Brewing up Files and Directories.. ")
        rootfolder = os.getcwd() + '/' + name
        if Path(rootfolder).is_dir():
                click.echo('The directory named {} is already there!!'.format(name))
        else:
                os.mkdir(name)
        
        if Path(rootfolder+'/setup.py').is_file():
                click.echo('setup.py is already there!!')
        else:
                Path(rootfolder + '/setup.py').touch()
        for modules in pymods:
                if Path(rootfolder + '/' + modules + '.py').is_file():
                        click.echo('{}.py is already there!!'.format(modules))
                else:
                        Path(rootfolder + '/' + modules + '.py').touch()


        click.echo(" (3/3) Adding Mints and scripts for smooth development..")
        set
        txt =   """
from setuptools import setup

setup(
        name={},
        version={},
        py_modules={},
        install_requires={},
        entry_points='''
        [console_scripts]
        {}=main:cli
        '''
)

                """
        main_txt = '''
import click

@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name",
              help="The person to greet.")
def cli(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo("Hello, %s!" % name)
                '''

        txt = txt.format(str(name),str(version),str(pymods),str(requires),str(name))
        setup_py = Path(rootfolder + '/setup.py')
        setup_py.write_text(txt)
        Path(rootfolder + '/main.py').write_text(main_txt)

        
        click.echo(" Project is Ready!!! ")
        click.echo(" Visit https://click.palletsprojects.com/en/7.x/ for futher help!! ")
        click.echo(" Happy Hacktober!!! ")