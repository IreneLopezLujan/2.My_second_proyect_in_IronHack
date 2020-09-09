from matplotlib import pyplot as plt
import pandas as pd 
import seaborn as sns
import plotly.express as px
import numpy as np


                                                #FUNCIONES CUSTOM

def countPlt(dataframe):
    """ Esta función permite crear un plot de barras a partir de la columna que
        que le indiques. El parámetro que necesita es el nombre del dataframe.
    """
    x = input('Introduce la columna que quieras comparar: ')
    print(type(x))
    sns.set()
    sns.countplot(x= f"{x}", data= dataframe)

def piePlt(df):
    """ Esta función permite crear un pie plot con los nueve valores más frecuentes
        de la columna que le indiques. El parámetro que necesita es el nombre del dataframe.
    """
    columnName=input('Introduce el nombre de la columna con la que quieras trabajar: ')
    top_column = df[columnName].value_counts()[0:10]
    top_column.index
    fig = px.pie(df,values = top_column,names = top_column.index,labels= top_column.index)
    fig.update_traces(textposition ='inside',textinfo='percent+label')
    fig.show()

                                                #FUNCIONES LIMPIEZA

def diaClass(x):
    """
    Esta función permite clasificar el día en Early Morning, Morning, Noon, Eve, Night y Late Night, 
    según las horas del día.
    """
    if (x > 4) and (x <= 8) :
       return 'Early Morning'
    elif (x > 8) and (x <= 12):
        return 'Morning'
    elif (x > 12) and (x <= 16):
        return'Noon'
    elif (x > 16) and (x <= 20) :
        return 'Eve'
    elif (x > 20) and (x <= 24):
        return'Night'
    elif (x <= 4):
        return'Late Night'