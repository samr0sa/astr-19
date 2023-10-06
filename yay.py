def f(x):
    return x**3 + 8

def main():
    x = 9 
    result = f(x)
    print()
    print("f(x)=x**3 + 8")
    print()
    print("The result of f(x) with x =", x, "is", result)
    
    if result > 27:
        print()
        print("YAY!")
        print()

if __name__ == "__main__":
    main()    

