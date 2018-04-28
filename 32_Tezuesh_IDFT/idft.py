from math import pi,e
import matplotlib.pyplot as plt

def plotLine(a,b):
	x = [b, b]
	y = [0, a]
	plt.plot(x, y, marker = 'o')

def plotGraph(t_n, xpos, ypos, heading):

	mxv= max([abs(t_n[x]) for x in range(len(t_n))])
	plt.axhline(0, color = 'black')
	plt.axvline(0, color = 'black')
	plt.axis([-1, len(t_n)+1, -5, mxv +2])

	plt.title(heading)
	plt.xlabel(xpos)
	plt.ylabel(ypos)


	for i in range(len(t_n)):
		plotLine(abs(t_n[i]), i)
	plt.show()

def plot_graph(x,ans):
	plotGraph(x,'n--->', 'x[n]---->', 'Input Signal')
	plotGraph(ans,'n--->', 'X[n]---->', 'Inverse Fourier Transform')


print("Enter N")
n = int(input())
print("Enter the input signal:")
x_n = [complex(i) for i in input().split()]
omega = e** complex (0, 2*pi/n)
D = []
for i in range(n):
	temp= [omega** (i*j) for j in range(n)]
	D.append(temp)
output=[]
for i in range(n):
	sum_temp=0j
	for j in range(n):
		sum_temp += D[i][j] * x_n[j]
	output.append(sum_temp)

#print(output)
ans =[]


for i in range(n):
	ans.append(round(output[i].real, 2) + round(output[i].imag, 2)*1j)

plot_graph(x_n, ans)
print("Output:")
print(ans)

	
#print(x)

