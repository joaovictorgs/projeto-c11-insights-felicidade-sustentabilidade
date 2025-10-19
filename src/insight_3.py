import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
import sys

sys.path.append(os.path.dirname(__file__))
from data_processing import load_happiness_data, load_co2_data


def main():
    print("="*60)
    print("INSIGHT 3: PARADOXO DO DESENVOLVIMENTO - PIB x FELICIDADE x CO2")
    print("="*60)
    
    df_happiness = load_happiness_data()
    df_co2 = load_co2_data()
    
    df_co2_filtered = df_co2[df_co2['Year'] == 2019]
    df_happiness_2019 = df_happiness[df_happiness['Year'] == 2019]
    
    df = pd.merge(df_happiness_2019, df_co2_filtered[['Country', 'CO2_Emissions']], 
                  on='Country', how='inner')
    
    df_clean = df[['GDP', 'Score', 'CO2_Emissions', 'Country']].dropna()
    
    print(f"\nDados 2019: {len(df_clean)} países")
    
    fig = plt.figure(figsize=(18, 12))
    
    ax1 = fig.add_subplot(2, 3, 1)
    ax1.scatter(df_clean['GDP'], df_clean['Score'], alpha=0.7, color='blue', s=50)
    z = np.polyfit(df_clean['GDP'], df_clean['Score'], 1)
    p = np.poly1d(z)
    ax1.plot(df_clean['GDP'], p(df_clean['GDP']), "r--", linewidth=2)
    ax1.set_xlabel('PIB per capita')
    ax1.set_ylabel('Happiness Score')
    ax1.set_title('PIB vs Felicidade')
    ax1.grid(True, alpha=0.3)
    
    ax2 = fig.add_subplot(2, 3, 2)
    ax2.scatter(df_clean['GDP'], df_clean['CO2_Emissions'], alpha=0.7, color='red', s=50)
    z2 = np.polyfit(df_clean['GDP'], df_clean['CO2_Emissions'], 1)
    p2 = np.poly1d(z2)
    ax2.plot(df_clean['GDP'], p2(df_clean['GDP']), "b--", linewidth=2)
    ax2.set_xlabel('PIB per capita')
    ax2.set_ylabel('CO2 Emissions (kt)')
    ax2.set_title('PIB vs CO2')
    ax2.grid(True, alpha=0.3)
    
    ax3 = fig.add_subplot(2, 3, 3)
    ax3.scatter(df_clean['Score'], df_clean['CO2_Emissions'], alpha=0.7, color='green', s=50)
    z3 = np.polyfit(df_clean['Score'], df_clean['CO2_Emissions'], 1)
    p3 = np.poly1d(z3)
    ax3.plot(df_clean['Score'], p3(df_clean['Score']), "orange", linestyle="--", linewidth=2)
    ax3.set_xlabel('Happiness Score')
    ax3.set_ylabel('CO2 Emissions (kt)')
    ax3.set_title('Felicidade vs CO2')
    ax3.grid(True, alpha=0.3)
    
    ax4 = fig.add_subplot(2, 3, 4, projection='3d')
    scatter = ax4.scatter(df_clean['GDP'], df_clean['Score'], df_clean['CO2_Emissions'], 
                         c=df_clean['CO2_Emissions'], cmap='RdYlGn_r', s=60, alpha=0.8)
    ax4.set_xlabel('PIB per capita')
    ax4.set_ylabel('Happiness Score')
    ax4.set_zlabel('CO2 Emissions (kt)')
    ax4.set_title('Análise 3D: PIB x Felicidade x CO2')
    
    df_clean['GDP_quartile'] = pd.qcut(df_clean['GDP'], 4, labels=['Q1-Baixo', 'Q2-Médio-Baixo', 'Q3-Médio-Alto', 'Q4-Alto'])
    
    ax5 = fig.add_subplot(2, 3, 5)
    quartile_co2 = df_clean.groupby('GDP_quartile')['CO2_Emissions'].mean()
    quartile_happiness = df_clean.groupby('GDP_quartile')['Score'].mean()
    
    colors = ['red', 'orange', 'yellow', 'green']
    bars1 = ax5.bar([x - 0.2 for x in range(len(quartile_co2))], quartile_co2.values, 
                   width=0.4, color=colors, alpha=0.7, label='CO2 Médio (kt)')
    
    ax5_twin = ax5.twinx()
    bars2 = ax5_twin.bar([x + 0.2 for x in range(len(quartile_happiness))], quartile_happiness.values, 
                        width=0.4, color='blue', alpha=0.7, label='Felicidade Média')
    
    ax5.set_xlabel('Quartil de PIB')
    ax5.set_ylabel('CO2 Emissions (kt)', color='red')
    ax5_twin.set_ylabel('Happiness Score', color='blue')
    ax5.set_title('CO2 e Felicidade por Quartil de PIB')
    ax5.set_xticks(range(len(quartile_co2)))
    ax5.set_xticklabels(quartile_co2.index, rotation=45)
    ax5.grid(True, alpha=0.3)
    
    df_clean['efficiency'] = df_clean['Score'] / (df_clean['CO2_Emissions'] / 1000 + 1)
    top_efficient = df_clean.nlargest(10, 'efficiency')
    bottom_efficient = df_clean.nsmallest(10, 'efficiency')
    
    ax6 = fig.add_subplot(2, 3, 6)
    ax6.scatter(top_efficient['GDP'], top_efficient['Score'], 
               color='green', label='Top 10 Eficientes', s=80, alpha=0.8)
    ax6.scatter(bottom_efficient['GDP'], bottom_efficient['Score'], 
               color='red', label='Bottom 10 Eficientes', s=80, alpha=0.8)
    ax6.set_xlabel('PIB per capita')
    ax6.set_ylabel('Happiness Score')
    ax6.set_title('Países Eficientes vs Ineficientes')
    ax6.legend()
    ax6.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    plt.figure(figsize=(10, 8))
    plt.scatter(df_clean['GDP'], df_clean['Score'], alpha=0.7, color='blue', s=50)
    z = np.polyfit(df_clean['GDP'], df_clean['Score'], 1)
    p = np.poly1d(z)
    plt.plot(df_clean['GDP'], p(df_clean['GDP']), "r--", linewidth=2)
    plt.xlabel('PIB per capita')
    plt.ylabel('Happiness Score')
    plt.title('PIB vs Felicidade')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('charts/insight_3_grafico_1_pib_vs_felicidade.jpg', dpi=300, bbox_inches='tight')
    plt.close()
    
    plt.figure(figsize=(10, 8))
    plt.scatter(df_clean['GDP'], df_clean['CO2_Emissions'], alpha=0.7, color='red', s=50)
    z2 = np.polyfit(df_clean['GDP'], df_clean['CO2_Emissions'], 1)
    p2 = np.poly1d(z2)
    plt.plot(df_clean['GDP'], p2(df_clean['GDP']), "b--", linewidth=2)
    plt.xlabel('PIB per capita')
    plt.ylabel('CO2 Emissions (kt)')
    plt.title('PIB vs CO2')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('charts/insight_3_grafico_2_pib_vs_co2.jpg', dpi=300, bbox_inches='tight')
    plt.close()
    
    plt.figure(figsize=(10, 8))
    plt.scatter(df_clean['Score'], df_clean['CO2_Emissions'], alpha=0.7, color='green', s=50)
    z3 = np.polyfit(df_clean['Score'], df_clean['CO2_Emissions'], 1)
    p3 = np.poly1d(z3)
    plt.plot(df_clean['Score'], p3(df_clean['Score']), "orange", linestyle="--", linewidth=2)
    plt.xlabel('Happiness Score')
    plt.ylabel('CO2 Emissions (kt)')
    plt.title('Felicidade vs CO2')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('charts/insight_3_grafico_3_felicidade_vs_co2.jpg', dpi=300, bbox_inches='tight')
    plt.close()
    
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter(df_clean['GDP'], df_clean['Score'], df_clean['CO2_Emissions'], 
                         c=df_clean['CO2_Emissions'], cmap='RdYlGn_r', s=60, alpha=0.8)
    ax.set_xlabel('PIB per capita')
    ax.set_ylabel('Happiness Score')
    ax.set_zlabel('CO2 Emissions (kt)')
    ax.set_title('Análise 3D: PIB x Felicidade x CO2')
    plt.colorbar(scatter, ax=ax, label='CO2 Emissions (kt)')
    plt.tight_layout()
    plt.savefig('charts/insight_3_grafico_4_analise_3d.jpg', dpi=300, bbox_inches='tight')
    plt.close()
    
    df_clean['GDP_quartile'] = pd.qcut(df_clean['GDP'], 4, labels=['Q1-Baixo', 'Q2-Médio-Baixo', 'Q3-Médio-Alto', 'Q4-Alto'])
    
    fig, ax1 = plt.subplots(figsize=(12, 8))
    quartile_co2 = df_clean.groupby('GDP_quartile')['CO2_Emissions'].mean()
    quartile_happiness = df_clean.groupby('GDP_quartile')['Score'].mean()
    
    colors = ['red', 'orange', 'yellow', 'green']
    bars1 = ax1.bar([x - 0.2 for x in range(len(quartile_co2))], quartile_co2.values, 
                   width=0.4, color=colors, alpha=0.7, label='CO2 Médio (kt)')
    
    ax2 = ax1.twinx()
    bars2 = ax2.bar([x + 0.2 for x in range(len(quartile_happiness))], quartile_happiness.values, 
                        width=0.4, color='blue', alpha=0.7, label='Felicidade Média')
    
    ax1.set_xlabel('Quartil de PIB')
    ax1.set_ylabel('CO2 Emissions (kt)', color='red')
    ax2.set_ylabel('Happiness Score', color='blue')
    ax1.set_title('CO2 e Felicidade por Quartil de PIB')
    ax1.set_xticks(range(len(quartile_co2)))
    ax1.set_xticklabels(quartile_co2.index, rotation=45)
    ax1.grid(True, alpha=0.3)
    
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    plt.tight_layout()
    plt.savefig('charts/insight_3_grafico_5_quartis_pib.jpg', dpi=300, bbox_inches='tight')
    plt.close()
    
    df_clean['efficiency'] = df_clean['Score'] / (df_clean['CO2_Emissions'] / 1000 + 1)
    top_efficient = df_clean.nlargest(10, 'efficiency')
    bottom_efficient = df_clean.nsmallest(10, 'efficiency')
    
    plt.figure(figsize=(10, 8))
    plt.scatter(top_efficient['GDP'], top_efficient['Score'], 
               color='green', label='Top 10 Eficientes', s=80, alpha=0.8)
    plt.scatter(bottom_efficient['GDP'], bottom_efficient['Score'], 
               color='red', label='Bottom 10 Eficientes', s=80, alpha=0.8)
    plt.xlabel('PIB per capita')
    plt.ylabel('Happiness Score')
    plt.title('Países Eficientes vs Ineficientes')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('charts/insight_3_grafico_6_eficientes_vs_ineficientes.jpg', dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"\nTOP 5 PAÍSES EFICIENTES (Alta felicidade, baixo CO2):")
    print("-" * 50)
    for i, (_, row) in enumerate(top_efficient.head().iterrows(), 1):
        print(f"{i}. {row['Country']}: Felicidade={row['Score']:.2f}, CO2={row['CO2_Emissions']:.0f}kt")
    
    print(f"\nBOTTOM 5 PAÍSES INEFICIENTES:")
    print("-" * 50)
    for i, (_, row) in enumerate(bottom_efficient.head().iterrows(), 1):
        print(f"{i}. {row['Country']}: Felicidade={row['Score']:.2f}, CO2={row['CO2_Emissions']:.0f}kt")
    
    print(f"\n✓ 6 gráficos salvos em charts/:")
    print(f"  - insight_3_grafico_1_pib_vs_felicidade.jpg")
    print(f"  - insight_3_grafico_2_pib_vs_co2.jpg")
    print(f"  - insight_3_grafico_3_felicidade_vs_co2.jpg")
    print(f"  - insight_3_grafico_4_analise_3d.jpg")
    print(f"  - insight_3_grafico_5_quartis_pib.jpg")
    print(f"  - insight_3_grafico_6_eficientes_vs_ineficientes.jpg")


if __name__ == "__main__":
    main()
