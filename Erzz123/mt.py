import matplotlib.pyplot as plt
x = ["jan","feb","march",]
y = ["1000","2000","3000"]

plt.plot(x,y)

#label
plt.xlabel("month")
plt.ylabel("income")
plt.title("income startup")

#menampilkan
plt.show()
