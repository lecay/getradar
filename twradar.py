import urllib.request

def fun(blocknum,blocksize,totalsize):
    """
    blocknum:当前的块编号
    blocksize:每次传输的块大小
    totalsize:网页文件总大小
    """
    percent = blocknum*blocksize/totalsize
    if percent > 1.0:
        percent = 1.0
    percent = percent*100
    print("download : %.2f%%" %(percent))

for i in range(8,24,1):
    for j in range(0,51,10):
        url = 'https://www.cwb.gov.tw/V7/observe/radar/Data/HD_Radar/CV1_TW_3600_20190825%02d%02d.png' % (i,j)
        print(url)
        urllib.request.urlretrieve(url,'D:/test/'+'25%02d%02d.png' % (i,j), fun)