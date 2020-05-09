

k = eval(input())

out = ''.join(sorted(k, key=lambda x: int(x) if sympy.isprime(x) else 100))
print(f'"{out}"')