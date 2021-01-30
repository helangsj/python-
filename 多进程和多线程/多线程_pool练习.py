from multiprocessing.dummy import Pool
import time
namelist = ['aa','bb','cc']
def get_name(a):
    start_time = time.time()
    #使用睡眠时间来充当线程阻塞
    time.sleep(2)
    print(a)
    return a+'11'
    end_time = time.time()
    print("耗时",end_time-start_time)
if __name__ == "__main__":
    # 这是使用单线程进行操作，需要等前面的执行完成之后才会执行后面的语句
    start_time1 = time.time()
    # for i in namelist:
    #     get_name(i)

    #多线程语句
    #创建线程池，参数为线程个数
    pool = Pool(3)
    #使用map函数传入参数，其中返回结果为列表
    d = pool.map(get_name,namelist)
    print(d)
    end_time1 = time.time()
    print("总耗时",end_time1-start_time1)
