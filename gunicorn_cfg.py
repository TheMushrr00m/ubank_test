import multiprocessing

accesslog = 'gunicorn_access.log'
errorlog = 'gunicorn_error.log'
pidfile = 'gunicorn_pid'
timeout = 300
workers = multiprocessing.cpu_count() * 2 + 1
