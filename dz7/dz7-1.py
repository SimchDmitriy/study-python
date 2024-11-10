import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df.head(15)

def create_scatterplot_seaborn(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='age', y='bill', data=df)
    plt.title('Диаграмма разброса (возраст vs расходы) - Seaborn')
    plt.xlabel('Возраст')
    plt.ylabel('Расходы')
    plt.show()

def create_scatterplot_plotly(df):
    fig = px.scatter(df, x='age', y='bill', title='Диаграмма разброса (возраст vs расходы) - Plotly')
    fig.update_xaxes(title_text='Возраст')
    fig.update_yaxes(title_text='Расходы')
    fig.show()

def main(file_path):
    df = load_data(file_path)
    create_scatterplot_seaborn(df)
    create_scatterplot_plotly(df)

file_path = '/Users/dmitrijsmirnov/Desktop/Учеба/2 курс/Python и аналитика/study-python/dz6/web_clients_correct.csv'

if __name__ == "__main__":
    main(file_path)