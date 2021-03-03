from django.db import models
import matplotlib.pyplot as plt 
import pandas as pd 
import mpld3 

class grafico(models.Model):
    data = pd.read_csv('./VisualApp/templates/visualapp/visualapp.csv')
    fig = plt.figure(figsize=(7,4))
    for item in data.Mes:
        if "EN" in item:
            plt.bar("Enero", data.Inversión)
        if "FE" in item:
            plt.bar("Febrero", data.Inversión)
        plt.legend(item)
    plt.xlabel("Meses")
    plt.ylabel("Inversión")
    visual = mpld3.fig_to_html(fig)
    grafica = open("./VisualApp/templates/visualapp/grafico.html","w")
    grafica.write(visual)
    grafica.close()
