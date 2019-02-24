database=[
['albert','1234'],['jones','9843']]
username=input('user name:')
pin=input("pin code:")
if [username,pin] in database:
	print('grant')
