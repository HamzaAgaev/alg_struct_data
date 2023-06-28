# -*- coding: utf-8 -*-

import os
import sys
import platform

#путь к проекту
sys.path.insert(0, '/home/c/cq01525/myprettysite/public_html/site_algorithms')
#путь к фреймворку
sys.path.insert(0, '/home/c/cq01525/myprettysite/public_html/site_algorithms/site_algorithms')
#путь к виртуальному окружению
sys.path.insert(0, '/home/c/cq01525/myprettysite//myenv/lib/python{0}/site-packages'.format(platform.python_version()[0:3]))
os.environ["DJANGO_SETTINGS_MODULE"] = "site_algorithms.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()