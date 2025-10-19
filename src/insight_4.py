import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

sys.path.append(os.path.dirname(__file__))
from data_processing import load_happiness_data, load_co2_data


def main():
    print("="*60)
    print("INSIGHT 4: EFICIÊNCIA AMBIENTAL - RANKING")
    print("="*60)
    
    df_happiness = load_happiness_data()
    df_co2 = load_co2_data()
    
    df_happiness_avg = df_happiness.groupby('Country')[['Score', 'GDP']].mean().reset_index()
    df_co2_avg = df_co2[df_co2['Year'].between(2015, 2019)].groupby('Country')['CO2_Emissions'].mean().reset_index()
    
    df = pd.merge(df_happiness_avg, df_co2_avg, on='Country', how='inner')
    
    df_clean = df[['Country', 'Score', 'CO2_Emissions', 'GDP']].dropna()
    
    df_clean['CO2_per_capita_proxy'] = df_clean['CO2_Emissions'] / 1000
    df_clean['efficiency_index'] = df_clean['Score'] / (df_clean['CO2_per_capita_proxy'] + 0.1)
    
    df_clean = df_clean.sort_values('efficiency_index', ascending=False)
    
    print(f"\nDados: {len(df_clean)} países (média 2015-2019)")
    
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    
    top_20 = df_clean.head(20)
    bottom_20 = df_clean.tail(20)
    
    ax1 = axes[0, 0]
    bars1 = ax1.barh(range(len(top_20)), top_20['efficiency_index'], color='green', alpha=0.7)
    ax1.set_yticks(range(len(top_20)))
    ax1.set_yticklabels(top_20['Country'], fontsize=8)
    ax1.set_xlabel('Índice de Eficiência')
    ax1.set_title('TOP 20 Países Mais Eficientes\n(Alta Felicidade / Baixo CO2)')
    ax1.grid(True, alpha=0.3)
    ax1.invert_yaxis()
    
    ax2 = axes[0, 1]
    bars2 = ax2.barh(range(len(bottom_20)), bottom_20['efficiency_index'], color='red', alpha=0.7)
    ax2.set_yticks(range(len(bottom_20)))
    ax2.set_yticklabels(bottom_20['Country'], fontsize=8)
    ax2.set_xlabel('Índice de Eficiência')
    ax2.set_title('BOTTOM 20 Países Menos Eficientes\n(Baixa Felicidade / Alto CO2)')
    ax2.grid(True, alpha=0.3)
    ax2.invert_yaxis()
    
    ax3 = axes[1, 0]
    scatter = ax3.scatter(df_clean['CO2_Emissions'], df_clean['Score'], 
                         c=df_clean['efficiency_index'], cmap='RdYlGn', 
                         s=60, alpha=0.8, edgecolors='black', linewidth=0.5)
    
    for i, row in top_20.head(5).iterrows():
        ax3.annotate(row['Country'], (row['CO2_Emissions'], row['Score']), 
                    xytext=(5, 5), textcoords='offset points', fontsize=8, 
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='green', alpha=0.7))
    
    for i, row in bottom_20.tail(5).iterrows():
        ax3.annotate(row['Country'], (row['CO2_Emissions'], row['Score']), 
                    xytext=(5, 5), textcoords='offset points', fontsize=8,
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='red', alpha=0.7))
    
    ax3.set_xlabel('CO2 Emissions (kt)')
    ax3.set_ylabel('Happiness Score')
    ax3.set_title('Mapa de Eficiência: CO2 vs Felicidade')
    ax3.grid(True, alpha=0.3)
    
    cbar = plt.colorbar(scatter, ax=ax3)
    cbar.set_label('Índice de Eficiência')
    
    efficiency_bins = pd.cut(df_clean['efficiency_index'], 
                           bins=5, labels=['Muito Baixa', 'Baixa', 'Média', 'Alta', 'Muito Alta'])
    efficiency_dist = efficiency_bins.value_counts()
    
    ax4 = axes[1, 1]
    colors = ['red', 'orange', 'yellow', 'lightgreen', 'green']
    wedges, texts, autotexts = ax4.pie(efficiency_dist.values, labels=efficiency_dist.index, 
                                      colors=colors, autopct='%1.1f%%', startangle=90)
    ax4.set_title('Distribuição de Países por\nNível de Eficiência Ambiental')
    
    plt.tight_layout()
    
    top_20 = df_clean.head(20)
    bottom_20 = df_clean.tail(20)
    
    plt.figure(figsize=(12, 10))
    bars1 = plt.barh(range(len(top_20)), top_20['efficiency_index'], color='green', alpha=0.7)
    plt.yticks(range(len(top_20)), top_20['Country'], fontsize=8)
    plt.xlabel('Índice de Eficiência')
    plt.title('TOP 20 Países Mais Eficientes\n(Alta Felicidade / Baixo CO2)')
    plt.grid(True, alpha=0.3)
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig('insight_4_grafico_1_top_20_eficientes.jpg', dpi=300, bbox_inches='tight')
    plt.close()
    
    plt.figure(figsize=(12, 10))
    bars2 = plt.barh(range(len(bottom_20)), bottom_20['efficiency_index'], color='red', alpha=0.7)
    plt.yticks(range(len(bottom_20)), bottom_20['Country'], fontsize=8)
    plt.xlabel('Índice de Eficiência')
    plt.title('BOTTOM 20 Países Menos Eficientes\n(Baixa Felicidade / Alto CO2)')
    plt.grid(True, alpha=0.3)
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig('insight_4_grafico_2_bottom_20_ineficientes.jpg', dpi=300, bbox_inches='tight')
    plt.close()
    
    plt.figure(figsize=(12, 10))
    scatter = plt.scatter(df_clean['CO2_Emissions'], df_clean['Score'], 
                         c=df_clean['efficiency_index'], cmap='RdYlGn', 
                         s=60, alpha=0.8, edgecolors='black', linewidth=0.5)
    
    for i, row in top_20.head(5).iterrows():
        plt.annotate(row['Country'], (row['CO2_Emissions'], row['Score']), 
                    xytext=(5, 5), textcoords='offset points', fontsize=8, 
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='green', alpha=0.7))
    
    for i, row in bottom_20.tail(5).iterrows():
        plt.annotate(row['Country'], (row['CO2_Emissions'], row['Score']), 
                    xytext=(5, 5), textcoords='offset points', fontsize=8,
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='red', alpha=0.7))
    
    plt.xlabel('CO2 Emissions (kt)')
    plt.ylabel('Happiness Score')
    plt.title('Mapa de Eficiência: CO2 vs Felicidade')
    plt.grid(True, alpha=0.3)
    
    cbar = plt.colorbar(scatter)
    cbar.set_label('Índice de Eficiência')
    plt.tight_layout()
    plt.savefig('insight_4_grafico_3_mapa_eficiencia.jpg', dpi=300, bbox_inches='tight')
    plt.close()
    
    efficiency_bins = pd.cut(df_clean['efficiency_index'], 
                           bins=5, labels=['Muito Baixa', 'Baixa', 'Média', 'Alta', 'Muito Alta'])
    efficiency_dist = efficiency_bins.value_counts()
    
    plt.figure(figsize=(10, 8))
    colors = ['red', 'orange', 'yellow', 'lightgreen', 'green']
    wedges, texts, autotexts = plt.pie(efficiency_dist.values, labels=efficiency_dist.index, 
                                      colors=colors, autopct='%1.1f%%', startangle=90)
    plt.title('Distribuição de Países por\nNível de Eficiência Ambiental')
    plt.tight_layout()
    plt.savefig('insight_4_grafico_4_distribuicao_eficiencia.jpg', dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"\nTOP 10 PAÍSES MAIS EFICIENTES:")
    print("-" * 60)
    top_20 = df_clean.head(20)
    bottom_20 = df_clean.tail(20)
    for i, (_, row) in enumerate(top_20.head(10).iterrows(), 1):
        print(f"{i:2d}. {row['Country']:20s} | Eficiência: {row['efficiency_index']:6.2f} | "
              f"Felicidade: {row['Score']:4.2f} | CO2: {row['CO2_Emissions']:8.0f}kt")
    
    print(f"\nBOTTOM 10 PAÍSES MENOS EFICIENTES:")
    print("-" * 60)
    for i, (_, row) in enumerate(bottom_20.tail(10).iterrows(), 1):
        print(f"{i:2d}. {row['Country']:20s} | Eficiência: {row['efficiency_index']:6.2f} | "
              f"Felicidade: {row['Score']:4.2f} | CO2: {row['CO2_Emissions']:8.0f}kt")
    
    print(f"\n✓ 4 gráficos salvos:")
    print(f"  - insight_4_grafico_1_top_20_eficientes.jpg")
    print(f"  - insight_4_grafico_2_bottom_20_ineficientes.jpg")
    print(f"  - insight_4_grafico_3_mapa_eficiencia.jpg")
    print(f"  - insight_4_grafico_4_distribuicao_eficiencia.jpg")


if __name__ == "__main__":
    main()
