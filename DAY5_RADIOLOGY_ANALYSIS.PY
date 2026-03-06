patients = ["Ramesh","sita","aman","neha","rahul","priya"]
scan_type = ["MRI","CT","X-RAY","MRI","CT","ultrasound"]
print("Total patient:",len(patients))
Bill = [5000,3000,800,5200,3100,1500]

total_revenue = sum (Bill)
print("total revenue:",total_revenue)
print("highest bill:",max(Bill))
print("lowest bill:",min(Bill))
for i in range(len(patients)):
    print(patients[i],"-",
          scan_type[i],"-bill:", Bill[i])
    count = 0
for scan in scan_type:
    if scan =="MRI":
        count = count + 1
print("total MRI scans:",count)