import pandas as pd 
import numpy as np

import math
import datetime as dt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense ,LSTM
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
plt.style.use('fivethirtyeight')

start = dt.datetime.now() - dt.timedelta(days= 360)
# df = yf.get_data_yahoo('TATASTEEL.NS',start=str(start))
# startdate = datetime(2022,1,1)

# data = pdr.get_data_yahoo(ticker_NS, str(start))
df = pdr.get_data_yahoo('TATASTEEL.NS', start=startdate)
print(df)


# plt.figure(figsize=(8,4))
# plt.title('Closing Price History')
# plt.plot(df['Close'])
# plt.xlabel('Date',fontsize=9)
# plt.ylabel('Closing Price',fontsize=9)
# plt.show()

data = df.filter(['Close'])
dataset = data.values
training_data_len = math.ceil(len(dataset)*.8)

scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(dataset)

train_data = scaled_data[:training_data_len,:]
x_train = []
y_train = []
for i in range(60,len(train_data)):
    x_train.append(train_data[i-60:i, 0])
    y_train.append(train_data[i,0])
    
x_train, y_train = np.array(x_train ), np.array(y_train)      

x_train = np.reshape(x_train,(x_train.shape[0], x_train.shape[1], 1))

model = Sequential()
model.add(LSTM(50, return_sequences=True,input_shape=(x_train.shape[1],1)))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))
model.compile(optimizer='adam' , loss='mean_squared_error')

model.fit(x_train, y_train, batch_size=1, epochs=1)

test_data = scaled_data[training_data_len - 60 : , :]

x_test = []
y_test = dataset[training_data_len:, :]
for i in range (60 , len(test_data)):
    x_test.append(test_data[i-60:i,0])

x_test = np.array(x_test)

x_test = np.reshape(x_test,(x_test.shape[0],x_test.shape[1],1))

print(x_test)

prediction = model.predict(x_test)
    
prediction = scaler.inverse_transform(prediction)



rmse = np.sqrt(np.mean(prediction - y_test)**2 )

train = data[: training_data_len]
valid = data[training_data_len:]

valid['Predictions'] = prediction

plt.figure(figsize=(8,4))
plt.title("Model")
plt.xlabel('Date')
plt.ylabel('Closing Price',fontsize=9)
plt.plot(train['Close'])
plt.plot(valid[['Close','Predictions']])

plt.legend(['Train','Val','Predictions','Future pred',f'{100-rmse}% correct'], loc='lower right')
plt.show()



