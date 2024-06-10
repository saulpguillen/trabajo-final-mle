# -*- coding: utf-8 -*-
"""Data_pre_processing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uic8ZLex6poDE1R8JylwGs3XMhumz3t-
"""

#Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

#Reading the dataset
def read_file_csv(filename):
    dataset = pd.read_csv(os.path.join('../data/', filename))
    print(filename, ' cargado correctamente')
    return dataset

#Chequeando valores nulos
def check_missing_values(df):
    # Verifica la suma de valores nulos
    missing_values = df.isna().sum().sum()

    # Si no hay valores nulos, devuelve el dataset original
    if missing_values == 0:
        print("No hay valores nulos en el dataset")
        return df
    else:
        print(f"El dataset contiene {missing_values} valores nulos. Por favor, maneje los valores nulos antes de continuar.")
        return None

#Check valores duplicados
def check_dup_values(df):
    # Verifica la suma de valores duplicados
    dup_values = df.duplicated().sum()

    # Si no hay valores duplicados, devuelve el dataset original
    if dup_values == 0:
        print("No hay valores duplicados en el dataset")
        return df
    else:
        print(f"El dataset contiene {dup_values} valores duplicados. Por favor, maneje los valores duplicados antes de continuar.")
        return None

# Escogiendo los valores X e Y
def select_x_y(df, X, Y):
    # Usa la variable X para seleccionar la columna
    x = df[[X]]
    # Usa la variable Y para seleccionar la columna
    y = df[Y]
    #dividiendo la data en entrenamiento y test
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 100)
    #guardando las datas de entrenamiento
    x_train.to_csv('../data/x_train.csv', index=False)
    x_test.to_csv('../data/x_test.csv', index=False)
    y_train.to_csv('../data/y_train.csv', index=False)
    y_test.to_csv('../data/y_test.csv', index=False)
    print("Datasets guardados correctamente en ../data/")
    return x_train, x_test, y_train, y_test