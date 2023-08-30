import matplotlib.pyplot as plt
import time

x = []
y = [] 

a, b = 0, 1
for i in range(20):
    x.append(i)
    y.append(a)
    
    plt.plot(x, y)
    plt.pause(0.5)

    a, b = b, a+b

plt.xlabel('Iteration')  
plt.ylabel('Fibonacci Sequence')
plt.title('Real-time Fibonacci Sequence')