import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
st.set_page_config(page_title='Business Insights Dashboard',page_icon='📈',layout='wide')
st.title('📈 Business Insights Dashboard')
st.caption('Interactive visual storytelling using a 100-row sales dataset.')
df=pd.read_csv(Path(__file__).parent/'data/sales_100_rows.csv')
regions=['All']+sorted(df.region.unique().tolist()); selected=st.sidebar.selectbox('Region',regions)
if selected!='All': df=df[df.region==selected]
a,b,c=st.columns(3); a.metric('Revenue',f"${df.revenue.sum():,.2f}"); b.metric('Units sold',int(df.units.sum())); c.metric('Orders',len(df))
left,right=st.columns(2)
with left: st.plotly_chart(px.bar(df.groupby('product',as_index=False).revenue.sum(),x='product',y='revenue',title='Revenue by product'),use_container_width=True)
with right: st.plotly_chart(px.pie(df,values='revenue',names='region',title='Revenue share by region'),use_container_width=True)
st.plotly_chart(px.line(df,x='date',y='revenue',color='region',title='Daily revenue trend'),use_container_width=True)
st.subheader('Underlying data'); st.dataframe(df,use_container_width=True)
st.download_button('Export filtered data',df.to_csv(index=False).encode(),file_name='filtered_sales.csv',mime='text/csv')
