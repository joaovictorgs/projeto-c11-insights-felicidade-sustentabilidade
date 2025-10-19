# Projeto C11: Felicidade e Sustentabilidade

## Resumo do Projeto

Este projeto analisa a relação entre felicidade e sustentabilidade ambiental através de dados do World Happiness Report (2015-2019) e emissões de CO2 por país.

## Dados Utilizados

- World Happiness Report (2015-2019): 782 registros de 170 países
- Emissões de CO2 (1960-2019): 13.953 registros de 256 países

## Insights Analisados

### Insight 1 ✅

**Pergunta:** Países com maiores índices de felicidade apresentam menores emissões de CO2 per capita? Qual é a força e direção dessa correlação no período 2015-2019?

**Metodologia:**

- Correlação de Pearson entre Happiness Score e emissões de CO2
- Análise de 673 observações (países × anos 2015-2019)
- Análise temporal ano a ano
- Comparação entre países mais felizes vs menos felizes

**Resultados:**

| Métrica Principal | Valor       |
| ----------------- | ----------- |
| Correlação Geral  | +0.0721     |
| Força             | Muito fraca |
| Direção           | Positiva    |

**Evolução Temporal da Correlação:**

- 2015: +0.0701
- 2016: +0.0689
- 2017: +0.0745
- 2018: +0.0698
- 2019: +0.0763

**CO2 Médio por Nível de Felicidade (2019):**

- **Baixa Felicidade**: 47.580 kt
- **Média-Baixa**: 158.934 kt
- **Média-Alta**: 136.842 kt
- **Alta Felicidade**: 203.029 kt

**Análise:**

- **Correlação positiva muito fraca** (+0.0721) indica que países mais felizes **tendem levemente** a emitir mais CO2, mas a relação é **quase inexistente**
- **Estabilidade temporal**: Correlação mantém-se consistente entre 2015-2019 (0.07±0.003)
- **Padrão não-linear**: Países de felicidade média-baixa emitem mais que média-alta, sugerindo relação complexa
- **Grande variabilidade**: Top 20 países mais felizes vs menos felizes mostram sobreposição significativa nas emissões
- **Conclusão:** **NÃO existe relação linear forte** entre felicidade e CO2. Outros fatores (desenvolvimento econômico, população, geografia) são mais determinantes das emissões que o nível de felicidade per se.

**Visualização:** insight_1_correlacao_felicidade_co2.png

---

### Insight 2 ✅

**Pergunta:** Qual é a contribuição relativa de cada componente da felicidade para as emissões de CO2?

**Metodologia:**

- Correlação de Pearson entre cada componente da felicidade e emissões de CO2
- Análise de 672 observações (países × anos 2015-2019)

**Resultados:**

| Componente      | Correlação | Interpretação                                    |
| --------------- | ---------- | ------------------------------------------------ |
| Life_Expectancy | +0.129     | 🔴 Saúde/longevidade associada a mais emissões   |
| GDP             | +0.114     | 🔴 Desenvolvimento econômico aumenta poluição    |
| Freedom         | +0.094     | 🔴 Liberdades individuais ligadas a mais consumo |
| Family          | +0.031     | 🟡 Suporte social tem impacto mínimo             |
| Trust           | -0.034     | 🟢 Confiança no governo reduz emissões           |
| Generosity      | -0.063     | 🟢 Generosidade é o fator mais sustentável       |

**Análise:**

- **Fatores econômicos e de saúde** (GDP, Life_Expectancy) têm correlação **positiva moderada** com CO2, indicando que desenvolvimento material está associado a maior poluição
- **Valores sociais** (Generosity, Trust) apresentam correlação **negativa fraca**, sugerindo que sociedades mais altruístas/confiantes tendem a poluir menos
- **Nenhum componente tem correlação forte** (todos < 0.15), indicando que a relação felicidade-CO2 é complexa e multifatorial
- **Conclusão:** A felicidade baseada em consumo material aumenta emissões, enquanto felicidade baseada em valores sociais pode ser mais sustentável

**Visualização:** charts/insight_2_grafico.png

---

### Insight 3 ✅

**Pergunta:** Como PIB per capita, felicidade e emissões de CO2 se relacionam simultaneamente? Existe um threshold de PIB onde a felicidade aumenta sem proporcional aumento nas emissões?

**Metodologia:**

- Análise tridimensional PIB × Felicidade × CO2 (dados 2019)
- Divisão em quartis por PIB per capita
- Índice de eficiência: Felicidade / (CO2/1000 + 1)
- Análise de 133 países

**Resultados por Quartil de PIB:**

| Quartil PIB    | CO2 Médio (kt) | Felicidade Média | Padrão                         |
| -------------- | -------------- | ---------------- | ------------------------------ |
| Q1-Baixo       | 15.847         | 4.45             | 🟢 Baixo CO2, felicidade baixa |
| Q2-Médio-Baixo | 38.285         | 5.12             | 🟡 CO2 moderado                |
| Q3-Médio-Alto  | 113.742        | 5.89             | 🟠 CO2 crescente               |
| Q4-Alto        | 394.826        | 6.95             | 🔴 Alto CO2, alta felicidade   |

**Top 5 Países Mais Eficientes:**

1. **Comoros**: Felicidade=3.97, CO2=320kt
2. **Iceland**: Felicidade=7.49, CO2=1.640kt
3. **Somalia**: Felicidade=4.67, CO2=690kt
4. **Malta**: Felicidade=6.73, CO2=1.660kt
5. **Central African Republic**: Felicidade=3.08, CO2=240kt

**Bottom 5 Países Menos Eficientes:**

1. **China**: Felicidade=5.19, CO2=10.707.220kt
2. **United States**: Felicidade=6.89, CO2=4.817.720kt
3. **India**: Felicidade=4.01, CO2=2.456.300kt
4. **Japan**: Felicidade=5.89, CO2=1.081.570kt
5. **Indonesia**: Felicidade=5.19, CO2=619.840kt

**Análise:**

- **Relação PIB-CO2 é mais forte que PIB-Felicidade**: Desenvolvimento econômico está mais associado a poluição que a bem-estar
- **Não existe threshold claro de desacoplamento**: Crescimento do PIB continua associado a aumento de CO2 em todos os quartis
- **Pequenos países insulares dominam eficiência**: Geografia e tamanho populacional são fatores-chave
- **Grandes economias são sistematicamente ineficientes**: Todos os top 5 poluidores têm baixa eficiência
- **Conclusão:** O **"Paradoxo do Desenvolvimento"** é real - não há evidência de Curva de Kuznets Ambiental. PIB alto **NÃO garante** felicidade proporcional, mas **sempre** aumenta CO2. Modelo de desenvolvimento baseado apenas em crescimento econômico é insustentável.

**Visualização:** insight_3_paradoxo_desenvolvimento.png

---

### Insight 4 ✅

**Pergunta:** Quais países são mais 'eficientes' em gerar felicidade com menores emissões de CO2 per capita? Como se distribuem os países eficientes vs ineficientes?

**Metodologia:**

- Índice de Eficiência = Happiness Score / (CO2_per_capita_proxy + 0.1)
- Ranking de 141 países (média 2015-2019)
- Análise de distribuição por níveis de eficiência

**Resultados:**

**Top 10 Países Mais Eficientes:**

1. **Comoros** - Eficiência: 10.94 | Felicidade: 3.96 | CO2: 262kt
2. **Central African Republic** - Eficiência: 9.86 | Felicidade: 3.13 | CO2: 218kt
3. **Djibouti** - Eficiência: 8.34 | Felicidade: 4.37 | CO2: 424kt
4. **Belize** - Eficiência: 7.96 | Felicidade: 5.96 | CO2: 648kt
5. **Somalia** - Eficiência: 6.62 | Felicidade: 5.06 | CO2: 664kt
6. **Lesotho** - Eficiência: 5.05 | Felicidade: 4.08 | CO2: 708kt
7. **Bhutan** - Eficiência: 4.86 | Felicidade: 5.12 | CO2: 954kt
8. **Burundi** - Eficiência: 4.69 | Felicidade: 3.08 | CO2: 556kt
9. **Sierra Leone** - Eficiência: 4.52 | Felicidade: 4.56 | CO2: 908kt
10. **Iceland** - Eficiência: 4.08 | Felicidade: 7.51 | CO2: 1.740kt

**Bottom 10 Países Menos Eficientes:**

1. **China** - Eficiência: 0.00 | Felicidade: 5.22 | CO2: 10.208.384kt
2. **United States** - Eficiência: 0.00 | Felicidade: 7.00 | CO2: 4.899.522kt
3. **India** - Eficiência: 0.00 | Felicidade: 4.30 | CO2: 2.316.382kt
4. **Japan** - Eficiência: 0.01 | Felicidade: 5.93 | CO2: 1.140.036kt
5. **Germany** - Eficiência: 0.01 | Felicidade: 6.93 | CO2: 717.352kt

**Distribuição por Níveis de Eficiência:**

- **Muito Alta**: 20.6% dos países
- **Alta**: 20.6% dos países
- **Média**: 19.9% dos países
- **Baixa**: 19.1% dos países
- **Muito Baixa**: 19.9% dos países

**Análise:**

- **Países pequenos e pobres dominam eficiência**: Top 10 são principalmente nações com baixo desenvolvimento industrial
- **Iceland é exceção notável**: Único país desenvolvido entre os eficientes (energia geotérmica)
- **Grandes economias são sistematicamente ineficientes**: Todas potências mundiais estão no bottom por volume absoluto de emissões
- **Distribuição equilibrada**: Países se distribuem uniformemente entre níveis de eficiência (~20% cada)
- **Paradoxo da eficiência**: Países mais "eficientes" têm felicidade baixa-moderada, sugerindo que alta eficiência pode indicar subdesenvolvimento
- **Conclusão:** Eficiência ambiental está **inversamente correlacionada** com desenvolvimento econômico. O desafio é encontrar modelos como **Iceland** (alta felicidade + baixo CO2) através de energia limpa e economia circular.

**Visualização:** insight_4_eficiencia_ambiental.png

---

### Insight 5 ✅

**Pergunta:** Países que emitiram mais CO2 historicamente são mais felizes hoje?

**Metodologia:**

- Cálculo de emissões cumulativas de CO2 por país (1960-2019)
- Correlação com Score de felicidade em 2019
- Análise de 135 países com dados completos
- Visualização com escala logarítmica para melhor distribuição

**Resultados:**

| Métrica        | Valor       |
| -------------- | ----------- |
| Correlação (r) | +0.136      |
| Força          | Muito fraca |
| Direção        | Positiva    |

**Top 10 Maiores Poluidores Históricos:**

| País           | CO2 Cumulativo (kt) | Felicidade 2019 |
| -------------- | ------------------- | --------------- |
| United States  | 284,036,649         | 6.89 🟢         |
| China          | 215,997,451         | 5.19 🟡         |
| Japan          | 57,260,821          | 5.89 🟡         |
| India          | 48,168,753          | 4.01 🔴         |
| United Kingdom | 32,786,247          | 7.05 🟢         |
| Canada         | 26,093,524          | 7.28 🟢         |
| Germany        | 24,367,020          | 6.99 🟢         |
| France         | 22,960,707          | 6.59 🟢         |
| Italy          | 21,235,506          | 6.22 🟢         |
| Poland         | 19,941,052          | 6.18 🟢         |

**Análise:**

- **Correlação positiva fraca** (r=0.136) indica que países que poluíram mais no passado **tendem levemente** a ser mais felizes hoje, mas a relação é **muito fraca**
- **Países desenvolvidos ocidentais** (EUA, Canadá, Europa) confirmam o padrão: muita poluição histórica → felizes hoje
- **Países asiáticos em desenvolvimento** (China, Índia) quebram o padrão: muita poluição histórica → felicidade moderada/baixa
- **Grande dispersão dos dados** mostra que poluir muito **NÃO garante** felicidade (Índia é 4º maior poluidor mas tem felicidade baixa)
- **Conclusão:** Existe uma "dívida ambiental" onde alguns países desenvolvidos se beneficiaram da industrialização poluente, mas este **NÃO é o único caminho** para felicidade. Países podem ser felizes sem histórico de alta poluição.

**Visualização:** charts/insight_5_grafico.png

---

### Insight 6 ✅

**Pergunta:** Países mais felizes (top 20%) reduziram suas emissões de CO2 per capita mais rapidamente que países menos felizes (bottom 20%) no período 2015-2019?

**Metodologia:**

- Classificação países: Top 20% vs Bottom 20% por felicidade média (2015-2019)
- Análise temporal comparativa das emissões
- Cálculo de variação percentual de CO2 por país
- 29 países felizes vs 29 países infelizes

**Resultados:**

**Grupos Identificados:**

- **Países Felizes (Top 20%)**: 29 países (Argentina, Australia, Austria, Belgium, etc.)
- **Países Infelizes (Bottom 20%)**: 29 países (Afghanistan, Angola, Benin, Botswana, etc.)

**Performance de Redução de CO2:**

- **Países Felizes**: Variação média **-2.5%** (2015-2019)
- **Países Infelizes**: Variação média **+22.4%** (2015-2019)
- **Diferença**: **24.9 pontos percentuais** a favor dos países felizes

**Evolução Temporal (CO2 Médio):**

- **2015**: Felizes: 315.823kt | Infelizes: 26.891kt
- **2019**: Felizes: 307.456kt | Infelizes: 32.941kt

**Gap entre Grupos por Ano:**

- Diferença (Felizes - Infelizes) mantém-se consistente: ~280.000kt
- Países felizes emitem **10x mais** que países infelizes em termos absolutos

**Análise:**

- **Países felizes reduzem emissões, infelizes aumentam**: Clara divergência nas trajetórias temporais
- **Paradoxo do nível vs tendência**: Países felizes emitem mais em termos absolutos, mas **estão reduzindo**; países infelizes emitem menos mas **estão aumentando**
- **Convergência improvável**: Gap absoluto mantém-se estável (~280.000kt) ao longo do período
- **Padrões regionais**: Países felizes (desenvolvidos) implementam políticas ambientais; países infelizes (em desenvolvimento) priorizam crescimento econômico
- **Conclusão:** Existe **desacoplamento temporal** - países com alta qualidade de vida conseguem manter felicidade enquanto reduzem emissões, enquanto países com baixa qualidade de vida ainda estão na fase de crescimento das emissões. Sugere que **políticas ambientais efetivas requerem primeiro um nível mínimo de desenvolvimento socioeconômico**.

**Visualização:** insight_6_trajetoria_temporal.png

---

### Insight 7 ✅

**Pergunta:** Países em desenvolvimento conseguem aumentar felicidade sem aumentar CO2 proporcionalmente?

**Metodologia:**

- Divisão de países em quartis por PIB per capita (2015)
- Cálculo de mudanças na felicidade e CO2 (2015-2019)
- Métrica: "Intensidade de Carbono da Felicidade" = ΔCO2 / ΔHappiness
- Análise de 129 países com dados completos

**Resultados:**

| Quartil PIB | Intensidade Média | Intensidade Mediana | Interpretação                           |
| ----------- | ----------------- | ------------------- | --------------------------------------- |
| Q1-Pobres   | +10,444           | +433                | 🟡 Aumentam CO2 moderadamente           |
| Q2-Baixo    | +394,371          | +2,848              | 🔴 Muito poluente para crescer          |
| Q3-Médio    | -44,341           | -55                 | 🟢 Crescem REDUZINDO CO2!               |
| Q4-Ricos    | +26,561           | -1,819              | 🟢 Mediana negativa (maioria desacopla) |

**Países que Cresceram SEM Poluir:**

- **18 países** conseguiram aumentar felicidade E reduzir CO2 simultaneamente (2015-2019)
- Concentrados principalmente no quartil Q3 (renda média)

**Análise:**

- **Países de renda MÉDIA (Q3) são os campeões do catching-up sustentável** com intensidade negativa (-44,341), conseguindo aumentar felicidade enquanto reduzem emissões
- **Países de renda BAIXA (Q2) apresentam o pior desempenho** com intensidade extremamente alta (+394,371), indicando que estão replicando trajetórias poluentes dos países desenvolvidos
- **Países POBRES (Q1) têm impacto moderado**, com aumento de CO2 controlado durante crescimento
- **Países RICOS (Q4) apresentam padrão misto**: média positiva mas mediana negativa, indicando que a maioria consegue desacoplar crescimento de emissões
- **Conclusão:** Existe uma "janela de oportunidade" no desenvolvimento intermediário (renda média) onde países conseguem fazer catching-up sustentável. Países mais pobres tendem a seguir modelos poluentes tradicionais, sugerindo necessidade de transferência de tecnologias limpas para evitar lock-in em trajetórias insustentáveis.

**Visualização:** charts/insight_7_grafico.png

---

### Insight 8 ✅

**Pergunta:** Indicadores de governança (Freedom, Trust) ajudam a reduzir emissões?

**Metodologia:**

- Cálculo da taxa de redução de CO2 por país (2015-2019)
- Correlação de Pearson entre indicadores de governança (Freedom, Trust) e taxa de redução
- Análise de controle com GDP per capita
- Análise de 140 países com dados completos

**Resultados:**

| Indicador      | Correlação (r) | Interpretação                       |
| -------------- | -------------- | ----------------------------------- |
| Freedom        | -0.041         | 🟡 Efeito negligível                |
| Trust          | -0.121         | 🟢 Efeito negativo fraco            |
| GDP per capita | -0.533         | 🟢 Efeito negativo moderado (forte) |

**Performance de Redução:**

- **45 de 140 países** (32.1%) conseguiram reduzir emissões no período
- **95 de 140 países** (67.9%) aumentaram emissões

**Análise:**

- **Trust tem efeito pequeno mas real** (r=-0.121): Países com maior confiança no governo tendem levemente a reduzir mais emissões
- **Freedom tem efeito quase inexistente** (r=-0.041): Liberdades individuais não impactam significativamente políticas ambientais
- **GDP é o fator mais importante** (r=-0.533): Países ricos conseguem reduzir emissões muito mais que países pobres
- **Governança sozinha não resolve**: Mesmo países com alta governança têm dificuldade de reduzir emissões se não tiverem recursos econômicos
- **Conclusão:** Indicadores de governança têm **impacto limitado** na redução de emissões comparado ao poder econômico. **Trust** importa mais que **Freedom** porque reflete capacidade do governo implementar políticas de longo prazo. O **desenvolvimento econômico** continua sendo o **preditor mais forte** da capacidade de reduzir emissões mantendo qualidade de vida.

**Visualização:** charts/insight_8_grafico.png

---

### Insight 9 ✅

**Pergunta:** Existe um cluster de países com alta felicidade E baixas emissões (modelo nórdico de coesão social)?

**Metodologia:**

- Análise de clustering baseada em 3 dimensões: Family (suporte social), Life_Expectancy (saúde), CO2 (sustentabilidade)
- Critério "Modelo Nórdico": Top 75% em Family E Life_Expectancy E Bottom 25% em CO2
- Análise de dados de 2019 (133 países)
- Identificação de países com alta coesão social + baixas emissões

**Resultados:**

**Clusters Identificados:**

| Cluster                         | Países | % Total | Características                              |
| ------------------------------- | ------ | ------- | -------------------------------------------- |
| 🌟 Modelo Nórdico               | 7      | 5.3%    | Alta felicidade, alta longevidade, baixo CO2 |
| 🏭 Desenvolvidos Insustentáveis | 28     | 21.1%   | Alta felicidade/longevidade, ALTO CO2        |
| 🌱 Em Desenvolvimento           | 98     | 73.7%   | Baixa/média felicidade, baixo/médio CO2      |

**Países do "Modelo Nórdico" (7 países):**

1. **Costa Rica**: Family=1.34, Life_Expectancy=1.10, CO2=7.360kt
2. **Iceland**: Family=1.48, Life_Expectancy=0.95, CO2=1.640kt
3. **Luxembourg**: Family=1.32, Life_Expectancy=1.03, CO2=8.830kt
4. **New Zealand**: Family=1.47, Life_Expectancy=1.03, CO2=31.110kt
5. **Norway**: Family=1.49, Life_Expectancy=1.03, CO2=33.460kt
6. **Singapore**: Family=1.34, Life_Expectancy=1.14, CO2=40.790kt
7. **Switzerland**: Family=1.41, Life_Expectancy=1.09, CO2=33.360kt

**Médias por Cluster:**

| Cluster        | Family (Suporte Social) | Life_Expectancy (Saúde) | CO2 (kt) |
| -------------- | ----------------------- | ----------------------- | -------- |
| Modelo Nórdico | 1.41                    | 1.05                    | 22.364   |
| Desenvolvidos  | 1.27                    | 0.88                    | 277.525  |
| Em Desenv.     | 1.03                    | 0.49                    | 90.238   |

**Análise:**

- **Apenas 5.3% dos países alcançam o "Modelo Nórdico"**: Combinação de alta coesão social + longevidade + baixas emissões é **extremamente rara**
- **Grupo é diverso geograficamente**: Inclui países europeus (Iceland, Norway, Switzerland, Luxembourg), asiáticos (Singapore), oceânicos (New Zealand) e latino-americanos (Costa Rica)
- **Não é exclusivamente nórdico**: Apenas 2 dos 7 países são escandinavos, sugerindo que o modelo é **replicável** em diferentes contextos culturais
- **Diferença dramática nas emissões**: Modelo Nórdico emite **12x menos** que países desenvolvidos tradicionais (22kt vs 278kt), mantendo níveis similares de bem-estar social
- **Coesão social é o diferencial**: Family score médio de 1.41 (vs 1.27 desenvolvidos) indica que **qualidade das relações sociais** substitui consumo material
- **Costa Rica é destaque latino**: Único país em desenvolvimento que alcançou o modelo, mostrando que **não é necessário ser rico** para ser sustentável
- **Conclusão:** O "Modelo Nórdico" existe e é **caracterizado por investimento em coesão social e saúde ao invés de consumo material**. É **replicável** mas **desafiador** - apenas 7 de 133 países conseguiram. Demonstra que é possível ter **alta qualidade de vida com baixo impacto ambiental** quando sociedade prioriza valores coletivos sobre individualismo consumista.

**Visualização:** charts/insight_9_grafico.png

---

### Insight 10 ✅

**Pergunta:** Baseado em tendências 2015-2019, quais países apresentam trajetória IDEAL (↑felicidade + ↓CO2), PREOCUPANTE (↓felicidade + ↑CO2), TRADE-OFF (↑felicidade + ↑CO2) ou ESTAGNAÇÃO (↓felicidade + ↓CO2)?

**Metodologia:**

- Regressão linear (polyfit) para calcular slopes de felicidade e CO2 (2015-2019)
- Classificação em 4 quadrantes por direção das tendências
- Projeção exploratória para 2025
- Análise de 133 países com dados completos

**Resultados:**

**Distribuição de Trajetórias:**

- **TRADE-OFF**: 51 países (38.3%) - ↑Felicidade ↑CO2
- **PREOCUPANTE**: 40 países (30.1%) - ↓Felicidade ↑CO2
- **ESTAGNAÇÃO**: 23 países (17.3%) - ↓Felicidade ↓CO2
- **IDEAL**: 19 países (14.3%) - ↑Felicidade ↓CO2

**Top 5 Países por Trajetória:**

**IDEAL (19 países) - Desenvolvimento Sustentável:**

1. **Bulgaria**: H=+0.230/ano, CO2=-1.153kt/ano | 2025: Felicidade=6.46, CO2=32.790kt
2. **Chad**: H=+0.190/ano, CO2=-30kt/ano | 2025: Felicidade=5.53, CO2=1.998kt
3. **Denmark**: H=+0.017/ano, CO2=-1.019kt/ano | 2025: Felicidade=7.69, CO2=24.844kt
4. **Ecuador**: H=+0.010/ano, CO2=-413kt/ano | 2025: Felicidade=6.07, CO2=36.558kt
5. **Estonia**: H=+0.115/ano, CO2=-1.139kt/ano | 2025: Felicidade=6.56, CO2=5.636kt

**PREOCUPANTE (40 países) - Declínio Insustentável:**

1. **Afghanistan**: H=-0.047/ano, CO2=+103kt/ano
2. **Albania**: H=-0.055/ano, CO2=+105kt/ano
3. **Algeria**: H=-0.185/ano, CO2=+4.059kt/ano
4. **Australia**: H=-0.015/ano, CO2=+1.954kt/ano
5. **Azerbaijan**: H=-0.010/ano, CO2=+797kt/ano

**TRADE-OFF (51 países) - Crescimento Poluente:**

- **Maioria dos países** está nesta categoria
- Incluem nações em desenvolvimento priorizando crescimento econômico

**ESTAGNAÇÃO (23 países) - Recessão:**

- Inclui **Argentina, Brazil, Colombia** com declínio em ambas métricas

**Análise:**

- **Apenas 14.3% dos países seguem trajetória IDEAL** - desenvolvimento sustentável é ainda **exceção, não regra**
- **68.4% dos países** estão em trajetórias problemáticas (Trade-off + Preocupante)
- **Trade-off é o padrão dominante** (38.3%) - países escolhem crescimento à custa do meio ambiente
- **Trajetória Preocupante é alarmante** (30.1%) - declínio social E ambiental simultaneamente
- **Projeções 2025**: Se tendências se mantiverem, gap entre países sustentáveis e insustentáveis irá **aumentar drasticamente**
- **Conclusão:** A **maioria dos países está em trajetórias insustentáveis**. Apenas pequeno grupo (principalmente europeus como Denmark, Estonia) consegue desacoplar felicidade de emissões. **Urgência de mudança de modelo de desenvolvimento** antes que trajetórias se consolidem.

**⚠️ DISCLAIMER:** Projeções baseadas em tendências lineares 2015-2019. Resultados são exploratórios e não consideram eventos futuros.

**Visualização:** insight_10_projecoes_2025.png

## Conclusões Gerais

### Principais Descobertas:

1. **Correlação Felicidade-CO2 é muito fraca** (+0.072) - felicidade não é bom preditor de emissões
2. **Desenvolvimento econômico é o principal driver de emissões**, não felicidade per se
3. **Pequenos países são mais "eficientes"**, mas principalmente por baixo desenvolvimento industrial
4. **Países desenvolvidos conseguem reduzir emissões mantendo felicidade**, países em desenvolvimento ainda aumentam
5. **Apenas 14.3% dos países seguem trajetória sustentável** (↑felicidade ↓CO2)
6. **Componentes materiais da felicidade** (PIB, saúde) **aumentam emissões**; componentes sociais (generosidade, confiança) **reduzem**
7. **Existe "dívida ambiental"** - países que poluíram historicamente são mais felizes hoje
8. **Catching-up sustentável é possível** - países de renda média conseguem crescer reduzindo emissões

### Implicações Políticas:

- **Desenvolvimento sustentável requer mudança de paradigma**: PIB não deve ser único objetivo
- **Priorizar componentes sociais da felicidade** (confiança, generosidade) sobre consumo material
- **Transferência de tecnologia limpa** é crucial para países em desenvolvimento
- **Políticas ambientais efetivas** requerem primeiro nível mínimo de desenvolvimento socioeconômico

## Tecnologias

- Python 3.12
- pandas, numpy, matplotlib
- pipenv (gerenciamento de ambiente)

## Como Executar

```bash
# Instalar dependências
pip install -r requirements.txt python src/insight_n.py (com n sendo o numero do insight desejado)

```
