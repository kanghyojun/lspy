from setuptools import setup, find_packages


install_requires = [
    'click == 3.3'
]

test_require = [
    'pytest == 2.6.4',
]

docs_require = [
    'sphinx == 1.2.3',
]

setup(
    name='lspy',
    version='0.0.1',
    author='Kang Hyojun',
    author_email='admire9@gmail.com',
    packages=find_packages(),
    install_requires=install_requires,
    tests_require=test_require,
    extras_require={
        'docs': docs_require,
        'tests': test_require
    },
    entry_points='''
        [console_scripts]
        lspy = lspy.cli:cli
    '''
)
