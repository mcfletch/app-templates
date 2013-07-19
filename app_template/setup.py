import os

from setuptools import setup, find_packages
version = [
    (line.split('=')[1]).strip().strip('"').strip("'")
    for line in open(os.path.join('{{app_name}}','version.py'))
    if line.startswith( '__version__' )
][0]

if __name__ == "__main__":
    setup(
        name='{{app_name}}',
        version='1.0.0',
        description='{{app_name}}',
        long_description='{{app_name}}',
        classifiers=[
            "Programming Language :: Python",
            "Framework :: Django",
            "Topic :: Internet :: WWW/HTTP",
            "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
        author='VRPlumber Consulting Inc.',
        author_email='mcfletch@vrplumber.com',
        url='http://www.vrplumber.com/programming/project/{{app_name}}',
        keywords='django',
        packages=find_packages(),
        include_package_data=True,
        license='Commercial',
        # Dev-only requirements:
        # nose
        # pychecker
        # coverage
        # globalsub
        package_data = {
            '{{app_name}}': [
                'templates/{{app_name}}/*.html',
                'static/js/*',
                'static/css/*',
                'static/img/*',
            ],
        },
        install_requires=[
            'django',
            'django-annoying',
            'south',
        ],
        scripts = [
        ],
        entry_points = dict(
            console_scripts = [
            ],
        ),
    )

