# Projeto Data Science – Análise Exploratória de Dados do Titanic

## 1. Objetivo
O objetivo deste projeto é realizar uma **Análise Exploratória de Dados (AED)** com a base de dados do Titanic, buscando identificar padrões, relações entre variáveis e fatores que influenciam a **sobrevivência dos passageiros**.

---

## 2. Estrutura dos arquivos

- `titanic.csv` → Base de dados original.  
- `aed_titanic.py` → Código Python com toda a análise e geração de gráficos.  
- `graficos/` → Pasta contendo todos os gráficos gerados automaticamente pelo script:
  - `idade.png`  
  - `classe.png`  
  - `sobrevivencia_sexo.png`  
  - `sobrevivencia_classe.png`  
  - `idade_sobrevivencia.png`  
  - `correlacao.png`  
- `README.md` → Documento de entrega com descrição do projeto.

> Observação: Pastas vazias não foram incluídas na entrega, apenas os arquivos necessários para o funcionamento do projeto.

---

## 3. Etapas do projeto

1. **Importação dos dados**  
   - Utilizando `pandas` para leitura do arquivo CSV.

2. **Compreensão do conjunto de dados**  
   - Verificação das colunas, tipos de dados, valores nulos e estatísticas descritivas.

3. **Tratamento e preparação dos dados**  
   - Preenchimento de valores nulos em `Age` com a mediana e `Embarked` com a moda.  
   - Remoção de colunas irrelevantes (`Cabin`, `Ticket`).  
   - Ajuste de tipagem das colunas quando necessário.

4. **Análise exploratória**  
   - Compreensão das variáveis com contagens, médias e filtros.  
   - Agrupamentos com `GroupBy` para analisar sobrevivência por classe e sexo.  
   - Construção de gráficos para visualizar distribuição e relações entre variáveis.

---

## 4. Principais decisões durante a análise

- Colunas `Cabin` e `Ticket` foram removidas por possuírem muitos valores nulos ou pouco significado para a análise.  
- Valores nulos em `Age` foram preenchidos pela mediana, pois a distribuição possui outliers.  
- Valores nulos em `Embarked` foram preenchidos com a moda.  
- Todas as análises gráficas foram geradas utilizando `matplotlib` e `seaborn`.

---

## 5. Insights obtidos

- **Classe e sobrevivência:** Passageiros da 1ª classe tiveram maior taxa de sobrevivência em comparação às demais classes.  
- **Sexo e sobrevivência:** Mulheres sobreviveram em maior proporção que homens.  
- **Idade:** A idade média dos sobreviventes é aproximadamente XX anos.  
- **Relações gerais:** [Adicione aqui outros insights que você identificou, como correlação entre variáveis, padrões em `SibSp` ou `Parch`, etc.]

---

## 6. Como rodar o projeto

1. Certifique-se que `titanic.csv` e `aed_titanic.py` estão na **mesma pasta**.  
2. Abra o terminal na pasta do projeto.  
3. Execute o script:

```bash
python aed_titanic.py
