from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='slitscan',
      version='0.2.1',
      description='Slit-scan photography.',
      url='http://github.com/markjarzynski/slitscan',
      author='Mark Jarzynski',
      author_email='mark.jarzynski@gmail.com',
      license='MIT',
      packages=['slitscan'],
      install_requires=[
          'numpy',
          'imageio'
      ],
      entry_points={
          'console_scripts': ['slitscan=slitscan.__main__:main'],
      },
      zip_safe=False)
