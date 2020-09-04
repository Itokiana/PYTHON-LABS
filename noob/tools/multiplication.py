def table(n, max=10):
    i = 0
    while i <= max:
        print(n, ' x ', i, ' = ', (n*i) )
        i+=1

if __name__ == "__main__":
    table(2)