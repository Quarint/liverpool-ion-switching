from scipy.signal import butter,filtfilt

def filter_data(data, btype='hight', cutoff=1/100):
    T = data.shape[0] / 10000
    fs = 10000
    order = 2
    nyq = 0.5 * fs
    def butter_highpass_filter(data, cutoff, fs, order):
        normal_cutoff = cutoff / nyq
        # Get the filter coefficients 
        b, a = butter(order, normal_cutoff, btype=btype, analog=False)
        y = filtfilt(b, a, data)
        return y
    return butter_highpass_filter(data, cutoff, fs, order)