try:
    from setuptools import setup
except ImportError:
    from distutils import setup

import scrapyjobparameters


packages = [
    'scrapyjobparameters',
]

requires = [
    'scrapy',
]

setup(
    name='scrapyjobparameter',
    version=scrapyjobparameters.__version__,
    description='Scrapy extension to make job_id and project_id available as spider fields.',
    #long_description=open('README.md').read(),
    author='Jean Maynier',
    author_email='jmaynier@kpler.com',
    url='http://github.com/kpler/scrapy-job-parameters-extension',
    packages=packages,
    install_requires=requires,
    #license=open('LICENSE').read(),
    classifiers=(
        'Development Status :: 4 - Beta'
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
    ),
)
