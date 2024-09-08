import Api 
import UI
import pandas as pd


pd.set_option('display.max_rows', None)  
pd.set_option('display.max_columns', None)  
pd.set_option('display.width', None)  
pd.set_option('display.max_colwidth', None)  

client = Api.get_Data1()
results = Api.get_Data(client)
dataFrame = Api.get_DataFrame(results)


userData = UI.getDataFromUser()


while (UI.verifyUserData(userData,dataFrame)):
    userData =UI.getDataFromUser()


filterTable = UI.visualizeTable(userData,dataFrame)
median = UI.calculate_edaphic_median(dataFrame,userData[2])

finalTable = UI.integrate_medians(filterTable,median)

