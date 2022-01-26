mkdir -p ~/.streamlit/

echo "[theme]
primaryColor='#105a5e'
backgroundColor='#e79b3b'
secondaryBackgroundColor='#e7c192'
textColor='#105a5e'
[server]
headless = true
port = $PORT
enableCORS = false
"> ~/.streamlit/config.toml
