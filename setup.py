from setuptools import setup, find_packages


setup(
    name='django-tls',
    version='0.0.3',
    description='Stores the current request in Thread Local Storage using Werkzeug',
    long_description=open('README.rst').read(),
    author='Roland van Laar',
    author_email='roland@micite.net',
    license='BSD',
    url='https://github.com/rvanlaar/django-tls',
    packages=find_packages(),
    install_requires=[ 'Werkzeug>=0.6.2' ],
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Framework :: Django',
    ],
)

