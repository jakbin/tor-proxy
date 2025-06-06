from setuptools import setup
from tor_proxy import __version__

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="tor-proxy",
    version=__version__,
    author="Jak Bin",
    description="A simple way to send your requests with tor using tor-proxy.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/jakbin/tor-proxy",
    project_urls={
    'Bug Tracker': 'https://github.com/jakbin/tor-proxy/issues',
    },
    license="MIT License",
    classifiers=[
        'Development Status :: 4 - Beta',
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='flask, tor, onion, stem, proxy, tor-proxy',
    python_requires=">=3",
    packages=['tor_proxy'],
    package_data={  
        'tor_proxy': [
            'torrc_template',
            'torrc_template-windows'
        ]},
    install_requires=['stem'],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'tor-proxy=tor_proxy.__main__:main',
        ],
    },
)
