"""
Data: 2019/5/27 13:56
Desc：验证url的合法性
"""
import re


def legal_url(url):
    pattern = re.compile(r'^(http|https|ftp|rtsp|mms)://'                                     # 头部协议
                         r'(((([0-9a-zA-Z_!~*().&=+$%-]+:)?[0-9a-zA-Z_!~*().&=+$%-]+@)?'      # ftp协议中的test@test部分   
                         r'([0-9]{1,3}.){3}[0-9][0-9]{1,3})|'                                 # ip地址，类似于172.25.254.250
                         r'[0-9a-zA-Z_!~*()-]+.'                                              # 域名的头部
                         r'([0-9a-zA-Z][0-9a-zA-Z-]{0,61})?[0-9a-zA-Z].'                     #  二级域名
                         r'[a-z]{2,6}'                                                        # 后缀，例如.com和.museum .cn
                         r'(:[0-9]{1,4})?'                                                    #  端口号
                         r'((/?)|'                                                            # 后面有没有反斜杠
                         r'(/[0-9a-zA-Z_!~*().;?:@&=+$,%#-\|\{\}]+)+/?)$)')                      # 反斜杠后面的内容
    result = re.match(pattern, url)
    if result == url:
        return True
    else:
        return False
















