#!/usr/bin/env python

import os.path
from nfl.update import update

data_path = os.path.join(os.path.dirname(__file__), 'data')
update(data_path)