from setuptools import find_packages, setup
from typing import List

hyphen_e_dot = "-e ."
def get_requirements(file_path:str)->List[str]:
    """
        This function will return the list of requirements.
    """
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [ requirement.replace("\n", "") for requirement in requirements]
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    
    return requirements



setup(name="mlproject",
      version="0.0.1",
      author="Nilesh Dhakane",
      author_email="nilesh.dhakane93@gmail.com",
      packages=find_packages(),
      install_requires=get_requirements("requirements.txt")
      )