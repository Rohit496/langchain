# Option 1: Visible directory

python -m venv venv
source venv/bin/activate # Activation

# Option 2: Hidden directory

python -m venv .venv
source .venv/bin/activate # Activation

# Deactivation

deactivate

# Remove virtual environment

rm -rf venv

# or

rm -rf .venv

# Install packages

pip install package_name

# List installed packages

pip list

# Freeze installed packages to a requirements file

pip freeze > requirements.txt

# Install packages from a requirements file

pip install -r requirements.txt

# Upgrade pip

pip install --upgrade pip

# Check Python version

python --version

# Check pip version

pip --version

# Check virtual environment location

which python
which pip
