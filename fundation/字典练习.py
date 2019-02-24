#字典练习
#将人名作为字典的键
#字典中包含吉安phone和addr
people={"alice":{
	'phone':'2341',
	'addr':'fodjfja'
},
'ben':{
	'phone':'32464646',
	 'addr':"dfsadfsadf"},
	'celi':{'phone':'31664654','addr':'dfadfasdfsadfsadf'}}
#电话号码标签
labels={'phone':'phone number','addr':'address'}
name=input('Name:')
request=input('输入选择')
#使用正确的键
if request=='p':key='phone'
if request=='a':key='addr'
#当名字是字典包含键时候打印
if name in people:
	print("{}'s {} is {}".format(name,labels[key],people[name][key]))
