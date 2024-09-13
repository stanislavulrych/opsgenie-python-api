# coding: utf-8

from atlassian.rest_client import AtlassianRestAPI


class Schedules(AtlassianRestAPI):
    
    def __init__(self, token, url="https://api.eu.opsgenie.com/v2/"):
        super().__init__(url=url)
        self._session_add_headers_genie_key(token)
        
    def _session_add_headers_genie_key(self, token):
        self._session.headers.update({"Authorization": "GenieKey {}".format(token)})

    def get(self, path, **kwargs):
        resp = super().get(path, **kwargs)
        if 'data' not in resp:
            return resp

        return resp['data']

    # Schedules

    def get_schedules(self, identifier=None):
        """
        Retrieves existing schedules.
        """

        url = "/schedules"
        if identifier:
            url += f"/{identifier}"
        return self.get(url)


    def get_schedule_timeline(self, identifier, identifierType=None, expand=None, interval=None, intervalUnit=None, date=None):
        """
        Retrieves schedule timeline
        """

        params = {}
        if identifierType:
            params["identifierType"] = identifierType
        if expand:
            params["expand"] = expand
        if interval:
            params["interval"] = interval
        if intervalUnit:
            params["intervalUnit"] = intervalUnit
        if date:
            params["date"] = date

        return self.get(f"/schedules/{identifier}/timeline", params=params)


    def get_schedule_rotations(self, identifier):
        """
        Retrieves schedule rotation.
        """
    
        return self.get(f"/schedules/{identifier}/rotations")


    def get_schedule_overrides(self, identifier):
        """
        Retrieves schedule overrides.
        """
        
        return self.get(f"/schedules/{identifier}/overrides")


    def get_users(self, identifier=None):
        """
        Retrieves users information.
        """
        url = "/users"
        if identifier:
            url += f"/{identifier}"
        return self.get(url)