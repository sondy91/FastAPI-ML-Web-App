Commands to get this working

Check your python version
py --version

created a virtual environment
py -m venv env3.10

Activate the virutal environment
& './env3.10/Scripts/activate.bat'

Upgrade pip
py -m pip install --upgrade pip

Install requirements
Dev requirements
mypy
ruff
black
ipykernel

Regular Requirements
fastapi[all]
diffusers==0.8.0
transformers
scipy
ftfy
