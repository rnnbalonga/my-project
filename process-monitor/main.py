import datetime, re

cron = [
    '0 5 * * * /path/to/eosps.sh GUI-AO-01 start',           
    '0 5 * * * /path/to/eosps.sh LH-MXOD-02 start',            
    '45 21 * * * /path/to/eosps.sh LH-MXOD-02 stop',           
    '15 23 * * * /path/to/systemctl stopall'
]

def make_process_dictionary(command_list):
    process_regex_pattern = r'(?<=\.sh\s)(?P<process>.*?)(?=\s+s)'

    process_dictionary = {}
    
    for command in command_list:
        match = re.search(process_regex_pattern, command)
        if match:
            process = match.group('process')

            if process not in process_dictionary:
                process_dictionary[process] = [parse_command_time(command)]
            else:
                process_dictionary[process].append(parse_command_time(command))

    for key, entries in process_dictionary.items():
        has_stop = any('stopminute' in entry for entry in entries)
        if not has_stop:
            process_dictionary[key].append(set_stop_all_time(command_list))

    print(process_dictionary)

def is_command_start(command):
    return 'start' if 'start' in command else 'stop'

def parse_command_time(command):
    timing_regex_pattern = r'^\s*(?P<minute>\S+)\s+(?P<hour>\S+)\s+(?P<day_of_month>\S+)\s+(?P<month>\S+)\s+(?P<day_of_week>\S+)'
    
    command_type = is_command_start(command)

    match = re.search(timing_regex_pattern, command)

    if match:
        return {
        command_type + '_minute': match.group("minute"),
        command_type + '_hour': match.group("hour"),
        command_type + '_day_of_month': match.group("day_of_month"),
        command_type + '_month': match.group("month"),
        command_type + '_day_of_week': match.group("day_of_week") 
    }

def set_stop_all_time(command_list):
    stop_all_regex = r'\bstopall\b'

    for command in command_list:
        stop_all = re.search(stop_all_regex, command)
        if stop_all:
            return parse_command_time(command)
    
    return None

make_process_dictionary(cron)