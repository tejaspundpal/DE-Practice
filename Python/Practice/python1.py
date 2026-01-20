def simple_interest(principal, rate, time):
    
    interest = principal * rate * time
    
    return interest

principal = 5000
rate = 0.1 
time = 5

interest = simple_interest(principal, rate, time)
print(interest) 