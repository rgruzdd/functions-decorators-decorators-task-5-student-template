
def decorator_apply(lambda_func):
    def wrapper(func):
        def wrapper(x):
            return func(lambda_func(x))
        return wrapper
    return wrapper





@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int) ->int:
    return num

