i=1
while i<4:
	name=input("�������û���")[6:]
	password=input("����������")[5:]
	if name =="Kate" and password=="666666":
		print("��¼�ɹ�")
		break
	else:
		i=i+1
		if i==4:
			print("3�ζ�����,�˳�����")