import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

sys.path.append(os.path.dirname(__file__))
from data_processing import load_happiness_data, load_co2_data


def main():
    print("="*60)
    print("INSIGHT 7: CATCHING-UP SUSTENTÁVEL")
    print("="*60)
    
    df_happiness = load_happiness_data()
    df_co2 = load_co2_data()
    
    happiness_2015 = df_happiness[df_happiness['Year'] == 2015][['Country', 'Score', 'GDP']].copy()
    happiness_2019 = df_happiness[df_happiness['Year'] == 2019][['Country', 'Score']].copy()
    
    happiness_2015.rename(columns={'Score': 'Happiness_2015', 'GDP': 'GDP_2015'}, inplace=True)
    happiness_2019.rename(columns={'Score': 'Happiness_2019'}, inplace=True)
    
    co2_2015 = df_co2[df_co2['Year'] == 2015][['Country', 'CO2_Emissions']].copy()
    co2_2019 = df_co2[df_co2['Year'] == 2019][['Country', 'CO2_Emissions']].copy()
    
    co2_2015.rename(columns={'CO2_Emissions': 'CO2_2015'}, inplace=True)
    co2_2019.rename(columns={'CO2_Emissions': 'CO2_2019'}, inplace=True)
    
    df = pd.merge(happiness_2015, happiness_2019, on='Country', how='inner')
    df = pd.merge(df, co2_2015, on='Country', how='inner')
    df = pd.merge(df, co2_2019, on='Country', how='inner')
    
    df_clean = df.dropna()
    
    df_clean['Delta_Happiness'] = df_clean['Happiness_2019'] - df_clean['Happiness_2015']
    df_clean['Delta_CO2'] = df_clean['CO2_2019'] - df_clean['CO2_2015']
    
    df_clean = df_clean[df_clean['Delta_Happiness'] != 0].copy()
    df_clean['Intensidade_Carbono'] = df_clean['Delta_CO2'] / df_clean['Delta_Happiness']
    
    df_clean['Quartil_PIB'] = pd.qcut(df_clean['GDP_2015'], q=4, labels=['Q1-Pobres', 'Q2-Baixo', 'Q3-Médio', 'Q4-Ricos'])
    
    print(f"\nDados: {len(df_clean)} países\n")
    
    print("INTENSIDADE DE CARBONO DA FELICIDADE (ΔCO2 / ΔHappiness):")
    print("-" * 60)
    print("Quanto CO2 aumenta para cada ponto de felicidade ganho")
    print("Valores NEGATIVOS = aumentou felicidade E reduziu CO2 (ideal!)")
    print("Valores POSITIVOS = aumentou felicidade MAS aumentou CO2\n")
    
    for quartil in ['Q1-Pobres', 'Q2-Baixo', 'Q3-Médio', 'Q4-Ricos']:
        subset = df_clean[df_clean['Quartil_PIB'] == quartil]
        media = subset['Intensidade_Carbono'].mean()
        mediana = subset['Intensidade_Carbono'].median()
        print(f"{quartil:15s} | Média: {media:+,.0f} | Mediana: {mediana:+,.0f}")
    
    fig, ax = plt.subplots(figsize=(12, 7))
    
    colors_map = {'Q1-Pobres': '#e74c3c', 'Q2-Baixo': '#f39c12', 
                  'Q3-Médio': '#27ae60', 'Q4-Ricos': '#3498db'}
    
    ax.axhline(y=0, color='gray', linestyle='-', linewidth=2, alpha=0.5, zorder=1)
    ax.axvline(x=0, color='gray', linestyle='-', linewidth=2, alpha=0.5, zorder=1)
    
    ax.fill_between([-1, 1], [0, 0], [50000, 50000], alpha=0.1, color='red', zorder=0)
    ax.fill_between([-1, 1], [-50000, -50000], [0, 0], alpha=0.1, color='green', zorder=0)
    
    ax.text(0.5, 35000, 'Zona Ruim\n↑Felicidade + ↑CO2', ha='center', fontsize=10, 
            color='darkred', fontweight='bold', alpha=0.6)
    ax.text(0.5, -35000, 'Zona Ideal\n↑Felicidade + ↓CO2', ha='center', fontsize=10, 
            color='darkgreen', fontweight='bold', alpha=0.6)
    
    for quartil in ['Q1-Pobres', 'Q2-Baixo', 'Q3-Médio', 'Q4-Ricos']:
        subset = df_clean[df_clean['Quartil_PIB'] == quartil]
        ax.scatter(subset['Delta_Happiness'], subset['Delta_CO2'], 
                   label=quartil, alpha=0.8, s=120, 
                   color=colors_map[quartil], edgecolors='black', linewidth=1, zorder=3)
    
    ax.set_xlabel('Mudança na Felicidade (2015-2019)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Mudança nas Emissões de CO2 (2015-2019)', fontsize=12, fontweight='bold')
    ax.set_title('Catching-Up Sustentável: Países Emergentes Conseguem Crescer Mais Limpo?', 
                 fontsize=13, fontweight='bold', pad=20)
    
    ax.legend(fontsize=11, loc='upper left', framealpha=0.95, edgecolor='black')
    ax.grid(alpha=0.3, linestyle='--', linewidth=0.5)
    ax.set_ylim(-50000, 50000)
    ax.set_xlim(-1.2, 1.5)
    
    quadrant_superior_esq = df_clean[(df_clean['Delta_Happiness'] > 0) & (df_clean['Delta_CO2'] < 0)]
    print(f"\n✓ CAMPEÕES SUSTENTÁVEIS (↑felicidade + ↓CO2): {len(quadrant_superior_esq)} países")
    
    plt.tight_layout()
    output_path = os.path.join(os.path.dirname(__file__), '..', 'charts', 'insight_7_grafico.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"\n✓ Gráfico salvo: charts/insight_7_grafico.png")
    plt.close()


if __name__ == "__main__":
    main()
