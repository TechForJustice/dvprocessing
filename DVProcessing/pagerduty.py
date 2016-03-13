import pygerduty
from db_passwords import pagerduty_api_key
pager = pygerduty.PagerDuty("dvprocess-serving", pagerduty_api_key)

#https://github.com/dropbox/pygerduty