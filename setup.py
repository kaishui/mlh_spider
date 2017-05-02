from setuptools import setup, find_packages

setup(
    name="py_mlh_scrapy",
    version="0.1",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=[
        'Scrapy>=1.3.3',
        'pymongo==3.4.0',
        'oss2==2.3.0',
        'scrapy_redis==0.6.8',
        'Twisted==17.1.0',
        'pymongo==3.4.0',
        'six==1.10.0',
        'setuptools==20.7.0'
    ],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
        # 'hello': ['*.msg'],
    },

    # metadata for upload to PyPI
    author="kaishui",
    author_email="fengzt@fengzt.com",
    description="爬虫项目",
    license="MIT",
    keywords="爬虫",
    url="http://www.mahoooo.com",  # project home page, if any

    entry_points={'scrapy': ['settings = py_mlh_scrapy.settings']},
)
