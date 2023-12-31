
import pandas as pd
import plotly.graph_objects as go 
import plotly.express as px
from plotly.subplots import make_subplots
import streamlit as st
from PIL import Image
from prophet import Prophet



st.set_page_config(page_title="Evolução", page_icon="📊")


df_resultado = pd.read_csv('./src/data/resultado.csv')
df_total_por_ano = pd.read_csv('./src/data/total_por_ano.csv')
df_volume_por_ano = pd.read_csv('./src/data/volume_por_ano.csv')
df_cotacao = pd.read_csv('./src/data/cotacao.csv', sep=";" , decimal=",")
df_boxplot_proj = pd.read_csv('./src/data/boxplot_projecao.csv')
df_valor2_agg = pd.read_csv('./src/data/base_100_exportacao.csv')
df_agg_boxplot_prophet = pd.read_csv('./src/data/previsao.csv')



image = Image.open("./src/img/download.jpg")
st.image(image)


tab0, tab1, tab2, tab3= st.tabs([ "Faturamento","Volumetria", "Preço Médio","Projeção"])


with tab0:
    st.markdown("""
        ## <div style="text-align: center; color: #8A2BE2;">Relatório de Faturamento de Exportação</div>

        <p style='text-indent: 40px;'> A evolução do faturamento total de vendas da nossa empresa ao longo dos últimos quinze anos. Como verão no gráfico a seguir, nossos esforços e investimentos contínuos nos posicionaram para um crescimento sustentável, culminando em uma receita expressiva em 2021.</p>

        <p style='text-indent: 40px;'> No gráfico, é importante notar o pico significativo de vendas em 2013. Isso se deve ao marco histórico em nossa história de negócios - a primeira exportação de vinho a granel para a Rússia, um empreendimento liderado pela Associação dos Vinicultores de Garibaldi (AVIGA), da qual fazemos parte. Este feito não só elevou o nosso perfil no mercado internacional de vinhos, mas também abriu portas para novas oportunidades de negócios.</p>

        <p style='text-indent: 40px;'> Naquele ano, juntamente com outras empresas associadas à AVIGA, exportamos um total de 840 mil litros de vinho tinto de mesa para o mercado russo, equivalente a 35 contêineres. Este acontecimento histórico foi o resultado de anos de trabalho árduo, qualidade do produto e articulação estratégica.</p>

        <p style='text-indent: 40px;'> Esta iniciativa pioneira de exportação para a Rússia é um testemunho do nosso compromisso com a inovação e a busca de novos mercados. É também um exemplo de como a colaboração e a parceria podem gerar resultados expressivos.</p>

        <p style='text-indent: 40px;'> Aproveitamos também para destacar o nosso desempenho recente em 2021, onde atingimos quase U$ 10 milhões em vendas. Este crescimento robusto reflete a força contínua da nossa marca e a qualidade dos nossos vinhos, além do sucesso das nossas estratégias de mercado.</p>

        <p style='text-indent: 40px;'> Para o futuro, continuaremos a buscar novas oportunidades e a melhorar nossos produtos e serviços. Agradecemos a todos pelo seu apoio contínuo e confiança em nossa empresa.</p>
        """,unsafe_allow_html=True) 

    line2 = px.line(df_total_por_ano, x='Anos', y='Total').update_traces(mode='lines', line=dict(color='#8A2BE2'))
    scatter2 = px.scatter(df_total_por_ano, x='Anos', y='Total').update_traces(mode='markers', hovertemplate='Ano: %{x} <br>Valor: U$ %{y:,.2f}', marker=dict(color='purple'))    
    fig2 = go.Figure(data=line2.data + scatter2.data)    
    fig2.update_layout(
        title="Evolução do Faturamento Total (2007-2021)",
        xaxis_title="Anos",
        yaxis_title="Faturamento (em U$)",
        xaxis = dict(
            tickangle=45
        )
    )
    st.plotly_chart(fig2)
   

with tab1:
    

    st.markdown("""
        <h1 style = "text-align: center; color: #8A2BE2;">Relatório de Volumetria</h1>
        <p style="text-indent: 40px;">As informações aqui fornecidas oferecem uma visão clara da evolução das nossas vendas, destacando os pontos altos e baixos deste período.
        <p style="text-indent: 40px;">Observe, a partir da demonstração de dados, que nossas vendas passaram por períodos de pico, como em 2009, onde alcançamos a incrível marca de mais de 25 milhões, seguido por uma desaceleração nos anos seguintes. Contudo, a resiliência e capacidade de adaptação do nosso negócio permitiram uma recuperação consistente ao longo dos anos.
        <p style="text-indent: 40px;">A tendência de crescimento que observamos desde 2016, culminando em mais de 8 milhões em vendas em 2021, reforça a força da nossa empresa no mercado. Esses resultados são reflexo do nosso comprometimento com a qualidade e inovação constante dos nossos produtos e serviços.
        <p style="text-indent: 40px;">Estamos animados com o futuro e confiantes de que continuaremos a ver essa tendência ascendente nos próximos anos. Agradecemos seu apoio contínuo e confiança em nossa empresa.
        <p style="text-indent: 40px;">Agora, apresentamos a vocês o gráfico de nossas vendas ao longo desses 15 anos para um olhar mais detalhado sobre a evolução do nosso desempenho.
    """,unsafe_allow_html=True )

    
    fig3 = go.Figure(layout=go.Layout(
            title=go.layout.Title(text="Evolução do Volume de Vendas (2007-2021)"),
            xaxis=dict(title='Anos'),
            yaxis=dict(title='Volumetria'),
            xaxis_tickangle=45
        ))    
    fig3.add_trace(go.Scatter(x=df_volume_por_ano['Anos'], 
                            y=df_volume_por_ano['Total'], 
                            mode='lines+markers',
                            name="Volume Anual",
                            hovertemplate='Ano: %{x} <br>Volume: %{y}',
                            line=dict(color='#8A2BE2')
                            ))

    st.plotly_chart(fig3)



    
with tab2:
    
    st.markdown("""
        <h1 style = "text-align: center; color: #8A2BE2;">Análise do Valor Médio de Venda por Litro de Vinho</h1>
        <p style="text-indent: 40px;">Os resultados obtidos ao longo dos últimos 15 anos na venda de nosso vinho. Nesse período, observamos uma notável dinâmica no valor médio de venda por litro, o que demonstra o esforço contínuo em melhorar a qualidade de nossos produtos e a adaptação às demandas de mercado.
        <p style="text-indent: 40px;">No gráfico abaixo, você verá a evolução do valor médio de venda por litro de vinho de 2007 a 2021. Os dados representam uma média anual, o que proporciona uma visão clara das tendências ao longo do tempo.
        <p style="text-indent: 40px;">Ressaltamos que a nossa unidade de medida considera 1 kg de uva igual a 1 litro de vinho. Essa é uma aproximação comum na indústria e permite uma fácil interpretação e comparação dos dados.
        <p style="text-indent: 40px;">Analise os dados e observe o compromisso da nossa equipe em buscar os melhores resultados e a valorização constante dos nossos produtos.
    """,unsafe_allow_html=True )
    fig = go.Figure(layout=go.Layout(
                title=go.layout.Title(text="Evolução do Valor Médio de Venda por Litro (2007-2021)"),
                xaxis=dict(title='Anos'),
                yaxis=dict(title='Valor Médio (em U$)'),
                xaxis_tickangle=45
            ))

    fig.add_trace(go.Scatter(x=df_resultado['Anos'], 
                            y=df_resultado['Total'], 
                            mode='lines+markers',
                            name="Valor Médio Anual",
                            hovertemplate='Ano: %{x} <br>Valor: U$ %{y}',
                            line=dict(color='#8A2BE2')  # adicionando a cor roxa
                            ))

    st.plotly_chart(fig)

with tab3:


    st.markdown("""
    <h1 style = "text-align: center; color: #8A2BE2;">Projeção temporal das exportação</h1>
    <p style="text-indent: 40px;">Esta analise foi contruida com objetivo de demonstrar a projeção de exportação dos países para os proximos meses, incialmente retirando os outlier para não prejudicar a séries temporal, em seguida serão demonstradas as principais variaveis que consideramos na projeção, com o objetivo de demonstrar quais são 
    """,unsafe_allow_html=True )

    fig3 = go.Figure()

    fig3.add_trace(go.Box(
        y=df_boxplot_proj['sumtOfExport'],
        x=df_boxplot_proj['País'],
        name='Boxplot',
        line=dict(color='#8A2BE2')
    ))

    fig3.update_layout(
        title='Identificação dos outlier dos top10 países exportadors',
        xaxis_title='Paises',
        yaxis_title='Valores'
    )

    st.plotly_chart(fig3)

    st.markdown("""
    <p style="text-indent: 40px;">Após retirar os registros outliers que estão fora do intervalo interquartil, identificamos uma tendência correlata entre o variação da cotação do dólar e o ticket médio do U$/Litro
    """,unsafe_allow_html=True )



    fig = px.scatter(df_cotacao, x='ticket_medio', y='cotacaoVenda', trendline='ols', labels={'ticket_medio': 'Ticket médio U$/Litro', 'cotacaoVenda': 'Cotação do Dólar'})
    # Personalize o gráfico
    fig.update_layout(
        title={
            'text': "Relação ticket médio e preço do dólar, últimos 15 anos",
            'x': 0.5,
            'y': 0.95,
            'xanchor': 'center',
            'yanchor': 'top'
        }
    )

    fig.update_xaxes(
        title_text="Ticket médio R$/Litro",
        showticklabels=True
    )

    fig.update_yaxes(
        title_text="Cotação do Dólar em Reais",
        showticklabels=True
    )

    fig.add_trace(go.Scatter(name='Dados de dispersão'))  # Adiciona um nome para o trace
    
    # Mostre o gráfico
    st.plotly_chart(fig)

    st.markdown("""
    <p style="text-indent: 40px;">Analisamos a participação no volume de litros exportados por país para proporcionalizar o volume da exportação na projeção
    """,unsafe_allow_html=True )


    # Criando o gráfico de colunas empilhadas
    fig_1 = go.Figure()


    for pais in df_valor2_agg['group'].unique():
        dados_pais = df_valor2_agg[df_valor2_agg['group'] == pais]
        fig_1.add_trace(go.Bar(x=dados_pais['anomes'], y=dados_pais['percent'], name =pais))



    # Personalizando o layout do gráfico
    fig_1.update_layout(
        title='Participação nas Vendas por País e Ano',
        xaxis_title='Ano e Mês da exportação',
        yaxis_title='Participação nas Vendas',
        barmode='stack'
    )

    # Exibindo o gráfico
    st.plotly_chart(fig_1)


        #Crie um dicionário de DataFrames, onde cada chave corresponda a um país e o valor seja um DataFrame filtrado por país:
    dfs_paises = {}
    for pais in df_agg_boxplot_prophet['country'].unique():
        dfs_paises[pais] = df_agg_boxplot_prophet[df_agg_boxplot_prophet['country'] == pais].drop('country', axis=1)
    #Crie um modelo Prophet para cada país e ajuste-o aos dados correspondentes:
    modelos = {}
    for pais, df_pais in dfs_paises.items():
        modelo = Prophet()
        modelo.fit(df_pais)
        modelos[pais] = modelo


    #Instancia e ajusta os dados ao modelo
    datas_futuras = pd.date_range(start='2022-01-01', periods=12, freq='MS')
    datas_futuras = pd.DataFrame({'ds': datas_futuras})
    #Faça a projeção das vendas para cada país usando os modelos Prophet correspondentes:
    previsoes_paises = {}
    for pais, modelo in modelos.items():
        previsao = modelo.predict(datas_futuras)
        previsoes_paises[pais] = previsao

    for pais, previsao in previsoes_paises.items():
        previsao.loc[previsao['yhat'] < 0, 'yhat'] = -previsao['yhat_lower']
        previsoes_paises[pais] = previsao

    fig4 = go.Figure()
    for pais, previsao in previsoes_paises.items():
        fig4.add_trace(go.Scatter(
            x=previsao['ds'],
            y=previsao['yhat'],
            mode='lines',
            name=pais
        ))
    fig4.update_layout(
        title='Projeção de Valor exporta por País',
        xaxis_title='Data',
        yaxis_title='Valor Exportado Previsto'
    )
    st.plotly_chart(fig4)


    st.markdown("""
    ## <div style="text-align: center; color: #8A2BE2;"> Análise dos Dados </div>
    <p style="text-indent: 40px;"> Avaliando o cenário de tendência do dólar e a evolução no volumes/litros exportados por cada país, os mercados do Haiti, Rússia e China são clientes em potêncial expansão.
    """, unsafe_allow_html=True)
    
   