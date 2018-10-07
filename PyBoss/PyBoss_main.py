import os
import csv

#state conversion dictionary
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#set path to read csv file
pyBoss_csv = os.path.join('employee_data.csv')

#set path to write csv file
cleanData_csv = os.path.join('employee_data_cleaned.csv')

#write the csv file
with open(cleanData_csv, 'w', newline='') as pyBossClean:

    csvwriter = csv.writer(pyBossClean, delimiter=',')

    # write and print the first row (column headers)
    headers = ['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']
    print(headers)
    csvwriter.writerow(headers)

    #read the csv file
    with open(pyBoss_csv, 'r') as pyBossData:
        csvreader = csv.reader(pyBossData, delimiter=",")

        #skip the header
        next(csvreader, None)

        for row in csvreader:

            #identify and split  name
            fullName = row[1]
            splitName = fullName.split()

            #insert first and last name in the row at the name position
            row.insert(1, splitName[0])
            row.insert(2, splitName[1])

            #remove non-split name data from row
            row.pop(3)

            #identify and split date
            oldDate = row[3]
            splitDate = oldDate.split("-")

            #construct new date
            newDate = f"{splitDate[1]}/{splitDate[2]}/{splitDate[0]}"

            #insert new date, remove old
            row.insert(3, newDate)
            row.pop(4)

            #identify ssn
            fullSSN = row[4]

            #create masked ssn
            maskSSN = "***-**-" + fullSSN[-4:]
            
            #insert masked ssn, remove old
            row.insert(4, maskSSN)
            row.pop(5)

            #identify and replace state with abbreviation
            fullState = row[5]
            state = us_state_abbrev[fullState]

            #remove old state and add abbreviation
            row.pop(5)
            row.append(state)

            print(row)
            csvwriter.writerow(row)

