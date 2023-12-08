import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('your_trading_data.csv')
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

def trading_strategy(data):

    signals = pd.DataFrame(index=data.index)
    signals['Buy_Signal'] = np.random.choice([0, 1], size=len(signals))
    signals['Sell_Signal'] = np.random.choice([0, 1], size=len(signals))

    return signals

signals = trading_strategy(data)

plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Close'], label='Цена закрытия', alpha=0.2)
plt.plot(signals.loc[signals['Buy_Signal'] == 1].index, data['Close'][signals['Buy_Signal'] == 1], '^', markersize=10, color='g', label='Buy Signal')
plt.plot(signals.loc[signals['Sell_Signal'] == 1].index, data['Close'][signals['Sell_Signal'] == 1], 'v', markersize=10, color='r', label='Sell Signal')
plt.title('Торговые сигналы')
plt.xlabel('Дата')
plt.ylabel('Цена закрытия')
plt.legend()
plt.show()
