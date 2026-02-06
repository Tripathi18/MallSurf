import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

df = pd.read_csv("features.csv")

# Define performance label
df['performance'] = pd.qcut(
    df['daily_revenue_inr'],
    q=3,
    labels=['Low', 'Medium', 'High']
)

X = df.drop(
    ['daily_revenue_inr', 'performance', 'store_name', 'shop_id', 'record_date', 'category'],
    axis=1
)
y = df['performance']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

clf = RandomForestClassifier(
    n_estimators=400,
    max_depth=15,
    min_samples_leaf=4,
    random_state=42
)

clf.fit(X_train, y_train)
pred = clf.predict(X_test)

print(classification_report(y_test, pred))
