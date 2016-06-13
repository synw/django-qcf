from setuptools import setup, find_packages


version = __import__('qcf').__version__

setup(
  name = 'django-qcf',
  packages=find_packages(),
  include_package_data=True,
  version = version,
  description = 'Quick contact form for Django',
  author = 'synw',
  author_email = 'synwe@yahoo.com',
  url = 'https://github.com/synw/django-qcf', 
  download_url = 'https://github.com/synw/django-qcf/releases/tag/'+version, 
  keywords = ['django', 'contact_form'],
  classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
  zip_safe=False
)
