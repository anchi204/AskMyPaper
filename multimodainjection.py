import os 
import requests

url = """https://web.stanford.edu/class/psych209/Readings/
SuttonBartoIPRLBook2ndEd.pdf"""
local_file = "sutter_barto.pdf"
with requests.get(url, stream=True) as response: 
    response.raise_for_status() 
    with open(local_file, "wb") as f: 
        for chunk in response.iter_content(chunk_size=8192): 
            if chunk: 
                f.write(chunk)