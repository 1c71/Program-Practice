# python2.7
# coding=utf-8


import httplib2
import re




def getAllImg(url):

    
    def get_page(url):
    # 给的网址必须带http://
        try:
            h = httplib2.Http(timeout=10)
            resp, content = h.request(url,"GET",
                                      headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.10 Safari/537.11'} )
            return content
        except:
            return None

      
    

    # 获取a标签里的url
    def get_next_target_a(S):
        
        start_link = S.find('href=')     # 先用小写的去匹配,试试看能不能匹配到,

        if start_link == -1:
            start_link = S.find('HREF=') # 用大写匹配, 如果网页上写的很奇葩,例如<a HrEf= 就抓不到了,
            if start_link == -1:
                return None, 0
        
        start_quote = S.find('"',start_link)
        end_quote = S.find('"',start_quote+1)
        url = S[start_quote+1:end_quote]
        return url, end_quote



    def get_next_target_img(S):
        
        start_link = S.find('src=')     # 先用小写的去匹配,试试看能不能匹配到,

        if start_link == -1:
            start_link = S.find('SRC=') # 用大写匹配, 如果网页上写的很奇葩,例如<a HrEf= 就抓不到了,
            if start_link == -1:
                return None, 0
        
        start_quote = S.find('"',start_link)
        end_quote = S.find('"',start_quote+1)
        url = S[start_quote+1:end_quote]
        return url, end_quote




    # 收集所有链接，返回一个列表
    def get_all_links_a(page):
        
        all = []
        
        while True:
            url, endpos = get_next_target_a(page)       # 获取所有a标签里面的链接
            if url:
                all.append(url)
                page = page[endpos:]
            else:
                break
        
        return all


    def get_all_links_img(page):    
        all = []
        while True:
            url, endpos = get_next_target_img(page)     # 获取所有img标签里面的链接
            if url:
                all.append(url)
                page = page[endpos:]
            else:
                break
        return all








    #这个函数获得url,通过下载这个url里面的信息
    def save_file(url):
        
        dirname = "images"      # 要保存图片的目录名,图片会保存到这里面

        # 尝试创建目录
        try:
            import os
            os.mkdir(dirname)   
        except:
            pass

        # 尝试打开url
        try:
            h = httplib2.Http(timeout=10)
            resp, content = h.request(url,"GET",
                                      headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.10 Safari/537.11'} )
            name = os.path.basename(url)
            f = open(dirname+"/"+name, "wb")    #以二进制方式保存，因为我们要下载的是图片
            f.write(content)
            f.close
        except:
            return False  





    #这里处理所有不以http开头,但以jpg之类的后缀结尾的链接，会认为是相对路径，并拼接网址尝试访问并下载。
    def start_not_by_http(list1):
        index = 0
        result = []
        for one in list1:
            pattern = re.compile(r'^[^http]',re.I)
            match = pattern.search(one)
            
            if match:
                #print list[index]
                result.append(list1[index])
            index = index + 1

        #print index+1  #这是每次循环都会自动增加的下标,循环完成后里面就是列表元素的个数，因为下标是从0开始的，所以要+1
        #print result



        last = []  #存放最终结果！
        lastIndex = 0 #又是存下标用的
        for o in result:
            linshi = o  #把每一个元素保存到linshi中，
            houzhui = linshi.split('.')[-1]    #拆分，拿到后缀(如果无法拆分会原样返回,比如拆分123123，会返回123123)
            if linshi == houzhui:
                lastIndex = lastIndex+1
                continue    # 去下一次循环
            
            pattern = re.compile(r'jpg$|png$|bmp$|gif$|jpeg$|ico$',re.I)
            match = pattern.findall(houzhui)


            if match:
                for ha in match:
                    last.append(result[lastIndex])
            #if match:
            #    last.append(result[lastIndex])
            lastIndex = lastIndex+1


        # 判断列表是否为空
        if last == []:
            print "last is empty"
            return None
        
        else:
            for one in last:
                print ("downloading......"+one)
                save_file(url+one)
                print ("done")
        
    


    # 这个函数处理以http开头并且以jpg,bmp什么的结尾的图片。会尝试打开并保存
    def start_with_http(list1):
        index = 0       # 用来存下标
        result = []     # 保存结果列表
        for one in list1:
            pattern = re.compile(r'^http.*jpg$|png$|bmp$|gif$|jpeg$|ico$',re.I)
            match = pattern.findall(one)
            
            if match:
                for ha in match:
                    result.append(list1[index])
            index = index + 1

        for one in result:
            print ("downloading......"+one)
            save_file(one)
            print ("done")



        

    source_code = get_page(url)  #拿到源代码
    # print source_code     # 输出源代码


    a = get_all_links_a(source_code)    #这个函数会以列表形式拿到图片的地址.例如: h0.gif
    a = a+get_all_links_img(source_code)



    list1 = []
    for b in a:
        list1.append(b)
    #print list1
    
    # list1里面是最终的所有链接的列表
    start_not_by_http(list1)
    start_with_http(list1)


        
       

if __name__ == '__main__':
    
    #getAllImg('http://www.chabudai.org/temp/wonderfl/honehone/img/')
    #getAllImg('http://jandan.net/')
    getAllImg('http://www.guokr.com/')
    
    # 
    # 会抓取该目录下所有a标签里的href，再访问并下载。所以有可能下载到不是图片的东西。
    







