import pandas as pd
col_names=['surgery', 'Age', 'Hospital number', 'rectal temperature', 'pulse', 'respiratory rate', 'temperature of extremities', 'peripheral pulse', 'mucous membranes', 'capillary refill time', 'pain', 'peristalsis', 'abdominal distension', 'nasogastric tube', 'nasogastric reflux', 'nasogastric reflux PH', 'rectal examination - feces', 'abdomen', 'packed cell volume', 'total protein', 'abdominocentesis appearance', 'abdomcentesis total protein', 'outcome', 'site of lesion', 'type of lesion', 'subtype of lesion', 'lesion code', 'cp_data']
horse = pd.read_csv(r'https://raw.githubusercontent.com/obulygin/pyda_homeworks/master/statistics_basics/horse_data.csv', names=col_names, header=None, decimal='.',na_values='?')
horse.head()

study_horse_df=horse[['surgery', 'Age','outcome', 'Hospital number', 'rectal temperature', 'pulse', 'packed cell volume', 'total protein']].copy()
study_horse_df['surgery']=study_horse_df['surgery'].astype(str)
study_horse_df['Age']=study_horse_df['Age'].astype(str)
study_horse_df['Hospital number']=study_horse_df['Hospital number'].astype(str)
study_horse_df['outcome']=study_horse_df['outcome'].astype(str)
study_horse_df.describe(include='all')

D=study_horse_df.quantile([0, 0.25, 0.5, 0.75, 1], numeric_only=True)
D=D.transpose()
D['B1']=D[0.25]-1.5*(D[0.75]-D[0.25])
D['B2']=D[0.75]+1.5*(D[0.75]-D[0.25])
D['outliners']=study_horse_df[(study_horse_df[D.index]<D['B1'])|(study_horse_df[D.index]>D['B2'])].count()
print(D)

l1=len(study_horse_df)
study_horse_new = study_horse_df.dropna(thresh=2)
study_horse_new = study_horse_new[(study_horse_new.surgery!='nan')|(study_horse_new.outcome!='nan')]
study_horse_new = study_horse_new.reset_index(drop=True)
l2=len(study_horse_new)
print('строк после обработки',l2, '. Строк после обработки',l1, '. Доля оставшихся данных', l2/l1)
print('Фрагмент нового датафрейма')
print(study_horse_new.head())