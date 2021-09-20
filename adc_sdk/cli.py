import os
import json
import typer
from datetime import datetime
from adc_sdk.client import ADCClient
from adc_sdk.exceptions import ADCError
from typing import List

app = typer.Typer()


@app.callback()
def adc():
    """
    Argonne Discovery Cloud CLI
    """


def get_token_from_env():
    """
    Fetch and returns ADC_ACCESS_TOKEN env var.
    Outputs error if it is not present.
    """
    try:
        return os.environ["ADC_ACCESS_TOKEN"]
    except KeyError:
        message = "You need to set ADC_ACCESS_TOKEN environment variable before you can interact with ADC API"
        typer.echo(message, err=True)
        raise typer.Exit()


def get_client() -> ADCClient:
    """
    Return an instance of ADCClient using the ADC_ACCESS_TOKEN env var.
    """
    token = get_token_from_env()
    return ADCClient(token)


def print_to_stdout(content: dict):
    typer.echo(json.dumps(content, indent=4))


def fetch_and_output_response(client_method, *args):
    try:
        client = get_client()
        response = getattr(client, client_method)(*args)
        print_to_stdout(response)
    except ADCError as e:
        typer.echo(e.error, err=True)


@app.command()
def current_user():
    """
    Fetch current user's information.
    """
    client_method = 'get_current_user'
    fetch_and_output_response(client_method)


@app.command()
def tokens():
    """
    List current user's available API tokens.
    """
    client_method = 'get_tokens'
    fetch_and_output_response(client_method)


@app.command()
def studies():
    """
    List studies available to the current user.
    """
    client_method = 'get_studies'
    fetch_and_output_response(client_method)


@app.command()
def study(study_id: str):
    """
    Get details of a specific study.
    """
    client_method = 'get_study'
    fetch_and_output_response(client_method, study_id)


@app.command()
def investigation(investigation_id: str):
    """
    Get details of a specific investigation.
    """
    client_method = 'get_investigation'
    fetch_and_output_response(client_method, investigation_id)


@app.command()
def job(job_id: str):
    """
    Get details of a specific job.
    """
    client_method = 'get_job'
    fetch_and_output_response(client_method, job_id)


@app.command()
def datafile(datafile_id: str):
    """
    Get details of a specific datafile.
    """
    client_method = 'get_datafile'
    fetch_and_output_response(client_method, datafile_id)


@app.command()
def sample(sample_id: str):
    """
    Get details of a specific sample.
    """
    client_method = 'get_sample'
    fetch_and_output_response(client_method, sample_id)


@app.command()
def create_token(name: str):
    """
    Create a new token for the current user.
    """
    client_method = 'create_token'
    fetch_and_output_response(client_method, name)


@app.command()
def delete_token(token_id: str):
    """
    Delete a specific token from the current user's available tokens.
    """
    client_method = 'delete_token'
    fetch_and_output_response(client_method, token_id)


@app.command()
def create_study(
    name: str,
    description: str,
    keywords: List[str] = typer.Option(default=None),
):
    """
    Create a new Study, current user will be the owner and will have admin permissions.
    """
    keywords = [] if not keywords else [k for k in keywords[0].split(' ')]
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
    """
    Create a Sample under the specified Study to (possibly) be used as input for a Job to generate Datafiles.
    Triggers notifications for Study subscriptors.
    """
    if not os.path.isfile(sample_file_path):
        typer.echo("Invalid sample file path", err=True)
    keywords = [] if not keywords else [k for k in keywords[0].split(' ')]
    with open(sample_file_path, 'rb') as file:
        client_method = 'create_sample'
        fetch_and_output_response(client_method, file, study_id, name, keywords, parent_id, source)


@app.command()
def create_datafile(
    file_path: str,
    job_id: str,
    name: str,
    description: str = typer.Option(default=None),
    source: str = typer.Option(default=None),
):
    """
    Create a Datafile that will be considered as a result file from the specified Job
    Triggers notifications for Job subscriptors.
    """
    if not os.path.isfile(file_path):
        typer.echo("Invalid sample file path", err=True)
    with open(file_path, 'rb') as file:
        client_method = 'create_datafile'
        fetch_and_output_response(client_method, name, job_id, file, description, source)


@app.command()
def create_investigation(
    study_id: str,
    name: str,
    description: str,
    keywords: List[str] = typer.Option(default=None),
    investigation_type: str = typer.Option(default=None),
):
    """
    Create an Investigation under the specified Study.
    Triggers notifications for Study subscriptors.
    """
    client_method = 'create_investigation'
    keywords = [] if not keywords else [k for k in keywords[0].split(' ')]
    fetch_and_output_response(client_method, study_id, name, description, keywords, investigation_type)


@app.command()
def create_job(
    investigation_id: str,
    sample_id: str,
    start_datetime: datetime,
    end_datetime: datetime = typer.Option(default=None),
    status: str = typer.Option(default=None),
    source: str = typer.Option(default=None)
):
    """
    Create a Job under the specified Investigation.
    Triggers notifications for Investigation subscriptors.
    """
    client_method = 'create_job'
    fetch_and_output_response(
        client_method,
        investigation_id,
        sample_id,
        start_datetime,
        end_datetime,
        status,
        source
    )


@app.command()
def update_job(
    job_id: str,
    status: str,
    end_datetime: datetime = typer.Option(default=None),
    source: str = typer.Option(default=None)
):
    """
    Update an already existing Job.
    Triggers notifications for Job subscriptors.
    """
    client_method = 'update_job'
    fetch_and_output_response(
        client_method,
        job_id,
        status,
        end_datetime,
        source
    )


@app.command()
def set_permissions(study_id: str, user_id: str, permission_level: str):
    """
    Set permission level for the specified User over the specified Study.
    """
    client_method = 'set_permissions'
    fetch_and_output_response(client_method, study_id, user_id, permission_level)


@app.command()
def remove_permissions(study_id: str, user_id: str):
    """
    Remove the specified User permissions over the specified Study.
    """
    client_method = 'remove_permissions'
    fetch_and_output_response(client_method, study_id, user_id)


@app.command()
def subscribe_to_study(study_id):
    """
    Subscribe to the specified study and print notifications to stdout.
    Notifications will be either for new Samples and Investigations under the specified Study.
    """
    client = get_client()
    for notification in client.subscribe_to_study(study_id):
        print_to_stdout(notification)


@app.command()
def subscribe_to_investigation(investigation_id):
    """
    Subscribe to the specified Investigation and print notifications to stdout.
    Notifications will be for Jobs created under the specified Study.
    """
    client = get_client()
    for notification in client.subscribe_to_investigation(investigation_id):
        print_to_stdout(notification)


@app.command()
def subscribe_to_job(job_id):
    """
    Subscribe to the specified Job and print notifications to stdout.
    Notifications will be for Job updates and new Datafiles added to the specified Job.
    """
    client = get_client()
    for notification in client.subscribe_to_job(job_id):
        print_to_stdout(notification)
