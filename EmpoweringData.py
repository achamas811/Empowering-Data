import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

#Turn csv into a data frame
lwd = pd.read_csv("C:/Users/alexa/Downloads/livwell135.csv")

#Setting: The countries and the events that occurred during the time period of 2000-2015
print("The Setting \n")
print("The setting of the data takes place in Colombia and Peru between the years of 2000 and 2015.")
input("Press enter to continue...")
print("\nColombia\n")
print("In Colombia, there was a recession that occurred in the late 1990s into the early 2000s.")
input("Press enter to continue...\n")
print(f"In 1999, Colombia’s economy fell by 4% and in 2000, Colombia’s unemployment level reached 20.4%.")
input("Press enter to continue...")
print("\nPeru\n")
print("In the 2000s, Peru suffered from a major natural disaster and violence.")
input("Press enter to continue...\n")
print("In 2002, a car bomb exploded in Lima, Peru killing nine people, injuring thirty-two, and caused heavy damage to the surrounding buildings and cars in the process of the event.\n")
print("In 2007, a magnitude 8 earthquake occurred on the coast of south Peru that killed 519 people, injuring 1,300 people, and causing damage to tens of thousands of  homes, churches, schools, and hospitals. The infrastructure damage was worth up to $300 million.\n")

print("Sources")
print("")