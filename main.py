import Api.Api as Api 
import Ui.UI as UI
import pandas as pd


pd.set_option('display.max_rows', None)  
pd.set_option('display.max_columns', None)  
pd.set_option('display.width', None)  
pd.set_option('display.max_colwidth', None)  

client = Api.getClient()
results = Api.getData(client)
dataFrame = Api.getDataFrame(results)


userData = UI.getDataFromUser()


while (UI.verifyUserData(userData,dataFrame)):
    userData =UI.getDataFromUser()


filterTable = UI.visualizeTable(userData,dataFrame)
median = UI.calculateMedian(dataFrame,userData[2])

print(filterTable)
UI.showMedians(median)
