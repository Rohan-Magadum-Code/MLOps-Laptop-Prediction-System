from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "MLOps-Laptop-Prediction-System"
AUTHOR_NAME = "Rohan-Magadum-Code"
SRC_PROJECT = "Laptop_Price_Prediction_System"
AUTHOR_EMAIL = "rohanmagadum2004@gmail.com"

setup(
    version=__version__,
    name=SRC_PROJECT,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Bug_tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=find_packages(where="src")
)