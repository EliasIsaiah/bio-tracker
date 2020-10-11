from django.shortcuts import render
import requests
import json
from decouple import config


def frontend(request):

    APIKEY = config('KINTONE_API_KEY')

    response = requests.get('https://bio-tracker.kintone.com/k/v1/records.json?app=3&totalCount=true', headers={'X-Cybozu-API-Token': APIKEY})
    kintone_data = response.json()
    print(json.dumps(kintone_data, indent=2))

    data = {
        'kintoneData': kintone_data,
    }

    return render(request, 'biotrackerapp/template.html', data)
