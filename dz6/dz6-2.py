import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df.head(15)

def filter_by_sex_and_age(df):
    return df[(df['sex'] == 'male') & (df['age'] > 30)]

def main(file_path):
    df = load_data(file_path)
    df_filtered = filter_by_sex_and_age(df)
    print("\nФильтрованные данные (пол — мужской, возраст — больше 30):\n", df_filtered)

file_path = '/Users/dmitrijsmirnov/Desktop/Учеба/2 курс/Python и аналитика/study-python/dz6/web_clients_correct.csv'

if __name__ == "__main__":
    main(file_path)