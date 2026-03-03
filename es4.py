def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

def binomial(f1,f2,nk):
    return f1/(f2*nk)

def main():
    n1=int(input("Primo numero: "))
    n2=int(input("Secondo numero: "))
    if n1==-1 and n2==-1:
        print("Exit.")
    else:
        f1=factorial(n1)
        f2=factorial(n2)
        if n1>n2:
            nk=factorial(n1-n2)
        else:
            nk=factorial(n2-n1)
        print("Il coefficiente binomiale è: ",binomial(f1,f2,nk))

main()

