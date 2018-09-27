with open("topdf/version.py") as fp:
    code = compile(fp.read(), "topdf/version.py", 'exec')
    exec(code)

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='topdf',
    packages=['topdf'],
    version=__VERSION__,
    description='topdf allows you to convert anything to a beautiful PDF.',
    long_description=open('Readme.rst').read(),
    url='https://github.com/dufferzafar/topdf',
    license='MIT',
    author='Shadab Zafar',
    author_email='dufferzafar0@gmail.com',
    install_requires=[
        'docopt',
        'pypandoc',
        'requests',
    ],
    scripts=[
        'bin/topdf',
    ],
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
)
