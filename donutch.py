#https://waynestalk.com/en/python-pie-donut-sunburst-charts-en/
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
sizes = [100, 500, 70, 54, 440]
labels = ['Apple', 'Banana', 'Mango', 'Grapes', 'Orange']
colors = ['#FF0000', '#0000FF', '#FFFF00', '#ADFF2F', '#FFA500']
explode = (0.05, 0.05, 0.05, 0.05, 0.05)

plt.pie(sizes, colors=colors, labels=labels,
        autopct='%1.1f%%', pctdistance=0.85, 
        explode=explode)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()

fig.gca().add_artist(centre_circle)
plt.title('Favourite Fruit Survey')

plt.legend(labels, loc="upper right")
#st.pyplot(plt.gcf()) # instead of plt.show()
st.pyplot(fig) # instead of plt.show()



data = dict(
    number=[39, 27.4, 20.6, 11, 2],
    stage=["Website visit", "Downloads", "Potential customers", "Requested price", "invoice sent"])
fig1 = px.funnel(data, x='number', y='stage')
#fig.show()
st.plotly_chart(fig1)