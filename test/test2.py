headers = '''
Host: www.http.header.free.fr
Accept: image/gif, image/x-xbitmap, image/jpeg, image/pjpeg,
Accept-Language: Fr
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 4.0)
Connection: Keep-Alive
'''

headers = dict([[field.strip() for field in pair.split(':', 1)] for pair in headers.strip().split('\n')])

print(headers)