"""
Data: 2019/5/27 15:29
Desc: 验证url的合法性
"""
import re

url = 'http://xn--6krw3qq4bh1bb25f.xn--fiqs8s/'

def legal_url(url):
    pattern = re.compile(r'^(http|https)://'                                                 # 头部协议
                         r'([0-9a-zA-Z_!~*()-]+.)?'                                          # 域名的头部,不一定存在
                         r'([0-9a-zA-Z][0-9a-zA-Z-]{0,61})?[0-9a-zA-Z].'                     # 二级域名
                         r'[0-9a-zA-Z-]{2,13}'                                               # 后缀，例如.cn以及.xn--fiqs8s
                         r'(:[0-9]{1,4})?'                                                    # 端口号
                         r'((/?)|'                                                            # 后面有没有反斜杠
                         r'(/[0-9a-zA-Z_!~*().;?:@&=+$,%#-\|\{\}]+)+/?)$')                   # 反斜杠后面的内容
    result = re.match(pattern, url)
    if result.group() == url:
        return True
    else:
        return False

if __name__ == '__main__':
    print(legal_url(url))