import backtrader as bt
from datetime import datetime


class FirstStrategy(bt.Strategy):
  def log(self,txt):
    print(txt)
   
  def __init__(self):
    self.dataclose = self.datas[0].close
  
  def next(self):
    self.log(self.dataclose[0])
    
if __name__ == "__main__":
    cerebro = bt.Cerebro()
    cerebro.addstrategy(FirstStrategy)
    
    datapath = "Nifty.csv"
    
    data = bt.feeds.GenericCSVData(
        dataname = datapath,
        fromdate = datetime(2015,12,1),
        todate = datetime(2021,12,22),
        dtformat = ("%Y-%m-%d"),
        datetime = 0,
        open = 1,
        high = 2,
        low =3,
        close =4,
        volume =6,reverse=False)
    
    cerebro.adddata(data)
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
    cerebro.run()
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
    
