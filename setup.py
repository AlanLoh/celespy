from setuptools import setup, find_packages
import skypy

setup(name       = 'skypy',
    packages     = find_packages(),
    include_package_data=True,
    install_requires=['astropy'],
    python_requires='>=3.5',
    scripts      = [],
    version      = skypy.__version__,
    description  = 'NenuFAR Python package',
    url          = 'https://github.com/AlanLoh/skypy.git',
    author       = 'Alan Loh',
    author_email = 'alan.loh@obspm.fr',
    license      = 'MIT',
    zip_safe     = False)

# make the package:
# python3 setup.py sdist bdist_wheel
# upload it:
# python3 -m twine upload dist/*version*

# Release:
# git tag -a v*version* -m "annotation for this release"
# git push origin --tags