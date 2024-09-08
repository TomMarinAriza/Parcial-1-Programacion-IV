import pandas as pd

def getDataFromUser ():

    deparment =  input("Digite el departamento donde va a filtrar los datos ")
    municipality=  input("Digite el municipio donde va a filtrar los datos ")
    crop =  input("Digite el cultivo donde va a filtrar los datos ")

    listData = [deparment.upper(),municipality.upper(),crop.capitalize()] 
    return listData


def visualizeTable(filters, dataFrame):
   
    filterDataFrame = dataFrame.copy()

    for column, filter_value in zip(dataFrame.columns, filters):
        if filter_value:
            filterDataFrame = filterDataFrame[filterDataFrame[column] == filter_value]

    
    columns_to_display = ["departamento", "municipio", "cultivo", "topografia"]
    
    
    if "topografia" in filterDataFrame.columns:
        filtered_table = filterDataFrame[columns_to_display]
    else:
        filtered_table = filterDataFrame[["departamento", "municipio", "cultivo"]]

    return filtered_table


def verifyUserData(filters, dataFrame):
    for column, filter_value in zip(dataFrame.columns, filters):
        if filter_value:
            
            if filter_value not in dataFrame[column].values:
                print(f"El valor '{filter_value}' no existe en la columna '{column}'")
                return True
    return False


def calculate_edaphic_median(df, crop_name):
    
    filtered_df = df[df['cultivo'].str.upper() == crop_name.upper()]
    
    
    if filtered_df.empty:
        return "El cultivo consultado no se encuentra en el DataFrame."
    
   
    edaphic_vars = ['ph_agua_suelo_2_5_1_0', 'f_sforo_p_bray_ii_mg_kg', 'potasio_k_intercambiable_cmol_kg']
    
   
    existing_vars = [var for var in edaphic_vars if var in filtered_df.columns]
    
    if not existing_vars:
        return "No se encontraron variables edáficas en el DataFrame."

    
    medians = {}
    for var in existing_vars:
       
        filtered_df[var] = pd.to_numeric(filtered_df[var], errors='coerce')
        
        medians[var] = filtered_df[var].median()
    
    return medians


def integrate_medians(dataFrame, medians):
   
    medians_df = pd.DataFrame(medians, index=['Mediana'])
    
    
    medians_df = medians_df.transpose()
    
    
    integrated_df = pd.concat([dataFrame, medians_df], ignore_index=True)
    
    return integrated_df