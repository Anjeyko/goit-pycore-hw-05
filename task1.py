def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n in cache:
            return cache[n]
        elif n == 1:
            return 1
        elif n <= 0:
            return 0
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        print(cache)
        return cache[n]

    return fibonacci

func = caching_fibonacci()
print(func(12))
