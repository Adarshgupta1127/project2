from setuptools import find_packages , setup
from typing import List


def get_requirements(file_path:str)-> List[str]:
    '''

    this function will return the list of requirements

    '''

    HYPEN_E_Dot= "-e."
    requirements =[]
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]

        if HYPEN_E_Dot in requirements:
            requirements.remove(HYPEN_E_Dot)
    return requirements
setup(
    name = 'project2',
    version='0.0.1',
    author='adarsh',
    author_email = 'adarshgupta1127@gmail.com',
    packages= find_packages(),
    install_requires= get_requirements('requirements.txt')
)