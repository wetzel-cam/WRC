""" Script to remotely connect to a minecraft server """
import urllib3
import json
from util.KeyHandler import read_key

# ui system
http = urllib3.PoolManager()
json_decoder = json.JSONDecoder()
json_encoder = json.JSONEncoder()

# make into key management system
key = read_key('test')
secret = read_key('test2')


# make each option on api a function
headers = {
    'Content-Type': 'application/json',
    'key': key,
    'secret': secret
}

body = {
    'path': '/mc-instances'
}

r = http.request('GET', 'https://api.creeper.host/filemanager/listdirectory',
                 headers=headers, body=json_encoder.encode(body))

dtmp = json.loads(r.data.decode('utf-8'))
instance_name = dtmp['tree'][0]['name']

command = 'say I AM ALIVE'

body = {
    'command': command,
    'instance': instance_name
}

print(body['command'])

r = http.request('PUT', 'https://api.creeper.host/mc/writeconsole',
                 headers=headers, body=json.dumps(body))

quit()
