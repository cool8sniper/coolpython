
# python 常用的魔术方法
首先说说什么是魔术方法？它是是面向对象的，它们是python 的一切。它们是以双下划线开头且以下划线结尾的(__init__)。它们可以给你的类增加“magic”的特殊方法.
感觉python魔术方法，没有一个比较好的总结文章。所以今天我总结一下比较常用的魔术方法。
首先一个类由哪些魔术方法那？python 给我们提供了dir()方法，可以方便的查看。
```python
In [47]: class A():
   ....:     pass
   ....:

In [48]: dir(A)
Out[48]:
['__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__']
```

通过上面的例子，可以列出A()类所有的魔术方法。咱们以这个例子为切入点。挑选一些比较常用的魔术方法来讲解一下。

# __init__ && __new__: 构造和初始化
这是一个最基本不过的魔术方法__init__。 通过此方法我们可以定义一个对象的初始化操作。
其实在一个对象初始化的时候第一个调用的并不是__init__()魔术方法，而是调用的__new__()方法。__new__(cls,[….])它的第一个参数是这个类，
其它的参数是用来直接传递给__init__()方法。__new__() 一般元类中比较常用，比如重新构造tuple、list等。
```python
In [1]: class ListMetaclass(type):
   ...:     def __new__(cls, name, bases, attrs):
   ...:         attrs['add'] = lambda self, value: self.append(value)
   ...:         return type.__new__(cls, name, bases, attrs)
   ...:

In [3]: class MyList(list, metaclass=ListMetaclass):
   ...:     pass
   ...:

In [4]: ld = MyList()

In [5]: ld.add('ni')

In [6]: ld
Out[6]: ['ni']
```
# __del__: 析构函数

__del__是__init__相对的一个魔术方法，析构函数。它定义的是当一个对象进行垃圾回收时候的行为。
当一个对象在删除的时候需要更多的清洁工作的时候此方法很有用，比如套接字对象或者文件对象。注意，
如果解释器退出的时候对象还存在，就不能保证__del__能够执行。python 垃圾回收有两种方式：
引用计数和GC。python的垃圾回收过程与常用语言的不一样，python是按照字典顺序进行的垃圾回收，
而不是按照创建顺序进行。所以当系统进行回收资源时，会按照类名A-Za-z顺序，以此进行，
我们无法掌控这里的流程。所以一般在创建类时，不需要__del__。而由系统自动进行回收。


# __slots__

当我们定义一个Class时，创建了一个Class实例后，我们可以给该实例绑定任何属性和方法。如果我们想要限制实例的属性该怎么办？为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加属性。

```python
In [7]: class Student(object):
   ...:     __slots__ = ('name', 'age')
   ...:

In [8]: s = Student()

In [9]: s.name='david'

In [10]: s.age=14

In [11]: s.sex=boy
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-11-bf834fc525cc> in <module>()
----> 1 s.sex=boy

NameError: name 'boy' is not defined
```
注意： 使用__slots__时，定义的属性仅对当前类实例起作用，对继承的子类是不起作用的，除非在子类中也定义了__slots__，
这样子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。

```python
In [12]: class GraduateStudent(Student):
   ....:     pass
   ....:

In [13]: g = GraduateStudent()

In [14]: g.score = 100




In [15]: class GraduateStudent(Student):
   ....:     __slots__ = ('score')
   ....:

In [16]: g = GraduateStudent()

In [17]: g.score=100

In [18]: g.name='david'

In [19]: g.age=13

In [20]: g.sex=boy
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-20-51fab9d614be> in <module>()
----> 1 g.sex=boy

NameError: name 'boy' is not defined
```

# __str__  && __repr__:  自定义标准输出

 一个Class实例之后，print()一个类时，格式为<__main__.Class object at 0x109afb190>，
 这样看起来让人看起来无法理解。python 中__str__ 和 __repr__ 帮我们解决了这个问题，使人更容易理解实例的stdout。
 __str__ 和__repr__ 什么区别那？ __str__(print() 打印)是给人看的，__repr__由程序stdout。

```python
In [21]: class A(object):
   ....:     def __str__(self):
   ....:         return "www.pydevops.com"
   ....:

In [22]: A()
Out[22]: <__main__.A at 0x106525ac8>

In [24]: print(A())
www.pydevops.com


In [25]: class A(object):
   ....:     def __str__(self):
   ....:         return "www.pydevops.com"
   ....:     __repr__ = __str__
   ....:

In [26]: A()
Out[26]: www.pydevops.com

In [27]: print(A())
www.pydevops.com
```

# __iter__:

 如果一个类像for… in循环，类似list或者tuple。python提供了__iter__()方法，
 该对象返回一个迭代对象，然后for循环就会不断调用该迭代对象__next__()方法拿到循环的下一个值，
 知道遇到StopIteration错误时退出循环。
 ```python
 In [29]: class Fib(object):
   ....:     def __init__(self):
   ....:         self.a, self.b = 0, 1
   ....:     def __iter__(self):
   ....:         return self
   ....:     def __next__(self):
   ....:         self.a, self.b = self.b, self.a+self.b
   ....:         if self.a > 10:
   ....:             raise StopIteration()
   ....:         return self.a
   ....:

In [30]: for n in Fib():
   ....:     print(n)
   ....:
1
1
2
3
5
8
 ```
# __getitem__:

  __iter__实例虽然能作用于for循环， 看起来和list有点儿像，但是 把它当成list来使用还是不行，python提供了__getitem__实现了这个功能。

```python
In [31]: class Fib(object):
   ....:     def __getitem__(self, n):
   ....:         a, b = 1, 1
   ....:         for x in range(n):
   ....:             a, b = b, a+b
   ....:         return a
   ....:

In [33]: f = Fib()

In [34]: f[0]
Out[34]: 1

In [35]: f[2]
Out[35]: 2
```
# __getattr__:

正常情况下， 当我们调用类的一个方法或者属性时，如果不存在，就会报错。为了避免这种错误，
python提供了__getattr__()方法，动态返回一个属性。

```python
In [36]: class Student(object):
   ....:     def __init__(self):
   ....:         self.name = "David"
   ....:     def __getattr__(self, attr):
   ....:         if attr == "score":
   ....:             return 59
   ....:         else:
   ....:             return "no value"
   ....:

In [37]: s = Student()

In [38]: s.name
Out[38]: 'David'

In [39]: s.score
Out[39]: 59

In [40]: s.na
Out[40]: 'no value'
```
注意： 只有在没有找到属性的情况下，才会调用__getattr__，如果已有属性，比如name， 就不会__getattr__中查找。此外，__getattr__默认时返回None,在上面的例子我们让其返回”no value”。如果不指定的话，会返回None.

# __call__:

一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用insance.method()来调用。
如果像直接在实例本身调用是否可以那？在python中提供了__call__()方法，可以实现该功能。

```python
In [41]: class Student(object):
   ....:     def __init__(self, name):
   ....:         self.name = name
   ....:     def __call__(self):
   ....:         return  "My name is {0}".format(self.name)
   ....:

In [43]: s = Student('David')
In [46]: s()
Out[46]: 'My name is David'
```
__call__() 还可以定义参数，对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，
把函数看成对象，因为这两者之间根本没有啥区别。



