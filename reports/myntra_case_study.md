
# Myntra Data Analysis Case Study

## 1. Problem Statement
Understanding what factors make a product popular on Myntra, one of India's leading online fashion retailers. The goal is to analyze product features like price, discount, ratings, and reviews to extract actionable business insights.

## 2. Dataset Description
The dataset was scraped from Myntra and contains product-level details such as price, MRP, discount information, ratings, number of reviews, and product categories.

## 3. Data Cleaning & Processing
- Price, MRP, and Discount columns were parsed to extract numeric values.
- Discount percentage was calculated as:

    ```
    discount_pct = ((mrp_num - price_num) / mrp_num) * 100
    ```
- Reviews were normalized from strings (e.g., '1.2k') to numbers.
- Log transformation applied to review counts: `log_reviews = np.log1p(reviews_num)`.
- A popularity proxy score was calculated:

    ```
    popularity_score = ratings * log_reviews
    ```

## 4. Exploratory Data Analysis (EDA) Insights
- **Discount vs Popularity**: Products with higher discounts tend to have higher ratings and more reviews.
- **Price Distribution**: Majority of products are priced within the mid-range, indicating the primary consumer segment.
- **Rating vs Reviews**: Strong positive correlation between number of reviews and ratings.
- **Brand Analysis**: Top brands by number of products do not always align with top brands by average popularity.

_Key Plot Examples:_
- Ratings vs Number of Reviews scatter plot
- Popularity Score vs Number of Reviews scatter plot (log scale)
- Feature Importance plot showing reviews_num and ratings as top contributors

## 5. Business Questions Addressed
- **Does discount impact product popularity?**

  Analysis suggests a positive correlation between discount percentage and number of ratings.
- **What price segments are most popular?**

  Mid-priced products receive the most engagement, both in terms of ratings and reviews.
- **Are higher rated products also those with higher discounts?**

  A moderate positive correlation observed.

## 6. Key Recommendations
- Focus marketing efforts on mid-priced products with reasonable discounts to maximize engagement.
- Regularly offer discounts in the range of 10-30% where data shows a noticeable uplift in product popularity.
- Monitor products that deviate from the trend (high price but high ratings) for potential premium segment strategies.

## 7. Limitations
- Data collected via scraping may have missing or inconsistent entries.
- External factors like brand reputation, seasonality, and advertisement spend are not captured.
- Causality cannot be confirmed—only correlation analysis performed.

## 8. Conclusion
The analysis confirms that **reviews, number of reviews, and ratings are the key factors driving product popularity** on Myntra. The popularity score was primarily influenced by these variables, as supported by the feature importance analysis. Pricing and discount also contribute but to a lesser extent. This highlights the importance of customer feedback and engagement in driving sales.

