import requests
from flask import json, render_template

def track_bills():
    tracked_bills = ('sb287', 'hb43')

    response = requests.get(
        'http://api.richmondsunlight.com/1.0/bills/2014.json'
    )

    return render_template(
        'bills.html',
        bills = (
            x for x in json.loads(response.content)
            if x.get('number') in tracked_bills
        )
    )