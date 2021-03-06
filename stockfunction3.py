import requests
from bs4 import BeautifulSoup as bs
import datetime
import pandas as pd
import mpl_finance as mpf
import matplotlib.pyplot as plt
import numpy as np

today = datetime.date.today()
year  = today.year
month = today.month

first = datetime.date(day=1, month=today.month, year=today.year)
lastYear = (first - datetime.timedelta(days=1)).year
lastMonth = (first - datetime.timedelta(days=1)).month

second= datetime.date(day=1, month=lastMonth, year=lastYear)
lastYear2 = (second - datetime.timedelta(days=1)).year
lastMonth2 = (second - datetime.timedelta(days=1)).month

#load csv
def GetSidcsv(sid,year,month):
	directory = 'stock' + '/' + str(sid) + '/' + year + '/'
	filename  = str(year)+'-'+str(month)+'.csv'
	openfile  = directory + filename
	#csvfile   = open(openfile)
	csvfile   = open(openfile,'r',encoding='utf-8')
	F_list=csvfile.read().strip().split('\n')[2:]
	return F_list

#csv to dataframe
def GetSidData(sid,year,month):
	data=GetSidcsv(sid,year,month)
	A_list=[]
	Temp_list=[]
	for i in data:
		try:
			i=i.split(',')
			date=str(i[0])
			Totalvol=int(i[1])
			Totalprice=int(i[2])
			price_O=float(i[3])
			price_H=float(i[4])
			price_L=float(i[5])
			price_C=float(i[6])
			Spread=str(i[7])
			num=int(i[8])
			Temp_list += (date,Totalvol,Totalprice,price_O,price_H,price_L,price_C,Spread,num)
			A_list.append(Temp_list)
			Temp_list=[]
		except ValueError as e:
			pass	
	return A_list



def Getmvg(sid,year,month):
	A_list=[]
	datas=GetSidData(sid,year,month)
	for data in datas:
		price_Mx100=data[2]*100/data[1]
		A_list.append(price_Mx100)		
	return A_list		

def GetmvgSignal(sid):
	Alist = []
	Blist = Getmvg(sid,str(lastYear2),str(lastMonth2))+Getmvg(sid,str(lastYear),str(lastMonth))+Getmvg(sid,str(year),str(month))
	d5mvg  = sum(Blist[-5:])/5
	d10mvg = sum(Blist[-10:])/10
	d20mvg = sum(Blist[-20:])/20
	old_d5mvg  = sum(Blist[-10:-5])/5
	old_d10mvg = sum(Blist[-15:-5])/10
	old_d20mvg = sum(Blist[-25:-5])/20	
	Alist.append(d5mvg)
	Alist.append(d10mvg)
	Alist.append(d20mvg)
	Alist.append(old_d5mvg)
	Alist.append(old_d10mvg)
	Alist.append(old_d20mvg)
	return Alist

def GetSidDataFrame(sid,start,end):
	year_start = int(start.split('-')[0])
	year_end   = int(end.split('-')[0])
	month_start= int(start.split('-')[1])
	month_end  = int(end.split('-')[1])
	df=[]
	while (year_start<year_end):
		while(month_start<=12):
			year="{0:0=4d}".format(year_start) 
			month="{0:0=2d}".format(month_start) 
			df+=GetSidData(sid,year,month)
			month_start+=1
		year_start+=1
		month_start=1
	while (year_start==year_end):
		while(month_start<=month_end):
			year="{0:0=4d}".format(year_start)
			month="{0:0=2d}".format(month_start)
			df+=GetSidData(sid,year,month)
			month_start+=1
		year_start+=1
		month_start=1	

	df=pd.DataFrame(df,columns=['date','vol','volprice','open','high','low','close','spread','num'])
	df=df[df["date"].between(start,end)].reset_index(drop=True)
	return df	

def GetAllSid():
	sids=['1262', '1435', '1437', '1516', '2062', '2348', '2358', '2443', '2514', '2904', '3040', '4536', '5284', '5871', '6184', '6464', '6504', '6581', '6625', '6641', '6655', '6670', '6671', '8033', '8341', '8404', '8411', '8422', '8427', '8442', '8463', '8464', '8466', '8467', '8473', '8478', '8480', '8481', '8482', '8488', '8497', '8499', '9802', '9902', '9904', '9905', '9907', '9910', '9911', '9914', '9917', '9919', '9921', '9924', '9925', '9927', '9928', '9929', '9930', '9933', '9934', '9935', '9938', '9939', '9940', '9941', '9941', '9942', '9944', '9945', '9955', '2302', '2303', '2329', '2330', '2337', '2338', '2342', '2344', '2351', '2363', '2369', '2379', '2388', '2401', '2408', '2434', '2436', '2441', '2449', '2451', '2454', '2458', '2481', '3006', '3014', '3016', '3034', '3035', '3041', '3054', '3094', '3189', '3257', '3413', '3443', '3519', '3530', '3532', '3536', '3545', '3579', '3583', '3588', '3661', '3686', '3711', '4919', '4952', '4961', '4968', '5269', '5285', '5305', '5471', '6202', '6239', '6243', '6257', '6271', '6415', '6451', '6525', '6531', '6533', '6552', '6573', '8016', '8028', '8081', '8110', '8131', '8150', '8261', '8271', '2301', '2305', '2324', '2331', '2352', '2353', '2356', '2357', '2362', '2364', '2365', '2376', '2377', '2380', '2382', '2387', '2395', '2397', '2399', '2405', '2417', '2424', '2425', '2442', '2465', '3002', '3005', '3013', '3017', '3022', '3046', '3057', '3060', '3231', '3416', '3494', '3515', '3701', '3706', '3712', '4916', '4938', '5215', '5258', '5264', '6117', '6128', '6166', '6172', '6206', '6230', '6235', '6277', '6414', '6579', '6591', '8114', '8163', '8210', '9912', '1101', '1102', '1103', '1104', '1108', '1109', '1110', '1201', '1203', '1210', '1213', '1215', '1216', '1217', '1218', '1219', '1220', '1225', '1227', '1229', '1231', '1232', '1233', '1234', '1235', '1236', '1256', '1702', '1737', '1301', '1303', '1304', '1305', '1307', '1308', '1309', '1310', '1312', '1312', '1313', '1314', '1315', '1319', '1321', '1323', '1324', '1325', '1326', '1337', '1339', '1340', '4306', '1402', '1409', '1410', '1413', '1414', '1416', '1417', '1418', '1419', '1423', '1434', '1439', '1440', '1441', '1443', '1444', '1445', '1446', '1447', '1449', '1451', '1452', '1453', '1454', '1455', '1456', '1457', '1459', '1460', '1463', '1464', '1465', '1466', '1467', '1468', '1470', '1472', '1473', '1474', '1475', '1476', '1477', '4414', '4426', '4438', '1503', '1504', '1506', '1507', '1512', '1513', '1514', '1515', '1517', '1519', '1521', '1522', '1524', '1525', '1526', '1527', '1528', '1529', '1530', '1531', '1532', '1533', '1535', '1536', '1537', '1538', '1539', '1540', '1541', '1558', '1560', '1568', '1583', '1587', '1589', '1590', '1592', '2049', '2228', '2231', '2236', '2371', '3167', '3346', '4526', '4532', '4540', '4551', '4552', '4555', '4557', '4560', '4562', '4566', '5288', '6605', '8222', '8374', '8996', '1603', '1604', '1605', '1608', '1609', '1611', '1612', '1614', '1615', '1616', '1617', '1618', '1626', '4930', '1316', '1704', '1708', '1709', '1710', '1711', '1712', '1713', '1714', '1717', '1718', '1721', '1722', '1723', '1724', '1725', '1726', '1727', '1730', '1732', '1735', '1773', '1776', '3708', '4720', '4722', '4725', '4739', '4755', '4763', '4764', '4766', '1598', '1701', '1707', '1720', '1731', '1733', '1734', '1736', '1760', '1762', '1783', '1786', '1789', '3164', '3705', '4104', '4106', '4108', '4119', '4133', '4137', '4141', '4142', '4144', '4148', '4155', '4164', '4190', '4737', '4746', '6452', '6541', '6666', '1802', '1806', '1809', '1810', '1817', '1902', '1903', '1904', '1905', '1906', '1907', '1909', '2002', '2002', '2006', '2007', '2008', '2009', '2010', '2012', '2013', '2014', '2015', '2017', '2020', '2022', '2023', '2024', '2025', '2027', '2028', '2029', '2030', '2031', '2032', '2033', '2034', '2038', '2069', '3004', '5007', '5538', '9958', '2101', '2102', '2103', '2104', '2105', '2106', '2107', '2108', '2109', '2114', '2115', '6582', '1338', '2201', '2204', '2206', '2207', '2227', '2239', '2243', '2323', '2340', '2349', '2374', '2393', '2406', '2409', '2426', '2438', '2448', '2466', '2475', '2486', '2489', '2491', '2499', '3008', '3019', '3024', '3031', '3038', '3049', '3050', '3051', '3059', '3149', '3356', '3383', '3406', '3437', '3454', '3481', '3504', '3535', '3557', '3576', '3591', '3622', '3669', '3673', '3698', '4934', '4935', '4942', '4956', '4960', '4976', '5234', '5243', '5259', '5484', '6116', '6120', '6131', '6164', '6168', '6176', '6209', '6225', '6226', '6278', '6288', '6289', '6405', '6431', '6443', '6456', '6477', '6668', '8105', '8215', '2314', '2321', '2332', '2345', '2412', '2419', '2439', '2444', '2450', '2455', '2485', '2496', '2498', '3025', '3027', '3045', '3047', '3062', '3311', '3380', '3419', '3596', '3682', '3694', '3704', '4904', '4906', '4977', '5388', '6136', '6142', '6152', '6216', '6285', '6416', '6442', '6674', '8011', '8101', '1471', '1582', '2059', '2308', '2313', '2316', '2327', '2328', '2355', '2367', '2368', '2375', '2383', '2385', '2392', '2402', '2413', '2415', '2420', '2421', '2428', '2429', '2431', '2440', '2456', '2457', '2460', '2462', '2467', '2472', '2476', '2478', '2483', '2484', '2492', '2493', '3003', '3011', '3015', '3021', '3023', '3026', '3032', '3037', '3042', '3044', '3058', '3090', '3229', '3296', '3308', '3321', '3338', '3376', '3432', '3501', '3533', '3550', '3593', '3605', '3607', '3645', '3653', '3679', '4545', '4912', '4915', '4927', '4943', '4958', '4989', '4999', '5469', '6108', '6115', '6133', '6141', '6153', '6155', '6165', '6191', '6197', '6205', '6213', '6224', '6251', '6269', '6282', '6412', '6449', '8039', '8046', '8103', '8213', '8249', '2347', '2414', '2430', '2459', '3010', '3028', '3033', '3036', '3048', '3055', '3209', '3312', '3528', '3702', '5434', '6189', '6281', '8070', '8072', '8112', '2427', '2453', '2468', '2471', '2480', '3029', '3130', '4994', '5203', '6112', '6183', '6214', '1436', '1438', '1442', '1805', '1808', '2501', '2504', '2505', '2506', '2509', '2511', '2515', '2516', '2520', '2524', '2527', '2528', '2530', '2534', '2535', '2536', '2537', '2538', '2539', '2540', '2542', '2543', '2545', '2546', '2547', '2548', '2597', '2841', '2923', '3052', '3056', '3266', '3703', '5515', '5519', '5521', '5522', '5525', '5531', '5533', '5534', '6177', '9906', '9946', '2208', '2603', '2605', '2606', '2607', '2608', '2609', '2610', '2611', '2612', '2613', '2615', '2617', '2618', '2630', '2633', '2634', '2636', '2637', '2642', '5607', '5608', '8367', '2701', '2702', '2704', '2705', '2706', '2707', '2712', '2722', '2723', '2727', '2731', '2739', '2748', '5706', '8940', '9943', '2801', '2809', '2812', '2816', '2820', '2823', '2832', '2834', '2836', '2838', '2838', '2845', '2849', '2850', '2851', '2852', '2855', '2867', '2880', '2881', '2881', '2881', '2882', '2882', '2882', '2883', '2884', '2885', '2886', '2887', '2887', '2888', '2889', '2890', '2891', '2891', '2892', '2897', '5876', '5880', '6005', '6024', '1432', '2601', '2614', '2901', '2903', '2905', '2906', '2908', '2910', '2911', '2912', '2913', '2915', '2929', '2936', '2939', '4807', '5906', '5907', '8429', '8443', '8454', '2616', '6505', '8926', '9908', '9918', '9926', '9931', '9937']

	return sids


#from yahoo get all sid list
def GetYahooSid():
	sidlist=[]	
	categorys=['其他','半導體','電腦週邊','水泥','食品','塑膠','紡織','電機','電器電纜','化學','生技醫療','玻璃','造紙','鋼鐵','橡膠','汽車',
				'光電','通信網路','電子零組件','電子通路','資訊服務','其他電子','營建','航運','觀光','金融','貿易百貨','油電燃氣']
	for category in categorys:
		url='https://tw.stock.yahoo.com/h/kimosel.php?tse=1&cat='+category+'&form=menu&form_id=stock_id&form_name=stock_name&domain=0'
		res=requests.get(url)
		soup=bs(res.text,'html.parser')
		for sid in soup.find_all('a',{'class':'none'}):
			sidlist.append(sid.text[1:5].strip('\n'))
	return sidlist

def plot_OHLC(df,name):
	df_m = df['volprice']/df['vol']
	sma_5=df_m.rolling(window=5).mean()
	sma_10=df_m.rolling(window=10).mean()
	sma_20=df_m.rolling(window=20).mean()
	x=round(len(df['date'])/14)
	fig = plt.figure(figsize=(24, 12))
	ax = fig.add_subplot(1, 1, 1)
	ax.set_xticks(range(0, len(df['date']),x))
	ax.set_xticklabels(df['date'][::x])
	ax.plot(sma_5, label='5MA',color='yellow')
	ax.plot(sma_10, label='10MA',color='blue')
	ax.plot(sma_20, label='20MA',color='purple')
	ax.legend(loc='upper left')
	mpf.candlestick2_ochl(ax, df['open'], df['close'], df['high'], df['low'],
                      width=0.5, colorup='r', colordown='green',
                      alpha=0.6)
	ax.set_title(name)
	plt.grid()
	plt.show()	