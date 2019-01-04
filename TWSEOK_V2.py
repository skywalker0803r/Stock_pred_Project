
# coding: utf-8

# In[9]:

import requests
import os
import random
import json
import csv,re
import time, datetime,os
from bs4 import BeautifulSoup as bs
from stock_module import stock_function


# In[10]:

dt = datetime.datetime.now()
dt.year
dt.month

# In[11]:

def GetAllSid():
	sids=['1262', '1435', '1437', '1516', '2062', '2348', '2358', '2443', '2514', '2904', '3040', '4536', '5284', '5871', '6184', '6464', '6504', '6581', '6625', '6641', '6655', '6670', '6671', '8033', '8341', '8404', '8411', '8422', '8427', '8442', '8463', '8464', '8466', '8467', '8473', '8478', '8480', '8481', '8482', '8488', '8497', '8499', '9802', '9902', '9904', '9905', '9907', '9910', '9911', '9914', '9917', '9919', '9921', '9924', '9925', '9927', '9928', '9929', '9930', '9933', '9934', '9935', '9938', '9939', '9940', '9941', '9941', '9942', '9944', '9945', '9955', '2302', '2303', '2329', '2330', '2337', '2338', '2342', '2344', '2351', '2363', '2369', '2379', '2388', '2401', '2408', '2434', '2436', '2441', '2449', '2451', '2454', '2458', '2481', '3006', '3014', '3016', '3034', '3035', '3041', '3054', '3094', '3189', '3257', '3413', '3443', '3519', '3530', '3532', '3536', '3545', '3579', '3583', '3588', '3661', '3686', '3711', '4919', '4952', '4961', '4968', '5269', '5285', '5305', '5471', '6202', '6239', '6243', '6257', '6271', '6415', '6451', '6525', '6531', '6533', '6552', '6573', '8016', '8028', '8081', '8110', '8131', '8150', '8261', '8271', '2301', '2305', '2324', '2331', '2352', '2353', '2356', '2357', '2362', '2364', '2365', '2376', '2377', '2380', '2382', '2387', '2395', '2397', '2399', '2405', '2417', '2424', '2425', '2442', '2465', '3002', '3005', '3013', '3017', '3022', '3046', '3057', '3060', '3231', '3416', '3494', '3515', '3701', '3706', '3712', '4916', '4938', '5215', '5258', '5264', '6117', '6128', '6166', '6172', '6206', '6230', '6235', '6277', '6414', '6579', '6591', '8114', '8163', '8210', '9912', '1101', '1102', '1103', '1104', '1108', '1109', '1110', '1201', '1203', '1210', '1213', '1215', '1216', '1217', '1218', '1219', '1220', '1225', '1227', '1229', '1231', '1232', '1233', '1234', '1235', '1236', '1256', '1702', '1737', '1301', '1303', '1304', '1305', '1307', '1308', '1309', '1310', '1312', '1312', '1313', '1314', '1315', '1319', '1321', '1323', '1324', '1325', '1326', '1337', '1339', '1340', '4306', '1402', '1409', '1410', '1413', '1414', '1416', '1417', '1418', '1419', '1423', '1434', '1439', '1440', '1441', '1443', '1444', '1445', '1446', '1447', '1449', '1451', '1452', '1453', '1454', '1455', '1456', '1457', '1459', '1460', '1463', '1464', '1465', '1466', '1467', '1468', '1470', '1472', '1473', '1474', '1475', '1476', '1477', '4414', '4426', '4438', '1503', '1504', '1506', '1507', '1512', '1513', '1514', '1515', '1517', '1519', '1521', '1522', '1524', '1525', '1526', '1527', '1528', '1529', '1530', '1531', '1532', '1533', '1535', '1536', '1537', '1538', '1539', '1540', '1541', '1558', '1560', '1568', '1583', '1587', '1589', '1590', '1592', '2049', '2228', '2231', '2236', '2371', '3167', '3346', '4526', '4532', '4540', '4551', '4552', '4555', '4557', '4560', '4562', '4566', '5288', '6605', '8222', '8374', '8996', '1603', '1604', '1605', '1608', '1609', '1611', '1612', '1614', '1615', '1616', '1617', '1618', '1626', '4930', '1316', '1704', '1708', '1709', '1710', '1711', '1712', '1713', '1714', '1717', '1718', '1721', '1722', '1723', '1724', '1725', '1726', '1727', '1730', '1732', '1735', '1773', '1776', '3708', '4720', '4722', '4725', '4739', '4755', '4763', '4764', '4766', '1598', '1701', '1707', '1720', '1731', '1733', '1734', '1736', '1760', '1762', '1783', '1786', '1789', '3164', '3705', '4104', '4106', '4108', '4119', '4133', '4137', '4141', '4142', '4144', '4148', '4155', '4164', '4190', '4737', '4746', '6452', '6541', '6666', '1802', '1806', '1809', '1810', '1817', '1902', '1903', '1904', '1905', '1906', '1907', '1909', '2002', '2002', '2006', '2007', '2008', '2009', '2010', '2012', '2013', '2014', '2015', '2017', '2020', '2022', '2023', '2024', '2025', '2027', '2028', '2029', '2030', '2031', '2032', '2033', '2034', '2038', '2069', '3004', '5007', '5538', '9958', '2101', '2102', '2103', '2104', '2105', '2106', '2107', '2108', '2109', '2114', '2115', '6582', '1338', '2201', '2204', '2206', '2207', '2227', '2239', '2243', '2323', '2340', '2349', '2374', '2393', '2406', '2409', '2426', '2438', '2448', '2466', '2475', '2486', '2489', '2491', '2499', '3008', '3019', '3024', '3031', '3038', '3049', '3050', '3051', '3059', '3149', '3356', '3383', '3406', '3437', '3454', '3481', '3504', '3535', '3557', '3576', '3591', '3622', '3669', '3673', '3698', '4934', '4935', '4942', '4956', '4960', '4976', '5234', '5243', '5259', '5484', '6116', '6120', '6131', '6164', '6168', '6176', '6209', '6225', '6226', '6278', '6288', '6289', '6405', '6431', '6443', '6456', '6477', '6668', '8105', '8215', '2314', '2321', '2332', '2345', '2412', '2419', '2439', '2444', '2450', '2455', '2485', '2496', '2498', '3025', '3027', '3045', '3047', '3062', '3311', '3380', '3419', '3596', '3682', '3694', '3704', '4904', '4906', '4977', '5388', '6136', '6142', '6152', '6216', '6285', '6416', '6442', '6674', '8011', '8101', '1471', '1582', '2059', '2308', '2313', '2316', '2327', '2328', '2355', '2367', '2368', '2375', '2383', '2385', '2392', '2402', '2413', '2415', '2420', '2421', '2428', '2429', '2431', '2440', '2456', '2457', '2460', '2462', '2467', '2472', '2476', '2478', '2483', '2484', '2492', '2493', '3003', '3011', '3015', '3021', '3023', '3026', '3032', '3037', '3042', '3044', '3058', '3090', '3229', '3296', '3308', '3321', '3338', '3376', '3432', '3501', '3533', '3550', '3593', '3605', '3607', '3645', '3653', '3679', '4545', '4912', '4915', '4927', '4943', '4958', '4989', '4999', '5469', '6108', '6115', '6133', '6141', '6153', '6155', '6165', '6191', '6197', '6205', '6213', '6224', '6251', '6269', '6282', '6412', '6449', '8039', '8046', '8103', '8213', '8249', '2347', '2414', '2430', '2459', '3010', '3028', '3033', '3036', '3048', '3055', '3209', '3312', '3528', '3702', '5434', '6189', '6281', '8070', '8072', '8112', '2427', '2453', '2468', '2471', '2480', '3029', '3130', '4994', '5203', '6112', '6183', '6214', '1436', '1438', '1442', '1805', '1808', '2501', '2504', '2505', '2506', '2509', '2511', '2515', '2516', '2520', '2524', '2527', '2528', '2530', '2534', '2535', '2536', '2537', '2538', '2539', '2540', '2542', '2543', '2545', '2546', '2547', '2548', '2597', '2841', '2923', '3052', '3056', '3266', '3703', '5515', '5519', '5521', '5522', '5525', '5531', '5533', '5534', '6177', '9906', '9946', '2208', '2603', '2605', '2606', '2607', '2608', '2609', '2610', '2611', '2612', '2613', '2615', '2617', '2618', '2630', '2633', '2634', '2636', '2637', '2642', '5607', '5608', '8367', '2701', '2702', '2704', '2705', '2706', '2707', '2712', '2722', '2723', '2727', '2731', '2739', '2748', '5706', '8940', '9943', '2801', '2809', '2812', '2816', '2820', '2823', '2832', '2834', '2836', '2838', '2838', '2845', '2849', '2850', '2851', '2852', '2855', '2867', '2880', '2881', '2881', '2881', '2882', '2882', '2882', '2883', '2884', '2885', '2886', '2887', '2887', '2888', '2889', '2890', '2891', '2891', '2892', '2897', '5876', '5880', '6005', '6024', '1432', '2601', '2614', '2901', '2903', '2905', '2906', '2908', '2910', '2911', '2912', '2913', '2915', '2929', '2936', '2939', '4807', '5906', '5907', '8429', '8443', '8454', '2616', '6505', '8926', '9908', '9918', '9926', '9931', '9937']

	return sids


# id_list = ['1101','2303','6666','1234'] #inout the stock IDs
id_list = GetAllSid()
now = datetime.datetime.now() #now time
year_list = range (2016,now.year+1)
# year_list = range (2007,now.year+1) #since 2007 to this year
month_list = range(1,13)  # 12 months
# ###http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20170605&stockNo=2330

# In[12]:
def get_adDate(curr_date):
    strDate = str(curr_date)
    year_str = strDate[:3]
    ad_year = str(int(year_str) + 1911)
    ad_date = ad_year +'-'+ strDate[4:6] +'-'+ strDate[7:9]
    return ad_date
#standard web crawing process
def get_webmsg (year, month, stock_id):
    try:
        date = str (year) + "{0:0=2d}".format(month) +'01' ## format is yyyymmdd
        sid = str(stock_id)
        url_twse = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date='+date+'&stockNo='+sid
        res =requests.post(url_twse,)
        soup = bs(res.text , 'html.parser')
        smt = json.loads(soup.text)     #convert data into json
    except Exception as e:
        e_type, e_value, e_tb = sys.exc_info()
        print("ErrorType:{}\nMessage:{}\nInformation:{}\n",format(e_type, e_value, e_tb))
        #print("After waiting 1200 Second(20minute) this process will to be continue down files")
        #time.sleep(1200)
    return smt
# In[13]:
#write in csv process
def write_csv(stock_id,directory,filename,smt):
    writefile = directory + filename               #set output file name
    outputFile = open(os.path.realpath(writefile),'w',newline='', encoding='utf-8')
    outputWriter = csv.writer(outputFile)
    #head = ''.join(smt['title'].split())
    #a = [head,""]
    tt=smt['title'].split()
    outputWriter.writerow(tt)
    outputWriter.writerow(smt['fields'])
    for data in (smt['data']):

        data[0] = get_adDate(data[0])
        data[1] = re.sub(r",","",data[1])
        data[2] = re.sub(r",","",data[2])
        data[-1] = re.sub(r",","",data[-1])
        outputWriter.writerow(data)

    outputFile.close()


# In[14]:

#create a directory in the current one doesn't exist
def makedirs (year, month, stock_id):
    sid = str(stock_id)
    yy      = str(year)
    mm       = str(month)
    #os.path.realpath('stock/2303/2007/2007-02.csv')
    directory = 'stock'+'/'+sid +'/'+ yy
    if not os.path.exists(os.path.realpath(directory)):
        os.makedirs (os.path.realpath(directory))  # os.makedirs able to create multi folders    
def get_stockdata(year, month, stock_id,directory,filename):
    global k
    try:
        smt = get_webmsg(year ,month, stock_id)           #put the data into smt 
        if smt["stat"]!='OK':return False
        makedirs (year, month, stock_id)                  #create directory function
        write_csv (stock_id,directory, filename, smt)    # write files into CSV
        currentdata=stock_id+","+str(year)+"年"+str(month)+"月"
        #i=random.randint(3,6)#set random second
        i=stock_function.get_sleepTime()
        # print("爬取資料中目前爬取完"+currentdata+"的資料..第["+str(k+1)+"]筆將在"+str(i)+"秒後抓取..")
        xx=stock_function.write_log('OK',stock_id,str(year),str(month),k)
        k=k+1
        # xx=stock_function.write_log("OK",sid,yy,str(mm),(k-1))
        # print(xx)
        time.sleep(i)
        while i>0 :
             print("爬取資料中目前爬取完"+currentdata+"的資料..第"+str(k)+"下一筆將在"+str(i)+"秒後抓取..第")
             i=i-1
             time.sleep(1)
             os.system("cls")
        return True
    except Exception as e:
        j=random.randint(5,20)*60
        xx=stock_function.write_log('Lock',stock_id,str(year),str(month),j)
        while j>0:
            print("等待重新連線中:",j)
            j=j-1
            time.sleep(1)
            # os.system("cls")                        
        #從剛剛中斷那一筆繼續做避免造成斷層
        # smt = get_webmsg(year ,month, stock_id)
        get_stockdata(year, month, stock_id,directory,filename)		
        # makedirs (year, month, stock_id)
        # write_csv (stock_id,directory, filename, smt)
        # currentdata=sid+","+yy+"年"+str(mm)+"月"
        # i=random.randint(3,6)#set random second
        # while i>0 :
        #     print("爬取資料中目前爬取完"+currentdata+"的資料")
        #     print("下一筆資料將在"+str(i)+"秒後抓取...")
        #     i=i-1
        #     time.sleep(1)
        #     os.system("cls")
# In[15]:
k=1
for stock_id in id_list:
    for year in year_list:
        for month in month_list:
            if (dt.year == year and month > dt.month) :break  # break loop while month over current month            
            sid = str(stock_id)
            yy  = str(year)
            mm  = month
            mm_next = int(month) + 1
            yy_next = str(year)
            if mm_next > 12:
                mm_next = 1
                yy_next = str(int(yy_next) + 1)            
            #os.path.realpath('stock/2303/2007/2007-02.csv')
            directory = 'stock'+'/'+sid +'/'+yy +'/'       #setting directory
            filename = str(yy)+'-'+str("%02d"%mm)+'.csv'
            # if os.path.isdir(os.path.realpath(directory+filename)):
            #     print('File '+filename+' is Exist!')
            #     continue
            if os.path.isfile(os.path.realpath(directory+filename)) and (os.path.isfile(os.path.realpath('stock'+'/'+sid +'/'+yy_next +'/'+yy_next+'-'+str("%02d"%mm_next)+'.csv'))):
                # print(os.path.realpath(directory+yy+'-'+str("%02d"%mm)+'.csv'))
                # print(os.path.realpath('stock'+'/'+sid +'/'+yy_next +'/'+yy_next+'-'+str("%02d"%mm_next)+'.csv'))
                # print(os.path.isfile(os.path.realpath('stock'+'/'+sid +'/'+yy_next +'/'+yy_next+'-'+str("%02d"%mm_next)+'.csv')))
                # time.sleep(3)
                continue
            else:    
                if not get_stockdata(year, month, stock_id,directory,filename):break
print("Success to Down files of Stock Total:"+str(k)+" record~")
xx=stock_function.write_log('Success','0000',stock_function.get_datetime_str('Y'),stock_function.get_datetime_str('M'),0)                	


                #continue
