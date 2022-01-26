# This entrypoint file to be used in development. Start by reading README.md
import demographic_data_analyzer
from unittest import main
import pandas as pd
import numpy as np


# Test your function by calling it here
demographic_data_analyzer.calculate_demographic_data()

# Run unit tests automatically
main(module='test_module', exit=False)

planilha = pd.read_csv('adult.data.csv')
race = planilha['race'].value_counts()
print(race)

loc_homens = planilha.loc[(planilha['sex'] == 'Male') , 'age'].mean()
print(loc_homens)

#porcentagem com bacharel
total_de_pessoas = planilha.value_counts().sum()
total_bacharel = planilha.loc[planilha['education'] == 'Bachelors'].value_counts().sum()
percentual_bacharel = total_bacharel/total_de_pessoas
print(percentual_bacharel)

#porcentagem de quem tem educacao avancada que ganha 50k ou mais

bacherel50k = (planilha['education'] =='Bachelors') & (planilha['salary'] == '>50K')
total_bacha50k = planilha.loc[bacherel50k].shape[0]
bacharel = (planilha['education'] =='Bachelors')
total_bachareal = planilha.loc[bacharel].shape[0]


masters50k = (planilha['education'] =='Masters') & (planilha['salary'] == '>50K')
total_masters50k = planilha.loc[masters50k].shape[0]
master = (planilha['education'] =='Masters')
total_masters = planilha.loc[master].shape[0]


doto50k = (planilha['education'] =='Doctorate') & (planilha['salary'] == '>50K')
total_doto50k = planilha.loc[doto50k].shape[0]
doto = (planilha['education'] =='Doctorate')
total_doto = planilha.loc[doto].shape[0]


percentual_high_edu_50k = (total_bacha50k + total_masters50k + total_doto50k)/(total_bachareal +total_masters+total_doto)
print(percentual_high_edu_50k)



salario50k = planilha['salary'] == '>50K'
total_salario50k = planilha.loc[salario50k].shape[0]
semhigh_edu = total_salario50k - (total_bacha50k + total_masters50k + total_doto50k) 
percentual_semhigh_edu = (semhigh_edu)/total_de_pessoas
print(percentual_semhigh_edu)

min_semana = planilha['hours-per-week'].min()
print(min_semana)

min_semana50k = (planilha['hours-per-week'] == 1) & (planilha['salary'] == '>50K')
total_min_semana50k = planilha.loc[min_semana50k].shape[0]

boolean_min_semana = (planilha['hours-per-week'] == 1)
total_min_semana = planilha.loc[boolean_min_semana].shape[0]

percentual_semanamin_50k = total_min_semana50k/total_min_semana
print(percentual_semanamin_50k)

#pais com maior percentual de 50
total_paises = planilha['native-country'].value_counts()

pt1 = planilha.loc[(planilha['salary'] == '>50K'), 'native-country'].value_counts()
pt1 = pt1.sort_index(key=lambda x: x.str.lower())
total_paises = total_paises.sort_index(key=lambda x: x.str.lower())

#remover holanda 15  e outlying us 28
total_paises = total_paises.drop(total_paises.index[15])
total_paises = total_paises.drop(total_paises.index[27])
percentual = np.zeros(total_paises.shape[0])

for n in range(0,pt1.shape[0]):
  percentual[n] = (pt1[n])/ (total_paises[n])

print(pt1.index[percentual.argmax()])

#profissao popular da india qe paga mais de 50k

booleano_india = (planilha["native-country"] == 'India') & (planilha['salary'] == '>50K')
india = planilha.loc[booleano_india]
india_trampo = india['occupation'].value_counts().index[0]
print(india_trampo)