#!/usr/bin/env python

from setuptools import setup
from setuptools.command.install import install as _install

class install(_install):
    def pre_install_script(self):
        pass

    def post_install_script(self):
        pass

    def run(self):
        self.pre_install_script()

        _install.run(self)

        self.post_install_script()

if __name__ == '__main__':
    setup(
        name = 'inova-proxy',
        version = '0.0.1',
        description = 'Centro Paula Souza - Inova - CNPq Proxy Server',
        long_description = 'Log service module created to integrate the CPS WebServices with the CNPq WebServices as a proxy',
        author = 'Lucas Nadalete, Eduardo Sakaue',
        author_email = 'lucas.nadalete@fatec.sp.gov.br, eduardo.sakaue@fatec.sp.gov.br',
        license = 'Python Software Foundation License (PSFL)',
        url = '',
        scripts = [],
        packages = ['controller'],
        namespace_packages = [],
        py_modules = [
            'webapp',
            '__init__',
            'helloworld'
        ],
        classifiers = [
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python'
        ],
        entry_points = {},
        data_files = [],
        package_data = {},
        install_requires = [
            'aniso8601==3.0.2',
            'certifi==2018.4.16',
            'chardet==3.0.4',
            'click==6.7',
            'coverage==5.0a1',
            'flake8==3.5.0',
            'Flask==1.0.2',
            'Flask-RESTful==0.3.6',
            'idna==2.7',
            'itsdangerous==0.24',
            'Jinja2==2.10',
            'MarkupSafe==1.0',
            'mccabe==0.6.1',
            'mockito==1.1.0',
            'pkginfo==1.4.2',
            'pybuilder==0.11.17',
            'pycodestyle==2.4.0',
            'pyflakes==2.0.0',
            'pypandoc==1.4',
            'pytz==2018.5',
            'requests==2.19.1',
            'requests-toolbelt==0.8.0',
            'six==1.11.0',
            'tailer==0.4.1',
            'tblib==1.3.2',
            'tqdm==4.24.0',
            'twine==1.11.0',
            'unittest-xml-reporting==2.2.0',
            'urllib3==1.23',
            'Werkzeug==0.14.1'
        ],
        dependency_links = [],
        zip_safe = True,
        cmdclass = {'install': install},
        keywords = 'cps inova log',
        python_requires = '',
        obsoletes = [],
    )
