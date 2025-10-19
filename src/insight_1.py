import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

sys.path.append(os.path.dirname(__file__))
from data_processing import load_happiness_data, load_co2_data


def main():
    print("="*60)
    print("INSIGHT 1: CORRELAÇÃO GLOBAL FELICIDADE x CO2")
    print("="*60)
    
    df_happiness = load_happiness_data()
    df_co2 = load_co2_data()
    
    df_co2_filtered = df_co2[df_co2['Year'].between(2015, 2019)]
    
    df = pd.merge(df_happiness, df_co2_filtered[['Country', 'Year', 'CO2_Emissions']], 
                  on=['Country', 'Year'], how='inner')
    
    df_clean = df[['Score', 'CO2_Emissions', 'Year']].dropna()
    
    print(f"\nDados: {len(df_clean)} observações (2015-2019)")
    
    pearson_corr = np.corrcoef(df_clean['Score'], df_clean['CO2_Emissions'])[0, 1]
    
    print(f"\nCORRELAÇÃO:")
    print(f"Pearson: {pearson_corr:+.4f}")
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    
    ax1 = axes[0, 0]
    ax1.scatter(df_clean['Score'], df_clean['CO2_Emissions'], alpha=0.6, color='blue')
    z = np.polyfit(df_clean['Score'], df_clean['CO2_Emissions'], 1)
    p = np.poly1d(z)
    ax1.plot(df_clean['Score'], p(df_clean['Score']), "r--", linewidth=2)
    ax1.set_xlabel('Happiness Score')
    ax1.set_ylabel('CO2 Emissions (kt)')
    ax1.set_title('Correlação Geral (2015-2019)')
    ax1.grid(True, alpha=0.3)
    
    years_data = {}
    for year in [2015, 2016, 2017, 2018, 2019]:
        year_data = df_clean[df_clean['Year'] == year]
        if len(year_data) > 10:
            corr = np.corrcoef(year_data['Score'], year_data['CO2_Emissions'])[0, 1]
            years_data[year] = corr
    
    ax2 = axes[0, 1]
    years = list(years_data.keys())
    corrs = list(years_data.values())
    ax2.plot(years, corrs, 'o-', linewidth=2, markersize=8, color='green')
    ax2.set_xlabel('Ano')
    ax2.set_ylabel('Correlação de Pearson')
    ax2.set_title('Evolução da Correlação por Ano')
    ax2.grid(True, alpha=0.3)
    ax2.axhline(y=0, color='red', linestyle='--', alpha=0.7)
    
    ax3 = axes[1, 0]
    df_2019 = df_clean[df_clean['Year'] == 2019]
    top_happy = df_2019.nlargest(20, 'Score')
    bottom_happy = df_2019.nsmallest(20, 'Score')
    
    ax3.scatter(top_happy['Score'], top_happy['CO2_Emissions'], 
                color='green', label='Top 20 Mais Felizes', alpha=0.8, s=50)
    ax3.scatter(bottom_happy['Score'], bottom_happy['CO2_Emissions'], 
                color='red', label='Top 20 Menos Felizes', alpha=0.8, s=50)
    ax3.set_xlabel('Happiness Score')
    ax3.set_ylabel('CO2 Emissions (kt)')
    ax3.set_title('Extremos de Felicidade (2019)')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    ax4 = axes[1, 1]
    df_2019_clean = df_clean[df_clean['Year'] == 2019].dropna()
    
    bins_happiness = pd.cut(df_2019_clean['Score'], bins=4, labels=['Baixa', 'Média-Baixa', 'Média-Alta', 'Alta'])
    co2_by_happiness = df_2019_clean.groupby(bins_happiness)['CO2_Emissions'].mean()
    
    colors = ['red', 'orange', 'yellow', 'green']
    bars = ax4.bar(co2_by_happiness.index, co2_by_happiness.values, color=colors, alpha=0.7)
    ax4.set_xlabel('Nível de Felicidade')
    ax4.set_ylabel('CO2 Médio (kt)')
    ax4.set_title('CO2 Médio por Nível de Felicidade (2019)')
    ax4.grid(True, alpha=0.3)
    
    for bar, value in zip(bars, co2_by_happiness.values):
        ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5000,
                f'{value:.0f}', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    
    plt.figure(figsize=(10, 8))
    plt.subplot(2, 2, 1)
    plt.scatter(df_clean['Score'], df_clean['CO2_Emissions'], alpha=0.6, color='blue')
    z = np.polyfit(df_clean['Score'], df_clean['CO2_Emissions'], 1)
    p = np.poly1d(z)
    plt.plot(df_clean['Score'], p(df_clean['Score']), "r--", linewidth=2)
    plt.xlabel('Happiness Score')
    plt.ylabel('CO2 Emissions (kt)')
    plt.title('Correlação Geral (2015-2019)')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('charts/insight_1_grafico_1_correlacao_geral.jpg', dpi=300, bbox_inches='tight')
    plt.close()
    
    plt.figure(figsize=(10, 6))
    years = list(years_data.keys())
    corrs = list(years_data.values())
    plt.plot(years, corrs, 'o-', linewidth=2, markersize=8, color='green')
    plt.xlabel('Ano')
    plt.ylabel('Correlação de Pearson')
    plt.title('Evolução da Correlação por Ano')
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='red', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('charts/insight_1_grafico_2_evolucao_temporal.jpg', dpi=300, bbox_inches='tight')
    plt.close()
    
    plt.figure(figsize=(10, 8))
    df_2019 = df_clean[df_clean['Year'] == 2019]
    top_happy = df_2019.nlargest(20, 'Score')
    bottom_happy = df_2019.nsmallest(20, 'Score')
    
    plt.scatter(top_happy['Score'], top_happy['CO2_Emissions'], 
                color='green', label='Top 20 Mais Felizes', alpha=0.8, s=50)
    plt.scatter(bottom_happy['Score'], bottom_happy['CO2_Emissions'], 
                color='red', label='Top 20 Menos Felizes', alpha=0.8, s=50)
    plt.xlabel('Happiness Score')
    plt.ylabel('CO2 Emissions (kt)')
    plt.title('Extremos de Felicidade (2019)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('charts/insight_1_grafico_3_extremos_felicidade.jpg', dpi=300, bbox_inches='tight')
    plt.close()
    
    plt.figure(figsize=(10, 6))
    df_2019_clean = df_clean[df_clean['Year'] == 2019].dropna()
    
    bins_happiness = pd.cut(df_2019_clean['Score'], bins=4, labels=['Baixa', 'Média-Baixa', 'Média-Alta', 'Alta'])
    co2_by_happiness = df_2019_clean.groupby(bins_happiness)['CO2_Emissions'].mean()
    
    colors = ['red', 'orange', 'yellow', 'green']
    bars = plt.bar(co2_by_happiness.index, co2_by_happiness.values, color=colors, alpha=0.7)
    plt.xlabel('Nível de Felicidade')
    plt.ylabel('CO2 Médio (kt)')
    plt.title('CO2 Médio por Nível de Felicidade (2019)')
    plt.grid(True, alpha=0.3)
    
    for bar, value in zip(bars, co2_by_happiness.values):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5000,
                f'{value:.0f}', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('charts/insight_1_grafico_4_co2_por_nivel.jpg', dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"\n✓ 4 gráficos salvos em charts/:")
    print(f"  - insight_1_grafico_1_correlacao_geral.jpg")
    print(f"  - insight_1_grafico_2_evolucao_temporal.jpg")
    print(f"  - insight_1_grafico_3_extremos_felicidade.jpg")
    print(f"  - insight_1_grafico_4_co2_por_nivel.jpg")


if __name__ == "__main__":
    main()
