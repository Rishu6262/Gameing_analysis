import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ---------------------
# Page Config
# ---------------------
st.set_page_config(
    page_title="Gaming Addiction Dashboard",
    page_icon="🎮",
    layout="wide"
)

# ---------------------
# Custom CSS
# ---------------------
st.markdown("""
<style>
.main {
    background-color: #0e1117;
}

.metric-card {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
}

h1,h2,h3 {
    color:white;
}
</style>
""", unsafe_allow_html=True)

# ---------------------
# Load Data
# ---------------------
df = pd.read_csv("gaming_addiction.csv")

# ---------------------
# Header
# ---------------------
st.title("🎮 Gaming Addiction Analysis Dashboard")
st.markdown("### Interactive Data Analytics Dashboard")

# ---------------------
# Sidebar Filters
# ---------------------
st.sidebar.header("Filters")

gender = st.sidebar.multiselect(
    "Select Gender",
    df["gender"].unique(),
    default=df["gender"].unique()
)

df = df[df["gender"].isin(gender)]

# ---------------------
# KPI Section
# ---------------------
col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric("Total Users", len(df))

with col2:
    st.metric(
        "Average Addiction Score",
        round(df["addiction_score"].mean(),2)
    )

with col3:
    st.metric(
        "Average Sleep Hours",
        round(df["sleep_hours"].mean(),2)
    )

with col4:
    st.metric(
        "Average Daily Playtime",
        round(df["daily_playtime_hours"].mean(),2)
    )

st.divider()

# ---------------------
# Target Analysis
# ---------------------

st.header("🎯 Target Analysis")

c1,c2 = st.columns(2)

with c1:

    fig,ax = plt.subplots(figsize=(6,4))

    sns.histplot(
        df["addiction_score"],
        kde=True,
        color="red"
    )

    plt.title("Addiction Score Distribution")

    st.pyplot(fig)

with c2:

    fig,ax = plt.subplots(figsize=(6,4))

    sns.countplot(
        x="addiction_binary",
        data=df
    )

    plt.title("Addicted vs Non-Addicted")

    st.pyplot(fig)

# ---------------------
# Severity Analysis
# ---------------------

fig,ax = plt.subplots(figsize=(8,5))

sns.countplot(
    x="addiction_severity",
    data=df,
    palette="viridis"
)

plt.title("Addiction Severity")

st.pyplot(fig)

# ---------------------
# Sleep vs Addiction
# ---------------------

st.header("😴 Sleep vs Addiction")

fig,ax = plt.subplots(figsize=(8,5))

sns.scatterplot(
    x="sleep_hours",
    y="addiction_score",
    hue="addiction_severity",
    data=df
)

st.pyplot(fig)

# ---------------------
# Playtime vs Addiction
# ---------------------

st.header("⏰ Playtime vs Addiction")

fig,ax = plt.subplots(figsize=(8,5))

sns.scatterplot(
    x="daily_playtime_hours",
    y="addiction_score",
    hue="addiction_severity",
    data=df
)

st.pyplot(fig)

# ---------------------
# Stress Analysis
# ---------------------

st.header("🧠 Stress Analysis")

fig,ax = plt.subplots(figsize=(8,5))

sns.boxplot(
    x="addiction_severity",
    y="stress_score",
    data=df
)

st.pyplot(fig)

# ---------------------
# Correlation Heatmap
# ---------------------

st.header("🔥 Correlation Heatmap")

numeric_df = df.select_dtypes(include="number")

fig,ax = plt.subplots(figsize=(12,8))

sns.heatmap(
    numeric_df.corr(),
    cmap="coolwarm"
)

st.pyplot(fig)

# ---------------------
# Dataset Preview
# ---------------------

st.header("📄 Dataset Preview")

st.dataframe(df.head())

# ---------------------
# Download Dataset
# ---------------------

csv = df.to_csv(index=False)

st.download_button(
    "⬇ Download Dataset",
    csv,
    "gaming_addiction.csv",
    "text/csv"
)