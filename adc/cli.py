import os
import json
import typer
from adc.client import ADCClient
from typing import List

app = typer.Typer()


@app.callback()
def callback():
    """
    Argonne Discovery Cloud CLI
    """


def get_token_from_env():
    try:
        return os.environ["ADC_ACCESS_TOKEN"]
    except KeyError:
        message = "You need to set ADC_ACCESS_TOKEN environment variable before you can interact with ADC API"
        typer.echo(message, err=True)
        raise typer.Exit()


def get_client():
    token = get_token_from_env()
    return ADCClient(token)


def print_response(response):
    typer.echo(json.dumps(response, indent=4))


@app.command()
def current_user():
    client = get_client()
    response = client.get_current_user()
    print_response(response)


@app.command()
def tokens():
    client = get_client()
    response = client.get_tokens()
    print_response(response)


@app.command()
def studies():
    client = get_client()
    response = client.get_studies()
    print_response(response)


@app.command()
def study(study_id: str):
    client = get_client()
    response = client.get_study(study_id)
    print_response(response)


@app.command()
def investigation(investigation_id: str):
    client = get_client()
    response = client.get_investigation(investigation_id)
    print_response(response)


@app.command()
def create_token(name: str):
    client = get_client()
    response = client.create_token(name)
    print_response(response)


@app.command()
def delete_token(token_id):
    client = get_client()
    response = client.delete_token(token_id)
    print_response(response)


@app.command()
def create_study(
    name: str,
    description: str,
    keywords: List[str] = typer.Option(default=None),
):
    keywords = [] if not keywords else list(keywords)
    client = get_client()
    response = client.create_study(name, description, keywords)
    print_response(response)


@app.command()
def create_sample(
    sample_file_path: str,
    study_id: str,
    name: str,
    keywords: List[str] = typer.Option(default=None),
    parent_id: str = typer.Option(default=None),
    source: str = typer.Option(default=None),
):
    if not os.path.isfile(sample_file_path):
        typer.echo("Invalid sample file path", err=True)
    keywords = [] if not keywords else list(keywords)
    client = get_client()
    with open(sample_file_path) as file:
        response = client.create_sample(
            file, study_id, name, keywords, parent_id, source
        )
    print_response(response)


@app.command()
def create_investigation(
    study_id: str,
    name: str,
    description: str,
    keywords: List[str] = typer.Option(default=None),
    investigation_type: str = typer.Option(default=None),
):
    client = get_client()
    response = client.create_investigation(
        study_id, name, description, keywords, investigation_type
    )
    print_response(response)


@app.command()
def set_permissions(study_id: str, user_id: str, permission_level: str):
    client = get_client()
    response = client.set_permissions(study_id, user_id, permission_level)
    print_response(response)


@app.command()
def remove_permissions(study_id: str, user_id: str):
    client = get_client()
    response = client.remove_permissions(study_id, user_id)
    print_response(response)


@app.command()
def subscribe_to_study(study_id):
    client = get_client()
    client.subscribe_to_study(
        study_id, lambda notification: print_response(notification)
    )
