import api.api as api 
import ui.ui as ui
import pandas as pd


pd.setOption('display.max_rows', None)  
pd.setOption('display.max_columns', None)  
pd.setOption('display.width', None)  
pd.setOption('display.max_colwidth', None)  

client = api.getClient()
results = api.getData(client)
dataFrame = api.getDataFrame(results)


userData = ui.getDataFromUser()


while (ui.verifyUserData(userData,dataFrame)):
    userData =ui.getDataFromUser()


filterTable = ui.visualizeTable(userData,dataFrame)
median = ui.calculateMedian(dataFrame,userData[2])

print(filterTable)
ui.showMedians(median)
