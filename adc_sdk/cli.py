import os
import json
import typer
import click
from datetime import datetime

from pydantic import BaseModel

from adc_sdk.client import ADCClient
from adc_sdk.exceptions import ADCError
from typing import List, Union


class NaturalOrderGroup(click.Group):
    def list_commands(self, ctx):
        return self.commands.keys()


app = typer.Typer(cls=NaturalOrderGroup)


@app.callback()
def adc():
    """
    Argonne Discovery Cloud CLI
    """


def get_token_from_env():
    """
    Fetch and returns ADC_ACCESS_TOKEN env var
    Outputs error if it is not present
    """
    try:
        return os.environ["ADC_ACCESS_TOKEN"]
    except KeyError:
        message = "You need to set ADC_ACCESS_TOKEN environment variable before you can interact with ADC API"
        typer.echo(message, err=True)
        raise typer.Exit()


def get_client() -> ADCClient:
    """
    Return an instance of ADCClient using the ADC_ACCESS_TOKEN env var
    """
    token = get_token_from_env()
    return ADCClient(token)


def print_to_stdout(content: Union[dict, BaseModel]):
    if isinstance(content, BaseModel):
        typer.echo(content.json(indent=4, exclude_unset=True))
    else:
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
    Fetch current user's information
    """
    client_method = "get_current_user"
    fetch_and_output_response(client_method)


@app.command()
def tokens():
    """
    List current user's available API tokens
    """
    client_method = "get_tokens"
    fetch_and_output_response(client_method)


@app.command()
def studies():
    """
    List studies available to the current user
    """
    client_method = "get_studies"
    fetch_and_output_response(client_method)


@app.command()
def samples():
    """
    List samples available to the current user
    """
    client_method = "get_samples"
    fetch_and_output_response(client_method)


@app.command()
def study(study_id: str):
    """
    Fetch a specific study
    """
    client_method = "get_study"
    fetch_and_output_response(client_method, study_id)


@app.command()
def sample(sample_id: str):
    """
    Fetch a specific sample
    """
    client_method = "get_sample"
    fetch_and_output_response(client_method, sample_id)


@app.command()
def investigation(investigation_id: str):
    """
    Fetch a specific investigation
    """
    client_method = "get_investigation"
    fetch_and_output_response(client_method, investigation_id)


@app.command()
def job(job_id: str):
    """
    Fetch a specific job
    """
    client_method = "get_job"
    fetch_and_output_response(client_method, job_id)


@app.command()
def datafile(datafile_id: str):
    """
    Fetch a specific datafile
    """
    client_method = "get_datafile"
    fetch_and_output_response(client_method, datafile_id)


@app.command()
def create_token(name: str):
    """
    Create a new API token
    """
    client_method = "create_token"
    fetch_and_output_response(client_method, name)


@app.command()
def delete_token(token_id: str):
    """
    Delete a specific token
    """
    client_method = "delete_token"
    fetch_and_output_response(client_method, token_id)


@app.command(short_help="Create a Study")
def create_study(
    name: str = typer.Argument(..., help="User-provided name of the study"),
    description: str = typer.Option(
        default=None, help="Longer-form description of the study"
    ),
    keywords: List[str] = typer.Option(default=None, help="Space separated keywords"),
    start_date: datetime = typer.Option(
        default=None, formats=["%Y-%m-%d"], help="Date when the study began"
    ),
    end_date: datetime = typer.Option(
        default=None, formats=["%Y-%m-%d"], help="Date when the study ended"
    ),
):
    """
    Create a new Study, current user will be the owner and will have admin permissions
    """
    if start_date:
        start_date = start_date.date()
    if end_date:
        end_date = end_date.date()
    if keywords:
        keywords = [k for k in keywords[0].split(" ")]
    client_method = "create_study"
    fetch_and_output_response(
        client_method, name, description, keywords, start_date, end_date
    )


@app.command(short_help="Create a Sample")
def create_sample(
    name: str = typer.Argument(..., help="User-provided name of the sample"),
    description: str = typer.Option(default=None, help="User-provided description of the sample"),
    formula: str = typer.Option(default=None, help="Chemical formula of the sample"),
    type: str = typer.Option(default='other', help='Sample type ["purchased", "synthesised", "purchased_and_synthesised"] (default: "other")'),
    company_name: str = typer.Option(default=None, help='Name of the company where the sample was generated'),
    product_url: str = typer.Option(default=None, help='URL of the sample'),
    product_number: str = typer.Option(default=None, help='Sample product SKU'),
    building: str = typer.Option(default=None, help='Building where the sample is stored'),
    room: str = typer.Option(default=None, help='Room where the sample is stored'),
    storage_unit: str = typer.Option(default=None, help='Storage unit where the sample is stored'),
    sub_unit: str = typer.Option(default=None, help='Sub unit of storage where the sample is stored'),
    parent_id: str = typer.Option(default=None, help="ID of the parent sample"),
    keywords: List[str] = typer.Option(default=None, help="Space separated keywords"),


):
    """
    Create a Sample under the specified Study to (possibly) be used as input for a Job to generate Datafiles
    """
    client_method = "create_sample"

    if keywords:
        keywords = [k for k in keywords[0].split(" ")]

    if not any([type, company_name, product_url, product_number]):
        source = None
    else:
        source = {
            "type": type,
            "companyName": company_name,
            "productUrl": product_url,
            "productNumber": product_number
        }

    if not any([building, room, storage_unit, sub_unit]):
        location = None
    else:
        location = {
            "building": building,
            "room": room,
            "storageUnit": storage_unit,
            "subUnit": sub_unit
        }

    preparation_steps = None

    fetch_and_output_response(
        client_method,
        name,
        description,
        formula,
        source,
        location,
        preparation_steps,
        parent_id,
        keywords,
    )


@app.command(short_help="Upload file attachment to Sample record")
def upload_sample_file(
    sample_id: str = typer.Argument(..., help="ID of the target sample"),
    name: str = typer.Argument(..., help="User-provided name of the file attachment"),
    file: str = typer.Argument(..., help="Local path to the actual file to be uploaded"),
    description: str = typer.Option(default=None, help='Description of the file to be uploaded',),
):
    """
    Upload file attachment to Sample record
    """
    client_method = "add_files_to_sample"
    if not os.path.isfile(file):
        typer.echo("Invalid file path", err=True)
    with open(file, "rb") as attachment:
        files = [{
            "name": name,
            "file": attachment,
            "description": description or name,
        }]

        fetch_and_output_response(
            client_method, sample_id, files
        )


@app.command(short_help="Upload file attachment to Sample record")
def remove_sample_file(
    sample_id: str = typer.Argument(..., help="ID of the target sample"),
    file_id: str = typer.Argument(..., help="ID of file to be removed from the Sample record"),
):
    """
    Remove file attachment from Sample record
    """
    client_method = "remove_files_from_sample"
    fetch_and_output_response(
        client_method, sample_id, [file_id]
    )


@app.command(short_help="Create an Investigation")
def create_investigation(
    study_id: str = typer.Argument(
        ..., help="ID of the study this investigation belongs to"
    ),
    name: str = typer.Argument(..., help="User-provided name of the investigation"),
    description: str = typer.Option(
        default=None, help="Longer-form description of the investigation"
    ),
    start_date: datetime = typer.Option(
        default=None, formats=["%Y-%m-%d"], help="Date when the investigation began"
    ),
    end_date: datetime = typer.Option(
        default=None, formats=["%Y-%m-%d"], help="Date when the investigation ended"
    ),
    keywords: List[str] = typer.Option(default=None, help="Space separated keywords"),
    type: str = typer.Option(default=None, help="Investigation type"),
    source: str = typer.Option(
        default=None,
        help='Custom message to include as the "source" field in the study\'s subscriptions',
    ),
):
    """
    Create an Investigation under the specified Study \n
    * Triggers notifications for its Study subscriptors
    """
    client_method = "create_investigation"
    if keywords:
        keywords = [k for k in keywords[0].split(" ")]
    if start_date:
        start_date = start_date.date()
    if end_date:
        end_date = end_date.date()
    fetch_and_output_response(
        client_method,
        study_id,
        name,
        description,
        type,
        keywords,
        start_date,
        end_date,
        source,
    )


@app.command(short_help="Create a Job")
def create_job(
    investigation_id: str = typer.Argument(
        ..., help="ID of the investigation this job belongs to"
    ),
    sample_id: str = typer.Option(default=None, help="ID of the job's input sample"),
    status: str = typer.Option(
        default=None,
        help="Job status. One of ['created', 'running', 'completed', 'canceled']",
    ),
    start_datetime: datetime = typer.Option(
        default=None, formats=["%Y-%m-%dT%H:%M:%S"], help="Datetime when the job began"
    ),
    end_datetime: datetime = typer.Option(
        default=None, formats=["%Y-%m-%dT%H:%M:%S"], help="Datetime when the job ended"
    ),
    source: str = typer.Option(
        default=None,
        help='Custom message to include as the "source" field in the investigation\'s subscriptions',
    ),
):
    """
    Create a Job under the specified Investigation \n
    * Triggers notifications for its Investigation subscriptors
    """
    client_method = "create_job"
    fetch_and_output_response(
        client_method,
        investigation_id,
        sample_id,
        start_datetime,
        end_datetime,
        status,
        source,
    )


@app.command(short_help="Update an already existing Job")
def update_job(
    job_id: str = typer.Argument(..., help="ID of the job to update"),
    status: str = typer.Option(
        default=None,
        help="Job status. One of ['created', 'running', 'completed', 'canceled']",
    ),
    start_datetime: datetime = typer.Option(
        default=None, formats=["%Y-%m-%dT%H:%M:%S"], help="Datetime when the job began"
    ),
    end_datetime: datetime = typer.Option(
        default=None, formats=["%Y-%m-%dT%H:%M:%S"], help="Datetime when the job ended"
    ),
    source: str = typer.Option(
        default=None,
        help='Custom message to include as the "source" field in the job\'s subscriptions',
    ),
):
    """
    Update an already existing Job \n
    * Triggers notifications for Job subscriptors
    """
    client_method = "update_job"
    fetch_and_output_response(
        client_method, job_id, status, start_datetime, end_datetime, source
    )


@app.command(short_help="Create a Datafile (Job result)")
def create_datafile(
    file: str = typer.Argument(..., help="Path to the datafile actual file"),
    job_id: str = typer.Argument(..., help="ID of the job this datafile results from"),
    name: str = typer.Argument(..., help="User-provided name of the datafile"),
    description: str = typer.Option(
        default=None, help="Longer-form description of the datafile"
    ),
    source: str = typer.Option(
        default=None,
        help='Custom message to include as the "source" field in the study\'s subscriptions',
    ),
):
    """
    Create a Datafile (Job result file) \n
    * Triggers notifications for Job subscriptors
    """
    if not os.path.isfile(file):
        typer.echo("Invalid file path", err=True)
    with open(file, "rb") as datafile_file:
        client_method = "create_datafile"
        fetch_and_output_response(
            client_method, name, job_id, datafile_file, description, source
        )


@app.command(short_help="Set user permissions over study")
def set_permissions(study_id: str, user_id: str, permission_level: str):
    """
    Set permission level for the specified user over the specified study
    """
    client_method = "set_permissions"
    fetch_and_output_response(client_method, study_id, user_id, permission_level)


@app.command(short_help="Remove user permissions over study")
def remove_permissions(study_id: str, user_id: str):
    """
    Remove the specified user permissions over the specified study
    """
    client_method = "remove_permissions"
    fetch_and_output_response(client_method, study_id, user_id)


@app.command(short_help="Subscribe to study")
def subscribe_to_study(study_id):
    """
    Subscribe to the specified study and print notifications to stdout \n
    Notifications will be either for new Samples and Investigations under the specified Study
    """
    client = get_client()
    try:
        for notification in client.subscribe_to_study(study_id):
            print_to_stdout(notification)
    except ADCError as e:
        typer.echo(e.error, err=True)


@app.command(short_help="Subscribe to investigation")
def subscribe_to_investigation(investigation_id):
    """
    Subscribe to the specified Investigation and print notifications to stdout \n
    Notifications will be for Jobs created under the specified Study
    """
    client = get_client()
    try:
        for notification in client.subscribe_to_investigation(investigation_id):
            print_to_stdout(notification)
    except ADCError as e:
        typer.echo(e.error, err=True)


@app.command(short_help="Subscribe to job")
def subscribe_to_job(job_id):
    """
    Subscribe to the specified Job and print notifications to stdout \n
    Notifications will be for Job updates and new Datafiles added to the specified Job
    """
    client = get_client()
    try:
        for notification in client.subscribe_to_job(job_id):
            print_to_stdout(notification)
    except ADCError as e:
        typer.echo(e.error, err=True)
