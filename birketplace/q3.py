tstring = 'this is {template} {template} is {state}'

variables = [['template', 'string'], ['state', 'changed']]

for i in variables:
    tstring = tstring.replace('{'+ i[0] + '}', i[1])

tstring


t = 'this is {template} {template} is {state}'

v = [['template', 'string'], ['state', '{template}']]

for i in v:
    t = t.replace('{'+ i[0] + '}', i[1])

t


t = 'this is {template} {template} is {state}'

v = [['template', '{state}'], ['state', '{template}']]

answer =''
vv = []
for i in v:
    vv.append(i[1])
vv


count = 0
for i in vv:
    l = i.replace('{', '')
    l = l.replace('}', '')
    for j in v:
        if l in j[0]:
            count +=1
    if count >=2:
        answer = t
    else:
        for i in v:
            answer = t.replace('{' + i[0] + '}', i[1])


answer

t


