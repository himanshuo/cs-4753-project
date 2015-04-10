from django.shortcuts import redirect
"""
def logger(func):
...     def inner(*args, **kwargs): #1
...         print "Arguments were: %s, %s" % (args, kwargs)
...         return func(*args, **kwargs) #2
...     return inner
"""

def user_is_logged_in(func):
    def check_user_is_logged_in(request, *args, **kwargs):
        if 'email' not in request.session:
            return redirect('landing')
        else:
            return func(request, *args, **kwargs)
    return check_user_is_logged_in