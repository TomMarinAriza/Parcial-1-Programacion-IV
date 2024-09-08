import pandas as pd
from sodapy import Socrata

def get_Data1():
    client = Socrata("www.datos.gov.co", None)
    return client
    
def get_Data(client):
    results = client.get("ch4u-f3i5", limit=2000)
    return results

def get_DataFrame(results):
    results_df = pd.DataFrame.from_records(results)
    return results_df

