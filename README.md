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

You need an API token for communicating with Opsgenie REST APIs. 

### Schedules API

```
from opsgenie.schedules_api import SchedulesApi

schedulesApi = SchedulesApi(auth_token='<your_api_auth_token>)

users = schedulesApi.get_users()
print(users)


schedules = schedulesApi.get_schedules()
print(schedules)


rotations = schedulesApi.get_schedule_rotations("<scheduleid>")
print(rotations)

overrides = schedulesApi.get_schedule_overrides("<scheduleid>")
print(overrides)

timeline = schedulesApi.get_schedule_timeline("<scheduleid>")
print(timeline)

```


## Contributing

Contribution is welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.
