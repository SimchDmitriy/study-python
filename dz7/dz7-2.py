import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df.head(15)

def create_regplot(df):
    plt.figure(figsize=(10, 6))
    sns.regplot(x='age', y='bill', data=df, line_kws={"color": "red"})
    plt.title('Диаграмма разброса с линией регрессии (возраст vs расходы) - Seaborn')
    plt.xlabel('Возраст')
    plt.ylabel('Расходы')
    plt.show()

def main(file_path):
    df = load_data(file_path)
    create_regplot(df)

file_path = '/Users/dmitrijsmirnov/Desktop/Учеба/2 курс/Python и аналитика/study-python/dz6/web_clients_correct.csv'

if __name__ == "__main__":
    main(file_path)