import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df.head(15)

def analyze_age(df):
    df['age'] = df['age'].apply(lambda x: 'Старше 25' if x > 25 else 'Младше или равен 25')
    return df

def main(file_path):
    df = load_data(file_path)
    df_analyzed = analyze_age(df)
    print("Данные с анализом возраста:\n", df_analyzed)

file_path = '/Users/dmitrijsmirnov/Desktop/Учеба/2 курс/Python и аналитика/study-python/dz6/web_clients_correct.csv'

if __name__ == "__main__":
    main(file_path)