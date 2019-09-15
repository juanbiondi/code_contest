bind = 'unix:flask.sock'
max_requests = 10000
workers = 3
worker_class = 'gevent'
timeout = 2000
preload = True
proc_name = 'api'
