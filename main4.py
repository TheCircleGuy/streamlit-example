import gspread
import streamlit as st

sa= gspread.service_account()
sh= sa.open(" bybit api")

wks = sh.worksheet("Analysis")

pnl_value = wks.acell('C17').value
positions_value = wks.acell('C13').value
trades_value = wks.acell('C14').value
pnl = int(float(pnl_value))
percent = 50/100
# percent  = st.number_input('Chia cho Tân (%)', value = 50)/100


print(pnl)

st.markdown("<h1 style='text-align: center;'>Trading Dashboard</h1>", unsafe_allow_html=True)
st.write("")

# Metrics centered
metrics_col = st.columns(5)

# PnL Metric
with metrics_col[0]:
    st.metric(label='PnL ($)', value=float(pnl_value))

# Positions Metric
with metrics_col[2]:
    st.metric(label='Positions', value=float(positions_value))

# Positions Metric
with metrics_col[3]:
    st.metric(label='tỉ lệ cho Tân', value=percent)

# Trades Metric
with metrics_col[4]:
    st.metric(label='của Chú TA', value=(pnl * (1-percent)))

with metrics_col[4]:
    st.metric(label='của Tân', value=(pnl*percent))



st.markdown("<h2 style='text-align: center;'>Charts</h2>", unsafe_allow_html=True)

# Curved border and shadow style
chart_style = """
<style>
    .chart-container {
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        overflow: hidden;
    }
</style>
"""
# Apply the style
st.markdown(chart_style, unsafe_allow_html=True)

# Chart 1
st.markdown("""
<div class="chart-container">
    <iframe width="600" height="371" seamless frameborder="0" scrolling="no" 
    src="https://docs.google.com/spreadsheets/d/e/2PACX-1vTV3KRzGqbMxwP4J6oRQdEU36VizRh580pdXQTZLkiMN_SfYH_pNawhJlWo6MQu1sDVHT9P4VPRLFoL/pubchart?oid=89569499&amp;format=interactive"></iframe>
</div>
""", unsafe_allow_html=True)

st.write("")
# Chart 2
st.markdown("""
<div class="chart-container">
    <iframe width="600" height="371" seamless frameborder="0" scrolling="no" 
    src="https://docs.google.com/spreadsheets/d/e/2PACX-1vTV3KRzGqbMxwP4J6oRQdEU36VizRh580pdXQTZLkiMN_SfYH_pNawhJlWo6MQu1sDVHT9P4VPRLFoL/pubchart?oid=1103638229&amp;format=interactive"></iframe>
</div>
""", unsafe_allow_html=True)
