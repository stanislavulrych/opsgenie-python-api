# coding: utf-8

import re
import six
from tempoapiclient.rest_client import RestAPIClient


class SchedulesApi(RestAPIClient):
    
    
    def __init__(self, auth_token, base_url="https://api.eu.opsgenie.com/"):
        self._base_url = base_url
        super().__init__(auth_token=auth_token)
        self._update_header("Authorization", "GenieKey {}".format(auth_token))

    
    def get(self, path, data=None, flags=None, params=None, headers=None, not_json_response=None, trailing=None):
        path_absolute = super().url_joiner(self._base_url, path)
        resp = super().get(path_absolute, data=data, flags=flags, params=params, headers=headers, not_json_response=not_json_response, trailing=trailing)
        
        if 'data' not in resp:
            return resp

        results = resp['data']
        return results

# Schedules

    def get_schedules(self, identifier=None):
        """
        Retrieves existing schedules.
        """
        url = f"/v2/schedules"
        if identifier:
            url += f"/{identifier}"
        return self.get(url)

    def get_schedule_rotations(self, identifier):
        """
        Retrieves schedule rotation.
        """
        return self.get(f"/v2/schedules/{identifier}/rotations")

    def get_schedule_overrides(self, identifier):
        """
        Retrieves schedule overrides.
        """
        return self.get(f"/v2/schedules/{identifier}/overrides")

    def get_users(self, identifier=None):
        """
        Retrieves users information.
        """
        url = f"/v2/users"
        if identifier:
            url += f"/{identifier}"
        return self.get(url)