from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import pandas as pd

# Features and target
features = ['price_num','discount_pct','ratings','reviews_num','price_to_mrp_ratio','log_reviews']
X = df[features].fillna(0)
y = df['popularity_score'].fillna(0)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


rf = RandomForestRegressor(n_estimators=200, random_state=42)
rf.fit(X_train, y_train)

# Predictions
y_pred = rf.predict(X_test)

# Metrics
import numpy as np

print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R² Score:", r2_score(y_test, y_pred))


importances = pd.Series(rf.feature_importances_, index=features).sort_values(ascending=True)

plt.figure(figsize=(7,5))
importances.plot(kind='barh', color='teal')
plt.title("Feature Importance for Popularity Score")
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.show()
