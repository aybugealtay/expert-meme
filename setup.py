import setuptools

if __name__ == '__main__':
   setuptools.setup(
       name='expert-meme',
       version='0.1.0.dev',
       author='Aybuge Altay',
       author_email='aybugealtay@gmail.com',
       description='tutorial',
       license='Apache 2.0 License',
       url='https://github.com/aybugealtay/expert-meme',

       # Look for python code inside /src/
       packages=setuptools.find_packages(where='src'),

       # Assign the package-level folder ('') to be the one it finds in 'src'
       package_dir={'': 'src'},

       install_requires=[
           'click',
       ],
  )