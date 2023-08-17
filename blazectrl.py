from flask import Flask

import os

app = Flask(__name__)


### Commands to run
blaze_path_cygwin = '"/cygdrive/c/Program Files (x86)/Backblaze/bztransmit.exe"'
blaze_path_win = '"c:\\Program Files (x86)\\Backblaze\\bztransmit.exe"'

# Choose your own CLI adventure
blaze_path = blaze_path_cygwin

# TODO: if the polite way is not enough - requires admin
service_stop_win = 'net stop "backblaze service"'
service_stop = service_stop_win

service_start_win = 'net start "backblaze service"'
service_start = service_start_win
###


page_text = """
<form action="/stop"><button style="color:red">Stop</button></form>
<form action="/start"><button style="color:green">Start</button></form>
"""

@app.route('/')
def hello_alex():
    return '<p>Click a button, Alex</p>{}'.format(page_text)


@app.route('/start')
def start():
    # subprocess was being janky
    os.system('{} -completesync'.format(blaze_path))
    return '<p>Started</p>{}'.format(page_text)


@app.route('/stop')
def stop():
    # subprocess was being janky
    os.system('{} -pausebackup'.format(blaze_path))
    return '<p>Stopped</p>{}'.format(page_text)


@app.route('/forcestop')
def forcestop():
    # subprocess was being janky
    os.system(service_stop)
    return '<p>Stopped Service</p>{}'.format(page_text)


@app.route('/forcestart')
def forcestart():
    # subprocess was being janky
    os.system(service_start)
    return '<p>Stopped Service</p>{}'.format(page_text)
