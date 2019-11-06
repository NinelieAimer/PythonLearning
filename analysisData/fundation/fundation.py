#python中的链式比较,A<B<C会变成(A<B and B<C)
print(-3<-2<-1)
print((-3<-2)<-1)

#arg,*args,**kwargs分别代表一个参数，一个元组参数，一个字典列表
def main(arg,*args,**kwargs):
    print(arg)
    print(args)
    print(kwargs)
main(1,[1,2,3,4,5],[1,2,3],inter=1,inter2=2)

#python中is 和 ==区别在于，一个判断地址相等，一个判断值相等
list_a=list_b=[1,2,3,4]
print(id(list_a),id(list_b),str(list_a),str(list_b))    #一个地址一个值

list_a=[4,5,6]
print(id(list_a),id(list_b))    #这里a地址不同了，但是b地址没有变

list_a[0]=7
list_a[1]=8
list_a[2]=9
print(id(list_a))   #当对列表修改时候，内存地址不会变的，但是地址中的内容会变得

#copy 和 deepcopy 在一般情况下相同的
import copy
list_c=[1,2,3,4,5]
list_d=copy.copy(list_c)
print(id(list_c),id(list_d))        #两个不同的地址

list_c.append(6)
print(list_c,list_d)        #不会受到影响

#但是如果有子对象，那就情况不一样了
import copy
list_e=[1,2,3,4,[1,2]]
list_f=copy.copy(list_e)

print(id(list_e),id(list_f))    #这里地址是不一样的
print(id(list_e[-1]),id(list_f[-1]))    #这个地址就是一样的了

list_e[-1].append(4)
print(list_e,list_f)    #这里都被改了

#值传递和引用传递
#值传递时候就是用副本传递，对地址不会改变，就是原来不会变
#这里tuple,int,str等就是值传递，不会改变
def test(number):
    number+=1
    return
a=6
test(a)
print(a)

#list和dict就是引用传递，会改变的
def test2(ls):
    ls[0]=5
    return
b=[1,2,3]
test2(b)
print(b)

#any()函数可以判断可迭代对象中是否含有除(0,'',False)之外的元素
a=[0,0,0]
b=[1,2,0]
print(any(a),any(b))   #这里就是False

#all函数就是可以判断可迭代对象中，是否全都是(False,'',0)

#format函数可以对任何变量进行赋值，但是%不能对tuple对象进行赋值
a='money'
b=[1,2]
print('time is %s %s'%(a,b))    #这里一定要用元组传入才可以

#del在python不会删除内存地址的
a=[1,2,3]
b=a
del a
print(id(b))    #这里b没有被删除

#对于数值型变量来说a=a+b和a=+b是一样的,都会生成新对象
#对于list和tuple说a+=b不会改变内存地址
a=[1,2,3]
b=[5,6,7]
print(id(a))
a+=b
print(id(a))    #一样的地址