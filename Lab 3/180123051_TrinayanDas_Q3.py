# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RRYkgDDoniD_MvImkdVqDxpsz_f5Lbig
"""

#Question Number 3
import numpy as np
S_0 = 100
K = 100
T = 1
M_values = [10, 15, 25, 50, 100]
r = 0.08
sigma = 0.2

def efficient_european(S_0, K, M, r, sigma, u, d, p):
    call_list = [0]*(M+1)
    for a in range(M+1):
        call_list[a] = max(S_0*(u**a)*(d**(M-a)) - K, 0)
    for a in range(M):
        for b in range(M-a):
            call_list[b] = ((1-p)*call_list[b] + p*call_list[b+1])*np.exp(-r*T/M)
    call = call_list[0]
    return call

def normal_european(S_0, K, M, r, sigma, u, d, p):
    P = [[[S_0, K]]]
    for a in range(M):
        Q = []
        for el in P[a]:
            Q.append([el[0]*u*p, el[1]*p])
            Q.append([el[0]*d*(1-p), el[1]*(1-p)])
        P.append(Q)
    solution = 0
    for el in P[len(P)-1]:
        solution = solution + max(el[0]-el[1], 0)
    return solution*np.exp(-r*T/M)

for M in M_values:
    dt = T/M
    u = np.exp(sigma*np.sqrt(dt) + (r-0.5*sigma*sigma)*dt)
    d = np.exp(-sigma*np.sqrt(dt) + (r-0.5*sigma*sigma)*dt)
    p = (np.exp(r*dt)-d)/(u-d)
    if M < 25:
        value = normal_european(S_0, K, M, r, sigma, u, d, p)
        print('European Call for M = ', M, 'is', value)
    else:
        print("Normal method cannot give value of M = ", M)
    value = efficient_european(S_0, K, M, r, sigma, u, d, p)
    print('Value of European Call for M = ', M, 'using efficient method is', value)