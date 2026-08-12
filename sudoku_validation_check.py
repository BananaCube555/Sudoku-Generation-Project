import json
import numpy as np

with open("Sodoku_Data\Easy.json","r" ) as file:
    EasySodukuData = np.array(json.load(file))




# class Check:
#     def __init__(self, data):
#         self.data = data

def check_col(data):
     for col in range(9):
          cash = []
          for row in range(9):
               cash.append(data[row][col])
          if len(cash) != len(set(cash)):
               print("Wrong")
               return False
            
               
        


def check_row(data):

    for row in range(9):
        cash = []
        for col in range(9):
            cash.append(data[row][col])

        if len(cash) != len(set(cash)):
                print("Wrong")
                return False

    
    return True

check_row(EasySodukuData[1]["board"])
check_col(EasySodukuData[1]["board"])