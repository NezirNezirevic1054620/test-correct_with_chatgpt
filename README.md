# Test-Correct met OpenAI integratie

## Introductie

We moesten voor ons werkplaats project een applicatie bouwen waarmee je notities kan aanmaken en vragen kan genereren van de notitie

## Showcase

#### Login
![Screenshot 2024-01-12 at 21-18-33 Title](https://github.com/Rac-Software-Development/wp2-2023-mvc-1e5-nlbl/assets/124694040/4b993c42-39db-49a7-b799-72e1bd1bbc5a)

#### Notities
![Screenshot 2024-01-12 at 21-19-24 Title](https://github.com/Rac-Software-Development/wp2-2023-mvc-1e5-nlbl/assets/124694040/6829e456-8be7-43a7-b4a2-4fe42e96ea41)

#### Vraag genereren
![Screenshot 2024-01-12 at 21-20-03 Title](https://github.com/Rac-Software-Development/wp2-2023-mvc-1e5-nlbl/assets/124694040/789f29b8-d23e-43d7-92c6-c3e95cec3ff0)

#### Categorieen
![Screenshot 2024-01-12 at 21-20-21 Title](https://github.com/Rac-Software-Development/wp2-2023-mvc-1e5-nlbl/assets/124694040/d930b6b7-1b75-4512-8a13-5a807521269d)

#### Leraren/Admins
![Screenshot 2024-01-12 at 21-20-57 Title](https://github.com/Rac-Software-Development/wp2-2023-mvc-1e5-nlbl/assets/124694040/3b645cba-6b64-4f6b-b05f-ea6f904e4924)

#### Vragen
![Screenshot 2024-01-12 at 21-21-26 Title](https://github.com/Rac-Software-Development/wp2-2023-mvc-1e5-nlbl/assets/124694040/48999e17-d6ba-4a80-bab3-1e3448384be8)

#### Profiel
![Screenshot 2024-01-12 at 21-22-16 Title](https://github.com/Rac-Software-Development/wp2-2023-mvc-1e5-nlbl/assets/124694040/70d964eb-c649-484f-afab-2156aebb5476)



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

#### Login

username: nezirnezirevic
password: nezirnezirevic


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

Pylint lint:

```yml
name: Lint with pylint

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
        pip install pylint
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Lint with pylint
      run: |
        pylint $(git ls-files '*.py')
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

Flask Bcrypt Docs. (n.d.). Flask-bcrypt — flask-bcrypt 1.0.1 documentation. Flask-Bcrypt — Flask-Bcrypt 1.0.1 documentation. https://flask-bcrypt.readthedocs.io/en/1.0.1/

Flask WTF Docs. (n.d.). Flask-WTF — Flask-WTF documentation (1.2.x). Flask-WTF — Flask-WTF Documentation (1.2.x). https://flask-wtf.readthedocs.io/en/1.2.x/

GeeksForGeeks. (n.d.). GeeksforGeeks. https://www.geeksforgeeks.org/

Github Actions Documentation. (n.d.). GitHub actions documentation. GitHub Docs. https://docs.github.com/en/actions

Github. (n.d.). GitHub. https://github.com/

Grinberg, M. (2018). Flask web development: Developing web applications with Python (1st ed.). O'Reilly Media.

Official Flask Docs Website. (n.d.). Welcome to flask — Flask documentation (3.0.x). Welcome to Flask — Flask Documentation (3.0.x). https://flask.palletsprojects.com/en/3.0.x/

Solomon, F., Jayaram, P., & Saqqa, A. A. (2019). The SQL workshop. Packt.

StackOverflow. (n.d.). Stack Overflow. https://stackoverflow.com/
