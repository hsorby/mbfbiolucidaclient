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


def read_config():
    global USER, PASSWORD, TOKEN
    config = configparser.ConfigParser()
    config.read(os.path.join(here, '.secrets_dir', 'hsorby.info'))
    USER = config['USERINFO']['Username']
    PASSWORD = config['USERINFO']['Password']
    TOKEN = config['USERINFO']['Token']


def main():
    read_config()
    args = sys.argv[:]
    print(args.pop(0))

    response = requests.post(authenticate(), authenticate_parameters())
    if response.status_code == 200:
        print(response.json())
        token = response.json()['token']

        for image_id in range(1, 5):
            response = requests.get(image(image_id))
            if response.status_code == 200:
                print(response.json())
            else:
                print('No access {}'.format(image_id))
        # Need to be admin user to get this data.
        # response = requests.get(user_all(), headers=authenticated_header(token))
        # print(response.json())

        response = requests.get(folders(), headers=authenticated_header(token))
        print(response.json())


if __name__ == "__main__":
    main()
