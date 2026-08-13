import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Customer Segmentation Dashboard")

rfm=pd.read_csv("C:/Users/Priyanka/Datascience/rfm_with_clusters.csv")
st.write(rfm.head())
cluster_names={
    0:"New/Low-Engagement",
    1:"Champions",
    2:"Promising/Regular",
    3:"At-Risk/Fading",
    4:"Lost"
}
rfm['Segment']=rfm["Cluster"].map(cluster_names)

st.subheader("Overview")

col1, col2, col3=st.columns(3)
col1.metric("Total Customers", len(rfm))
col2.metric("Avg Monetary Value", f"{rfm['Monetory'].mean():.2f}")
col3.metric("Avg Frequency",f"{rfm['Monetory'].mean():.1f}")

st.subheader("Segment Profiles")

cluster_summary=rfm.groupby('Cluster')[['Recency','Frequency','Monetory']].mean().round(2)
st.write(cluster_summary)

st.subheader("Explore a cluster")
selected_segment=st.selectbox("Select a Segment", rfm["Segment"].unique())
filtered_data=rfm[rfm['Segment']==selected_segment]

st.write(f"showing {len(filtered_data)} customers in Cluster{selected_segment}segment")
st.write(filtered_data.head(10))

st.subheader("Customer Segments(PCA Visualization)")

fig,ax=plt.subplots(figsize=(8,6))
sns.scatterplot(data=rfm ,x='PCA1',y='PCA2',hue='Segment',palette='tab10',ax=ax)
st.pyplot(fig)
