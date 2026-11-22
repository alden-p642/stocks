import yfinance as yf, os
syms = ["RELIANCE","TCS","HDFCBANK","INFY","ICICIBANK","HINDUNILVR","SBIN","BHARTIARTL","ITC","KOTAKBANK","LT","AXISBANK","ASIANPAINT","MARUTI","SUNPHARMA","TITAN","BAJFINANCE","WIPRO","ULTRACEMCO","NTPC","ONGC","TATAMOTORS","TATASTEEL","POWERGRID","M&M","HCLTECH","ADANIENT","COALINDIA","JSWSTEEL","NESTLEIND","VEDL","DCMSHRIRAM","JIOFIN"]
ticker = {"TATAMOTORS": "TMPV"}  # Tata Motors demerged; adjust if Yahoo uses another symbol
os.makedirs("csv", exist_ok=True)
for s in syms:
    try:
        df = yf.download(ticker.get(s, s) + ".NS", period="5y", interval="1d", auto_adjust=False, progress=False)
        if df.empty:
            print("FAILED", s); continue
        df.columns = [c[0] if isinstance(c, tuple) else c for c in df.columns]
        out = df.reset_index()[["Date","Close","Volume"]]
        out["Date"] = out["Date"].astype(str).str[:10]
        out.to_csv(f"csv/{s}.NS.csv", index=False)
        print("saved", s, len(df))
    except Exception as e:
        print("ERROR", s, e)
