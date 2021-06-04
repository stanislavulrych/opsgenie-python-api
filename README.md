# opsgenie-python-api

Low-level Python bindings for Opsgenie API.

This is a Opsgenie API client library to simplify the interaction with Opsgenie.

Opsgenie API documentation can be found at https://docs.opsgenie.com/docs/

## Installation

Install current reelase by pip

```
pip install opsgenie-python-api
```

## Getting Started

You need an API token for communicating with tempo REST APIs. 

```
from opsgenie import client

schedulesApi = SchedulesApi(auth_token='<your_api_auth_token>)

schedules = self.schedulesapi.get_schedules()
print(schedules)
```


## Contributing

Contribution is welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.
