from fedora.client import OpenIdBaseClient


class BodhiClient(OpenIdBaseClient):

    def query(self, **kwargs):
        return self.send_request('updates', req_params=kwargs)

    def save(self, **kwargs):
        return self.send_request('updates', req_params=kwargs,
                                 verb='POST', auth=True)

    def admin(self, **kwargs):
        return self.send_request('admin', req_params=kwargs, auth=True)
