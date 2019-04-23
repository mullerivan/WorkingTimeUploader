#!/usr/bin/env python3
import subprocess

""" Install:        
        sudo pip install gcalcli         
    First  at all  get  your times  on  Git log
        git log --since=march1 --until=march30 --author='Muller' --no-merges --date=format:'%Y-%m-%d' --pretty=format:'{%n "subject": "%s",%n "date": "%cd"%n  },' >> ../somefile.json
    It will  get you a  Broken Json  like: {},{},{},

    Copy it into the value of the month = [HERE!]
    Set Up your calendar name
        my_calendar_name = 'YOUR-CALENDAR-HERE' 


    TODO: Get the git log from python to not need to copy  logs down here!
"""
my_calendar_name = 'CharlesTutor'
month = [  # Remplace me with result of  Git Log!
{
 "subject": "change site name",
 "date": "2019-04-20"
  },
{
 "subject": "remove   extension",
 "date": "2019-04-20"
  },
{
 "subject": "host allowed",
 "date": "2019-04-16"
  },
{
 "subject": "agora sdk 2.6.1",
 "date": "2019-04-16"
  },


]  # Remplace me with result of  Git Log!
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
base_command_string = 'gcalcli|--cal|{calendar}|add|--title|{title}|--where|work|--duration|{duration}|--when|"{when}"|--description|{desc}|--noprompt'


def upload(bashCommand):
    process = subprocess.Popen(bashCommand.split('|'), stdout=subprocess.PIPE)
    process.communicate()


def group_month_group_by_day(month):
    grouped_commits = {}
    for commit in month:
        duration = 0
        subject = commit['subject']
        date = commit['date']
        if date in grouped_commits:
            grouped_commits[date] = grouped_commits[date] + '\n' + subject
        else:
            grouped_commits[date] = subject

        if ':duration:' in subject:
            if len(subject.split(':duration:')) > 0:
                duration += int(subject.split(':duration:')[1])

        if not date + '_duration' in grouped_commits:
            grouped_commits[date + '_duration'] = duration
        else:
            grouped_commits[date + '_duration'] += duration
    return grouped_commits


by_day = group_month_group_by_day(month)
print('############################################')
print(my_calendar_name)
print('############################################')
for key, day in by_day.items():
    '''Time est'''
    # Skip  duration count for each day
    if not '_duration' in key:
        gcalcli = base_command_string.format(
            calendar=my_calendar_name,
            title='Ivan Muller',
            desc=day,
            duration=by_day[key + '_duration'],
            when=key)
        upload(gcalcli)
        print('############################################')
        print('############################################')
        print('Date:')
        print(key)
        print('Description:')
        print(day)
        print('Duration: ' + str(by_day[key + '_duration']))
