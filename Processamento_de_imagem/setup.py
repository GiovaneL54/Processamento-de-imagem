from setuptools import setup, find_packages

setup(
    name='image-processing',
    version='0.1.0',
    author='Seu Nome',
    author_email='seuemail@example.com',
    description='Um pacote simples para processamento de imagens.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'Pillow',  # Dependência para processamento de imagens
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)