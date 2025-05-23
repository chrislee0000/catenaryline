#기본 라이브러리 호출
import numpy as np
import cmath
import math

#현수선 테일러 근사식 이용 필요한 줄 길이 계산
H=float(input("높이차(m)를 입력해주세요:"))
L=float(input("두 점 사이의 간격(m)을 입력해주세요:"))

#3차방정식 근의 공식이용 해 도출(이 부분만 chatgpt 참고고)
def solve_cubic(a3, a2, a1, a0):
    if a3 == 0:
        raise ValueError("a3 cannot be zero for a cubic equation.")

    # 정규형: x^3 + px + q = 0 로 바꾸기
    a = a2 / a3
    b = a1 / a3
    c = a0 / a3

    # 변수를 치환하여 depressed cubic 형태로 바꾸기: x = t - a/3
    p = b - a**2 / 3
    q = (2 * a**3) / 27 - (a * b) / 3 + c

    # 판별식
    D = (q / 2)**2 + (p / 3)**3

    if D > 0:
        # 하나의 실근 + 두 개의 켤레 복소근
        u = (-q / 2 + cmath.sqrt(D))**(1/3)
        v = (-q / 2 - cmath.sqrt(D))**(1/3)
        t1 = u + v
        roots = [t1 - a / 3]
    elif D == 0:
        # 중근 포함
        u = (-q / 2)**(1/3)
        t1 = 2 * u
        t2 = -u
        roots = [t1 - a / 3, t2 - a / 3]
    else:
        # 세 실근
        r = np.sqrt(-(p**3) / 27)
        theta = np.arccos(-q / (2 * np.sqrt(-(p**3) / 27)))
        t1 = 2 * np.sqrt(-p / 3) * np.cos(theta / 3)
        t2 = 2 * np.sqrt(-p / 3) * np.cos((theta + 2 * np.pi) / 3)
        t3 = 2 * np.sqrt(-p / 3) * np.cos((theta + 4 * np.pi) / 3)
        roots = [t1 - a / 3, t2 - a / 3, t3 - a / 3]

    # 복소근까지 포함해 3개의 해로 맞추기
    while len(roots) < 3:
        roots.append(roots[-1])

    a_real = [r.real for r in roots if np.isreal(r) and r.real > 0]
    if not a_real:
        raise ValueError("양의 실근이 존재하지 않습니다.")
    return a_real[0]

#현수선 a 값 도출출
a=solve_cubic(L**4/384,0,L**2/8,H*-1)
#현수선 길이 계산산
result = 2*a*np.asinh(L/(2*a))

#출력력
print("줄의 길이: {}".format(result))

#이외 코드는 chatgpt로 오류검수만 진행
