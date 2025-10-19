import pandas as pd
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data')


def load_happiness_data():
    print("Carregando dados de felicidade (2015-2019)...")
    
    df_2015 = pd.read_csv(os.path.join(DATA_PATH, 'data-2015.csv'))
    df_2016 = pd.read_csv(os.path.join(DATA_PATH, 'data-2016.csv'))
    df_2017 = pd.read_csv(os.path.join(DATA_PATH, 'data-2017.csv'))
    df_2018 = pd.read_csv(os.path.join(DATA_PATH, 'data-2018.csv'))
    df_2019 = pd.read_csv(os.path.join(DATA_PATH, 'data-2019.csv'))
    
    df_2015 = df_2015.rename(columns={'Rank 2015': 'Rank', 'Score 2015': 'Score', 'GDP 2015': 'GDP', 
                                       'Family 2015': 'Family', 'Life Expectancy 2015': 'Life_Expectancy',
                                       'Freedom 2015': 'Freedom', 'Trust 2015': 'Trust', 
                                       'Generosity 2015': 'Generosity'})
    df_2015['Year'] = 2015
    
    df_2016 = df_2016.rename(columns={'Rank 2016': 'Rank', 'Score 2016': 'Score', 'GDP 2016': 'GDP',
                                       'Family 2016': 'Family', 'Life Expectancy 2016': 'Life_Expectancy',
                                       'Freedom 2016': 'Freedom', 'Trust 2016': 'Trust',
                                       'Generosity 2016': 'Generosity'})
    df_2016['Year'] = 2016
    
    df_2017 = df_2017.rename(columns={'Rank 2017': 'Rank', 'Score 2017': 'Score', 'GDP 2017': 'GDP',
                                       'Family 2017': 'Family', 'Life Expectancy 2017': 'Life_Expectancy',
                                       'Freedom 2017': 'Freedom', 'Trust 2017': 'Trust',
                                       'Generosity 2017': 'Generosity'})
    df_2017['Year'] = 2017
    
    df_2018 = df_2018.rename(columns={'Rank 2018': 'Rank', 'Score 2018': 'Score', 'GDP 2018': 'GDP',
                                       'Family 2018': 'Family', 'Life Expectancy 2018': 'Life_Expectancy',
                                       'Freedom 2018': 'Freedom', 'Trust 2018': 'Trust',
                                       'Generosity 2018': 'Generosity'})
    df_2018['Year'] = 2018
    
    df_2019 = df_2019.rename(columns={'Rank 2019': 'Rank', 'Score 2019': 'Score', 'GDP 2019': 'GDP',
                                       'Family 2019': 'Family', 'Life Expectancy 2019': 'Life_Expectancy',
                                       'Freedom 2019': 'Freedom', 'Trust 2019': 'Trust',
                                       'Generosity 2019': 'Generosity'})
    df_2019['Year'] = 2019
    
    df_happiness = pd.concat([df_2015, df_2016, df_2017, df_2018, df_2019], 
                             ignore_index=True)
    
    print(f"✓ Dados de felicidade carregados: {len(df_happiness)} registros")
    print(f"  Anos: 2015-2019 | Países únicos: {df_happiness['Country'].nunique()}")
    
    return df_happiness


def load_co2_data():
    print("\nCarregando dados de emissões de CO2...")
    
    df_co2 = pd.read_csv(os.path.join(DATA_PATH, 'co2_emissions_kt_by_country.csv'))
    
    df_co2 = df_co2.rename(columns={'country_code': 'Country_Code', 
                                     'country_name': 'Country',
                                     'year': 'Year', 
                                     'value': 'CO2_Emissions'})
    
    print(f"✓ Dados de CO2 carregados: {len(df_co2)} registros")
    print(f"  Anos disponíveis: {df_co2['Year'].min()} a {df_co2['Year'].max()}")
    print(f"  Países únicos: {df_co2['Country'].nunique()}")
    
    return df_co2


if __name__ == "__main__":
    print("="*60)
    print("CARREGAMENTO DE DADOS")
    print("="*60)
        
    df_happiness = load_happiness_data()
    df_co2 = load_co2_data()
        
    print("\n" + "="*60)
    print("RESUMO")
    print("="*60)
    print(f"\nDataset de Felicidade:")
    print(f"  - {len(df_happiness)} registros")
    print(f"  - {df_happiness['Country'].nunique()} países")
    print(f"  - Colunas: {list(df_happiness.columns)}")
        
    print(f"\nDataset de CO2:")
    print(f"  - {len(df_co2)} registros")
    print(f"  - {df_co2['Country'].nunique()} países")
    print(f"  - Colunas: {list(df_co2.columns)}")
        
    print("\n✓ Processamento concluído!")
