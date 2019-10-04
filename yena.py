import os
import click
from pathlib import Path

def curate(lst, thing):
        lst = [words.strip() for words in lst.split(',')]
        if thing not in lst:
                lst.append(thing)
        return lst

@click.command()
@click.option('--name', prompt ='Application Name', default ='Ap1',
                help ='The Name of the Application')
@click.option('--version', prompt ='Application Version', default ='1.0',
                help ='The Version of the Application')
@click.option('--pyModules', prompt ='Modules in Application', default ='main',
                help ='The Name of modules to be used by the Application')
@click.option('--requires', prompt ='Packages required (other that click)', default ='Click',
                help ='The Name of the python packages required for this  Application')


def cli(name, version, pyModules, requires):
        """
                                                                              
     _/_/_/  _/  _/            _/          _/_/_/                     
  _/        _/        _/_/_/  _/  _/    _/          _/_/    _/_/_/    
 _/        _/  _/  _/        _/_/      _/  _/_/  _/_/_/_/  _/    _/   
_/        _/  _/  _/        _/  _/    _/    _/  _/        _/    _/    
 _/_/_/  _/  _/    _/_/_/  _/    _/    _/_/_/    _/_/_/  _/    _/     
                                                                      


        Generates Basic Click development Enviornment
   
        
        """
        click.echo(" (1/3) Processing Input Data.. ")
        pyModules = curate(pyModules, 'main')
        requires = curate(requires, 'Click')


        click.echo(" (2/3) Brewing up Files and Directories.. ")
        os.mkdir(name)
        rootfolder = os.getcwd() + '/' + name
        Path(rootfolder + '/setup.py').touch
        for modules in pyModules:
                Path(rootfolder + '/' + modules + '.py').touch


        click.echo(" (3/3) Adding Mints and scripts for smooth development..")
        setup_txt = Path('setup.txt')
        txt = setup_txt.read_text()
        txt = txt.format(name,version,str(pyModules),str(requires),name)
        setup_py = Path(rootfolder + '/setup.py')
        setup_py.write_text(txt)

        click.echo(" Project is Ready!!! ")
        click.echo(" Visit https://click.palletsprojects.com/en/7.x/ for futher help!! ")
        click.echo(" Happy Hacktober!!! ")