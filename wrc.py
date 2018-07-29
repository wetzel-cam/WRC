""" Script to remotely connect to a minecraft server """
from ftplib import *
server = FTP_TLS('107.172.159.200:22', "minecraft")
server.login()
server.dir()
