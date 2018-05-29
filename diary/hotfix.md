  
# 热更新（hotfix）
 这种技术主要是针对情况比较紧急，并且bug是脚本逻辑错误导致的。
 如客户端逻辑写的有问题导致出现exception，使得玩家某个玩法不能玩，
 或者是服务端某个代码逻辑写的有问题。这种技术实现的主要思路是（以热更新客户端为例）
 ：服务器将修正的代码发送到客户端，客户端动态执行这段代码来修复bug
 。用python来实现这个其实非常简单，
 只需要在客户端内嵌的python虚拟机中动态编译服务端发过来的代码，
 并执行这段代码就行了。例如：现在客户端有下面一段的代码，这段代码是有错误的。

1 #模块test 
```python
def not_has_a(x):
    return hasattr(x, 'a')
```
本来上面代码是希望x对象没有a属性后返回True，但现在情况正好反过来了。
现在我们需要写一段代码来修正这个问题，也就是写一段代码给python虚拟机执行，
动态修改test模块中not_has_a函数的定义。这个在python中很好实现的，
因为python中函数也是一个对象，模块中只是根据函数名来索引对应的函数对象的，
所以我们只需要重新定义一个新的not_has_a函数对象，
将模块中根据not_has_a函数名索引的对象指向新定义的函数对象就行。具体代码如下：

```python
import test

def not_has_a(x):
    return not hasattr(x, 'a')

setattr(test, 'not_has_a', not_has_a)
```
最后就是让python虚拟机执行上面的代码。
首先服务端会把上面代码的字符串发送给客户端，
客户端接收到代码后编译这段字符串，然后执行就可以了，具体代码如下：
```python
def hotfix(self, hotfix_content):
     compiled_code = compile(hotfix_content, 'hotfix', 'exec')
     import __main__
     exec compiled_code in __main__.__dict__

```


