import hrcalc

#m = max30102.MAX30102()
ir=[]
with open("ir.log","r") as f:
	for line in f:
		ir.append(int(line))
red=[]
with open("red.log","r") as f:
	for line in f:
		red.append(int(line))
for i in range(5):
	print(hrcalc.calc_hr_and_spo2(ir[2*i:2*i+100], red[2*i:2*i+100]))
#red, ir = m.read_sequential(1000)
print(ir)
print(red)
