import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Function for checking account analysis and graph
def saving_breakdown():
    df = pd.read_csv(r"D:\income_data_analysis\pyfi_venv\23_ReguSave.csv")
    #print(df)

    td = 'Transaction Description'
    ta = 'Transaction Amount'

    df[td] = np.where(df[td].str.contains('Interest'), 'Interest', df[td])
    df[td] = np.where(df[td].str.contains('Deposit'), 'Deposits', df[td])
    df[td] = np.where(df[td].str.contains('Withdrawal'), 'Withdrawals', df[td])
   #print(df[td])

    selected_columns = [ta, td, 'Balance']
    selected_df = df[selected_columns]
    print(selected_df)

    '''
    # Ex. sum the values in the ta column corresponding to rows selected
    sum_interest = df.loc[df[td] == 'Interest', ta].sum()
    print(f'total Deposits: {sum_interest:.2f}')
    sum_deposits = df.loc[df[td] == 'Deposits', ta].sum()
    print(f'total Interest: {sum_deposits:.2f}')
    '''
    # Convert 'Date' column to datetime if it's not already
    df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])
    
    BALN = []
    INTR = []
    WTDL = []
    DEPT = []

    column_name = 'Balance'
    row_index = 0
    
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

        # Get last month balance and sum the values in the ta column corresponding to rows
        by_date_last_balance = by_date_df['Balance'].iloc[0]
        BALN.append(by_date_last_balance)
        print(f'total balance: {by_date_last_balance:.2f}')

        by_date_sum_interest = by_date_df.loc[df[td] == 'Interest', ta].sum()
        INTR.append(by_date_sum_interest)
        print(f'total interest: {by_date_sum_interest:.2f}')

        by_date_sum_withdrawal = by_date_df.loc[df[td] == 'Withdrawals', ta].sum()
        WTDL.append(by_date_sum_withdrawal)
        print(f'total interest: {by_date_sum_withdrawal:.2f}')

        by_date_sum_interest = by_date_df.loc[df[td] == 'Deposits', ta].sum()
        DEPT.append(by_date_sum_interest)
        print(f'total deposits: {by_date_sum_interest:.2f}')

    list_o_data_lists = [INTR, DEPT, BALN, WTDL]
    absolute_val_o_lists = [[abs(x) for x in lst] for lst in list_o_data_lists]

    Interest_data = absolute_val_o_lists[0]
    Deposit_data = absolute_val_o_lists[1]
    Balance_data = absolute_val_o_lists[2]
    Withdrawal_data = absolute_val_o_lists[3]

    print(Interest_data)
    print(Deposit_data)
    print(Balance_data)
    print(Withdrawal_data)
    
    # Set the width of each bar
    bar_width = 0.4

   # Set the positions of the bars on the x-axis for each set
    
    r = np.arange(len(months))
    '''
    r2 = [x + bar_width for x in r1]
    r3 = [x + bar_width for x in r2]
    '''

    # Create the overlaying bar plot
    plt.bar(r, Deposit_data, color='blue', width=bar_width, edgecolor='white', label='Deposits')
    plt.bar(r, Interest_data, color='orange', width=bar_width, edgecolor='white', label='Interest', bottom=Deposit_data)
    plt.bar(r, Balance_data, color='cyan', width=bar_width, edgecolor='white', label='Balance', alpha=0.7)
    plt.bar(r, Withdrawal_data, color='pink', width=bar_width, edgecolor='white', label='Withdrawals', alpha=0.8)

    # Add x-axis labels and title
    plt.xlabel('Months')
    #plt.ylabel('Data')
    # Add a title
    plt.title('1944 Saving Account Data By Month')
    # Add legend
    plt.legend()
    # Adjust the x-axis tick labels
    plt.xticks(r, months)
    # Display the chart
    plt.show()

saving_breakdown()