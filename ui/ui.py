import pandas as pd

def getDataFromUser ():

    deparment =  input("Digite el departamento donde va a filtrar los datos ")
    municipality=  input("Digite el municipio donde va a filtrar los datos ")
    crop =  input("Digite el cultivo donde va a filtrar los datos ")

    listData = [deparment.upper(),municipality.upper(),crop.capitalize()] 
    return listData


def visualizeTable(filters, dataFrame):
   
    filterDataFrame = dataFrame.copy()

    for column, FilterValue in zip(dataFrame.columns, filters):
        if FilterValue:
            filterDataFrame = filterDataFrame[filterDataFrame[column] == FilterValue]

    
    columnsToDisplay = ["departamento", "municipio", "cultivo", "topografia"]
    
    
    if "topografia" in filterDataFrame.columns:
        FilterTable = filterDataFrame[columnsToDisplay]
    else:
        FilterTable = filterDataFrame[["departamento", "municipio", "cultivo"]]

    return FilterTable


def verifyUserData(filters, dataFrame):
    for column, FilterValue in zip(dataFrame.columns, filters):
        if FilterValue:
            
            if FilterValue not in dataFrame[column].values:
                print(f"El valor '{FilterValue}' no existe en la columna '{column}'")
                return True
    return False


def calculateMedian(df, cropName):
    
   
    filteredDataFrame = df[df['cultivo'].str.upper() == cropName.upper()].copy() 
    
    if filteredDataFrame.empty:
        return "El cultivo consultado no se encuentra en el DataFrame."
    
   
    edaphicVariable = ['ph_agua_suelo_2_5_1_0', 'f_sforo_p_bray_ii_mg_kg', 'potasio_k_intercambiable_cmol_kg']
    
    
    existingVariable = [var for var in edaphicVariable if var in filteredDataFrame.columns]
    
    if not existingVariable:
        return "No se encontraron variables edáficas en el DataFrame."

    
    medians = {}
    for var in existingVariable:
        filteredDataFrame[var] = pd.to_numeric(filteredDataFrame[var], errors='coerce')  
        medians[var] = filteredDataFrame[var].median()  
    
    return medians


def showMedians(medians):
    if isinstance(medians, dict):
        print("\nMedianas de las variables edáficas:")
        for var, median in medians.items():
            print(f"{var}: {median:.2f}")
    else:
       
        print(medians)
