import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("myntra_dataset_ByScraping.csv")
df

import re
def parse_price(x):
    if pd.isna(x): return None
    s = str(x)
    # remove currency symbols and commas
    s = re.sub(r'[^\d.]', '', s)
    try:
        return float(s)
    except:
        return None

# example column names; adjust if different
for col in ['price', 'mrp', 'discount']:
    if col in df.columns:
        df[col + '_num'] = df[col].apply(parse_price)

# If discount isn't present or inconsistent, compute it
if 'price_num' in df.columns and 'mrp_num' in df.columns:
    df['discount_pct'] = ((df['mrp_num'] - df['price_num']) / df['mrp_num']).clip(0,1)*100

import re
import numpy as np

# helper to clean ₹1,299 → 1299
def parse_price(x):
    if pd.isna(x): return None
    s = str(x)
    s = re.sub(r'[^\d.]', '', s)
    try:
        return float(s)
    except:
        return None

# clean price + MRP
df['price_num'] = df['price'].apply(parse_price)
df['mrp_num'] = df['MRP'].apply(parse_price)

# clean discount (already % but might have strings like '40% OFF')
def parse_discount(x):
    if pd.isna(x): return None
    s = re.sub(r'[^\d.]', '', str(x))
    try:
        return float(s)
    except:
        return None

df['discount_pct'] = df['discount_percent'].apply(parse_discount)

# reviews (number_of_ratings)
def parse_reviews(x):
    if pd.isna(x): return 0
    s = str(x).lower().strip()
    if 'k' in s:
        return float(s.replace('k','')) * 1000
    if 'm' in s:
        return float(s.replace('m','')) * 1_000_000
    try:
        return float(re.sub(r'[^\d.]','',s))
    except:
        return 0

df['reviews_num'] = df['number_of_ratings'].apply(parse_reviews)

# log transformation
df['log_reviews'] = np.log1p(df['reviews_num'])

# ratio (safe division)
df['price_to_mrp_ratio'] = np.where(df['mrp_num']>0, df['price_num']/df['mrp_num'], None)

# popularity proxy (ratings * log_reviews)
df['popularity_score'] = df['ratings'] * df['log_reviews']

