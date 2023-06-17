from setuptools import find_packages, setup

HYPEN_E_DOT = '-e .'


def get_requirement(req_file):
    requirements = []
    with open(req_file) as file_object:
        requirements = file_object.readlines()
        requirements = [req.replace("\n", "") for req in requirements]


        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements


setup(
    name = 'Diamond Price Prediction',
    version = '2.0',
    author = 'Iqbal Hossain Limon',
    author_email = 'Limon.hossain26@gmail.com',
    install_requires = get_requirement('requirements.txt'),
    packages = find_packages()
)