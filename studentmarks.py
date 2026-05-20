sub1=int(input("enter marks for sub1 :"))
sub2=int(input("enter marks for sub2 :"))
sub3=int(input("enter marks for sub3 :"))
sub4=int(input("enter marks for sub4 :"))
sub5=int(input("enter marks for sub5 :"))
total = sub1+sub2+sub3+sub4+sub5
average=total/5
print(f"Total: {total}")
print(f"Average: {average}")
if average>=90:
    print("A grade")
elif average>=80:
    print("B grade")
elif average>=70:
    print("C grade")
elif average>=60:
    print("D grade")
else:
    print("fail")
