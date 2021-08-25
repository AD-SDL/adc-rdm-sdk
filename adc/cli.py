import os
import json
import typer
from adc.client import ADCClient
from adc.exceptions import ADCError
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


def fetch_and_output_response(client_method, *args):
    try:
        client = get_client()
        response = getattr(client, client_method)(*args)
        typer.echo(json.dumps(response, indent=4))
    except ADCError as e:
        typer.echo(e.error, err=True)


@app.command()
def current_user():
    client_method = 'get_current_user'
    fetch_and_output_response(client_method)


@app.command()
def tokens():
    client_method = 'get_tokens'
    fetch_and_output_response(client_method)


@app.command()
def studies():
    client_method = 'get_studies'
    fetch_and_output_response(client_method)


@app.command()
def study(study_id: str):
    client_method = 'get_study'
    fetch_and_output_response(client_method, study_id)


@app.command()
def investigation(investigation_id: str):
    client_method = 'get_investigation'
    fetch_and_output_response(client_method, investigation_id)


@app.command()
def create_token(name: str):
    client_method = 'create_token'
    fetch_and_output_response(client_method, name)


@app.command()
def delete_token(token_id):
    client_method = 'delete_token'
    fetch_and_output_response(client_method, token_id)


@app.command()
def create_study(
    name: str,
    description: str,
    keywords: List[str] = typer.Option(default=None),
):
    keywords = [] if not keywords else list(keywords)
    client_method = 'create_study'
    fetch_and_output_response(client_method, name, description, keywords)


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
    with open(sample_file_path, 'rb') as file:
        client_method = 'create_sample'
        fetch_and_output_response(client_method, file, study_id, name, keywords, parent_id, source)


@app.command()
def create_investigation(
    study_id: str,
    name: str,
    description: str,
    keywords: List[str] = typer.Option(default=None),
    investigation_type: str = typer.Option(default=None),
):
    client_method = 'create_investigation'
    fetch_and_output_response(client_method, study_id, name, description, keywords, investigation_type)


@app.command()
def set_permissions(study_id: str, user_id: str, permission_level: str):
    client_method = 'set_permissions'
    fetch_and_output_response(client_method, study_id, user_id, permission_level)


@app.command()
def remove_permissions(study_id: str, user_id: str):
    client_method = 'remove_permissions'
    fetch_and_output_response(client_method, study_id, user_id)


@app.command()
def subscribe_to_study(study_id):
    client = get_client()
    client.subscribe_to_study(
        study_id, lambda notification: typer.echo(json.dumps(notification, indent=4))
    )
