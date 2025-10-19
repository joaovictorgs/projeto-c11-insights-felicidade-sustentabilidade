import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

sys.path.append(os.path.dirname(__file__))
from data_processing import load_happiness_data, load_co2_data


def main():
    print("="*60)
    print("INSIGHT 5: DÍVIDA HISTÓRICA")
    print("="*60)
    
    df_happiness = load_happiness_data()
    df_co2 = load_co2_data()
    
    happiness_2019 = df_happiness[df_happiness['Year'] == 2019][['Country', 'Score']].copy()
    happiness_2019.rename(columns={'Score': 'Happiness_2019'}, inplace=True)
    
    co2_historico = df_co2[df_co2['Year'].between(1960, 2019)].copy()
    co2_cumulativo = co2_historico.groupby('Country')['CO2_Emissions'].sum().reset_index()
    co2_cumulativo.rename(columns={'CO2_Emissions': 'CO2_Cumulativo_1960_2019'}, inplace=True)
    
    df = pd.merge(happiness_2019, co2_cumulativo, on='Country', how='inner')
    df_clean = df.dropna()
    
    print(f"\nDados: {len(df_clean)} países\n")
    
    corr = df_clean['CO2_Cumulativo_1960_2019'].corr(df_clean['Happiness_2019'])
    print(f"CORRELAÇÃO: {corr:+.4f}")
    print(f"\nInterpretação:")
    if corr > 0.5:
        print("✓ Países que poluíram mais HISTORICAMENTE são MAIS felizes HOJE")
        print("✓ Correlação FORTE e POSITIVA - existe 'dívida ambiental'")
    elif corr > 0.3:
        print("✓ Países que poluíram mais HISTORICAMENTE tendem a ser mais felizes HOJE")
        print("✓ Correlação MODERADA e POSITIVA")
    else:
        print("✓ Correlação FRACA ou INEXISTENTE")
    
    fig, ax = plt.subplots(figsize=(12, 7))
    
    colors = ['red' if h < 5.0 else 'orange' if h < 6.0 else 'green' 
              for h in df_clean['Happiness_2019']]
    
    ax.scatter(df_clean['CO2_Cumulativo_1960_2019'], 
               df_clean['Happiness_2019'], 
               alpha=0.7, 
               s=100,
               c=colors,
               edgecolors='black',
               linewidth=0.8)
    
    ax.set_xscale('log')
    
    log_co2 = np.log10(df_clean['CO2_Cumulativo_1960_2019'])
    z = np.polyfit(log_co2, df_clean['Happiness_2019'], 1)
    p = np.poly1d(z)
    x_line_log = np.linspace(log_co2.min(), log_co2.max(), 100)
    x_line_original = 10**x_line_log
    ax.plot(x_line_original, p(x_line_log), "b--", linewidth=3, 
            label=f'Tendência (r={corr:.3f})', alpha=0.8)
    
    ax.set_xlabel('Emissões Cumulativas de CO2 1960-2019 (escala log)', 
                  fontsize=12, fontweight='bold')
    ax.set_ylabel('Felicidade em 2019', fontsize=12, fontweight='bold')
    ax.set_title('Dívida Histórica: Países que Poluíram Mais no Passado São Mais Felizes Hoje?', 
                 fontsize=13, fontweight='bold', pad=20)
    
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='green', edgecolor='black', label='Felizes (>6.0)'),
        Patch(facecolor='orange', edgecolor='black', label='Médios (5.0-6.0)'),
        Patch(facecolor='red', edgecolor='black', label='Infelizes (<5.0)'),
        plt.Line2D([0], [0], color='b', linewidth=3, linestyle='--', label=f'Tendência (r={corr:.3f})')
    ]
    ax.legend(handles=legend_elements, fontsize=10, loc='lower right')
    ax.grid(alpha=0.3, which='both')
    
    plt.tight_layout()
    output_path = os.path.join(os.path.dirname(__file__), '..', 'charts', 'insight_5_grafico.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"\n✓ Gráfico salvo: charts/insight_5_grafico.png")
    plt.close()
    
    top10_poluentes = df_clean.nlargest(10, 'CO2_Cumulativo_1960_2019')[['Country', 'CO2_Cumulativo_1960_2019', 'Happiness_2019']]
    print(f"\nTOP 10 MAIORES POLUIDORES HISTÓRICOS:")
    print("-" * 60)
    for idx, row in top10_poluentes.iterrows():
        print(f"{row['Country']:25s} | CO2: {row['CO2_Cumulativo_1960_2019']:,.0f} kt | Felicidade: {row['Happiness_2019']:.2f}")


if __name__ == "__main__":
    main()
