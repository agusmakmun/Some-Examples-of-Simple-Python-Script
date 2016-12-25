import json
import base64
import requests
requests.packages.urllib3.disable_warnings()

client_id = 'key-key-key-key'
api_key = 'key-key-key-key-key-key-key-key'


def imgur_uploader(client_id, api_key, image_path):
    """
    Basic imgur uploader return as json data.

    :param `client_id` is API client id.
    :param `api_key` is API key.
    :param `image_path` is image path.

    Return:
        success: {'status': 200, 'link': <link_image_uploaded>, 'name': <image_name>}
        error: {'status': <error_code>, 'erorr': <erorr_message>}
    """
    url_api = 'https://api.imgur.com/3/upload.json'
    headers = {'Authorization': 'Client-ID ' + client_id}

    response = requests.post(
        url_api,
        headers=headers,
        data={
            'key': api_key,
            'image': base64.b64encode(open(image_path, 'rb').read()),
            'type': 'base64',
            'name': image_path.split('/')[-1],
        }
    )
    respdata = json.loads(response)

    if respdata['status'] == 200:
        return json.dumps({
            'status': respdata['status'],
            'link': respdata['data']['link'],
            'name': respdata['data']['name']
        })
    return json.dumps({
        'status': respdata['status'],
        'error': respdata['data']['error']
    })
