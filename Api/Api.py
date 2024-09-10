import pandas as pd
from sodapy import Socrata

def getClient():
    client = Socrata("www.datos.gov.co", None)
    return client
    
def getData(client):
    results = client.get("ch4u-f3i5", limit=2000)
    return results

def getDataFrame(results):
    results_df = pd.DataFrame.from_records(results)
    return results_df

