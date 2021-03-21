def calc(x,y):
    def avg(z = []):
        return float(sum(z)/len(z))
    def calc(a = [],b = [],c = 0.0):
        for i in a:
            b.append(round(i-c,3))
    xavg = avg(x)
    yavg = avg(y)
    xma = []
    yma =[]
    sxma = []
    calc(x,xma,xavg)
    calc(y,yma,yavg)
    for i in xma:
        sxma.append(i*i)
    xyma = []
    for i in range(0,len(x)):
        xyma.append(xma[i] * yma[i])
    m = float(sum(xyma)/sum(sxma))
    c = yavg - m * xavg
    value = (round(m,3),round(c,3))
    return value

def diff(data,temp,rain):
    value = []
    dist = []
    ret_data = []
    for i,j in data.iteritems():
   
        value.append(i)
        t,r = j
        dist.append((pow((t-temp),2)+pow((r-rain),2))**(0.5))
    for i in range(3):
        ret_data.append(value[dist.index(min(dist))])
        dist.remove(dist[dist.index(min(dist))])
        value.remove(value[dist.index(min(dist))])
        
    return ret_data
        
        
    
