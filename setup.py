import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__="0.0.0"

REPO_NAME = "Chicken_disease_classification"
AUTHOR_USER_NAME = "chenkham"
SRC_REPO = "Chicken_disease_classification"
AUTHOR_EMAIL = "chenkhamchowlu@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description = "python package for Chicken_disease_classification",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}.git",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}.issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)