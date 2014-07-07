from setuptools import setup
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

version = "1.0b2-dev"

install_requires = [
    'PyYAML',
    'jinja2',
    'setuptools',
    'ploy>=1.0rc11',
    'ploy_ansible>=1.0b6',
    'ploy_ezjail>=1.0b8',
    'ploy_fabric>=1.0b4',
    'ploy_virtualbox>=1.0b2',
]

# workaround for installing via buildout, as ansible
# violates its sandbox limitations
try:
    import ansible  # noqa
except ImportError:
    install_requires.append('ansible')


setup(
    version=version,
    description="A tool to provision, configure and maintain FreeBSD jails",
    name="bsdploy",
    author='Tom Lazar',
    author_email='tom@tomster.org',
    url='http://github.com/ployground/bsdploy',
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'Operating System :: POSIX :: BSD :: FreeBSD',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2 :: Only',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Systems Administration',
    ],
    license='Beerware Licence',
    zip_safe=False,
    packages=['bsdploy'],
    install_requires=install_requires,
    extras_require={
        'development': [
            'Sphinx',
            'repoze.sphinx.autointerface',
            'coverage',
            'jarn.mkrelease',
            'pytest >= 2.4.2',
            'pytest-flakes',
            'pytest-pep8',
            'tox',
            'mock',
        ],
    },
    entry_points="""
        [console_scripts]
        ploy = ploy:ploy
        ploy-ssh = ploy:ploy_ssh
        ploy-download = bsdploy.download:run
        [ansible_paths]
        bsdploy = bsdploy:ansible_paths
        [ploy.plugins]
        bsdploy = bsdploy:plugin
    """)
