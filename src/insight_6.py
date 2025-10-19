import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

sys.path.append(os.path.dirname(__file__))
from data_processing import load_happiness_data, load_co2_data


def main():
    print("="*60)
    print("INSIGHT 6: TRAJETÓRIA TEMPORAL - FELIZES vs INFELIZES")
    print("="*60)
    
    df_happiness = load_happiness_data()
    df_co2 = load_co2_data()
    
    df_co2_filtered = df_co2[df_co2['Year'].between(2015, 2019)]
    
    df = pd.merge(df_happiness, df_co2_filtered[['Country', 'Year', 'CO2_Emissions']], 
                  on=['Country', 'Year'], how='inner')
    
    df_clean = df[['Country', 'Year', 'Score', 'CO2_Emissions']].dropna()
    
    happiness_avg = df_clean.groupby('Country')['Score'].mean()
    
    top_20_pct = happiness_avg.quantile(0.8)
    bottom_20_pct = happiness_avg.quantile(0.2)
    
    happy_countries = happiness_avg[happiness_avg >= top_20_pct].index.tolist()
    unhappy_countries = happiness_avg[happiness_avg <= bottom_20_pct].index.tolist()
    
    df_happy = df_clean[df_clean['Country'].isin(happy_countries)]
    df_unhappy = df_clean[df_clean['Country'].isin(unhappy_countries)]
    
    print(f"\nPaíses Felizes (Top 20%): {len(happy_countries)}")
    print(f"Países Infelizes (Bottom 20%): {len(unhappy_countries)}")
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    
    happy_yearly = df_happy.groupby('Year')['CO2_Emissions'].mean()
    unhappy_yearly = df_unhappy.groupby('Year')['CO2_Emissions'].mean()
    
    ax1 = axes[0, 0]
    ax1.plot(happy_yearly.index, happy_yearly.values, 'o-', 
             color='green', linewidth=3, markersize=8, label=f'Países Felizes (n={len(happy_countries)})')
    ax1.plot(unhappy_yearly.index, unhappy_yearly.values, 'o-', 
             color='red', linewidth=3, markersize=8, label=f'Países Infelizes (n={len(unhappy_countries)})')
    ax1.set_xlabel('Ano')
    ax1.set_ylabel('CO2 Médio (kt)')
    ax1.set_title('Evolução das Emissões de CO2\nPaíses Felizes vs Infelizes')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    happy_change = []
    unhappy_change = []
    
    for country in happy_countries:
        country_data = df_happy[df_happy['Country'] == country].sort_values('Year')
        if len(country_data) >= 3:
            change = (country_data['CO2_Emissions'].iloc[-1] - country_data['CO2_Emissions'].iloc[0]) / country_data['CO2_Emissions'].iloc[0] * 100
            happy_change.append(change)
    
    for country in unhappy_countries:
        country_data = df_unhappy[df_unhappy['Country'] == country].sort_values('Year')
        if len(country_data) >= 3:
            change = (country_data['CO2_Emissions'].iloc[-1] - country_data['CO2_Emissions'].iloc[0]) / country_data['CO2_Emissions'].iloc[0] * 100
            unhappy_change.append(change)
    
    ax2 = axes[0, 1]
    ax2.boxplot([happy_change, unhappy_change], 
                labels=['Países Felizes', 'Países Infelizes'],
                patch_artist=True,
                boxprops=dict(facecolor='lightblue', alpha=0.7),
                medianprops=dict(color='red', linewidth=2))
    ax2.set_ylabel('Variação % CO2 (2015-2019)')
    ax2.set_title('Distribuição da Variação de CO2')
    ax2.grid(True, alpha=0.3)
    ax2.axhline(y=0, color='black', linestyle='--', alpha=0.7)
    
    years = [2015, 2016, 2017, 2018, 2019]
    co2_diff_by_year = []
    
    for year in years:
        happy_year = df_happy[df_happy['Year'] == year]['CO2_Emissions'].mean()
        unhappy_year = df_unhappy[df_unhappy['Year'] == year]['CO2_Emissions'].mean()
        diff = happy_year - unhappy_year
        co2_diff_by_year.append(diff)
    
    ax3 = axes[1, 0]
    colors = ['green' if x > 0 else 'red' for x in co2_diff_by_year]
    bars = ax3.bar(years, co2_diff_by_year, color=colors, alpha=0.7, edgecolor='black')
    ax3.set_xlabel('Ano')
    ax3.set_ylabel('Diferença CO2 (Felizes - Infelizes)')
    ax3.set_title('Gap de Emissões entre Grupos por Ano')
    ax3.grid(True, alpha=0.3)
    ax3.axhline(y=0, color='black', linestyle='--', linewidth=2)
    
    for bar, value in zip(bars, co2_diff_by_year):
        ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + (5000 if value > 0 else -8000),
                f'{value:.0f}', ha='center', va='bottom' if value > 0 else 'top', fontweight='bold')
    
    sample_happy = df_happy[df_happy['Country'].isin(happy_countries[:5])]
    sample_unhappy = df_unhappy[df_unhappy['Country'].isin(unhappy_countries[:5])]
    
    ax4 = axes[1, 1]
    
    for country in sample_happy['Country'].unique():
        country_data = sample_happy[sample_happy['Country'] == country].sort_values('Year')
        ax4.plot(country_data['Year'], country_data['CO2_Emissions'], 
                'o-', alpha=0.7, color='green', linewidth=2)
    
    for country in sample_unhappy['Country'].unique():
        country_data = sample_unhappy[sample_unhappy['Country'] == country].sort_values('Year')
        ax4.plot(country_data['Year'], country_data['CO2_Emissions'], 
                'o-', alpha=0.7, color='red', linewidth=2)
    
    ax4.set_xlabel('Ano')
    ax4.set_ylabel('CO2 Emissions (kt)')
    ax4.set_title('Trajetórias Individuais (Amostra de 5 países cada)')
    ax4.grid(True, alpha=0.3)
    
    from matplotlib.lines import Line2D
    legend_elements = [Line2D([0], [0], color='green', lw=2, label='Países Felizes'),
                      Line2D([0], [0], color='red', lw=2, label='Países Infelizes')]
    ax4.legend(handles=legend_elements)
    
    plt.tight_layout()
    plt.savefig('insight_6_trajetoria_temporal.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print(f"\nRESUMO DA ANÁLISE:")
    print("-" * 50)
    print(f"Variação média CO2 - Países Felizes: {np.mean(happy_change):+.1f}%")
    print(f"Variação média CO2 - Países Infelizes: {np.mean(unhappy_change):+.1f}%")
    print(f"Diferença: {np.mean(happy_change) - np.mean(unhappy_change):+.1f} pontos percentuais")
    
    print(f"\nPAÍSES FELIZES (Top 20%):")
    print("-" * 30)
    for i, country in enumerate(happy_countries[:10], 1):
        happiness_score = happiness_avg[country]
        print(f"{i:2d}. {country} (Felicidade: {happiness_score:.2f})")
    
    print(f"\nPAÍSES INFELIZES (Bottom 20%):")
    print("-" * 30)
    for i, country in enumerate(unhappy_countries[:10], 1):
        happiness_score = happiness_avg[country]
        print(f"{i:2d}. {country} (Felicidade: {happiness_score:.2f})")
    
    print(f"\n✓ Gráfico salvo: insight_6_trajetoria_temporal.png")


if __name__ == "__main__":
    main()
