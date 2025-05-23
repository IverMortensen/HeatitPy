# HeatitPY
A client library for accessing Heatit WiFi Panel Heater

## Install

To install the latest version run:

    pip install git+https://github.com/IverMortensen/HeatitPy.git

After installation, you can verify it’s working:

    python -c "import heatitpy; print(heatitpy.__version__)"


### Editable version
---

If you want to make changes to HeatitPy itself, use an editable install so local changes take effect immediately:

1. Download the repo.

2. Move the repo to where you want and go to it’s directory (e.g. "C:\Users\user\Downloads\HeatitPy") in your terminal.

3. Run the command:

        pip install -e .

4. Verify that it’s working:

        python -c "import heatitpy; print(heatitpy.__version__)"

Any changes made to the downloaded repo will take effect immediately.

## Usage
First, create a client:

```python
from heatitpy import Client

client = Client(base_url="https://api.example.com")
```

If the endpoints you're going to hit require authentication, use `AuthenticatedClient` instead:

```python
from heatitpy import AuthenticatedClient

client = AuthenticatedClient(base_url="https://api.example.com", token="SuperSecretToken")
```

Now call your endpoint and use your models:

```python
from heatitpy.models import MyDataModel
from heatitpy.api.my_tag import get_my_data_model
from heatitpy.types import Response

with client as client:
    my_data: MyDataModel = get_my_data_model.sync(client=client)
    # or if you need more info (e.g. status_code)
    response: Response[MyDataModel] = get_my_data_model.sync_detailed(client=client)
```

Or do the same thing with an async version:

```python
from heatitpy.models import MyDataModel
from heatitpy.api.my_tag import get_my_data_model
from heatitpy.types import Response

async with client as client:
    my_data: MyDataModel = await get_my_data_model.asyncio(client=client)
    response: Response[MyDataModel] = await get_my_data_model.asyncio_detailed(client=client)
```

By default, when you're calling an HTTPS API it will attempt to verify that SSL is working correctly. Using certificate verification is highly recommended most of the time, but sometimes you may need to authenticate to a server (especially an internal server) using a custom certificate bundle.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com", 
    token="SuperSecretToken",
    verify_ssl="/path/to/certificate_bundle.pem",
)
```

You can also disable certificate validation altogether, but beware that **this is a security risk**.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com", 
    token="SuperSecretToken", 
    verify_ssl=False
)
```

Things to know:
1. Every path/method combo becomes a Python module with four functions:
    1. `sync`: Blocking request that returns parsed data (if successful) or `None`
    1. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.
    1. `asyncio`: Like `sync` but async instead of blocking
    1. `asyncio_detailed`: Like `sync_detailed` but async instead of blocking

1. All path/query params, and bodies become method arguments.
1. If your endpoint had any tags on it, the first tag will be used as a module name for the function (my_tag above)
1. Any endpoint which did not have a tag will be in `heatitpy.api.default`

## Advanced customizations

There are more settings on the generated `Client` class which let you control more runtime behavior, check out the docstring on that class for more info. You can also customize the underlying `httpx.Client` or `httpx.AsyncClient` (depending on your use-case):

```python
from heatitpy import Client

def log_request(request):
    print(f"Request event hook: {request.method} {request.url} - Waiting for response")

def log_response(response):
    request = response.request
    print(f"Response event hook: {request.method} {request.url} - Status {response.status_code}")

client = Client(
    base_url="https://api.example.com",
    httpx_args={"event_hooks": {"request": [log_request], "response": [log_response]}},
)

# Or get the underlying httpx client to modify directly with client.get_httpx_client() or client.get_async_httpx_client()
```

You can even set the httpx client directly, but beware that this will override any existing settings (e.g., base_url):

```python
import httpx
from heatitpy import Client

client = Client(
    base_url="https://api.example.com",
)
# Note that base_url needs to be re-set, as would any shared cookies, headers, etc.
client.set_httpx_client(httpx.Client(base_url="https://api.example.com", proxies="http://localhost:8030"))
```

## Example
Here is code example that checks the current setpoint and changes it:

```python
from heatitpy.client import Client
from heatitpy.api.panel import get_api_status
from heatitpy.api.parameters import post_api_parameters

client = Client("http://192.168.1.100")

# Get current setpoint
status = get_api_status.sync(client=client)
print(f"Current setpoint: {status.parameters.heating_setpoint}")

# Update setpoint
post_api_parameters.sync(client=client, heating_setpoint=22.0)

# Check updated setpoint
status = get_api_status.sync(client=client)
print(f"New setpoint: {status.parameters.heating_setpoint}")
```
