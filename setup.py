from setuptools import setup, find_packages

HYPEN_E_DOT = "-e ."

def get_requirements():
    with open("requirements.txt", "r") as f:
        requirements = f.read().splitlines()
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="subscription_churn_ml_system",
    version="0.0.1",
    author="Riyan Ozair",
    packages=find_packages(),
    install_requires=get_requirements()
)