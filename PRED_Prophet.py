import pandas as pd
from stocker import Stocker
import stockfunction3 as st3 
import datetime
import warnings

#remove warrning
warnings.filterwarnings('ignore')

today = datetime.date.today()
#year  = str(today.year)
#month = str(today.month)

sids=['2816']

for sid in sids:
	start='2015-01-01'
	#end=str(today).split('-')[0]+'-'+str(today).split('-')[1]
	end='2018-12-26'
	df= st3.GetSidDataFrame(sid,start,end)
	df['date'] = pd.to_datetime(df['date'])
	df.set_index("date", inplace=True)

	df = df['close']
	price = df.squeeze()
	#print(price.head())
	#print(price.index)

	Target = Stocker(price,name=sid)


	#Target.changepoint_prior_validation(start_date ='2015-12-03',end_date ='2018-12-21',changepoint_priors = [0.3,0.4,0.45,0.5,0.6])

	#Target.plot_stock()

	
	#原始參數預測
	#model, model_data = Target.create_prophet_model(days=10)
	#原始參數回測
	#Target.evaluate_prediction()

	#Target.changepoint_prior_analysis(changepoint_priors=[0.001, 0.05, 0.1, 0.2])

	#Target.changepoint_prior_validation(start_date='2015-01-07', end_date='2018-12-21', changepoint_priors=[0.05,0.1,0.2,0.3,0.4])
	
	#調整參數為0.4
	Target.changepoint_prior_scale = 0.1
	#Target.changepoint_prior_scale = 0.6	
	#修改後回測
	Target.evaluate_prediction()
	#修改後參數預測
	Target.predict_future(days=30)
	Target.predict_future(days=90)
	model, model_data = Target.create_prophet_model(days=60)
	



	#Target.evaluate_prediction(start_date='2017-12-15', end_date='2018-12-17', nshares=1000)


	