try:
    r = requests.get(url, params={'s': thing})
except requests.exceptions.RequestException as e:
    # Handle the error here
