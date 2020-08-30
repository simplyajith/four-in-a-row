# Four in a row game -Python

Designed Four in a row game, played from command terminal using Python

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
git
python3
python3 in system path
pip3

```

### Installation

##Mac OS 
```
git clone https://github.com/simplyajith/four-in-a-row.git
cd four-in-a-row/
pip install virtualenv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt 
python play_game.py

```

##Windows

```
git clone https://github.com/simplyajith/four-in-a-row.git
cd four-in-a-row/
pip install virtualenv
python -m venv venv
cd venv/Scripts
activate

#After activating the virtual environment. go back to four-in-a-row folder.
cd four-in-a-row/
pip install -r requirements.txt
python play_game.py
```


## Test results
In four-in-a-row folder, run the below command

```
pytest -m smoke -v -s --html=results/report.html  --self-contained-html
```
HTML output will be present in the results folder.

## Built With

* [Python3](https://www.python.org/download/releases/3.0/) - Language used


## Authors

* **Ajith Sundararaj** - *Initial work* - [simplyajith](https://github.com/simplyajith)

