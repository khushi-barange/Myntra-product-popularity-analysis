# Myntra Product Popularity Analysis

##  Project Overview
This project analyzes **52,000+ products from Myntra** to uncover the factors driving **product popularity**.  
The focus is on how **price, discounts, ratings, reviews, and brand strategies** influence customer perception and sales.  
A mix of **Exploratory Data Analysis (EDA)** and **Machine Learning (Random Forest Regression)** was used to identify popularity drivers and provide **business recommendations**.

---

## Objectives
- Identify **key drivers of product popularity** on Myntra.  
- Explore **brand-level performance** (consistency, discounts, popularity).   

---

## Dataset
- Source: Web-scraped Myntra dataset  
- Size: ~52,120 rows × 7 columns  
- Key fields:  
  - `brand_name`  
  - `price`  
  - `MRP`  
  - `discount_percent`  
  - `ratings`  
  - `number_of_ratings`  

### Feature Engineering
- `price_num` / `mrp_num` → Numeric conversions  
- `discount_pct` → Cleaned discount values  
- `reviews_num` & `log_reviews` → Review count (log-transformed for skew)  
- `price_to_mrp_ratio` → Pricing efficiency  
- `popularity_score = ratings × log(reviews)` → Proxy for product popularity  

---

## Exploratory Data Analysis (EDA)
### Price & Discount
- Most products priced **₹500–₹3000**  
- Discounts mostly in **20–40% range**  
- Very high discounts don’t guarantee popularity  

### Ratings & Reviews
- Ratings cluster around **3.5–4.5**  
- Reviews are **heavily skewed** (most products <100 reviews)  
- Popularity correlates strongly with **review volume**  

### Brand-Level Insights
- Big brands (WROGN, Roadster, UCB) dominate in **volume**  
- Smaller brands (ESPRIT, 7OUNCE, Killer) excel in **popularity**  
- **Consistency** matters more than deep discounts  

---

## Modeling Popularity
- Model: **Random Forest Regressor**  
- Features: Price, Discount, Ratings, Reviews, Price-to-MRP ratio  
- Results:  
  - **RMSE = 0.0469**  
  - **R² = 0.9999**  

### Feature Importance
- `log_reviews` (52%) + `reviews_num` (42%) → **strongest predictors**  
- `ratings` (~6%) → minor effect  
- `price` & `discount_pct` (~0%) → negligible  

--> Popularity is **driven by social proof, not discounts**.  

---

## Business Insights
1. **Social Proof is King** → Reviews drive popularity more than discounts.  
2. **Moderate Discounts (30–50%)** are more effective than deep markdowns.  
3. **Consistent Brands** should be promoted as “Trusted Sellers.”  
4. **Hidden Gems** (high-rated but low-review products) offer growth potential.  
5. **Review Campaigns** for new products are critical to boost trust.  

---

## Business Impact
- Optimizing discounts and reviews could raise sales by **10–15%**.  
- Review-boosting strategies improve **conversion rates** and **customer trust**.  
- Brand benchmarking strengthens **partnership negotiations**.  
- Promoting hidden gems expands catalog appeal with minimal cost.  

---

## Deliverables
- **Jupyter Notebooks**: Data cleaning, EDA, Modeling  
- **Business Report (PDF)**: Insights + recommendations  
- **Visualizations**: Price distribution, Ratings & Reviews Analysis
- **README.md (this file)**: Case study summary  

---

## Tech Stack
- **Python**: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn  
- **Visualization**: Matplotlib, Seaborn  
- **Modeling**: RandomForestRegressor (Sklearn)  
- **Reporting**: Markdown  

---

## Future Scope
- Deploy interactive dashboard (Streamlit/Power BI)  
- Sentiment analysis of customer reviews (NLP)  
- Recommendation system based on popularity drivers  

---

## Author
**Khushi Barange**  
Aspiring Data Scientist 
