import setuptools
with open('README.md','r',encoding='utf-8') as f:
    long_description=f.read()

__version__='0.0.0'
REPO_NAME='text_summariser'
AUTHOR_NAME='Anish Deepak'
SRC_REPO='text_summariser'
AUTHOR_EMAIL='anishdeepak34@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    long_description=long_description,
    long_description_content='text/markdown',
    url=f'https://github.com/AnishDeepak/text_summariser'
)