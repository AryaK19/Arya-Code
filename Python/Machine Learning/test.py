from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,1))
print(scaler.fit_transform([[12],[1]]))
print(scaler.inverse_transform(scaler.fit_transform([[12],[1]])))