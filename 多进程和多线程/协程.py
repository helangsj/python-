#导入协程对象
import asyncio
#
# async  def request(url):
#     print("输入的",url)
#
# #async 修饰的函数，调用之后返回的一个协程对象
# c = request('www.baidu.com')
#
# #创建一个事件循环对象
# loop = asyncio.get_event_loop()
# #将协程对象注册到loop中，然后启动loop
# loop.run_until_complete(c)
#
# #task的使用
# loop = asyncio.get_event_loop()
# #基于loop创建了一个task对象
# task = loop.create_task(c)
# print(task)
# loop.run_until_complete(task)
# print(task)
#
# #future的使用
# loop = asyncio.get_event_loop()
# #基于loop创建了一个task对象
# task = asyncio.ensure_future(c)
# print(task)
# loop.run_until_complete(task)
# print(task)
#

async  def request1(url):
    print("输入的",url)
    return url
def callback_func(task):
    #result 返回的是任务对象中封装的协程对象对应函数的返回值
    print(task.result())
 
#绑定回调
c = request1('www.baidu.com')
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(c)
#将回调函数绑定到任务对象中
task.add_done_callback(callback_func)
loop.run_until_complete(task)