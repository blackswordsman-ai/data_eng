# def add_three(input_var):
#     output_var = input_var + 3
#     return output_var

# result = add_three(10)
# print(result)

def get_pay(num_hours):
    pay_pertax =num_hours * 15

    pay_aftertax =pay_pertax * (1 - 0.2) # 20% tax

    return pay_aftertax

# Calculate pay based on working 40 hours
pay_fulltime = get_pay(40)
print(pay_fulltime)