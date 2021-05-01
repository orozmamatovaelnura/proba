spendings = [140, 30, 999, 145, 538, 878, 901, 613, 471, 286, 147, 90]
income = [300, 40, 0, 4000, 8911, 73, 85, 0, 9000, 941, 658, 190]

def average(spend,profit):
  all_coeffs=[]
  for i in range(12):
    try:
      coeff=spend[i]/profit[i]
    except ZeroDivisionError:
      coeff=0
    finally:
      all_coeffs.append(coeff)
  sum_up_average=sum(all_coeffs)/12
  print('The average of coefficients of company\'s spendings : ',end='')
  print ("{0:.6f}".format(sum_up_average))

average(spendings,income)
