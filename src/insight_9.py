import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

sys.path.append(os.path.dirname(__file__))
from data_processing import load_happiness_data, load_co2_data


def main():
    print("="*60)
    print("INSIGHT 9: COESÃO SOCIAL E MODELO NÓRDICO")
    print("="*60)
    
    df_happiness = load_happiness_data()
    df_co2 = load_co2_data()
    
    happiness_avg = df_happiness.groupby('Country')[['Score', 'Family', 'Life_Expectancy']].mean().reset_index()
    co2_avg = df_co2[df_co2['Year'].between(2015, 2019)].groupby('Country')['CO2_Emissions'].mean().reset_index()
    
    df = pd.merge(happiness_avg, co2_avg, on='Country', how='inner')
    df_clean = df.dropna()
    
    print(f"\nDados: {len(df_clean)} países\n")
    
    corr_family = df_clean['Family'].corr(df_clean['CO2_Emissions'])
    corr_life = df_clean['Life_Expectancy'].corr(df_clean['CO2_Emissions'])
    
    print("CORRELAÇÕES COM CO2:")
    print("-" * 60)
    print(f"Family (Suporte Social):      {corr_family:+.4f}")
    print(f"Life_Expectancy (Longevidade): {corr_life:+.4f}")
    
    high_social = df_clean['Family'] >= df_clean['Family'].quantile(0.75)
    high_life = df_clean['Life_Expectancy'] >= df_clean['Life_Expectancy'].quantile(0.75)
    low_co2 = df_clean['CO2_Emissions'] <= df_clean['CO2_Emissions'].quantile(0.25)
    
    modelo_nordico = df_clean[high_social & high_life & low_co2].copy()
    desenvolvido_insustentavel = df_clean[high_social & high_life & ~low_co2].copy()
    em_desenvolvimento = df_clean[~high_social & ~high_life].copy()
    
    print(f"\nCLUSTERS IDENTIFICADOS:")
    print("-" * 60)
    print(f"Modelo Nórdico (alto social + alta vida + baixo CO2): {len(modelo_nordico)} países")
    print(f"Desenvolvido Insustentável (alto social + alta vida + alto CO2): {len(desenvolvido_insustentavel)} países")
    print(f"Em Desenvolvimento (baixo social + baixa vida): {len(em_desenvolvimento)} países")
    
    if len(modelo_nordico) > 0:
        print(f"\nCAMPEÕES DO MODELO NÓRDICO:")
        print("-" * 60)
        modelo_nordico_sorted = modelo_nordico.sort_values('Score', ascending=False).head(10)
        for idx, row in modelo_nordico_sorted.iterrows():
            print(f"{row['Country']:25s} | Felicidade: {row['Score']:.2f} | CO2: {row['CO2_Emissions']:,.0f} kt")
    
    fig, ax = plt.subplots(figsize=(14, 9))
    
    if len(em_desenvolvimento) > 0:
        ax.scatter(em_desenvolvimento['Family'], em_desenvolvimento['CO2_Emissions'], 
                   label=f'🌱 Em Desenvolvimento ({len(em_desenvolvimento)})', 
                   alpha=0.4, s=60, color='#95a5a6', edgecolors='gray', linewidth=0.5)
    
    if len(desenvolvido_insustentavel) > 0:
        ax.scatter(desenvolvido_insustentavel['Family'], desenvolvido_insustentavel['CO2_Emissions'], 
                   label=f'🏭 Desenvolvido Insustentável ({len(desenvolvido_insustentavel)})', 
                   alpha=0.6, s=100, color='#e74c3c', edgecolors='darkred', linewidth=1)
    
    if len(modelo_nordico) > 0:
        ax.scatter(modelo_nordico['Family'], modelo_nordico['CO2_Emissions'], 
                   label=f'🌟 Modelo Nórdico ({len(modelo_nordico)})', 
                   alpha=0.9, s=250, color='#27ae60', edgecolors='darkgreen', linewidth=2, marker='*', zorder=5)
        
        for idx, row in modelo_nordico.iterrows():
            ax.annotate(row['Country'], 
                       xy=(row['Family'], row['CO2_Emissions']),
                       xytext=(8, 8), textcoords='offset points',
                       fontsize=9, fontweight='bold', color='darkgreen',
                       bbox=dict(boxstyle='round,pad=0.3', facecolor='lightgreen', alpha=0.7, edgecolor='darkgreen'),
                       zorder=6)
    
    ax.set_yscale('log')
    
    family_threshold = df_clean['Family'].quantile(0.75)
    co2_threshold = df_clean['CO2_Emissions'].quantile(0.25)
    
    ax.axvline(family_threshold, color='green', linestyle='--', alpha=0.5, linewidth=1.5, 
               label=f'Threshold Suporte Social: {family_threshold:.2f}')
    ax.axhline(co2_threshold, color='blue', linestyle='--', alpha=0.5, linewidth=1.5,
               label=f'Threshold CO2: {co2_threshold:,.0f} kt')
    
    ax.set_xlabel('Suporte Social (Family)', fontsize=13, fontweight='bold')
    ax.set_ylabel('Emissões de CO2 (kt) - escala logarítmica', fontsize=13, fontweight='bold')
    ax.set_title('Modelo Nórdico: Alta Coesão Social + Baixas Emissões\nApenas 7 países (5.3%) alcançam alta coesão social e baixo impacto ambiental', 
                 fontsize=14, fontweight='bold', pad=20)
    ax.legend(fontsize=10, loc='upper left', framealpha=0.95, edgecolor='black')
    ax.grid(alpha=0.3, linestyle='--', linewidth=0.5)
    
    plt.tight_layout()
    output_path = os.path.join(os.path.dirname(__file__), '..', 'charts', 'insight_9_grafico.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"\n✓ Gráfico salvo: charts/insight_9_grafico.png")
    plt.close()


if __name__ == "__main__":
    main()
