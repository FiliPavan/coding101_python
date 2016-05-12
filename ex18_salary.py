def calculate_salary(yearly_salary):
	print "monthly_salary: %r" % (float(yearly_salary) / 12)

def lifetime_salary(yearly_salary):
	print "lifetime value of fili: %r" % (float(yearly_salary) *40)

print "type yearly salary"
yearly_salary = raw_input()

calculate_salary(yearly_salary)
lifetime_salary(yearly_salary)

#print "How much do you earn in a year",
#yearly_salary = raw_input()
#monthly_salary = float(yearly_salary) / 12
#print monthly_salary