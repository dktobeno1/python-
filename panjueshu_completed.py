# -*- coding: utf-8 -*-

import re,requests,time,random,queue,json
import multiprocessing
import mysql.connector

anyou = '破坏社会主义市场经济秩序'
year = '2016'

def randHeader():  # 随机获取headers头
    head_user_agent = ['Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
                       'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; rv:11.0) like Gecko)',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
                       'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
                       'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
                       'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/4.0.6.2000 Chrome/26.0.1410.43 Safari/537.1 ',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E; QQBrowser/7.3.9825.400)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0 ',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; BIDUBrowser 2.x)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/3.0 Safari/536.11']

    header = [
        {
            'Host': 'wenshu.court.gov.cn',
            'User-Agent': random.choice(head_user_agent),
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive'},
        {
            'Host': 'wenshu.court.gov.cn',
            'User-Agent': random.choice(head_user_agent),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'}
    ]
    return header

def get_ips():
    list_ip = ['125.88.74.122:81',
               '183.95.80.165:8080',
               '124.133.230.254:80',
               '183.78.183.156:82',
               '124.88.67.83:843',
               '42.81.58.199:80',
               '183.78.183.156:82',
               '125.88.74.122:85',
               '182.38.36.42:8998',
               '122.96.59.98:82',
               '221.3.6.2:8081',
               '171.8.79.143:8080',
               '220.174.236.211:80',
               '42.81.58.199:80',
               '183.165.150.216:8998',
               '183.78.183.156:82',
               '175.30.124.128:80',
               '60.250.72.252:8080',
               '222.92.141.250:80',
               '202.107.222.50:80',
               '122.116.229.240:80',
               '112.11.126.198:80',
               '220.174.236.211:80',
               '119.254.84.90:80',
               '118.122.250.109:80',
               '211.140.151.220:80',
               '118.99.178.21:8080',
               '222.169.193.162:8099',
               '112.11.126.202:80',
               '120.132.6.206:80',
               '122.228.179.178:80',
               '218.4.101.130:83',
               '111.12.96.188:80',
               '111.7.174.135:80',
               '101.204.163.82:8080',
               '58.52.201.119:8080',
               '183.95.80.165:8080',
               '124.234.157.250:80',
               '112.11.126.197:80',
               '111.206.163.235:80',
               '58.221.38.170:8080',
               '101.230.214.25:8080',
               '220.174.236.211:80',
               '183.78.183.156:82',
               '106.58.127.229:80',
               '112.11.126.202:8080',
               '61.135.217.3:80',
               '111.12.96.188:80',
               '119.254.84.90:80',
               '124.234.157.250:80',
               '112.11.126.204:8080',
               '222.92.141.250:80',
               '106.58.115.12:80',
               '112.11.126.198:8080',
               '60.250.72.252:8080',
               '218.104.148.157:8080',
               '122.229.17.128:80',
               '122.228.179.178:80',
               '202.107.222.50:80',
               '112.11.126.201:8080',
               '42.81.58.199:80',
               '118.99.178.21:8080',
               '61.191.41.130:80',
               '42.81.58.198:80',
               '222.73.27.178:80',
               '61.135.217.3:80',
               '61.191.41.130:80',
               '222.92.141.250:80',
               '218.4.101.130:83',
               '111.206.163.235:80',
               '125.140.111.61:80',
               '223.100.12.12:80',
               '124.88.67.63:80',
               '119.254.84.90:80',
               '124.133.230.254:80',
               '122.228.179.178:80',
               '111.13.7.42:83',
               '222.73.27.178:80',
               '222.76.217.25:80',
               '61.139.104.216:80',
               '211.140.151.220:80',
               '58.23.16.240:80',
               '124.88.67.13:81',
               '222.92.141.250:80',
               '61.139.104.216:80',
               '124.88.67.31:81',
               '118.122.250.109:80',
               '122.228.179.178:80',
               '218.4.101.130:83',
               '222.76.217.25:80',
               '111.13.7.42:81',
               '124.88.67.63:80',
               '111.206.163.235:80',
               '61.135.217.3:80',
               '211.140.151.220:80',
               '124.88.67.32:82',
               '119.254.84.90:80',
               '183.78.183.156:82',
               '58.23.16.240:80',
               '124.235.182.130:80',
               '122.142.77.84:80',
               '180.167.34.187:80',
               '111.13.7.42:81',
               '218.26.227.108:80',
               '124.88.67.35:82',
               '61.135.217.3:80',
               '218.4.101.130:83',
               '118.122.250.109:80',
               '183.254.149.120:80',
               '122.228.179.178:80',
               '124.88.67.54:81',
               '124.88.67.20:82',
               '124.88.67.30:83',
               '124.88.67.52:81',
               '111.206.163.235:80',
               '124.133.230.254:80',
               '111.12.96.188:80',
               '61.191.41.130:80',
               '124.88.67.31:83',
               '124.202.198.182:80',
               '124.88.67.54:80',
               '58.23.16.240:80',
               '122.228.179.178:80',
               '223.100.12.12:80',
               '124.88.67.35:83',
               '218.4.101.130:83',
               '118.122.250.109:80',
               '119.254.84.90:80',
               '124.133.230.254:80',
               '124.88.67.20:83',
               '61.191.41.130:80',
               '124.88.67.19:81',
               '222.76.217.25:80',
               '222.92.141.250:80',
               '218.241.153.211:81',
               '61.135.217.3:80',
               '61.139.104.216:80',
               '211.140.151.220:80',
               '111.13.7.42:83',
               '175.173.206.232:80',
               '183.190.148.221:80',
               '124.88.67.13:81',
               '111.206.163.235:80',
               '124.88.67.22:80',
               '222.169.193.162:8099',
               '61.135.217.3:80',
               '122.228.179.178:80',
               '119.254.84.90:80',
               '124.88.67.32:80',
               '218.27.165.22:80',
               '183.190.148.221:80',
               '118.122.250.109:80',
               '218.241.153.211:81',
               '222.169.193.162:8099',
               '111.13.7.42:81',
               '222.76.217.25:80',
               '111.206.163.235:80',
               '111.12.96.188:80',
               '222.92.141.250:80',
               '223.100.12.12:80'
               ]
    return list_ip

def failHandler():
    conn = mysql.connector.connect(user="root", password="", database="caipan")
    cursor = conn.cursor()
    proxy_ip = {}
    ip_time = 0
    sql = 'select * from failure where content is null order by id asc limit 10'
    while True:
        cursor.execute(sql)
        list_results = cursor.fetchall()
        if list_results:
            for t in list_results:
                docid = t[3]
                doc_url = 'http://wenshu.court.gov.cn/CreateContentJS/CreateContentJS.aspx?DocID=%s'%docid
                id = t[0]
                for a in range(5):
                    time.sleep(a*1.5)
                    try:
                        #headers = randHeader()
                        time.sleep(random.randint(0,2)+random.random())
                        if (int(time.time())-ip_time) > 60 or not proxy_ip:
                            proxy_ip={'http':'http://%s'%random.choice(get_ips())}
                            ip_time=int(time.time())
                        #print('爬取的问题')
                        result = requests.get(doc_url, proxies = proxy_ip, timeout = 5)
                        #print('不是爬取的问题',result.text)                   
                        pattern = re.compile(r'jsonHtmlData = "(.*?)";')
                        content = re.findall(pattern, result.text)[0]
                        #print(content)
                        content_sql = 'update failure set content=%s where id=%s'
                        cursor.execute(content_sql,[content, id])
                        conn.commit()
                        print('%s条数据已填充'%id)
                        break
                    except:
                        print('第%s次抓取失败，压入队列'%(a+1))
                        print(doc_url)
                        proxy_ip={'http':'http://%s'%random.choice(get_ips())}
                        ip_time=int(time.time())
                        continue
        else:
            print('>>>>>>>>>>>>>>>>fail补充抓取完成<<<<<<<<<<<<<<<<<<<')
            fsql = 'insert into panjueshu (name, yiju, docid, produce, type, num, court, date, content, url) select name, yiju, docid, produce, type, num, court, date, content, url from failure'
            cursor.execute(fsql)
            conn.commit()
            conn.close()
            break
#def getips():
#    ip_url = 'http://s.zdaye.com/?api=201612191506234219&count=200&fitter=2&px=2'
#    header = {'Connection': 'close'}
#    while True:
#        try:
#            obtan = requests.get(ip_url,headers = header,timeout = 300)
#            if '<bad>' not in obtan.text:
#                break
#        except:
#            time.sleep(3)
#            continue
#    ip_list = obtan.text.split('\r\n')
#    return ip_list

def worker(que):
    province = que.get()
    print(province)
    #qishi = 1
    jieshu = 100#不是定值
    proxy_ip = {}
    ip_time = 0
    ip_list=[]
    ip_list_time = 0
    s = queue.Queue(10)  # 案件数目请求未成功队列
    q = queue.Queue(10) # 案件详情未成功队列
    conn = mysql.connector.connect(user="root", password="", database="caipan")
    cursor = conn.cursor()
    the_url = 'http://wenshu.court.gov.cn/List/ListContent'
    index = 0
    try_j = 0
    while True:
        if not s.empty():
            index = s.get()
            try_j += 1
            if 2 <= try_j <= 3:
                time.sleep(3)
            elif 4 <= try_j <=5:
                time.sleep(6)
            elif try_j == 6:
                time.sleep(10)
            elif try_j == 7:
                time.sleep(20)
            elif try_j >=8:
                try_j = 0
        else:
            index += 1
            try_j = 0
            if index > jieshu:
                print('>>>>>>>>>>>>> %s 年 %s  %s 判决书抓取完毕<<<<<<<<<<<<<<'% (year,province,anyou))
                break
                
        try:
            data={'Param':'裁判年份:%s,二级案由:%s,法院地域:%s'% (year,anyou,province),
            'Page':'20',
            'Order':'法院层级',
            'Index':str(index),
            'Direction':'asc'

            }
            headers = randHeader()
            time.sleep(random.random())
            #if (int(time.time())-ip_list_time) >500 or not ip_list:
            #    ip_list = getips()
            #    print(ip_list)
            #    ip_list_time = int(time.time())
                                   
            if (int(time.time())-ip_time) > 60 or not proxy_ip:
                proxy_ip={'http':'http://%s'%random.choice(get_ips())}
                ip_time=int(time.time())
            print('正在爬取%s第%s页'%(province,index))
            resp=requests.post(the_url,data = data,headers = headers[0],proxies=proxy_ip,timeout=40)
            time.sleep(1)
            #respons=resp.text
            #pattern=re.compile(r'{\\"裁判要旨段原文\\":\\"(.*?)\\",\\"案件类型\\":\\"(.*?)\\",\\"裁判日期\\":\\"(.*?)\\",\\"案件名称\\":\\"(.*?)\\",\\"文书ID\\":\\"(.*?)\\",\\"审判程序\\":\\"(.*?)\\",\\"案号\\":\\"(.*?)\\",\\"法院名称\\":\\"(.*?)\\"}')
            #list_info = re.findall(pattern,respons)
            list_info = json.loads(json.loads(resp.text))
            print('第%s页有%s条(%s)'%(index,len(list_info)-1,province))
            #if len(list_info) == 0:
            #    print(respons,proxy_ip,'被禁')
            #    s.put(index)
            #    proxy_ip={'http':'http://%s'%random.choice(get_ips())}
            #    ip_time=int(time.time())
            #    print ("(Post)未访问成功，压入队列 %s (%s)"%(index,province))
            #    continue
            print('第%s页概要爬取成功(%s)'%(index,province))
        except:
            print(proxy_ip,'request出错')
            s.put(index)
            proxy_ip={'http':'http://%s'%random.choice(get_ips())}
            ip_time=int(time.time())
            print ("(Post)未访问成功，压入队列 %s (%s)"%(index,province))
            continue
        if index == 1:
            count = int(list_info[0]['Count'])
            if count%20 == 0:
                jieshu = count//20
            else:
                jieshu = count//20 + 1
            print('%s共%s页'% (province,jieshu))

        i = 0 #一页中的第i个案例
        try_i = 0 #一个案例的重试次数
        while True:
            if not q.empty():
                i = q.get()
                try_i += 1
                time.sleep(try_i * 1.5)
                if try_i > 4:
                    cursor.execute('insert into failure (name, yiju, docid, produce, type, num, court, date, url, doc_url) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',[name, yiju, docid, produce, type, num, court, date, url, doc_url])
                    conn.commit()
                    print ('!!!!!!!!!!!!!!!!!!! 请求过多,%s页第%s个案件:%s 写入Failure表中(%s) !!!!!!!!!!!!!!!!!!!'% (index, i, name, province))
                    i += 1
                    try_i = 0
                    q.queue.clear()
                    if i > len(list_info)-1:
                        print('第%s页爬取完成(%s)'%(index, province))
                        break
            else:
                i += 1
                try_i = 0
                if i > len(list_info)-1:
                    print('第%s页爬取完成(%s)'%(index, province))
                    break
            yiju = list_info[i]['裁判要旨段原文']
            type = list_info[i]['案件类型']
            date = list_info[i]['裁判日期']
            name = list_info[i]['案件名称']
            docid = list_info[i]['文书ID']
            produce = list_info[i]['审判程序']
            num = list_info[i]['案号']
            court = list_info[i]['法院名称']  
            url='http://wenshu.court.gov.cn/content/content?DocID=%s'%docid
            doc_url = 'http://wenshu.court.gov.cn/CreateContentJS/CreateContentJS.aspx?DocID=%s'%docid
            try:
                time.sleep(random.randint(0, 2) + random.random())
                if (int(time.time())-ip_time) > 60 or not proxy_ip:
                    proxy_ip={'http':'http://%s'%random.choice(get_ips())}
                    ip_time=int(time.time())
                html = requests.get(doc_url, proxies=proxy_ip, timeout=5)
                #print(html.text)
                pattern = re.compile(r'jsonHtmlData = "(.*?)";')
                content = re.findall(pattern,html.text)[0]
            except:
                q.put(i)
                proxy_ip={'http':'http://%s'%random.choice(get_ips())}
                ip_time=int(time.time())
                print ("(Get) %s未抓取成功,压入队列(%s) "% (name, province)) 
                print(doc_url)
                continue
            print('第%s页第%s个案件导入数据库(%s)'% (index, i, province))
            sql = 'insert into panjueshu (name, yiju, docid, produce, type, num, court, date, content, url) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            cursor.execute(sql,[name, yiju, docid, produce, type, num, court, date, content, url])
        conn.commit()               
        #print(self.count)
    if not que.empty():
        worker(que)
    conn.close()
if __name__=='__main__':
    q = multiprocessing.Queue()
    list_province = ['北京市', '广东省', '浙江省', '江苏省', '河南省', '四川省', '河北省', '山西省', '山东省', '湖北省', '湖南省', '辽宁省', '吉林省', '福建省', '安徽省',
               '黑龙江省', '上海市', '江西省', '内蒙古自治区', '广西壮族自治区', '海南省', '重庆市', '贵州省', '天津市', '云南省', '西藏自治区', '陕西省', '甘肃省',
               '青海省', '宁夏回族自治区', '新疆维吾尔自治区', '新疆维吾尔自治区高级人民法院生产建设兵团分院']
    for a in list_province:
        q.put(a)
    r = []
    for b in range(6):
        print('进程 %s'%(b+1))
        p = multiprocessing.Process(target = worker,args = (q,))
        p.start()
        r.append(p)
        time.sleep(3)
    for x in r:
        x.join()
    failHandler()
