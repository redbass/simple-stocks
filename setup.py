from distutils.core import setup

setup(
    name='Stock service',
    description = 'Stock service',
    packages=['stock_service'],
    version='1',
    author='Luca Gallici',
    author_email='luca.gallici@gmail.com',
    script_name='./build/setup.py',
    data_files=['./build/setup.py']
)
