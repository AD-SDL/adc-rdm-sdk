# Quick start

## Configuration

The CLI relies on you having the proper credentials and permissions in Argonne Discovery Cloud.
In order to use it you will need to define the `ADC_ACCESS_TOKEN` environment variable on your system:
```
export ADC_ACCESS_TOKEN=<Your API access token>
```
*  You can create/manage your access tokens in [Argonne Discovery Cloud](https://stage.discoverycloud.anl.gov/)

## Try it out

### List the available commands

Run the `adc` command in your terminal, you will get a list of all the available commands:
```
Usage: adc [OPTIONS] COMMAND [ARGS]...

  Argonne Discovery Cloud CLI

Commands:
  create-datafile
  create-investigation
  create-job
  create-sample
  upload-sample-file
  create-study
  create-token
  current-user
  datafile
  delete-token
  investigation
  job
  remove-permissions
  samples
  sample
  set-permissions
  studies
  study
  subscribe-to-investigation
  subscribe-to-job
  subscribe-to-study
  tokens
  update-job
```

You can see the usage of each command by running the `--help` tag next to it.
* e.g. `adc study --help`

### Test it

If you follow the steps above you should be able to interact with our API.
Run the following command to verify everything works:
```
adc current-user
```

You should get something like this printed out:
```
{
    "me": {
        "email": <your email>,
        "name": <your name>,
        "globusUsername": <your globus username>,
        "organization": <your globus auth provider>,
        "created": <user creation date>,
        "id": <your user unique identifier>
    }
}
```