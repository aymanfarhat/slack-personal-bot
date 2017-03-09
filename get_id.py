import os
import configparser
from slackclient import SlackClient


config = configparser.ConfigParser()
config.read('config.ini')

slack_client = SlackClient(config['SLACK']['BOT_TOKEN'])

if __name__ == "__main__":
    api_call = slack_client.api_call('users.list')

    if api_call.get('ok'):
        users = api_call.get('members')

        for user in users:
            if 'name' in user and user.get('name') == config['SLACK']['BOT_NAME']:
                print('Bot ID for ' + user['name'] + ' is ' + user.get('id'))
    else:
        print('could not find bot user with the name ' + config['SLACK']['BOT_NAME'])
