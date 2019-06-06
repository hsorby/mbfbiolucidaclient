import os
import sys
import configparser

import requests


ENDPOINT = "https://sparc.biolucida.net/api/v1"

here = os.path.abspath(os.path.dirname(__file__))

USER = ""
PASSWORD = ""
TOKEN = ""


def user_all():
    return ENDPOINT + "/user/all"


def image(id):
    return ENDPOINT + "/image/{}".format(id)


def folders():
    return ENDPOINT + "/folders"


def authenticate():
    return ENDPOINT + "/authenticate"


def authenticate_parameters():
    return {'username': USER, 'password': PASSWORD, 'token': TOKEN}


def authenticated_header(token):
    return {'token': token}


def read_config(user_info=None):
    global USER, PASSWORD, TOKEN
    config = configparser.ConfigParser()
    config.read(os.path.join(here, '.secrets_dir', user_info if user_info else 'empty.info'))

    if 'USERINFO' in config:
        USER = config['USERINFO']['Username']
        PASSWORD = config['USERINFO']['Password']
        TOKEN = config['USERINFO']['Token']


def response_ok(response):
    json_output = response.json()
    return response.status_code == 200 and json_output['status'] == 'success'


def response_error(response):
    json_output = response.json()
    return json_output['status']


def main():
    user_info = None
    args = sys.argv[:]
    if len(args) > 1:
        args.pop(0)
        user_info = args.pop(0)

    read_config(user_info)

    response = requests.post(authenticate(), authenticate_parameters())
    if response_ok(response):
        token = response.json()['token']

        for image_id in range(0, 6):
            response = requests.get(image(image_id))
            if response_ok(response):
                print(response.json())
            else:
                print('No access to {} - {}'.format(image_id, response_error(response)))
        # Need to be admin user to get this data.
        # response = requests.get(user_all(), headers=authenticated_header(token))
        # print(response.json())

        response = requests.get(folders(), headers=authenticated_header(token))
        print(response.json())
    else:
        print('Authentication did not go well - {}'.format(response_error(response)))


if __name__ == "__main__":
    main()
