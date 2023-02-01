def main():
    ##################################################
    # Comlete your code here
    ##################################################
    reg_hours = 40
    reg_rate = 18.25
    o_rate = 27.78
    workhours = int(input('Enter your work hours: '))
    normal_amount_earned = reg_hours * reg_rate
    reg_hours: workhours - ot_hours
    ot_hours = workhours - reg_hours
    overtime_earned = ot_hours * o_rate
    total_wage = normal_amount_earned + overtime_earned
    
    print('Regular Hours:',reg_hours)
    print('Regular Charge:',normal_amount_earned)
    print('Overtime Hours:',ot_hours)
    print('Overtime Charge:',overtime_earned)
    print('Total Wage:',total_wage)
    
    
    
    pass


if __name__ == '__main__':
    main()
