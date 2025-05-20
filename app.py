import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🎮 Video Game Sales Dashboard")
st.write("Analisi vendite e distribuzione videogame a livello globale.")

# KPI principali
st.subheader("📊 KPI principali")
st.metric("Numero giochi", total_game)
st.metric("Top vendite (milioni)", total_sales.head(1).values[0])

# Top 10 giochi più venduti
st.subheader("🎮 Top 10 giochi più venduti")
fig1, ax1 = plt.subplots()
top_10_games.plot(kind='bar', ax=ax1, color='skyblue')
plt.title('Top 10 Best Seller Games')
plt.xticks(rotation=45)
st.pyplot(fig1)

# Vendite per piattaforma
st.subheader("💾 Vendite globali per piattaforma")
fig2, ax2 = plt.subplots()
top_platform.plot(kind='bar', ax=ax2, color='green')
plt.title('Total Sales by Platform')
plt.xticks(rotation=45)
st.pyplot(fig2)

# Vendite per anno
st.subheader("📅 Vendite globali per anno")
fig3, ax3 = plt.subplots()
sales_per_year.plot(kind='line', ax=ax3, color='blue')
plt.title('Total Global Sales by Year')
plt.xticks(rotation=45)
st.pyplot(fig3)

# Distribuzione per genere
st.subheader("🎮 Distribuzione giochi per genere")
fig4, ax4 = plt.subplots()
ax4.pie(game_dist, labels=game_dist.index, autopct='%1.1f%%', startangle=140)
ax4.axis('equal')
plt.title('Distribution by Genre')
st.pyplot(fig4)

st.write("Realizzato da Federico D'Ubaldi 🚀")
