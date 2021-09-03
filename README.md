# Argonne Discovery Cloud SDK & CLI

## Installation

* When positioned in this repo's root directory:
```
pip install .
```

* with poetry:
```
poetry install
```

## Commands
```
adc create-datafile
adc create-investigation
adc create-job
adc create-sample
adc create-study
adc create-token
adc current-user
adc datafile
adc delete-token
adc investigation
adc job
adc remove-permissions
adc sample
adc set-permissions
adc studies
adc study
adc subscribe-to-investigation
adc subscribe-to-job
adc subscribe-to-study
adc tokens
adc update-job
```
You can run `adc <command> --help` for more information.

## Development
We are using [poetry](https://python-poetry.org/) to package this code.

Use `poetry add <package name>` to add new dependencies to the repo.
