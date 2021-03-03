b = [1-.001,.001]
e = [1-.002,.002]
# a conditioned on b and e, a[b_val][e_val]
a_be = [[[1-.001,.001],[1-.29,.29]],[[1-.94,.94],[1-.95,.95]]]
j_a = [.05,.9]
m_a = [.01,.7]
p_m = 0
#This is the example from the HW to calculate P(m)
for a_val in range(2):
    for b_val in range(2):
        for e_val in range(2):
            p_m += b[b_val]*e[a_val]*a_be[b_val][e_val][a_val]*m_a[a_val]
print("P(m) = %f" % p_m)
# This is the marginilzation of (m,j) so it sums across A,B and E 
p_j_m = 0
for a_val in range(2):
    for b_val in range(2):
        for e_val in range(2):
            p_j_m += b[b_val]*e[a_val]*a_be[b_val][e_val][a_val]*m_a[a_val]*j_a[a_val]

p_j_not_m = 0
for a_val in range(2):
    for b_val in range(2):
        for e_val in range(2):
            p_j_not_m += b[b_val]*e[a_val]*a_be[b_val][e_val][a_val]*(1-m_a[a_val])*j_a[a_val]
print("P(m,j) = %f" % p_j_m)
print("P(j | m) = %f" % (p_j_m / p_m))
print("P(j | ~m) = %f" % (p_j_not_m / (1-p_m)))

