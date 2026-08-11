import json
import numpy as np

with open("Sodoku_Data\Easy.json","r" ) as file:
    EasySodukuData = np.array(json.load(file))




# class Check:
#     def __init__(self, data):
#         self.data = data


def CheckRow(data):
    for r in range(9):
        row = []

        for c in range(9):
            row.append(data[r][c])

        if len(row) != len(set(row)):
            print("Wrong")
            return False

    return True

def CheckRow(data):
    cash = []

    for c in range(9):
        for r in range(9):
            cash.append(data[c][r])

    set_cash = set(cash)

    if len(cash) != len(set_cash):
        cash.append("Wrong")

CheckRow(EasySodukuData)   

