import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

sys.path.append(os.path.dirname(__file__))
from data_processing import load_happiness_data, load_co2_data


def main():
    print("="*60)
    print("INSIGHT 8: GOVERNANÇA E REDUÇÃO DE EMISSÕES")
    print("="*60)
    
    df_happiness = load_happiness_data()
    df_co2 = load_co2_data()
    
    happiness_avg = df_happiness.groupby('Country')[['Freedom', 'Trust', 'GDP']].mean().reset_index()
    
    co2_2015 = df_co2[df_co2['Year'] == 2015][['Country', 'CO2_Emissions']].copy()
    co2_2019 = df_co2[df_co2['Year'] == 2019][['Country', 'CO2_Emissions']].copy()
    
    co2_2015.rename(columns={'CO2_Emissions': 'CO2_2015'}, inplace=True)
    co2_2019.rename(columns={'CO2_Emissions': 'CO2_2019'}, inplace=True)
    
    df = pd.merge(happiness_avg, co2_2015, on='Country', how='inner')
    df = pd.merge(df, co2_2019, on='Country', how='inner')
    
    df_clean = df.dropna()
    df_clean = df_clean[df_clean['CO2_2015'] > 0].copy()
    
    df_clean['Taxa_Reducao_CO2'] = ((df_clean['CO2_2019'] - df_clean['CO2_2015']) / df_clean['CO2_2015']) * 100
    
    print(f"\nDados: {len(df_clean)} países\n")
    
    corr_freedom = df_clean['Freedom'].corr(df_clean['Taxa_Reducao_CO2'])
    corr_trust = df_clean['Trust'].corr(df_clean['Taxa_Reducao_CO2'])
    corr_gdp = df_clean['GDP'].corr(df_clean['Taxa_Reducao_CO2'])
    
    print("CORRELAÇÕES COM TAXA DE REDUÇÃO DE CO2:")
    print("-" * 60)
    print(f"Freedom (Liberdade):        {corr_freedom:+.4f}")
    print(f"Trust (Confiança/Baixa corrupção): {corr_trust:+.4f}")
    print(f"GDP (Controle):             {corr_gdp:+.4f}")
    print()
    
    print("INTERPRETAÇÃO:")
    if corr_freedom < -0.1:
        print("✓ Países com MAIS liberdade tendem a REDUZIR mais CO2")
    elif corr_freedom > 0.1:
        print("✗ Países com MAIS liberdade tendem a AUMENTAR CO2")
    else:
        print("○ Liberdade tem relação FRACA com redução de CO2")
    
    if corr_trust < -0.1:
        print("✓ Países com MAIS confiança (menos corrupção) tendem a REDUZIR mais CO2")
    elif corr_trust > 0.1:
        print("✗ Países com MAIS confiança tendem a AUMENTAR CO2")
    else:
        print("○ Confiança tem relação FRACA com redução de CO2")
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    colors1 = ['green' if x < 0 else 'red' for x in df_clean['Taxa_Reducao_CO2']]
    ax1.scatter(df_clean['Freedom'], df_clean['Taxa_Reducao_CO2'], 
               alpha=0.7, s=100, c=colors1, edgecolors='black', linewidth=0.8)
    
    z1 = np.polyfit(df_clean['Freedom'], df_clean['Taxa_Reducao_CO2'], 1)
    p1 = np.poly1d(z1)
    x_line1 = np.linspace(df_clean['Freedom'].min(), df_clean['Freedom'].max(), 100)
    ax1.plot(x_line1, p1(x_line1), "b--", linewidth=2.5, 
            label=f'Tendência (r={corr_freedom:.3f})', alpha=0.8)
    
    ax1.axhline(y=0, color='black', linestyle='-', linewidth=1.5, alpha=0.5)
    ax1.set_xlabel('Liberdade (Freedom)', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Taxa de Redução de CO2 (%)', fontsize=12, fontweight='bold')
    ax1.set_title('Liberdade vs Redução de Emissões', fontsize=13, fontweight='bold')
    ax1.legend(fontsize=10)
    ax1.grid(alpha=0.3)
    
    colors2 = ['green' if x < 0 else 'red' for x in df_clean['Taxa_Reducao_CO2']]
    ax2.scatter(df_clean['Trust'], df_clean['Taxa_Reducao_CO2'], 
               alpha=0.7, s=100, c=colors2, edgecolors='black', linewidth=0.8)
    
    z2 = np.polyfit(df_clean['Trust'], df_clean['Taxa_Reducao_CO2'], 1)
    p2 = np.poly1d(z2)
    x_line2 = np.linspace(df_clean['Trust'].min(), df_clean['Trust'].max(), 100)
    ax2.plot(x_line2, p2(x_line2), "b--", linewidth=2.5, 
            label=f'Tendência (r={corr_trust:.3f})', alpha=0.8)
    
    ax2.axhline(y=0, color='black', linestyle='-', linewidth=1.5, alpha=0.5)
    ax2.set_xlabel('Confiança no Governo (Trust)', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Taxa de Redução de CO2 (%)', fontsize=12, fontweight='bold')
    ax2.set_title('Confiança vs Redução de Emissões', fontsize=13, fontweight='bold')
    ax2.legend(fontsize=10)
    ax2.grid(alpha=0.3)
    
    plt.tight_layout()
    output_path = os.path.join(os.path.dirname(__file__), '..', 'charts', 'insight_8_grafico.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"\n✓ Gráfico salvo: charts/insight_8_grafico.png")
    plt.close()
    
    reducao = df_clean[df_clean['Taxa_Reducao_CO2'] < 0]
    print(f"\n✓ Países que REDUZIRAM emissões (2015-2019): {len(reducao)} de {len(df_clean)}")
    
    if len(reducao) > 0:
        print(f"\nGovernança média dos que REDUZIRAM:")
        print(f"  Freedom: {reducao['Freedom'].mean():.3f}")
        print(f"  Trust:   {reducao['Trust'].mean():.3f}")
        
        aumento = df_clean[df_clean['Taxa_Reducao_CO2'] >= 0]
        if len(aumento) > 0:
            print(f"\nGovernança média dos que AUMENTARAM:")
            print(f"  Freedom: {aumento['Freedom'].mean():.3f}")
            print(f"  Trust:   {aumento['Trust'].mean():.3f}")


if __name__ == "__main__":
    main()
