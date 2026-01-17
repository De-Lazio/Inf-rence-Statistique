import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def df_to_rlist(df):
    rlist = []
    for index, ligne in df.iterrows():
                # Convertir la ligne en liste et l'ajouter à la liste de lignes
                rlist.append(list(ligne))
    return rlist

def arrondir_si_nombre(element, n_nbr=4):
    if isinstance(element, (int, float)):
        return round(element, n_nbr)
    else:
        return element
    
def round_df_mixt(df, n_nbr=4): 
    return df.applymap(arrondir_si_nombre, n_nbr=n_nbr)

def round_list(m_list):
    return [round(element, 4) for element in m_list]

def round_list_mixt(m_list):
    return [round(element, 4) if isinstance(element, (int, float)) else element for element in m_list]