from turtle import color
import matplotlib.pyplot as plt

Tom_score = [62, 67, 65, 78, 80, 74, 76, 83, 85, 78, 88, 89]
Peter_score = [87, 63, 67, 78, 71, 62, 88, 72, 73, 84, 88, 65]

x_coord = range(len(Tom_score))
plt.plot(x_coord, Tom_score, label='Tom score',color="b")
plt.plot(x_coord, Peter_score,label='Peter score',color="r")

plt.ylim(50, 100)
plt.xlabel('Months')
plt.ylabel('Score')

plt.legend()
plt.show()