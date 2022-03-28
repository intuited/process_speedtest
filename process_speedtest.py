#!/usr/bin/python3
# uses speedtest.net's `speedtest` command-line utility

from json import loads as decode
from subprocess import run
from pprint import pprint as pp
from datetime import datetime

timestamp = datetime.now().isoformat(timespec='seconds')

result = run(['speedtest', '-f', 'json'], capture_output=True)
#pp(result)  #debug output
output = decode(result.stdout)
ping = output['ping']['latency']
down = output['download']['bandwidth']
up = output['upload']['bandwidth']

convert_to_mbps = lambda bits: float(bits) / (1024*1024) * 8

down = round(convert_to_mbps(down), ndigits=2)
up =   round(convert_to_mbps(up), ndigits=2)

print(f'(--{timestamp}--) {ping}ms/{down}Mbps D/{up}Mbps U')
