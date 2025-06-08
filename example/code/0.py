def empty_function(*args, **kwargs):
    pass  # 定义一个空函数用于替换

class SuppressAfterMeta(type):
    def __new__(cls, name, bases, attrs):
        # 遍历所有父类，查找以'after_'开头的方法
        for base in bases:
            for method_name in dir(base):
                if method_name.startswith('after_'):
                    # 如果子类未显式定义该方法，则动态添加空实现
                    if method_name not in attrs:
                        pass
                        # attrs[method_name] = empty_function
                
        # 创建新类
        return super().__new__(cls, name, bases, attrs)

class SuppressPrivateAfterMeta(type):
    def __new__(cls, name, bases, attrs):
        for base in bases:
            # 获取父类中所有以 '__after_' 开头的方法（修饰后的名称）
            private_methods = {
                method_name: getattr(base, method_name)
                for method_name in dir(base)
                if method_name.startswith(f'_{base.__name__}__after_')
            }
            # 在子类中动态置空这些方法
            for method_name, method in private_methods.items():
                if method_name not in attrs:
                    attrs[method_name] = lambda self, *args, **kw: None
        return super().__new__(cls, name, bases, attrs)

class B:
    def __after_save(self):
        print("B的私有after方法")

class A(B, metaclass=SuppressPrivateAfterMeta):
    pass

a = A()
a._B__after_save()  # 无输出

class B:
    def __after_save(self):
        print("B的after_save方法")

    def after_delete(self):
        print("B的after_delete方法")

class A(B, metaclass=SuppressAfterMeta):
    pass  # 无需显式重写，元类自动处理

a = A()
print(a.__after_save())