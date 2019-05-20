from json import loads, dump
from requests import get

def get_data(mid, page):
    ls = []
    for i in range(1, page + 1):
        url = 'https://space.bilibili.com/ajax/member/getSubmitVideos?mid=' + str(mid) + '&pagesize=30&tid=0&page=' + str(i) + '&keyword=&order=pubdate'
        html = get(url)
        text = loads(html.text)
        for i in text['data']['vlist']:
            video = {}
            url_1 = 'https://www.bilibili.com/video/av'
            video['视频名称'] = i['title']
            video['视频长度'] = i['length']
            video['视频链接'] = url_1 + str(i['aid'])
            video['发布时间'] = int(i['created'])

            ls.append(video)
    ls1 = sorted(ls, key = lambda x:x['发布时间'], reverse = False)
    for i in ls1:
        del i['发布时间']
    return ls1

def to_json(data, txt):
    txtname = txt + '.txt'
    with open(txtname, 'w', encoding='utf-8') as f:
    
        dump(data,f,ensure_ascii=False,indent=4)
    
def main():
    id = input("请输入up主的UID：")
    page =  eval(input("请输入要爬取的页数："))
    txt = input("请输入保存的文件名：")
    data = get_data(id, page)
    to_json(data, txt)


if __name__ == '__main__':
    main()
