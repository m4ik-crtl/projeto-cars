# Projeto de Análise de Dados de Vendas de Veículos Usados nos EUA

Este projeto tem como objetivo realizar uma análise exploratória (EDA) e desenvolver uma aplicação web interativa para visualização de dados de vendas de veículos usados nos EUA. A análise foi realizada com o uso de Python, pandas e plotly, e o app foi construído utilizando o Streamlit.

## Estrutura do Repositório

- `README.md`: Descrição do projeto.
- `app.py`: Código principal da aplicação Streamlit.
- `vehicles_us.csv`: Conjunto de dados de vendas de veículos usados.
- `requirements.txt`: Dependências do projeto.
- `notebooks/EDA.ipynb`: Jupyter Notebook com a análise exploratória dos dados.
- `.streamlit/config.toml`: Arquivo de configuração para o Streamlit.

## Análise Exploratória de Dados (EDA)

A análise exploratória dos dados foi realizada no arquivo `EDA.ipynb` e fornece insights valiosos sobre o mercado de veículos usados nos EUA. A análise pode ser acessada através do seguinte link: [Análise Exploratória - EDA.ipynb](https://colab.research.google.com/github/m4ik-crtl/projeto-cars/blob/main/notebooks/EDA.ipynb).

### Resumo da Análise

Com base nos dados de vendas de veículos usados, foram extraídos os seguintes insights:

1. **Preço dos veículos**: A maioria dos veículos anunciados está concentrada abaixo de $20.000, com alguns poucos outliers mais caros.
2. **Quilometragem (odômetro)**: Veículos com preços mais baixos tendem a ter maior quilometragem, sugerindo que o desgaste afeta diretamente o valor de revenda.
3. **Ano do modelo**: Veículos mais novos têm um preço mais alto, mas ainda existem veículos antigos com preços elevados, provavelmente devido à marca ou condição.
4. **Condições do veículo**: A maioria dos veículos está em boas ou excelentes condições, indicando que os vendedores utilizam estratégias de marketing para atrair compradores.
5. **Combustível e transmissão**: A maioria dos veículos é a gasolina e possui câmbio automático, características comuns no mercado norte-americano.
6. **Cores e tipos de veículos**: As cores mais comuns são preto, branco e prata, enquanto os tipos de veículos mais frequentes são sedan, SUV e pickup.

Esses insights ajudam a entender o perfil dos veículos no mercado de usados e podem ser úteis tanto para compradores quanto para vendedores.

---

## Aplicação Web Interativa

O aplicativo web foi desenvolvido com o Streamlit para permitir que os usuários explorem visualizações interativas baseadas no conjunto de dados de vendas de veículos usados.

### Funcionalidades do App

- **Histograma da Quilometragem**: Visualize a distribuição da quilometragem dos veículos.
- **Gráfico de Dispersão (Preço x Ano)**: Explore a relação entre o preço e o ano do modelo dos veículos.

Você pode acessar o aplicativo web aqui: https://projeto-cars.onrender.com

---

## Como Executar o Projeto

### Pré-requisitos

- Python 3.x
- Bibliotecas: pandas, plotly-express, streamlit

### Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/m4ik-crtl/projeto-cars.git

2. Navegue até o diretório do projeto:
   ```bash
   cd projeto-cars

3. Crie e ative o ambiente virtual:
    ```bash
    python -m venv vehicles_env
    source vehicles_env/bin/activate  # no Windows, use 'vehicles_env\Scripts\activate'

4. Instale as dependências:
    ```bash
     pip install -r requirements.txt

5. Execute o aplicativo Streamlit:
 ```bash
 streamlit run app.py