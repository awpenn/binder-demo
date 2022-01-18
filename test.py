import matplotlib.pyplot as plt

def main():
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    xax = ['1', '2', '3', '4', '5']
    students = [23,17,35,29,12]
    ax.bar(xax,students)
    plt.show()

if __name__ == '__main__':
    main( )