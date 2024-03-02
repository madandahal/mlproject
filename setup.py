from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)-> List[str]:

    "THis function will return the list of requirements"
    requirements = []
    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)



setup(

    name = 'mlproject',
    version='0.0.1',
    author='Madan',
    author_email='madandahal2014@gmai.com',
    packages=find_packages(),
    # install_requires=['pandas','numpy','seaborn']
    install_requires = get_requirements('requirements.txt')


)
