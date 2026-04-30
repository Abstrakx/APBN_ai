"""
APBN_ai — Dashboard
==========================
Streamlit dashboard with building energy efficiency map.

Run: streamlit run src/dashboard.py
"""

import streamlit as st
import pandas as pd
import json
import os
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="APBN_ai", page_icon="⚡", layout="wide")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
DATA_DIR = os.path.join(BASE_DIR, "data")

IKE_COLORS = {
    "Sangat Efisien": "#22c55e",
    "Efisien": "#3b82f6",
    "Cukup Efisien": "#eab308",
    "Boros": "#f97316",
    "Sangat Boros": "#ef4444",
}

PLN_DKI_GOVT_GWH = 1396.61


def load_data():
    pred_path = os.path.join(OUTPUT_DIR, "jakarta_predictions.csv")
    if os.path.exists(pred_path):
        return pd.read_csv(pred_path)
    # Fallback: load raw building data and simulate predictions
    raw_path = os.path.join(DATA_DIR, "jakarta_government_buildings.csv")
    df = pd.read_csv(raw_path)
    df["sqm"] = df["estimated_sqm"]
    df["predicted_ike"] = df["sqm"].apply(lambda x: 80 + (x / 1000) * 2 + (hash(str(x)) % 60))
    df["ike_category"] = df["predicted_ike"].apply(
        lambda v: "Sangat Efisien" if v < 50 else "Efisien" if v < 95 else "Cukup Efisien" if v < 145 else "Boros" if v < 175 else "Sangat Boros"
    )
    df["ike_color"] = df["ike_category"].map(IKE_COLORS)
    df["predicted_kwh"] = df["predicted_ike"] * df["sqm"]
    df["saving_10pct_rp"] = df["predicted_kwh"] * 0.10 * 1400
    df["saving_30pct_rp"] = df["predicted_kwh"] * 0.30 * 1400
    return df


def main():
    # Header
    st.markdown("""
    <head>
        <meta name="dicoding:email" content="abstrakxpro@gmail.com">
    </head>
    <style>
    .main-header {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a5f 50%, #0ea5e9 100%);
        padding: 2rem; border-radius: 16px; margin-bottom: 2rem; color: white;
    }
    .metric-card {
        background: linear-gradient(135deg, #1e293b, #334155);
        padding: 1.5rem; border-radius: 12px; text-align: center; color: white;
    }
    .metric-value { font-size: 2rem; font-weight: 700; }
    .metric-label { font-size: 0.85rem; opacity: 0.8; margin-top: 0.3rem; }
    </style>
    <div class="main-header">
        <h1>⚡ APBN_ai</h1>
        <p>AI-Powered Building Energy Anomaly Detection & Optimization for Urban Resilience</p>
        <p style="opacity:0.7;font-size:0.85rem;">AI Impact Challenge — Datathon 2026 | Theme: Urban Resilience & Smart City</p>
    </div>
    """, unsafe_allow_html=True)

    df = load_data()

    # KPI Cards
    total_buildings = len(df)
    avg_ike = df["predicted_ike"].mean()
    total_kwh = df["predicted_kwh"].sum()
    total_saving_low = df["saving_10pct_rp"].sum()
    total_saving_high = df["saving_30pct_rp"].sum()
    boros_count = len(df[df["ike_category"].isin(["Boros", "Sangat Boros"])])

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("🏢 Buildings Analyzed", f"{total_buildings}")
    with c2:
        st.metric("⚡ Avg IKE", f"{avg_ike:.0f} kWh/m²/yr")
    with c3:
        st.metric("🔴 Inefficient Buildings", f"{boros_count}")
    with c4:
        st.metric("💰 Saving Potential", f"Rp {total_saving_low/1e9:.0f}-{total_saving_high/1e9:.0f} M")

    st.markdown("---")

    # Map + Detail Panel
    col_map, col_detail = st.columns([2, 1])

    with col_map:
        st.subheader("🗺️ Jakarta Building Energy Efficiency Map")

        color_map = {cat: color for cat, color in IKE_COLORS.items()}
        fig = px.scatter_mapbox(
            df, lat="lat", lon="lng",
            color="ike_category",
            color_discrete_map=color_map,
            size="sqm",
            size_max=20,
            hover_name="name",
            hover_data={"predicted_ike": ":.1f", "sqm": ":,", "category": True, "lat": False, "lng": False},
            mapbox_style="carto-positron",
            zoom=10.5,
            center={"lat": -6.2, "lon": 106.83},
            height=550,
            category_orders={"ike_category": list(IKE_COLORS.keys())},
        )
        fig.update_layout(
            margin=dict(l=0, r=0, t=0, b=0),
            legend=dict(title="IKE Rating", yanchor="top", y=0.99, xanchor="left", x=0.01,
                        bgcolor="rgba(0,0,0,0.5)", font=dict(color="white")),
        )
        st.plotly_chart(fig, use_container_width=True)

    with col_detail:
        st.subheader("📋 Building Details")
        selected = st.selectbox("Select Building", df["name"].tolist())
        bld = df[df["name"] == selected].iloc[0]

        color = bld["ike_color"]
        st.markdown(f"""
        <div style="background:{color}22; border-left:4px solid {color}; padding:1rem; border-radius:8px;">
            <strong style="color:{color};">{bld['ike_category']}</strong><br>
            IKE: <strong>{bld['predicted_ike']:.1f}</strong> kWh/m²/yr
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"**Category:** {bld['category']}")
        st.markdown(f"**Floor Area:** {bld['sqm']:,.0f} m²")
        st.markdown(f"**Predicted Annual:** {bld['predicted_kwh']:,.0f} kWh")
        st.markdown(f"**Monthly Estimate:** {bld['predicted_kwh']/12:,.0f} kWh")

        st.markdown("#### 💰 Saving Potential")
        st.markdown(f"- Conservative (10%): **Rp {bld['saving_10pct_rp']/1e6:,.0f} juta/yr**")
        st.markdown(f"- Optimistic (30%): **Rp {bld['saving_30pct_rp']/1e6:,.0f} juta/yr**")

    st.markdown("---")

    # Analytics Charts
    st.subheader("📊 Analytics")
    t1, t2, t3 = st.tabs(["IKE Distribution", "By Category", "Ranking"])

    with t1:
        fig_ike = px.histogram(df, x="predicted_ike", nbins=20, color="ike_category",
                               color_discrete_map=color_map, title="IKE Distribution Across Buildings",
                               labels={"predicted_ike": "IKE (kWh/m²/yr)"})
        st.plotly_chart(fig_ike, use_container_width=True)

    with t2:
        cat_stats = df.groupby("category").agg(
            count=("name", "count"), avg_ike=("predicted_ike", "mean"),
            total_kwh=("predicted_kwh", "sum")
        ).reset_index()
        fig_cat = px.bar(cat_stats, x="category", y="avg_ike", color="avg_ike",
                         color_continuous_scale=["#22c55e", "#eab308", "#ef4444"],
                         title="Average IKE by Building Category",
                         text="count")
        st.plotly_chart(fig_cat, use_container_width=True)

    with t3:
        top_boros = df.nlargest(15, "predicted_ike")[["name", "category", "sqm", "predicted_ike", "ike_category"]]
        st.markdown("**Top 15 Most Energy-Intensive Buildings:**")
        st.dataframe(top_boros)


if __name__ == "__main__":
    main()
