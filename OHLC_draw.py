import stockfunction3 as st3 


#success-Match: ['1110',2816']
#抓一年來看
sids=['2816']
for sid in sids:
	df= st3.GetSidDataFrame(sid,'2018-01-01','2018-12-26')
	st3.plot_OHLC(df,'2816')	