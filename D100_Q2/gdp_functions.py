import pandas as pd
import matplotlib.pyplot as plt

def load_gdp_data(filepath):
    df = pd.read_excel(filepath, sheet_name='Data')
    return df

def clean_gdp_data(df):
    target_countries = {
        'United Kingdom': 'UK',
        'United States': 'USA',
        'Brazil': 'Brazil',
        'Japan': 'Japan',
        'China': 'China',
        'Germany': 'Germany',
        'Switzerland': 'Switzerland'
    }
    
    df = df[df['Country Name'].isin(target_countries.keys())]
    df = df[['Country Name'] + [str(y) for y in range(2000, 2023)]]
    df = df.set_index('Country Name').T
    df.index = df.index.astype(int)
    df = df.rename(columns=target_countries)
    df = df.apply(pd.to_numeric, errors='coerce')
    return df

def plot_gdp_data(df):
    plt.figure(figsize=(10,6))
    for country in df.columns:
        plt.plot(df.index, df[country], label=country)
    plt.title('GDP (current US$) 2000–2022')
    plt.xlabel('Year')
    plt.ylabel('GDP (current US$)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()



    !pip install xlrd

