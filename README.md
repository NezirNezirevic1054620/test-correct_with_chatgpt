# Test-Correct met OpenAI integratie

## Installatie en Setup

#### Clone de repository
```git
git clone https://github.com/Rac-Software-Development/wp2-2023-mvc-1e5-nlbl.git
```

#### Maak een Virtual Environment
```python
python -m venv c:\path\to\myenv
```


#### Activeer de Virtual Environment


MacOS:

```zsh
source <venv>/bin/activate
```

Windows:

```bash
<venv>\Scripts\activate.bat
```


#### Installeer alle modules
```python
pip install -r requirements.txt
```

#### Setup .env

Maak een nieuw bestand genaamd .env in de ROOT van de repository

```bash
touch.env
```

Zet dit in de .env

```python
SECRET_KEY="<your_secret_key>"
API_KEY="<your_open_ai_api_key>"
```

#### Run de flask applicatie

```python
python -m flask run
```


## Github Actions

Voor dit project hebben we gebruik gemaakt van github actions die onze code lint, test en format wanneer er wordt gepusht of gemerged naar de main branch.

Black format:

```yml
name: Format with black

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  format:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Format code with black
        run: |
          pip install black
          black .
      - name: Commit changes
        uses: EndBug/add-and-commit@v4
        with:
          author_name: ${{ github.actor }}
          author_email: ${{ github.actor }}@users.noreply.github.com
          message: "Format code with black"
          add: "."
          branch: ${{ github.ref }}
```

Flake8 lint:

```yml
name: Lint with flake8

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

permissions:
  contents: read

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python 3.10
      uses: actions/setup-python@v3
      with:
        python-version: "3.10"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8 pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Lint with flake8
      run: |
        # stop the build if there are Python syntax errors or undefined names
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
```

Test met Pytest:

```yml
name: Test with pytest

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

permissions:
  contents: read

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python 3.10
      uses: actions/setup-python@v3
      with:
        python-version: "3.10"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8 pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Test with pytest
      run: |
        python -m pytest
```


## Bronvermelding

