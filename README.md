# Projeto Final - Análise de Felicidade e Sustentabilidade

## 📊 Sobre o Projeto

Este projeto analisa a relação entre felicidade e sustentabilidade ambiental através de 10 insights únicos, utilizando dados do World Happiness Report (2015-2019) e emissões de CO2 por país.

### Datasets Utilizados

- **World Happiness Report (2015-2019)** - Kaggle
- **CO2 Emissions by Country** - Kaggle

## 👥 Divisão de Trabalho

### Integrante 1 (Insights 1, 3, 4, 6, 10)

- Correlações básicas
- Desenvolvimento econômico
- Eficiência ambiental
- Predição temporal

### Integrante 2 (Insights 2, 5, 7, 8, 9)

- Decomposição de componentes
- Justiça climática
- Desigualdade
- Governança
- Perfis sociais

## 📁 Estrutura de Arquivos

```
projeto/
│
├── data-2015.csv                    # Dados de felicidade 2015
├── data-2016.csv                    # Dados de felicidade 2016
├── data-2017.csv                    # Dados de felicidade 2017
├── data-2018.csv                    # Dados de felicidade 2018
├── data-2019.csv                    # Dados de felicidade 2019
├── co2_emissions_kt_by_country.csv  # Dados de emissões CO2
│
├── data_processing.py               # Módulo de processamento de dados
├── insight_2.py                     # Análise do Insight 2 (Integrante 2)
├── insight_5.py                     # Análise do Insight 5 (Integrante 2) [A CRIAR]
├── insight_7.py                     # Análise do Insight 7 (Integrante 2) [A CRIAR]
├── insight_8.py                     # Análise do Insight 8 (Integrante 2) [A CRIAR]
├── insight_9.py                     # Análise do Insight 9 (Integrante 2) [A CRIAR]
│
├── requirements.txt                 # Dependências do projeto
├── README.md                        # Este arquivo
└── PROJETO_FINAL_10_INSIGHTS.txt   # Documentação completa dos insights
```

## 🚀 Como Executar

### 1. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 2. Executar Processamento de Dados

```bash
python data_processing.py
```

Este script irá:

- Carregar todos os datasets (2015-2019)
- Padronizar nomes de colunas
- Mesclar dados de felicidade e CO2
- Calcular CO2 per capita
- Exibir estatísticas descritivas

### 3. Executar Análises dos Insights

#### Insight 2 - Decomposição da Felicidade

```bash
python insight_2.py
```

**Saídas:**

- `insight2_correlation_matrix.png` - Heatmap de correlações
- `insight2_feature_importance.png` - Importância dos componentes
- `insight2_classification.png` - Classificação sustentável vs poluente

## 📋 Insights do Integrante 2

### ⭐ Insight 2: Decomposição da Felicidade

**Dificuldade:** ⭐⭐⭐ (Intermediário)

**Pergunta:** Qual é a contribuição relativa de cada componente da felicidade para as emissões de CO2?

**Métodos:**

- Matriz de correlação
- Regressão linear múltipla
- Coeficientes padronizados
- Classificação de componentes

**Bibliotecas:** pandas, scipy, seaborn, scikit-learn, matplotlib

---

### ⭐ Insight 5: Desigualdade Global - Dívida Ambiental

**Dificuldade:** ⭐⭐⭐⭐ (Avançado)

**Pergunta:** Países que emitiram mais CO2 historicamente são mais felizes hoje?

**Métodos:**

- Emissões cumulativas (1960-2019)
- Análise de justiça climática
- Mapas mundiais

---

### ⭐ Insight 7: Catching-Up Sustentável

**Dificuldade:** ⭐⭐⭐⭐ (Avançado)

**Pergunta:** Países em desenvolvimento podem crescer de forma mais limpa?

**Métodos:**

- Análise de trajetórias
- Intensidade de carbono da felicidade
- Comparação quartis de PIB

---

### ⭐ Insight 8: Governança e Política Ambiental

**Dificuldade:** ⭐⭐⭐⭐ (Avançado)

**Pergunta:** Boa governança prediz redução de emissões?

**Métodos:**

- Regressão com controles
- Análise de mediação
- Controle por PIB

---

### ⭐ Insight 9: Coesão Social e Modelo Nórdico

**Dificuldade:** ⭐⭐⭐ (Intermediário)

**Pergunta:** Existe um "modelo nórdico" de sustentabilidade?

**Métodos:**

- K-means clustering
- Identificação de perfis
- Análise de coesão social

## 📊 Variáveis Disponíveis

### Happiness Dataset

- `Country` - Nome do país
- `Region` - Região geográfica
- `Year` - Ano (2015-2019)
- `Rank` - Ranking de felicidade
- `Happiness_Score` - Score de felicidade
- `GDP_per_capita` - PIB per capita
- `Social_support` - Suporte social
- `Healthy_life_expectancy` - Expectativa de vida saudável
- `Freedom` - Liberdade para fazer escolhas
- `Perceptions_of_corruption` - Percepção de corrupção
- `Generosity` - Generosidade

### CO2 Dataset

- `Country` - Nome do país
- `Year` - Ano
- `CO2_emissions_kt` - Emissões totais de CO2 (kilotons)
- `CO2_per_capita` - Emissões per capita (toneladas/pessoa)

## 📝 Observações Importantes

1. **Dados de População:** O módulo `data_processing.py` contém estimativas de população para cálculo de CO2 per capita

2. **Dados Históricos:** Para análises históricas (Insight 5), o dataset de CO2 contém dados desde 1960

3. **Missing Data:** Alguns países podem não ter dados completos em todos os anos

4. **Padronização:** Todos os nomes de colunas foram padronizados para facilitar a análise

## 🎯 Próximos Passos (Integrante 2)

- [ ] ✅ Criar `data_processing.py`
- [ ] ✅ Criar `insight_2.py`
- [ ] ⬜ Criar `insight_5.py`
- [ ] ⬜ Criar `insight_7.py`
- [ ] ⬜ Criar `insight_8.py`
- [ ] ⬜ Criar `insight_9.py`

## 📧 Contato

Para dúvidas sobre o projeto, consulte o arquivo `PROJETO_FINAL_10_INSIGHTS.txt` com a documentação completa.
