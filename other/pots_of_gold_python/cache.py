import sys
import functools

not_cached = {}
cached = {}

def cache(func):
    'Optimize a pure function by caching prior results'
    prior_results = {}
    @functools.wraps(func)
    def newfunc(*args):
        key = str(*args)
        if key in prior_results:
            cached.setdefault(func.__name__, 0)
            cached[func.__name__] += 1
            return prior_results[key]
        not_cached.setdefault(func.__name__, 0)
        not_cached[func.__name__] += 1
        result = func(*args)
        prior_results[key] = result
        return result
    return newfunc

def report(func):
    func_name = func.__name__
    if func_name in cached:
        print '\nCache report for function {}()'.format(func_name)
        print '- Non-cached calls: {:2}'.format(not_cached[func_name])
        print '- Cached calls:     {:2}'.format(cached[func_name])
