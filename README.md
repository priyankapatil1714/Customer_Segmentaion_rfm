1. Objective
Customer segmentation based on purchase behavior using RFM analysis so that the business can target each customer group differently, improving marketing efficiency and customer retention.

2. Dataset
The dataset was obtained from Kaggle and is named "UCI Online Retail II".
Total rows: 541,910
Each row represents a single product line item within a customer's invoice.
Time period: December 2010 – December 2011
After data cleaning and aggregation, the data was converted into a customer-level RFM table containing 4,338 unique customers.

3. Methodology
The following steps were performed:

-Downloaded the dataset from Kaggle.
-Performed data cleaning:
    Dropped rows with missing Customer IDs.
    Removed returns/negative quantities.
    Removed StockCode = 'B'.
    Removed records where Price = 0.
-Performed RFM Feature Engineering:
    Recency: Number of days since the customer's last purchase.
    Frequency: Number of unique invoices/purchases.
    Monetary: Total amount spent by the customer.
-Applied Log Transformation to reduce the effect of outliers by compressing their scale without removing the data.
-Applied StandardScaler to bring all features to a comparable scale.
-Used two methods to determine the suitable number of clusters:
   Elbow Method: Suggested k = 4 as a reasonable bend point.
   Silhouette Score: The highest score was obtained at k = 2. However, a two-cluster segmentation provides limited actionable business insights. Therefore, k = 5 was selected because it provides a more granular and useful understanding of customer behavior.
-Performed K-Means Clustering using k = 5.
-Performed PCA visualization to visualize the clusters in a two-dimensional space.

4. Choosing K
The Elbow Method indicated that k = 4 was a reasonable choice based on the bend in the WCSS curve.
The Silhouette Score was highest at k = 2. However, dividing customers into only two groups, such as "High Value" and "Low Value," provides limited business insight.
k = 5 showed a local peak in the silhouette score compared with its neighboring values (k = 4 and k = 6) and provided a more granular and actionable segmentation of customer behavior.
Therefore, k = 5 was selected for the final K-Means clustering model.

5.Segment Profiles
| Cluster | Segment | Recency | Frequency | Monetary |
|---|---|---|---|---|
| 0 | New/Low-Engagement | 63 | 1 | 390.89 |
| 1 | Champions | 26 | 16 | 10066.26 |
| 2 | Promising/Regular | 55 | 4 | 1617.88 |
| 3 | At-Risk/Fading | 245 | 1 | 392.30 |
| 4 | Lost | 583 | 1 | 343.27 |

6.Segment Interpretation
Champions:          Recent, frequent, and high-value customers.
Promising/Regular:  Customers with moderate purchase frequency and spending who have the potential to become Champions.
New/Low-Engagement: Customers with recent purchases but low purchase frequency.
At-Risk/Fading:     Customers who have not purchased recently and show low engagement.
Lost:               Customers who have been inactive for a long period.

7.Business Recommendations
Segment	Recommended Strategy
New/Low-Engagement:  	Send welcome-back messages and small incentives to encourage another purchase.
Champions:              Offer loyalty rewards, cashback, exclusive offers, and referral perks.
Promising/Regular:	    Provide personalized recommendations and discounts to encourage them to become Champions.
At-Risk/Fading:	        Run stronger win-back campaigns with attractive incentives and limited-time offers.
Lost:	                Make one low-cost automated reactivation attempt and minimize further marketing investment if there is no response

8.Tools and Technologies
Python
Pandas
NumPy
Scikit-learn
Matplotlib
Seaborn
K-Means Clustering
PCA
RFM Analysis