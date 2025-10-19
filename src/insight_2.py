import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

sys.path.append(os.path.dirname(__file__))
from data_processing import load_happiness_data, load_co2_data


def main():
    print("="*60)
    print("INSIGHT 2: DECOMPOSIÇÃO DA FELICIDADE")
    print("="*60)
    
    df_happiness = load_happiness_data()
    df_co2 = load_co2_data()
    
    df_co2_filtered = df_co2[df_co2['Year'].between(2015, 2019)]
    
    df = pd.merge(df_happiness, df_co2_filtered[['Country', 'Year', 'CO2_Emissions']], 
                  on=['Country', 'Year'], how='inner')
    
    components = ['GDP', 'Family', 'Life_Expectancy', 'Freedom', 'Trust', 'Generosity']
    df_clean = df[components + ['CO2_Emissions']].dropna()
    
    print(f"\nDados: {len(df_clean)} observações\n")
    
    print("CORRELAÇÕES COM CO2:")
    print("-" * 60)
    correlations = {}
    for comp in components:
        corr = df_clean[comp].corr(df_clean['CO2_Emissions'])
        correlations[comp] = corr
        print(f"{comp:20s}: {corr:+.4f}")
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    sorted_comps = sorted(correlations.items(), key=lambda x: x[1])
    comps_names = [x[0] for x in sorted_comps]
    comps_values = [x[1] for x in sorted_comps]
    colors = ['green' if v < 0 else 'red' for v in comps_values]
    
    ax.barh(comps_names, comps_values, color=colors, alpha=0.7, edgecolor='black')
    ax.axvline(x=0, color='black', linestyle='--', linewidth=2)
    ax.set_xlabel('Correlação com CO2', fontsize=12, fontweight='bold')
    ax.set_title('Correlação dos Componentes da Felicidade com Emissões de CO2', 
                 fontsize=13, fontweight='bold')
    ax.grid(axis='x', alpha=0.3)
    
    x_min = min(comps_values)
    x_max = max(comps_values)
    margin = (x_max - x_min) * 0.15
    ax.set_xlim(x_min - margin, x_max + margin)
    
    for i, (name, value) in enumerate(zip(comps_names, comps_values)):
        if value > 0:
            x_pos = value + 0.008
            ha = 'left'
        else:
            x_pos = value - 0.008
            ha = 'right'
        ax.text(x_pos, i, f'{value:+.3f}', va='center', ha=ha, fontweight='bold', fontsize=10)
    
    plt.tight_layout()
    output_path = os.path.join(os.path.dirname(__file__), '..', 'insight2_analise.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"\n✓ Gráfico salvo: insight2_analise.png")
    plt.close()


if __name__ == "__main__":
    main()
