# Projeto C11: Felicidade e Sustentabilidade

## Resumo do Projeto

Este projeto analisa a relação entre felicidade e sustentabilidade ambiental através de dados do World Happiness Report (2015-2019) e emissões de CO2 por país.

## Dados Utilizados

- World Happiness Report (2015-2019): 782 registros de 170 países
- Emissões de CO2 (1960-2019): 13.953 registros de 256 países

## Insights Analisados

### Insight 1 🚧

**Pergunta:** Países mais felizes emitem mais CO2?

**Status:** Não iniciado

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

**Visualização:** insight2_analise.png

---

### Insight 3 🚧

**Pergunta:** Mudanças no Score de felicidade ao longo do tempo impactam as emissões?

**Status:** Não iniciado

---

### Insight 4 🚧

**Pergunta:** A relação entre felicidade e CO2 varia por região?

**Status:** Não iniciado

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

**Visualização:** insight5_analise.png

---

### Insight 6 🚧

**Pergunta:** Existe relação entre variação de CO2 e variação de felicidade?

**Status:** Não iniciado

---

### Insight 7 🚧

**Pergunta:** Países em desenvolvimento conseguem aumentar felicidade sem aumentar CO2 proporcionalmente?

**Status:** Não iniciado

---

### Insight 8 🚧

**Pergunta:** Indicadores de governança (Freedom, Trust) ajudam a reduzir emissões?

**Status:** Não iniciado

---

### Insight 9 🚧

**Pergunta:** Existe um cluster de países com alta felicidade E baixas emissões?

**Status:** Não iniciado

---

### Insight 10 🚧

**Pergunta:** Qual componente da felicidade oferece melhor custo-benefício ambiental?

**Status:** Não iniciado

## Tecnologias

- Python 3.14
- pandas, numpy, matplotlib

## Como Executar

pip install -r requirements.txt
python src/insight_n.py (com n sendo o numero do insight desejado)
