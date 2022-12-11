#!/usr/bin/env python3
# this is our sentence generator that smashes together our people/places/things from our CSV dictionary
# imports
import pandas as pd
import os


## TESTS TEST TEST

df = pd.read_csv('~/programming/personalized_art_generation/prompts/matts_list.csv')
#might be crap

print(df.to_string())
# TEST TEST TEST