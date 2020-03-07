def currency_converter(rate, dollar):
    Naria = dollar // rate
    return Naria

r=input("Enter rate: ")
d=input("Enter dollar: ")
print(currency_converter(float(r),float(d)))
