from collections import namedtuple
import yaml


config = yaml.load(open('config.yaml', 'r'))


TOKEN = config['bot']['token']

server_template = namedtuple("server", ['host',
                                        'cert',
                                        'pkey',
                                        'port',
                                        'public_host'])

server = server_template(
    public_host = config['server']['public_host'],
    host = config['server']['host'],
    cert = config['server']['cert'],
    pkey = config['server']['pkey'],
    port  = config['server']['port'],
    )


db_template = namedtuple("db", ['host','port'])

db = db_template(
    config['db']['host'],
    config['db']['port']
    )