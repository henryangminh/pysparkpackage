from setuptools import setup, find_packages 
  
with open('requirements.txt') as f: 
    requirements = f.readlines()

setup( 
        name ='pysparkpackage', 
        version ='0.0.1', 
        author ='Minmin', 
        # url ='https://github.com/Vibhu-Agarwal/vibhu4gfg', 
        description ='Demo for pyspark', 
        long_description_content_type ="text/markdown", 
        license='MIT', 
        packages=find_packages(), 
        entry_points ={ 
            'console_scripts': [ 
                'hello-world = pysparkpackage.helper.hello_world.components:main',
                'transform = pysparkpackage.transformation.main:main'
            ] 
        }, 
        keywords ='pyspark package whl egg', 
        install_requires = requirements, 
        zip_safe = False
)