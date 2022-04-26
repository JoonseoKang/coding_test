a = ['/', '/hello', '/hello/tmp', '/root/tmp', '/root/hello', '/root/tmp/hello']

s = '/hello'

s.split('/')[-1]
s.index(s.split('/')[-1])

d_list = []

for i in a:
    k = i.split('/')
    if s in i and k.index(s.split('/')[-1]) == s.index(s.split('/')[-1]):

        d_list.append(i)

d_list

for i in a:
    if i in d_list:
        a.remove(i)

for i in d_list:
    a.remove(i)

