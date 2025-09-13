import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(6,4))
df['price_num'].hist(bins=50)
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(6,4))
df[df['price_num'] <= 10000]['price_num'].hist(bins=50, color='blue')
plt.title("Price Distribution (Zoomed: 0–10,000)")
plt.xlabel("Price")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(6,4))
df[df['price_num'] <= 4000]['price_num'].hist(bins=50, color='blue')
plt.title("Price Distribution (Zoomed: 0–4000)")
plt.xlabel("Price")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(6,4))
df['ratings'].hist(bins=20, color='green')
plt.title("Ratings Distribution")
plt.xlabel("Ratings")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(6,4))
df['reviews_num'].hist(bins=50, color='purple')
plt.title("Number of Reviews Distribution")
plt.xlabel("Number of Reviews")
plt.ylabel("Count")
plt.yscale("log")  # log scale to handle skew
plt.show()

plt.figure(figsize=(6,5))
plt.scatter(df['reviews_num'], df['ratings'], alpha=0.3, color='red')
plt.xscale("log")
plt.title("Ratings vs Number of Reviews")
plt.xlabel("Number of Reviews (log scale)")
plt.ylabel("Ratings")
plt.show()

plt.figure(figsize=(6,5))
plt.scatter(df['reviews_num'], df['popularity_score'], alpha=0.3, color='blue')
plt.xscale("log")
plt.title("Popularity vs Number of Reviews")
plt.xlabel("Number of Reviews (log scale)")
plt.ylabel("Popularity Score")
plt.show()

df['review_bucket'] = pd.cut(df['reviews_num'], 
                             bins=[0,10,50,200,1000,5000,10000,50000],
                             labels=["0-10","10-50","50-200","200-1k","1k-5k","5k-10k","10k+"])

rating_by_bucket = df.groupby('review_bucket')['ratings'].mean()

plt.figure(figsize=(7,4))
rating_by_bucket.plot(kind='bar', color='teal')
plt.title("Average Rating by Review Bucket")
plt.xlabel("Review Bucket")
plt.ylabel("Average Rating")
plt.show()

top_brands_count = df['brand_name'].value_counts().head(15)

plt.figure(figsize=(12,5))
top_brands_count.plot(kind='bar', color='skyblue')
plt.title("Top 15 Brands by Number of Products")
plt.xlabel("Brand")
plt.ylabel("Number of Products")
plt.xticks(rotation=90)
plt.show()

brand_summary = df.groupby('brand_name').agg(
    n_products=('pants_description','count'),
    avg_rating=('ratings','mean'),
    avg_discount=('discount_pct','mean'),
    avg_price=('price_num','mean'),
    avg_popularity=('popularity_score','mean'),
    rating_variance=('ratings','std')
).reset_index()

brand_summary.sort_values('n_products', ascending=False).head(10)

top_brands_popularity = brand_summary.sort_values('avg_popularity', ascending=False).head(15)

plt.figure(figsize=(10,5))
sns.barplot(data=top_brands_popularity, x='brand_name', y='avg_popularity', palette="viridis")
plt.title("Top 15 Brands by Average Popularity")
plt.xticks(rotation=90)
plt.ylabel("Average Popularity Score")
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(data=brand_summary, x='avg_discount', y='avg_rating', size='n_products', alpha=0.6, legend=False)
plt.title("Brand-Level Discount vs Rating")
plt.xlabel("Average Discount %")
plt.ylabel("Average Rating")
plt.show()

consistent_brands = brand_summary.sort_values('rating_variance').head(10)
consistent_brands[['brand_name','avg_rating','rating_variance','n_products']]


importances = pd.Series(rf.feature_importances_, index=features).sort_values(ascending=True)

plt.figure(figsize=(7,5))
importances.plot(kind='barh', color='teal')
plt.title("Feature Importance for Popularity Score")
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.show()


