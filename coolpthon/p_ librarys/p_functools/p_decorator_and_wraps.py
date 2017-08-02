from functools import wraps


# use warps() keep function  __name__ and __doc__ and so on...

def my_decorator(f):
    @wraps(f)
    def wrapper():
        """wrapper_doc"""
        print('Calling decorated function')
        return f()
    return wrapper


@my_decorator
def example():
    """example_doc"""
    print('Called example function')


print(example.__name__)
print(example.__doc__)
