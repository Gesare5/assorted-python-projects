# May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)

#!/usr/bin/env python3

import re
import csv
import sys
import operator

def get_statistics(logfile):
  errors = {}
  per_user={}

  with open(logfile, "r") as file:
    for line in file.readlines():
      pattern = r": ([A-Z]*) ([\w ']*) [\[#\d\] ]*\(([\w\.]*)\)$"
      result = re.search(pattern, line)
      log_type = result.group(1)
      log_message = result.group(2)
      log_user = result.group(3)
        
      """ Check if user exists in per_user, if not add them with their corresponding values"""
      if log_user in per_user:
        if log_type == "INFO":
          per_user[log_user][log_type] += 1
        elif log_type == "ERROR":
          per_user[log_user][log_type] += 1  
      else:
        if log_type == "INFO":
          per_user[log_user] = {"ERROR": 0, "INFO": 1}   
        elif log_type == "ERROR":
          per_user[log_user] = {"ERROR": 1, "INFO": 0}  

      """ Check if error message exists in errors, if not add it and increase its count"""
      if log_type == "ERROR":
        if log_message in errors:
          errors[log_message] += 1
        else:
          errors[log_message] = 1

  errors = sorted(errors.items(), key = operator.itemgetter(1), reverse=True)
  per_user = sorted(per_user.items())
  return errors, per_user

def to_csv( errors, per_user):
  with open("user_statistics.csv", "w") as users:
    writer = csv.writer(users)
    writer.writerow(["Username", "INFO", "ERROR"])
    for item in per_user:
      user, log_type = item
      line = [user,log_type["INFO"],log_type["ERROR"]]
      writer.writerow(line)

  with open('error_message.csv', 'w') as error_csv:
    writer = csv.writer(error_csv)
    writer.writerow(["Error", "Count"])
    writer.writerows(errors)

if __name__ == "__main__":
  logfile = sys.argv[1]
  errors, per_user =  get_statistics(logfile)
  to_csv(errors, per_user)       




        
