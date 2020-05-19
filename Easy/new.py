def bonAppetit(bill, k, b):
    b_ac = 0
    for i in range(bill):
        if i != bill[k]:
            b_ac += i
    b_ac = b_ac/2
    if b_ac == b:
        print("Bon Apetit!")
    else:
        print(b-b_ac)

if __name__ == '__main__':
    bill = [3,10,2,9]
    k = 1
    b = 7
    bonAppetit(bill,k,b)
