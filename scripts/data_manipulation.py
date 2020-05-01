import pandas as pd
import numpy as np
import os
from IPython.display import Audio, display
import matplotlib.pyplot as plt

def training_done():
    display(Audio(os.path.join("../", "ice-cubes-glass-daniel_simon.wav"), autoplay=True))

def load_data():
    data_folder = "../data"
    predictions_folder = "../predictions"
    train_file = os.path.join(data_folder, "train_clean.csv")
    test_file = os.path.join(data_folder, "test_clean.csv")
    all_data = pd.read_csv(train_file)
    test_data = pd.read_csv(test_file)
    return (predictions_folder, all_data, test_data)

def load_shifted_values(df_list):
    def add_shifted(df, shift=1):
        first_value_fill = np.full(shift, df['signal'].iloc[0])
        last_value_fill = np.full(shift, df['signal'].iloc[-1])
        df['previous_signal_'+str(i)] = np.insert(df['signal'].iloc[0:-1*shift].values, 0, first_value_fill)
        df['next_signal_'+str(i)] = np.append(df['signal'].iloc[shift:].values, last_value_fill)
    for df in df_list:
        for i in range(1, 4):
            add_shifted(df, i)
        if 'open_channels' in df.columns:
            df = df[['time', 'previous_signal_3', 'previous_signal_2', 'previous_signal_1', 'signal', 'next_signal_1', 'next_signal_2', 'next_signal_3', 'open_channels']]
        else:
            df = df[['time', 'previous_signal_3', 'previous_signal_2', 'previous_signal_1', 'signal', 'next_signal_1', 'next_signal_2', 'next_signal_3']]

def save_for_submission(test_df, predictions, predictions_folder, file_name):
    predictions_df = test_df[['time']].copy(deep=True)
    predictions_df['open_channels'] = predictions
    predictions_df.to_csv(os.path.join(predictions_folder, file_name), index=False, float_format='%07.4f')

def plot_signal_and_channels(df):
    fig, ax = plt.subplots(1, 2, figsize=(15, 5))
    ax[0].plot(range(len(df)), df['signal'], label="signal")
    ax[1].plot(range(len(df)), df['open_channels'], label="open_channels")

def plot_signal(df):
    fig, ax = plt.subplots(1, 1, figsize=(15, 5))
    ax.plot(range(len(df)), df['signal'], label="signal")