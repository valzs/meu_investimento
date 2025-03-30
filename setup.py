from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setup(
   name='prj_investiment',
   version='0.1.1',
   packages=find_packages(),
   install_requires=[],
   author='Valéria Santos - professor Thiago S Adriano',
   author_email='valeria.souzadsantos@gmail.com',
   description='Uma biblioteca para cálculos de investimentos.',
   url='https://github.com/valzs/meu_investimento.git',
   classifiers=[
       'Programming Language :: Python :: 3',
       'License :: OSI Approved :: MIT License',
       'Operating System :: OS Independent',
   ],
   python_requires='>=3.6',
   long_description=long_description,
   long_description_content_type="text/markdown",
)