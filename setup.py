from setuptools import setup, find_packages 
  
with open('requirements.txt') as f: 
    requirements = f.readlines()

with open('README.md') as f:
    readme = f.read()

setup( 
        name ='pysparkpackage', 
        version ='0.0.1', 
        author ='Minmin', 
        author_email = 'minmin@xxx.com.vn',
        url = '',
        description ='Demo for pyspark', 
        long_description_content_type ="text/markdown",
        long_description = readme,
        license='MIT', 
        packages=find_packages(), 
        entry_points ={ 
            'console_scripts': [ 
                'hello-world = pysparkpackage.helper.components.hello_world:main',
                'transform = pysparkpackage.transformation.main:main'
            ] 
        }, 
        keywords ='pyspark package whl egg', 
        install_requires = requirements
)

