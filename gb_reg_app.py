import streamlit as st
import pickle
import numpy as np
import pandas as pd

with open('gb_reg.pkl', 'rb') as f:
    gb_reg = pickle.load(f)


def make_prediction(short_name, long_name, dob, club_name, potential, value_eur, wage_eur,
                    release_clause_eur, passing, dribbling, attacking_short_passing, movement_reactions,
                    power_shot_power, mentality_vision, mentality_composure):

    player_data = [short_name, long_name, dob, club_name, potential, value_eur, wage_eur,
                   release_clause_eur, passing, dribbling, attacking_short_passing, movement_reactions,
                   power_shot_power, mentality_vision, mentality_composure]

    prediction = gb_reg.predict(player_data)

    return prediction
