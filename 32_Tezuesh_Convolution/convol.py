import matplotlib.pyplot as plt

def plotLine(a,b):
	x = [b, b]
	y = [0, a]
	plt.plot(x, y, marker = 'o')

def plotGraph(fnx, pos_fnx, xpos, ypos, heading):

	plt.axhline(0, color = 'black')
	plt.axis([pos_fnx[0]-1, pos_fnx[len(pos_fnx)-1]+1, min(fnx)-1, max(fnx)+1])

	plt.title(heading)
	plt.xlabel(xpos)
	plt.ylabel(ypos)


	for i in range(len(fnx)):
		plotLine(fnx[i], pos_fnx[i])
	plt.show()


def indexed(fnx_y, pos_fnx_y):

	final = {x:0 for x in pos_fnx_y}

	for i in range(len(fnx_y)):
		final[pos_fnx_y[i]] += fnx_y[i]

	return final

def convolution(fnx_x, pos_fnx_x, fnx_h, pos_fnx_h):
	fnx_y = []
	pos_fnx_y = []

	for i in range(len(fnx_x)):
		for j in range(len(fnx_h)):
			fnx_y.append(fnx_x[i] * fnx_h[j])
			pos_fnx_y.append(pos_fnx_x[i] + pos_fnx_h[j])

	temp = indexed(fnx_y, pos_fnx_y)

	pos_fnx_y = temp.keys()
	fnx_y = temp.values()
	pos_fnx_y, fnx_y = zip(*sorted(zip(pos_fnx_y, fnx_y)))

	return fnx_y, pos_fnx_y


def main():
	fnx_x = [int(x) for x in input("Enter the value of x[n]: \n").split()]
	pos_fnx_x = [int(x) for x in input("Give position of x[n]: \n").split()]
	fnx_h = [int(x) for x in input("Enter the value of h[n]: \n").split()]
	pos_fnx_h = [int(x) for x in input("Give positions of h[n]: \n").split()]

	fnx_y, pos_fnx_y = convolution(fnx_x, pos_fnx_x, fnx_h, pos_fnx_h)


	print("Convolution of the given signal is y[n] ")
	print(fnx_y)
	print("Position of the y[n] i.e n: ")
	print(pos_fnx_y)

	plotGraph(fnx_x, pos_fnx_x,'n -->','x[n] -->','EL241')
	plotGraph(fnx_h, pos_fnx_h,'n -->','h[n] -->','EL241')
	plotGraph(fnx_y, pos_fnx_y,'n -->','y[n] -->','EL241')


if __name__ == '__main__':
	main()
