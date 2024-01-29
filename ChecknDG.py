import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Function for checking account analysis and graph
def venture_distro():
    df = pd.read_csv(r"D:\income_data_analysis\pyfi_venv\23_VentCard.csv")
    #df[3:5]
    #print(df)

    td = 'Description'
    tp = 'Credit'
    ta = 'Debit'
    tc = 'Category'

    # Create new dataframe to recategorize transaction types
    df[td] = np.where(df[td].str.contains('GLF'), 'Golf', df[td])
    df[td] = np.where(df[td].str.contains('SAMS|SOOPERS'), 'Groceries', df[td])
    df[td] = np.where(df[td].str.contains('PYMT'), 'CC Payment', df[td])
    df[td] = np.where(df[td].str.contains('LOWES'), 'Lowes', df[td])
    df[td] = np.where(df[td].str.contains('LANES'), 'Bowling', df[td])
    df[td] = np.where(df[td].str.contains('QUADRATEC|ADVANCE'), 'Jp Parts', df[td])
    df[td] = np.where(df[td].str.contains('CLIMBING'), 'Climbing', df[td])
    df[td] = np.where(df[td].str.contains('REI'), 'REI', df[td])
    df[td] = np.where(df[td].str.contains('DENTAL'), 'Dentist', df[td])
    df[td] = np.where(df[tc].str.contains('Dining'), 'Dining', df[td])
    defined_label_list = ['Golf', 'Dining', 'Groceries', 'CC Payment', 
                        'Lowes', 'Bowling', 'Jp Parts', 'Climbing', 'REI', 'Dentist']
    df[td] = np.where(~df[td].str.contains('|'.join(defined_label_list)), 'Misc', df[td])

    print(df[td])
    #selected_columns = [ta, td, 'Balance']
    #selected_df = df[selected_columns]
    #print(selected_df)
    
    # Sum the values in the ta column corresponding to rows that have been re-labeled
    sum_golf = df.loc[df[td] == 'Golf', ta].sum()
    print(f'total Golf: {sum_golf:.2f}')
    sum_groc = df.loc[df[td] == 'Groceries', ta].sum()
    print(f'total Groceries: {sum_groc:.2f}')
    sum_ccpy = df.loc[df[td] == 'CC Payment', tp].sum()
    print(f'total CC Payment: {sum_ccpy:.2f}')
    sum_lows = df.loc[df[td] == 'Lowes', ta].sum()
    print(f'total Lowes: {sum_lows:.2f}')
    sum_bowl = df.loc[df[td] == 'Bowling', ta].sum()
    print(f'total Bowling: {sum_bowl:.2f}')
    sum_jppt = df.loc[df[td] == 'Jp Parts', ta].sum()
    print(f'total Jp Parts: {sum_jppt:.2f}')
    sum_clmb = df.loc[df[td] == 'Climbing', ta].sum()
    print(f'total Climbing: {sum_clmb:.2f}')
    sum_reis = df.loc[df[td] == 'REI', ta].sum()
    print(f'total REI: {sum_reis:.2f}')
    sum_dnts = df.loc[df[td] == 'Dentist', ta].sum()
    print(f'total Dentist: {sum_dnts:.2f}')
    sum_dine = df.loc[df[td] == 'Dining', ta].sum()
    print(f'total Dining: {sum_dine:.2f}')
    sum_misc = df.loc[df[td] == 'Misc', ta].sum()
    print(f'total Misc: {sum_misc:.2f}')

    # Logic code block for doughnut graph creation
    labels = ['Golf', 'Groceries', 'REI', 'Lowes', 'Bowling', 'Jp Parts', 'Climbing',
              'Dentist', 'Dining',  'Misc']
    cat_list = [sum_golf, sum_groc, sum_reis, sum_lows, sum_bowl,
                  sum_jppt, sum_clmb, sum_dnts, sum_dine, sum_misc]
    sum_values = round(sum(cat_list),2)
    rnd_sum_ccpy = round(sum_ccpy,2)
    #outcome_values = [sum_golf, sum_groc, sum_ccpy, sum_lows, sum_lows, 
    #              sum_bowl, sum_jppt, sum_clmb, sum_reis, sum_dnts, sum_dine, sum_misc]
    #absolute_values = [abs(x) for x in outcome_values]
    #abs_value_sum = sum(absolute_values)

    #print(income_values_sum)
    #print(abs_value_sum)
    #print(absolute_values)

    # Create a pie chart
    plt.pie(cat_list, labels=labels, autopct = '%1.1f%%')

    # Add a white circle at the center to create the doughnut shape
    circle = plt.Circle((0, 0), 0.35, color='white')
    plt.gca().add_artist(circle)

    # Add a label at the center of the doughnut
    center_label = 'Total Credit: {}\nTotal Debit: {}'.format(sum_values, rnd_sum_ccpy)

    plt.text(0, 0, center_label, ha='center', va='center', fontsize=10)

    # Add a title
    plt.title('Venture CC Distribution')

    # Equal aspect ratio ensures the doughnut shape
    plt.axis('equal')

    # Display the chart
    plt.show()

'''

def barplot_checking_func():

    df = pd.read_csv(r"D:\income_data_analysis\pyfi_venv\23_Checking.csv")

    td = 'Transaction Description'
    ta = 'Transaction Amount'

    months_list = []

    #df =  df[df[td] != "Deposit from UNIVERSITY OF CO DIR DEP"]
    df[td] = np.where(df[td].str.contains('UNIVERSITY OF CO DIR DEP'), 'CU Income', df[td])
    df[td] = np.where(df[td].str.contains('ROBINHOOD'), 'RBHD Investing', df[td])
    df[td] = np.where(df[td].str.contains('BANKCARD'), 'JEEP CC PMT', df[td])
    df[td] = np.where(df[td].str.contains('CANVAS'), 'TRSFR to Audrey', df[td])
    df[td] = np.where(df[td].str.contains('Savings'), 'SAVE', df[td])
    df[td] = np.where(df[td].str.contains('Interest'), 'Interest', df[td])
    df[td] = np.where(df[td].str.contains('CRCARDPMT'), 'Timed CC PMT', df[td])
    df[td] = np.where(df[td].str.contains('MOBILE PMT'), 'Ventr CC PMT', df[td])
    defined_label_list = ['CU Income', 'RBHD Investing', 'JEEP CC PMT', 'TRSFR to Audrey', 
                        'SAVE', 'Interest', 'Timed CC PMT', 'Ventr CC PMT']
    df[td] = np.where(~df[td].str.contains('|'.join(defined_label_list)), 'Misc', df[td])


    # Convert 'Date' column to datetime if it's not already
    df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])
    INCM = []
    RBHD = []
    JEEP = []
    TRFR = [] 
    SAVR = [] 
    INTR = []
    T_CC = []
    V_CC = []
    MISC = []
    m = 1
    months = ['January', 'February', 'March', 'April']

    for i in range (len(months)):
        # Define a specific month
        specific_month = datetime(year=2023, month=m, day=1)
        # Retrieve the month value
        month = specific_month.strftime('%B')
        months_list.append(month)
        # Calculate the start date of the month
        start_date = specific_month.replace(day=1)
        # Calculate the end date of the month
        next_month = specific_month.replace(day=28) + timedelta(days=4)  # Add 4 days to ensure we are in the next month
        end_date = next_month - timedelta(days=next_month.day)
        # Print the month, start date, and end date
        print(f"Month: {month}")
        print(f"Start Date: {start_date}")
        print(f"End Date: {end_date}")
        m += 1

        by_date_df = df[(df['Transaction Date'] >= start_date) & (df['Transaction Date'] <= end_date)]

        # Print the filtered DataFrame
        print(by_date_df)

        # Ex. sum the values in the ta column corresponding to rows labeled as 'CU Income'
        by_date_sum_income = by_date_df.loc[df[td] == 'CU Income', ta].sum()
        INCM.append(by_date_sum_income)
        print(f'total CU Income: {by_date_sum_income:.2f}')

        by_date_sum_interest = by_date_df.loc[df[td] == 'Interest', ta].sum()
        INTR.append(by_date_sum_interest)
        print(f'total Interest: {by_date_sum_interest:.2f}')

        by_date_sum_invest = by_date_df.loc[df[td] == 'RBHD Investing', ta].sum()
        RBHD.append(by_date_sum_invest)
        print(f'total RBHD Investing: {by_date_sum_invest:.2f}')

        by_date_sum_jeep_cc = by_date_df.loc[df[td] == 'JEEP CC PMT', ta].sum()
        JEEP.append(by_date_sum_jeep_cc)
        print(f'total JEEP CC PMT: {by_date_sum_jeep_cc:.2f}')

        by_date_sum_trsfr_to_audrey = by_date_df.loc[df[td] == 'TRSFR to Audrey', ta].sum()
        TRFR.append(by_date_sum_trsfr_to_audrey)
        print(f'total TRSFR to Audrey: {by_date_sum_trsfr_to_audrey:.2f}')

        by_date_sum_save = by_date_df.loc[df[td] == 'SAVE', ta].sum()
        SAVR.append(by_date_sum_save)
        print(f'total SAVE: {by_date_sum_save:.2f}')

        by_date_sum_timed_cc = by_date_df.loc[df[td] == 'Timed CC PMT', ta].sum()
        T_CC.append(by_date_sum_timed_cc)
        print(f'total Timed CC PMT: {by_date_sum_timed_cc:.2f}')

        by_date_sum_ventr_cc = by_date_df.loc[df[td] == 'Ventr CC PMT', ta].sum()
        V_CC.append(by_date_sum_ventr_cc)
        print(f'total Ventr CC PMT: {by_date_sum_ventr_cc:.2f}')

        by_date_sum_miscellaneous = by_date_df.loc[df[td] == 'Misc', ta].sum()
        MISC.append(by_date_sum_miscellaneous)
        print(f'total Misc: {by_date_sum_miscellaneous:.2f}')

    # Sample data for each month and group
    list_o_data_lists = [INCM, RBHD, JEEP, TRFR, SAVR, INTR, T_CC, V_CC, MISC]
    absolute_val_o_lists = [[abs(x) for x in lst] for lst in list_o_data_lists]

    Income_data = absolute_val_o_lists[0]
    RBHD_data = absolute_val_o_lists[1]
    JEEP_data = absolute_val_o_lists[2]
    TRSFR_data = absolute_val_o_lists[3]
    SAVE_data = absolute_val_o_lists[4]
    Interest_data = absolute_val_o_lists[5]
    Timed_CC_data = absolute_val_o_lists[6]
    Ventr_CC_data = absolute_val_o_lists[7]
    Misc_data = absolute_val_o_lists[8]

    print(Income_data)
    print(RBHD_data)
    print(JEEP_data)
    print(TRSFR_data)
    print(SAVE_data)
    print(Interest_data)
    print(Timed_CC_data)
    print(Ventr_CC_data)
    print(Misc_data)
    
    # Set the width of each bar
    bar_width = 0.5

    # Set the positions of the bars on the x-axis
    r = np.arange(len(months))

    # Create the stacked bar plot
    plt.bar(r, RBHD_data, color='orange', width=bar_width, edgecolor='white', label='Invest')
    plt.bar(r, JEEP_data, color='green', width=bar_width, edgecolor='white', bottom=RBHD_data, label='JeepCC')
    plt.bar(r, Ventr_CC_data, color='red', width=bar_width, edgecolor='white', bottom=[i + j for i, j in zip(RBHD_data, JEEP_data)], label='VntrCC')
    plt.bar(r, TRSFR_data, color='purple', width=bar_width, edgecolor='white', bottom=[i + j + k for i, j, k in zip(RBHD_data, JEEP_data, Ventr_CC_data)], label='Transf')
    plt.bar(r, SAVE_data, color='gray', width=bar_width, edgecolor='white', bottom=[i + j + k + l for i, j, k, l in zip(RBHD_data, JEEP_data, Ventr_CC_data, TRSFR_data)], label='Saving')
    plt.bar(r, Misc_data, color='yellow', width=bar_width, edgecolor='white', bottom=[i + j + k + l + m for i, j, k, l, m in zip(RBHD_data, JEEP_data, Ventr_CC_data, TRSFR_data, SAVE_data)], label='Miscle')

    # Add x-axis labels and title
    plt.xlabel('Months')
    plt.ylabel('Dollars')
    # Add a title
    plt.title('Checking Account Data By Month')
    # Add legend
    plt.legend()
    # Adjust the x-axis tick labels
    plt.xticks(r, months)
    # Display the chart
    plt.show()
'''
venture_distro()
