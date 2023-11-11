#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import seaborn as sns
import statsmodels.api as sm
from scipy import stats as st
from scipy.stats import shapiro, wilcoxon


# In[3]:


sns.set_theme(style="whitegrid")


# # T-test for the mean of ONE group of scores

# In[4]:


#Amostra aleatória de resultado de glicemia.
Glicemia = [106.25,103.88,94.52,90.41,102.80,100.25,93.62,100.69,104.21,107.78,104.90,103.04,
95.06,99.04,104.13,95.65,98.55,105.62,95.29,101.42,99.48,92.93,102.97,103.92,97.67,109.36,109.78,
94.86,95.97,112.25]
glicemia = np.array(Glicemia)


# In[5]:


sns.histplot(glicemia, kde=True)
st.describe(glicemia)


# O teste de Shapiro-Wilk avalia a hipótese nula de que os dados foram extraídos de uma distribuição normal.
# 
# - **Hipótese Nula (H0):** A amostra segue uma distribuição normal.
# - **Hipótese Alternativa (H1):** A amostra não segue uma distribuição normal.
# 
# Com um nível de significância de 5%, não temos evidências suficientes para rejeitar a hipótese nula. Isso sugere que a amostra pode seguir uma distribuição normal.
# 

# In[6]:


st.shapiro(glicemia)


# **Teste de Hipóteses para Média de Glicemia e Pré-Diabetes**
# 

# Temos como objetivo investigar se a média dos resultados de glicemia na nossa amostra sugere a presença de pré-diabetes.\
# Aqui estão as hipóteses e o resultado do teste:
# 
# - **Hipótese Nula (H0):** A média dos resultados de glicemia é igual a 100 (limiar para pré-diabetes).
# - **Hipótese Alternativa (H1):** A média dos resultados de glicemia é maior que 100, indicando pré-diabetes.
# 
# Usando um nível de significância de 5%, realizamos um teste t unicaudal (à direita).

# In[7]:


glicemia_limiar = 100


# In[8]:


st.ttest_1samp(glicemia, popmean= glicemia_limiar, alternative = "greater") # alternative{‘two-sided’, ‘less’, ‘greater’}


# O resultado do teste t foi calculado como 0.867, e o p-valor associado foi 0.196. Como o p-valor é maior que 0.05, não temos evidências suficientes para rejeitar a hipótese nula. Concluímos que não há indícios significativos de que a média dos resultados de glicemia na amostra seja maior que 100, sugerindo pré-diabetes.

# In[ ]:




