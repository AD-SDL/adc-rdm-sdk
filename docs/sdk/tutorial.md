# Getting started with Argonne Discovery Cloud SDK

## Meet `adc.client.ADCClient`

The `ADCClient` will be pretty much all you need from `adc-sdk` in order to interact with Argonne Discovery Cloud API.
```
from adc_sdk.client import ADCClient

ADC_ACCESS_TOKEN = "<your API Access Token>"
client = ADCClient(ADC_ACCESS_TOKEN)
```

### Test your `ADCClient` instance

```
response = client.get_current_user()
print(response)
"""
Will output the following:
{
    "email": <your email>,
    "name": <your name>,
    "globusUsername": <your globus username>,
    "organization": <your globus auth provider>,
    "created": <user creation date>,
    "id": <your user unique identifier>
}
"""
```

### `ADCClient` code reference and functionalities

You can find the full specification of the available methos from `ADCClient` [here](code_reference.md)  