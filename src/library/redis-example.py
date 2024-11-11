import redis

'''
https://blog.csdn.net/qq_42402854/article/details/129324497?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-0-129324497-blog-105775652.235^v43^pc_blog_bottom_relevance_base3&spm=1001.2101.3001.4242.1&utm_relevant_index=3
'''

def connectRedis():
    r = redis.Redis(
        host='127.0.0.1',
        port=6379,
        password=""
    )

    r.set('foo', 'Bar')
    print(r.get('foo'))

if __name__ == '__main__':
    connectRedis()