
import sympy
k = eval(input())

out = ''.join(sorted(k, key=lambda x: int(x) if sympy.isprime(int(x)) else 100))
print(f'"{out}"')