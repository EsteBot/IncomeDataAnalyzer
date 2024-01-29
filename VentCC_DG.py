import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Function for checking account analysis and graph
def venture_distro():
    df = pd.read_csv(r"D:\income_data_analysis\pyfi_venv\23_VentCard.csv")
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

    # Create a pie chart
    plt.pie(cat_list, labels=labels, autopct = '%1.1f%%')

    # Add a white circle at the center to create the doughnut shape
    circle = plt.Circle((0, 0), 0.35, color='white')
    plt.gca().add_artist(circle)

    # Add a label at the center of the doughnut
    center_label = 'Total Credit: {}\nTotal Debit: {}'.format(sum_values, rnd_sum_ccpy)

    plt.text(0, 0, center_label, ha='center', va='center', fontsize=10)

    # Add a title
    plt.title('Venture CC Distribution', pad=20)

    # Equal aspect ratio ensures the doughnut shape
    plt.axis('equal')

    # Display the chart
    plt.show()

def barplot_ventr_func():
    df = pd.read_csv(r"D:\income_data_analysis\pyfi_venv\23_VentCard.csv")

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


    # Convert 'Date' column to datetime if it's not already
    df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])
    GOLF = []
    GROC = []
    PYMT = []
    LOWS = [] 
    BOWL = [] 
    JEEP = []
    CLMB = []
    REIS = []
    DENT = []
    DINE = []
    MISC = []
    months_list = []
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
        by_date_sum_golf = by_date_df.loc[df[td] == 'Golf', ta].sum()
        GOLF.append(by_date_sum_golf)
        print(f'total Golf: {by_date_sum_golf:.2f}')

        by_date_sum_groceries = by_date_df.loc[df[td] == 'Groceries', ta].sum()
        GROC.append(by_date_sum_groceries)
        print(f'total Grocieries: {by_date_sum_groceries:.2f}')

        by_date_sum_cc_payments = by_date_df.loc[df[td] == 'CC Payment', tp].sum()
        PYMT.append(by_date_sum_cc_payments)
        print(f'total CC Payments: {by_date_sum_cc_payments:.2f}')

        by_date_sum_jeep_parts = by_date_df.loc[df[td] == 'Jp Parts', ta].sum()
        JEEP.append(by_date_sum_jeep_parts)
        print(f'total Jp Parts: {by_date_sum_jeep_parts:.2f}')

        by_date_sum_lowes = by_date_df.loc[df[td] == 'Lowes', ta].sum()
        LOWS.append(by_date_sum_lowes)
        print(f'total Lowes: {by_date_sum_lowes:.2f}')

        by_date_sum_bowling = by_date_df.loc[df[td] == 'Bowling', ta].sum()
        BOWL.append(by_date_sum_bowling)
        print(f'total Bowling: {by_date_sum_bowling:.2f}')

        by_date_sum_climbing = by_date_df.loc[df[td] == 'Climbing', ta].sum()
        CLMB.append(by_date_sum_climbing)
        print(f'total Climbing: {by_date_sum_climbing:.2f}')

        by_date_sum_REI = by_date_df.loc[df[td] == 'REI', ta].sum()
        REIS.append(by_date_sum_REI)
        print(f'total REI: {by_date_sum_REI:.2f}')

        by_date_sum_dental = by_date_df.loc[df[td] == 'Dentist', ta].sum()
        DENT.append(by_date_sum_dental)
        print(f'total Dentist: {by_date_sum_dental:.2f}')

        by_date_sum_dining = by_date_df.loc[df[td] == 'Dining', ta].sum()
        DINE.append(by_date_sum_dining)
        print(f'total Dining: {by_date_sum_dining:.2f}')

        by_date_sum_miscellaneous = by_date_df.loc[df[td] == 'Misc', ta].sum()
        MISC.append(by_date_sum_miscellaneous)
        print(f'total Misc: {by_date_sum_miscellaneous:.2f}')

    # Sample data for each month and group
    list_o_data_lists = [GOLF, GROC, PYMT, JEEP, LOWS, BOWL, CLMB, REIS, DENT, DINE, MISC]
    absolute_val_o_lists = [[abs(x) for x in lst] for lst in list_o_data_lists]

    GOLF_data = absolute_val_o_lists[0]
    GROC_data = absolute_val_o_lists[1]
    PYMT_data = absolute_val_o_lists[2]
    JEEP_data = absolute_val_o_lists[3]
    LOWS_data = absolute_val_o_lists[4]
    BOWL_data = absolute_val_o_lists[5]
    CLMB_data = absolute_val_o_lists[6]
    REIS_data = absolute_val_o_lists[7]
    DENT_data = absolute_val_o_lists[8]
    DINE_data = absolute_val_o_lists[9]
    MISC_data = absolute_val_o_lists[10]

    print(GOLF_data)
    print(GROC_data)
    print(PYMT_data)
    print(JEEP_data)
    print(LOWS_data)
    print(BOWL_data)
    print(CLMB_data)
    print(REIS_data)
    print(DENT_data)
    print(DINE_data)
    print(MISC_data)
    
    # Set the width of each bar
    bar_width = 0.35

    # Set the positions of the bars on the x-axis
    r = np.arange(len(months))

    # Create the stacked bar plot
    plt.bar(r, GROC_data, color='orange', width=bar_width, edgecolor='white', label='Groceries')
    plt.bar(r, DINE_data, color='green', width=bar_width, edgecolor='white', bottom=GROC_data, label='Dining')
    plt.bar(r, MISC_data, color='red', width=bar_width, edgecolor='white', bottom=[i + j for i, j in zip(GROC_data, DINE_data)], label='Misc.')
    plt.bar(r, JEEP_data, color='purple', width=bar_width, edgecolor='white', bottom=[i + j + k for i, j, k in zip(GROC_data, DINE_data, MISC_data)], label='Jp Parts')
    plt.bar(r, LOWS_data, color='gray', width=bar_width, edgecolor='white', bottom=[i + j + k + l for i, j, k, l in zip(GROC_data, DINE_data, MISC_data, JEEP_data)], label='Lowes')
    plt.bar(r, CLMB_data, color='blue', width=bar_width, edgecolor='white', bottom=[i + j + k + l + m for i, j, k, l, m in zip(GROC_data, DINE_data, MISC_data, JEEP_data, LOWS_data)], label='Climb')
    plt.bar(r, BOWL_data, color='pink', width=bar_width, edgecolor='white', bottom=[i + j + k + l + m + n for i, j, k, l, m, n in zip(GROC_data, DINE_data, MISC_data, JEEP_data, LOWS_data, CLMB_data)], label='Bowl')
    plt.bar(r, REIS_data, color='cyan', width=bar_width, edgecolor='white', bottom=[i + j + k + l + m + n + o for i, j, k, l, m, n , o in zip(GROC_data, DINE_data, MISC_data, JEEP_data, LOWS_data, CLMB_data, BOWL_data)], label='REI')
    plt.bar(r, DENT_data, color='brown', width=bar_width, edgecolor='white', bottom=[i + j + k + l + m + n + o + p for i, j, k, l, m, n, o, p in zip(GROC_data, DINE_data, MISC_data, JEEP_data, LOWS_data, CLMB_data, BOWL_data, REIS_data)], label='Dentist')
    plt.bar(r, GOLF_data, color='yellow', width=bar_width, edgecolor='white', bottom=[i + j + k + l + m + n + o + p + q for i, j, k, l, m, n, o, p, q in zip(GROC_data, DINE_data, MISC_data, JEEP_data, LOWS_data, CLMB_data, BOWL_data, REIS_data, DENT_data)], label='Golf')

    # Update the x-coordinates for the "PYMT_data" bar
    plt.bar(r + bar_width, PYMT_data, color='slateblue', width=bar_width, edgecolor='white', label='CC PYMT')

    # Add x-axis labels and title
    #plt.xlabel('Months')
    plt.ylabel('Dollars')
    # Add a title
    plt.title('Venture CC Data By Month')
    # Add legend
    plt.legend()
    # Adjust the x-axis tick labels
    plt.xticks(r + bar_width/2, months)  # Shifting the tick labels as well
    # Display the chart
    plt.show()

#venture_distro()
barplot_ventr_func()
