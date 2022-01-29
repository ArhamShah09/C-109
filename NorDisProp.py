import pandas as pd
import statistics as st

df = pd.read_csv("height-weight.csv")

height = df["Height(Inches)"].tolist()

height_mean = st.mean(height)

height_mode = st.mode(height)

height_median = st.median(height)
print(height_mean, height_mode, height_median)

height_stdev = st.stdev(height)
print(height_stdev)

stdev_1_start = height_mean-height_stdev
stdev_1_end = height_mean+height_stdev

stdev_2_start = height_mean-(2*height_stdev)
stdev_2_end = height_mean+(2*height_stdev)

stdev_3_start = height_mean-(3*height_stdev)
stdev_3_end = height_mean+(3*height_stdev)

height_data_within_1_stdev = [result for result in height if result > stdev_1_start and result < stdev_1_end]
height_data_within_2_stdev = [result for result in height if result > stdev_2_start and result < stdev_2_end]
height_data_within_3_stdev = [result for result in height if result > stdev_3_start and result < stdev_3_end]

percent_heightdata_within_1_stdev = (len(height_data_within_1_stdev)/len(height))*100
percent_heightdata_within_2_stdev = (len(height_data_within_2_stdev)/len(height))*100
percent_heightdata_within_3_stdev = (len(height_data_within_3_stdev)/len(height))*100

print(percent_heightdata_within_1_stdev)
print(percent_heightdata_within_2_stdev)
print(percent_heightdata_within_3_stdev)