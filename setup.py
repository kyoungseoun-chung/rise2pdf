import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='rise2pdf', # Replace with your own username
    version='0.0.1',
    author='Kyoungseoun Chung',
    author_email='kchung@student.ethz.ch',
    description='Convert RISE slides to PDF using decktape',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kyoungseoun-chung/rise2pdf',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
