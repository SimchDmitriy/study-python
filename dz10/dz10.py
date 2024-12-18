import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr, spearmanr
from sklearn.linear_model import LinearRegression

file_path = '/Users/dmitrijsmirnov/Desktop/Учеба/2 курс/Python и аналитика/study-python/dz10'
data = pd.read_csv(file_path)

data = data.drop(columns=['Unnamed: 0'])

plt.scatter(data['hardness'], data['mortality'], alpha=0.7)
plt.title('Связь между жёсткостью воды и смертностью')
plt.xlabel('Жёсткость воды (hardness)')
plt.ylabel('Средняя годовая смертность (mortality)')
plt.grid()
plt.show()

pearson_corr, _ = pearsonr(data['hardness'], data['mortality'])
spearman_corr, _ = spearmanr(data['hardness'], data['mortality'])

X = data['hardness'].values.reshape(-1, 1)
y = data['mortality']
model = LinearRegression()
model.fit(X, y)

r2 = model.score(X, y)

plt.scatter(data['hardness'], data['mortality'], alpha=0.7, label='Данные')
plt.plot(data['hardness'], model.predict(X), color='red', label='Линейная регрессия')
plt.title('Линейная регрессия')
plt.xlabel('Жёсткость воды (hardness)')
plt.ylabel('Средняя годовая смертность (mortality)')
plt.legend()
plt.grid()
plt.show()

residuals = y - model.predict(X)
plt.scatter(data['hardness'], residuals, alpha=0.7)
plt.axhline(0, color='red', linestyle='--', label='Ось y=0')
plt.title('График остатков')
plt.xlabel('Жёсткость воды (hardness)')
plt.ylabel('Остатки')
plt.legend()
plt.grid()
plt.show()

print({
    'Коэффициент корреляции Пирсона': pearson_corr,
    'Коэффициент корреляции Спирмена': spearman_corr,
    'Коэффициент детерминации (R^2)': r2
})

north_data = data[data['location'] == 'North']
south_data = data[data['location'] == 'South']

def analyze_group(group_data, title):
    plt.scatter(group_data['hardness'], group_data['mortality'], alpha=0.7)
    plt.title(f'{title}: Связь между жёсткостью воды и смертностью')
    plt.xlabel('Жёсткость воды (hardness)')
    plt.ylabel('Средняя годовая смертность (mortality)')
    plt.grid()
    plt.show()

    pearson_corr, _ = pearsonr(group_data['hardness'], group_data['mortality'])
    spearman_corr, _ = spearmanr(group_data['hardness'], group_data['mortality'])

    X = group_data['hardness'].values.reshape(-1, 1)
    y = group_data['mortality']
    model = LinearRegression()
    model.fit(X, y)

    r2 = model.score(X, y)

    plt.scatter(group_data['hardness'], group_data['mortality'], alpha=0.7, label='Данные')
    plt.plot(group_data['hardness'], model.predict(X), color='red', label='Линейная регрессия')
    plt.title(f'{title}: Линейная регрессия')
    plt.xlabel('Жёсткость воды (hardness)')
    plt.ylabel('Средняя годовая смертность (mortality)')
    plt.legend()
    plt.grid()
    plt.show()

    # График остатков
    residuals = y - model.predict(X)
    plt.scatter(group_data['hardness'], residuals, alpha=0.7)
    plt.axhline(0, color='red', linestyle='--', label='Ось y=0')
    plt.title(f'{title}: График остатков')
    plt.xlabel('Жёсткость воды (hardness)')
    plt.ylabel('Остатки')
    plt.legend()
    plt.grid()
    plt.show()

    return {
        'Коэффициент корреляции Пирсона': pearson_corr,
        'Коэффициент корреляции Спирмена': spearman_corr,
        'Коэффициент детерминации (R^2)': r2
    }

north_results = analyze_group(north_data, 'Северные города')

south_results = analyze_group(south_data, 'Южные города')

print("Результаты для северных городов:", north_results)
print("Результаты для южных городов:", south_results)
