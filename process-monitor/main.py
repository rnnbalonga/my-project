import re, datetime

cron = [
    '0 5 * * * /path/to/eosps.sh GUI-AO-01 start',  
    ' '         
    '0 5 * * * /path/to/eosps.sh LH-MXOD-02 start',  
    '#0 8 * * * /path/to/eosps.sh LH-MXOD-02 start',          
    '45 21 * * * /path/to/eosps.sh LH-MXOD-02 stop',           
    '15 23 * * * /path/to/systemctl stopall'
]

process_name_regex = r'(?<=\.sh\s)(?P<process>.*?)(?=\s+s)'
timing_regex = r'^\s*(?P<minute>\S+)\s+(?P<hour>\S+)\s+(?P<day_of_month>\S+)\s+(?P<month>\S+)\s+(?P<day_of_week>\S+)'

# Expected Output
    # Dictionary with process_name as key
    # Must grab all timing details of start and stop schedule of each process name
    # If no dedicated stop schedule, grab timing detail of stopall

ps_details = {
    'GUI-AO-01': 
    # Up to you if you want each command as a separate dictionary inside a list or if you want to combine all in one dictionary
    # I prefer using a list since one dictionary for one command

    [
        {
        'start_time': datetime.time(5, 0),
        'start_day_of_month': '*',
        'start_month': '*',
        'start_day_of_week': '*',
        },

        {
        'stop_time': datetime.time(23, 15),
        'stop_day_of_month': '*',
        'stop_month': '*',
        'stop_day_of_week': '*',
        }
    ],
    'LH-MXOD-02': 
    [
        {
        'start_time': datetime.time(5, 0),
        'start_day_of_month': '*',
        'start_month': '*',
        'start_day_of_week': '*',
        },

        {
        'stop_time': datetime.time(21, 45),
        'stop_day_of_month': '*',
        'stop_month': '*',
        'stop_day_of_week': '*',
        }
    ]
}
