import urllib.request
import os

city = '华南'
time = [2019, 8, 18, 16, 0]  #初始时间：年-月-日-时-分 (世界时)
endt = [2019, 8, 18, 16, 0]  #结束时间
inter = 12  #间隔时间（分钟）,只能为6的整数倍且不大于60
path = 'J:/影响天气/lecay/雷达图获取/'

f = open(path+'station.txt', 'r')
data = f.read()
rows = data.split('\n')
rows.pop()
stl=[]
for row in rows:
    sr = row.split('\t')
    stl.append(sr)
sta = dict(stl)
f.close()

def mkdir(path):
    folder = os.path.exists(path)
    if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
    else:
        pass  
file = path+city
mkdir(file)  

area = ['全国','东北','华北','西北','西南','华中','华南','华东']
if city in area:
    eni = 1
else:
    eni = 0

daynum = [31,28,31,30,31,30,31,31,30,31,30,31]
while not(time[1]==endt[1] and time[2]==endt[2] and time[3]==endt[3] and time[4]==endt[4]):
    url='http://pi.weather.com.cn/i/product/pic/l/sevp_aoc_rdcp_sldas_ebref_%s_l88_pi_%d%02d%02d%02d%02d0000%d.png' % (sta[city],time[0],time[1],time[2],time[3],time[4],eni)
    print(url)
    urllib.request.urlretrieve(url,file+'\%s%d%02d%02d%02d%02d.png' % (city,time[0],time[1],time[2],time[3],time[4]))
    time[4] = time[4] + inter
    if time[4] >= 60 :
        time[4] = time[4] - 60
        time[3] = time[3] + 1
        if time[3] >= 24 :
            time[3] = 0
            time[2] = time[2] + 1
            if time[2] > daynum[time[1]-1] :
                time[2] = 1
                time[1] = time[1] + 1
url='http://pi.weather.com.cn/i/product/pic/l/sevp_aoc_rdcp_sldas_ebref_%s_l88_pi_%d%02d%02d%02d%02d0000%d.png' % (sta[city],time[0],time[1],time[2],time[3],time[4],eni)
print(url)
urllib.request.urlretrieve(url,file+'\%s%d%02d%02d%02d%02d.png' % (city,time[0],time[1],time[2],time[3],time[4]))
