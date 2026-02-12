# ===========================
# Importar bibliotecas
# ===========================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configurações visuais
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10,6)

# Criar pasta para salvar gráficos
output_dir = "graficos"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# ===========================
# 1️⃣ Importar o dataset
# ===========================
titanic = pd.read_csv("titanic.csv")  # CSV deve estar na mesma pasta que o script
print("Primeiras linhas do dataset:")
print(titanic.head(), "\n")

# ===========================
# 2️⃣ Informações gerais
# ===========================
print("Informações do dataset:")
print(titanic.info(), "\n")

print("Estatísticas descritivas:")
print(titanic.describe(), "\n")

print("Valores nulos por coluna:")
print(titanic.isnull().sum(), "\n")

# ===========================
# 3️⃣ Limpeza básica
# ===========================
# Preencher valores nulos sem gerar warning
titanic['Age'] = titanic['Age'].fillna(titanic['Age'].median())
titanic['Embarked'] = titanic['Embarked'].fillna(titanic['Embarked'].mode()[0])

# Remover colunas irrelevantes, se existirem
for col in ['Cabin', 'Ticket']:
    if col in titanic.columns:
        titanic.drop(columns=[col], inplace=True)

# ===========================
# 4️⃣ Análise exploratória com gráficos salvos
# ===========================

# Função auxiliar para salvar gráfico
def salvar_grafico(fig, nome):
    fig.savefig(os.path.join(output_dir, nome), bbox_inches='tight')
    plt.close(fig)

# Distribuição de Idade
fig = plt.figure()
sns.histplot(titanic['Age'], bins=30, kde=True)
plt.title("Distribuição de Idade dos Passageiros")
plt.xlabel("Idade")
plt.ylabel("Quantidade")
salvar_grafico(fig, "idade.png")

# Distribuição por Classe
fig = plt.figure()
sns.countplot(x='Pclass', data=titanic)
plt.title("Quantidade de Passageiros por Classe")
salvar_grafico(fig, "classe.png")

# Sobrevivência por Sexo
fig = plt.figure()
sns.countplot(x='Sex', hue='Survived', data=titanic)
plt.title("Sobrevivência por Sexo")
salvar_grafico(fig, "sobrevivencia_sexo.png")

# Sobrevivência por Classe
fig = plt.figure()
sns.countplot(x='Pclass', hue='Survived', data=titanic)
plt.title("Sobrevivência por Classe")
salvar_grafico(fig, "sobrevivencia_classe.png")

# Boxplot Idade x Sobrevivência
fig = plt.figure()
sns.boxplot(x='Survived', y='Age', data=titanic)
plt.title("Idade x Sobrevivência")
salvar_grafico(fig, "idade_sobrevivencia.png")

# Correlação entre variáveis numéricas
fig = plt.figure(figsize=(10,8))
corr = titanic.select_dtypes(include=np.number).corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Mapa de Correlação")
salvar_grafico(fig, "correlacao.png")

# ===========================
# 5️⃣ Insights rápidos
# ===========================
total_passageiros = len(titanic)
sobreviventes = titanic['Survived'].sum()
percentual_sobreviventes = (sobreviventes / total_passageiros) * 100

print(f"Total de passageiros: {total_passageiros}")
print(f"Total de sobreviventes: {sobreviventes}")
print(f"Percentual de sobreviventes: {percentual_sobreviventes:.2f}%")

print(f"\nTodos os gráficos foram salvos na pasta '{output_dir}'")

