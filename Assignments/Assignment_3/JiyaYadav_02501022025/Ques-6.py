# create a function to generate Fibonacci series up to n terms
def fibonacci_series(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

n = int(input("Enter the number of terms for Fibonacci series: "))
print("Fibonacci series up to", n, "terms:")
print(fibonacci_series(n))

