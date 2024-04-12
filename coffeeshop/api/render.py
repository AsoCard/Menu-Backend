from rest_framework.renderers import BaseRenderer
import json


class CustomRenderer(BaseRenderer):
    """
    Renderer which serializes to JSON and wraps the result in a custom format.
    """

    media_type = 'application/json'
    format = 'json'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Renders the given data into JSON format.
        """
        try:
            if list(data.keys())[0] in ['msg', 'message']:
                return json.dumps({
                    'result': [],
                    'message': data[list(data.keys())[0]]
                })
        except:
            pass

        return json.dumps({
            'result': data,
            'message': ''
        })
