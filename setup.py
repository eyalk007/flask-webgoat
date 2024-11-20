from setuptools import setup, find_packages

setup(
    name='your_package_name',  # Replace with your package name
    version='0.1.0',          # Initial version number
    author='Your Name',       # Your name
    author_email='your.email@example.com',  # Your email
    description='A short description of your package',  # Brief description
    long_description=open('README.md').read(),  # Long description (can also use another file)
    long_description_content_type='text/markdown',  # Specify the type of long description
    url='https://github.com/yourusername/your_repository',  # URL to your package's repository
    packages=find_packages(),  # Automatically find packages in the folder
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Specify the license your package falls under
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version required
    install_requires=[
        'click==7.1.2',
        'Flask==1.1.2',
        'itsdangerous==1.1.0',
        'Jinja2==2.11.3',
        'Werkzeug==1.0.1',
        'Django==3.1.7',
        'SQLAlchemy==2.0.36',
        'jeepney==0.8.0',
        'markupsafe==2.1.1',
        'pygithub==1.55',
        'pyjwt==2.4.0',
        'pynacl==1.5.0',
        'pyyaml==6.0.1',
        'secretstorage==3.3.2'
    ],
)
