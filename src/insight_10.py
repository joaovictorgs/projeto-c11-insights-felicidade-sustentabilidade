import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

sys.path.append(os.path.dirname(__file__))
from data_processing import load_happiness_data, load_co2_data


def main():
    print("="*60)
    print("INSIGHT 10: MODELAGEM PREDITIVA - PROJEÇÕES 2025")
    print("="*60)
    
    df_happiness = load_happiness_data()
    df_co2 = load_co2_data()
    
    df_co2_filtered = df_co2[df_co2['Year'].between(2015, 2019)]
    
    df = pd.merge(df_happiness, df_co2_filtered[['Country', 'Year', 'CO2_Emissions']], 
                  on=['Country', 'Year'], how='inner')
    
    df_clean = df[['Country', 'Year', 'Score', 'CO2_Emissions']].dropna()
    
    country_trends = {}
    
    for country in df_clean['Country'].unique():
        country_data = df_clean[df_clean['Country'] == country].sort_values('Year')
        if len(country_data) >= 4:
            
            years = country_data['Year'].values
            happiness = country_data['Score'].values
            co2 = country_data['CO2_Emissions'].values
            
            happiness_coeffs = np.polyfit(years, happiness, 1)
            co2_coeffs = np.polyfit(years, co2, 1)
            
            happiness_slope = happiness_coeffs[0]
            co2_slope = co2_coeffs[0]
            
            happiness_2025 = np.polyval(happiness_coeffs, 2025)
            co2_2025 = np.polyval(co2_coeffs, 2025)
            
            data_2019 = country_data[country_data['Year'] == 2019]
            if len(data_2019) > 0:
                happiness_2019 = data_2019['Score'].iloc[0]
                co2_2019 = data_2019['CO2_Emissions'].iloc[0]
            else:
                happiness_2019 = country_data['Score'].iloc[-1]
                co2_2019 = country_data['CO2_Emissions'].iloc[-1]
            
            country_trends[country] = {
                'happiness_slope': happiness_slope,
                'co2_slope': co2_slope,
                'happiness_2019': happiness_2019,
                'co2_2019': co2_2019,
                'happiness_2025': happiness_2025,
                'co2_2025': max(0, co2_2025)
            }
    
    df_trends = pd.DataFrame(country_trends).T
    df_trends.index.name = 'Country'
    df_trends = df_trends.reset_index()
    
    def classify_trajectory(row):
        h_slope = row['happiness_slope']
        c_slope = row['co2_slope']
        
        if h_slope > 0 and c_slope < 0:
            return 'IDEAL'
        elif h_slope > 0 and c_slope > 0:
            return 'TRADE-OFF'
        elif h_slope < 0 and c_slope > 0:
            return 'PREOCUPANTE'
        else:
            return 'ESTAGNAÇÃO'
    
    df_trends['trajectory'] = df_trends.apply(classify_trajectory, axis=1)
    
    print(f"\nPaíses analisados: {len(df_trends)}")
    
    trajectory_counts = df_trends['trajectory'].value_counts()
    print(f"\nDistribuição de Trajetórias:")
    for traj, count in trajectory_counts.items():
        print(f"  {traj}: {count} países ({count/len(df_trends)*100:.1f}%)")
    
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    
    colors = {'IDEAL': 'green', 'TRADE-OFF': 'orange', 'PREOCUPANTE': 'red', 'ESTAGNAÇÃO': 'gray'}
    
    ax1 = axes[0, 0]
    for traj in df_trends['trajectory'].unique():
        subset = df_trends[df_trends['trajectory'] == traj]
        ax1.scatter(subset['happiness_slope'], subset['co2_slope'], 
                   color=colors[traj], label=f'{traj} ({len(subset)})', 
                   alpha=0.7, s=60, edgecolors='black', linewidth=0.5)
    
    ax1.axhline(y=0, color='black', linestyle='--', alpha=0.7)
    ax1.axvline(x=0, color='black', linestyle='--', alpha=0.7)
    ax1.set_xlabel('Tendência de Felicidade (slope)')
    ax1.set_ylabel('Tendência de CO2 (slope)')
    ax1.set_title('Classificação de Trajetórias (2015-2019)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    ax1.text(0.02, 0.98, 'Q2: TRADE-OFF\n↑Felicidade ↑CO2', transform=ax1.transAxes, 
             bbox=dict(boxstyle='round', facecolor='orange', alpha=0.7), 
             verticalalignment='top', fontsize=9)
    ax1.text(0.02, 0.02, 'Q3: PREOCUPANTE\n↓Felicidade ↑CO2', transform=ax1.transAxes, 
             bbox=dict(boxstyle='round', facecolor='red', alpha=0.7), 
             verticalalignment='bottom', fontsize=9)
    ax1.text(0.72, 0.98, 'Q1: IDEAL\n↑Felicidade ↓CO2', transform=ax1.transAxes, 
             bbox=dict(boxstyle='round', facecolor='green', alpha=0.7), 
             verticalalignment='top', fontsize=9)
    ax1.text(0.72, 0.02, 'Q4: ESTAGNAÇÃO\n↓Felicidade ↓CO2', transform=ax1.transAxes, 
             bbox=dict(boxstyle='round', facecolor='gray', alpha=0.7), 
             verticalalignment='bottom', fontsize=9)
    
    ax2 = axes[0, 1]
    wedges, texts, autotexts = ax2.pie(trajectory_counts.values, labels=trajectory_counts.index, 
                                      colors=[colors[x] for x in trajectory_counts.index],
                                      autopct='%1.1f%%', startangle=90)
    ax2.set_title('Distribuição de Trajetórias')
    
    ax3 = axes[1, 0]
    ideal_countries = df_trends[df_trends['trajectory'] == 'IDEAL'].head(10)
    if len(ideal_countries) > 0:
        bars = ax3.barh(range(len(ideal_countries)), ideal_countries['happiness_slope'], 
                       color='green', alpha=0.7)
        ax3.set_yticks(range(len(ideal_countries)))
        ax3.set_yticklabels(ideal_countries['Country'], fontsize=8)
        ax3.set_xlabel('Tendência de Felicidade (slope)')
        ax3.set_title('TOP Países com Trajetória IDEAL\n(↑Felicidade ↓CO2)')
        ax3.grid(True, alpha=0.3)
        ax3.invert_yaxis()
    
    ax4 = axes[1, 1]
    preoccupying_countries = df_trends[df_trends['trajectory'] == 'PREOCUPANTE'].head(10)
    if len(preoccupying_countries) > 0:
        bars = ax4.barh(range(len(preoccupying_countries)), preoccupying_countries['co2_slope'], 
                       color='red', alpha=0.7)
        ax4.set_yticks(range(len(preoccupying_countries)))
        ax4.set_yticklabels(preoccupying_countries['Country'], fontsize=8)
        ax4.set_xlabel('Tendência de CO2 (slope)')
        ax4.set_title('Países com Trajetória PREOCUPANTE\n(↓Felicidade ↑CO2)')
        ax4.grid(True, alpha=0.3)
        ax4.invert_yaxis()
    
    plt.tight_layout()
    plt.savefig('insight_10_projecoes_2025.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print(f"\nPROJEÇÕES PARA 2025 - TOP 5 POR CATEGORIA:")
    print("="*60)
    
    for traj in ['IDEAL', 'TRADE-OFF', 'PREOCUPANTE', 'ESTAGNAÇÃO']:
        subset = df_trends[df_trends['trajectory'] == traj]
        if len(subset) > 0:
            print(f"\n{traj} ({len(subset)} países):")
            print("-" * 40)
            top_5 = subset.head(5)
            for i, (_, row) in enumerate(top_5.iterrows(), 1):
                print(f"{i}. {row['Country']}")
                print(f"   2019: Felicidade={row['happiness_2019']:.2f}, CO2={row['co2_2019']:.0f}kt")
                print(f"   2025: Felicidade={row['happiness_2025']:.2f}, CO2={row['co2_2025']:.0f}kt")
                print(f"   Tendências: H={row['happiness_slope']:+.3f}/ano, CO2={row['co2_slope']:+.0f}kt/ano")
    
    print(f"\n⚠️  DISCLAIMER: Projeções baseadas em tendências lineares 2015-2019.")
    print(f"    Resultados são exploratórios e não consideram eventos futuros.")
    
    print(f"\n✓ Gráfico salvo: insight_10_projecoes_2025.png")


if __name__ == "__main__":
    main()
