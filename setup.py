from setuptools import setup, find_packages

setup(
    name="py_mlh_scrapy",
    version="0.1",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=[
        'scrapy_redis==0.6.8',
        'setuptools==37.0.0',
        'pymongo==3.4.0',
        'Twisted==17.9.0',
        'Scrapy==1.4.0',
        'oss2==2.3.0',
        'pyOpenSSL==17.3.0'
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
    url="http://www.mlhang.com",  # project home page, if any

    entry_points={'scrapy': ['settings = py_mlh_scrapy.settings']},
)
