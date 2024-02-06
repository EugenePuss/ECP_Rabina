import random
#функция РАЕ
def RAE(a, b):
    if b == 0:
        return 1, 0, a

    x1, y1, gcd = RAE(b, a % b)
    x = y1
    y = x1 - (a // b) * y1

    return x, y, gcd

#фунция для нахождения с и d для которых cp + dq = 1.
def find_c_d(p, q):
    c, d, gcd = RAE(p, q)

    if gcd != 1:
        return "Нет решения, так как НОД(p, q) ≠ 1"
    else:
        return c, d

#вычисление символа лежандра
def legendre_symbol(a, md):
    legendre = pow(a, (md - 1) // 2, md)
    if legendre == md - 1:
        return -1
    else:
        return legendre

#функция нахождения b для которого (b/p)= –1.
def find_b(md):
    while True:
        b = random.randint(2, md - 1)
        if legendre_symbol(b, md) == -1:
            return b

#общая фукция нахожденя корня r
def compute_roots(a, md):
    legendre = legendre_symbol(a, md)

    if legendre != 1:
        return "Корень не существует"

    b = find_b(md)

    # Представляем p - 1 в виде 2^s * t
    w, t = 0, md - 1
    while t % 2 == 0:
        w += 1
        t //= 2

    # Вычисляем a^(-1) mod p
    a_inv = pow(a, -1, md)

    # Вычисляем c и r
    c = pow(b, t, md)
    r = pow(a, (t + 1) // 2, md)

    for i in range(1, w):
        d = ((r ** 2 * a_inv) ** 2 ** (w - i - 1)) % md
        if d == md - 1:
            r = (r * c) % md
        c = (c * c) % md


    root1 = r
    return root1
#Публикуемая функция R
def r_funct(p,q,m):
    w=m
    while True:
        w = w+1
        if legendre_symbol(w, p) == 1 and legendre_symbol(w, q) == 1:
            return w

print("КЛЮЧИ :")
p = 5443
q = 5953
m = 1472727
n = p * q
print("Открытый ключ n=p*q:", n)
print("Секретный ключ (p,q):","(", p,",",q,")")
print("Вычисление подписи:")
w=r_funct(p,q,m)
print("w=",m)
i=w-m
print("i=",i)
r = compute_roots(w, p)
s = compute_roots(w, q)
c, d = find_c_d(p, q)
x = (r * d * q + s * c * p) % n
y = (r * d * q - s * c * p) % n
print("s1:")
print("Корень 1:", x)
print("Корень 2:", n - x)
print("Корень 3:", y)
print("Корень 4:", n - y)
e = random.randint(1, 4)
if e == 1:
    s1 = x

if e == 2:
    s1 = n - x

if e == 3:
    s1 = y

if e == 4:
    s1 = n - y
print("Подпись :","(",s1,",",i,")")
print("Проверка подписи:")
podp = pow(s1, 2, n)
print(podp)
print("m=",podp-i)
