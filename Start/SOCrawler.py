import requests
import urllib.robotparser as r_parser

AGENT_NAME = 'C_SO_SPYDER'
URL = 'http://www.stackoverflow.com/'

robo_parser = r_parser.RobotFileParser(URL + "robots.txt")
robo_parser.read()

