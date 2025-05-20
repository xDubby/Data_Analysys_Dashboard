import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Titolo app
st.title("🎮 Video Game Sales Dashboard")
st.write("Analisi vendite e distribuzione videogame a livello globale.")

# Carica dataset
df = pd.read_csv('vgsales.csv')

# Pulizia dati
df['Publisher'] = df['Publisher'].fillna('Unknown')
df['Year'] = df['Year'].fillna(0).astype(int)
df_clean = df.dropna(subset=['Year'])

# KPI
total_game = df_clean['Name'].nunique()
total_sales = df.groupby('Name')['Global_Sales'].sum().sort_values(ascending=False)
game_pp = df_clean.groupby('Platform')['Name'].count().sort_values(ascending=False)
sales_pp = df_clean.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False)
df_valid_years = df_clean[(df_clean['Year'] >= 1980) & (df_clean['Year'] <= 2020)]
sales_per_year = df_valid_years.groupby('Year')['Global_Sales'].sum()
game_dist = df_clean.groupby('Genre')['Name'].count()

# Mostra KPI
st.subheader("KPI principali")
st.metric("Numero giochi unici", total_game)
st.metric("Top vendite (milioni)", round(total_sales.head(1).values[0], 2))

# Top 10 giochi più venduti
st.subheader("Top 10 giochi più venduti")
fig1, ax1 = plt.subplots(figsize=(14,7))
total_sales.head(10).plot(kind='bar', ax=ax1, color='skyblue')
plt.title('Top 10 Best Seller Games')
plt.xlabel('Games')
plt.ylabel('Sales (Millions)')
plt.xticks(rotation=60)
st.pyplot(fig1)

# Vendite per piattaforma
st.subheader("Vendite globali per piattaforma")
fig2, ax2 = plt.subplots(figsize=(14,6))
sales_pp.plot(kind='bar', ax=ax2, color='green')
plt.title('Total Sales by Platform')
plt.xlabel('Platform')
plt.ylabel('Sales (Millions)')
plt.xticks(rotation=75, ha='right')
plt.tight_layout()
st.pyplot(fig2)


# Vendite per anno
st.subheader("Vendite globali per anno")
fig3, ax3 = plt.subplots()
sales_per_year.plot(kind='line', ax=ax3, color='blue')
plt.title('Total Global Sales by Year')
plt.xlabel('Year')
plt.ylabel('Sales (Millions)')
plt.xticks(rotation=45)
st.pyplot(fig3)

# Distribuzione per genere
st.subheader("Distribuzione giochi per genere")
fig4, ax4 = plt.subplots()
ax4.pie(game_dist, labels=game_dist.index, autopct='%1.1f%%', startangle=140)
ax4.axis('equal')
plt.title('Distribution by Genre')
st.pyplot(fig4)
