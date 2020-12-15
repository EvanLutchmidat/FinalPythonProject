#This is Evan Lutchmidat's python code for CS102-B on microsoft stocks over the last 3 years using 3 month intervals
#all of the modules I believed I would need
import yfinance as yf
import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

#finds the stock data we will be using
tickerSymbol = 'MSFT'

#This identifies the data from the stocks database
tickerData = yf.Ticker(tickerSymbol)

#Retrieves the data from microsoft stocks of the last 3 years in 3 month intervals
tickerDf = tickerData.history(period = '3y', interval = '3mo')

#displays a table of the stock
print(tickerDf)

#asks for the coulumn of your choice to run a statistical analysis on
print('What coulumn would you like to analyze?')
print('Choose 1 for Open, 2 for High, 3 for Low, 4 for Close (Only choose a number 1-4, inclusive)')

#requests your user input value based on the criteria above
val = input('Enter your choice: ').lower()

#if the user chose the Open column
if val == '1':
        #data of the column
        y = [82.556168, 90.513230, 96.021941, 107.624844, 110.18625, 110.549098, 121.730778, 134.719558, 150.218647, 164.023923, 181.6243, 224.921131, 214.509995, 213.100006]

        #dates of each row
        x = ['2017-12', '2018-3', '2018-6', '2018-9', '2018-12', '2019-3', '2019-6', '2019-9', '2019-12', '2020-3', '2020-6', '2020-9', '2020-12-01', '2020-12-13']

        #finds the mean of the data then converts the data from float to string
        mean11 = statistics.mean(y)
        mean12 = str(mean11)

        #finds the median of the data and converts the data from float to string
        median11 = statistics.median(y)
        median12 = str(median11)

        #finds the mode of the data and converts the data from float to string
        mode11 = statistics.mode(y)
        mode12 = str(mode11)

        #finds the variance of the data and converts the data from float to string
        var11 = statistics.variance(y)
        var12 = str(var11)

        #finds the standard deviaiton of the data and converts the data from float to string
        std11 = statistics.stdev(y)
        std12 = str(std11)

        #finds the 25%, 50%, and 75% percentiles of the data and converts the data from list to string
        per11 = statistics.quantiles(y, n=4)
        per12 = str(per11)

        #finds the range of the data and converts the data from float to string
        range11 = max(y) - min(y)
        range12 = str(range11)

        #This print will displasy all the calculated values above in an organized fashion
        print('The mean is ' +mean12, ';', 'The median is ' +median12, ';', 'The mode is ' +mode12, ';', 'The variance is ' +var12, ';', 'The sample standard deviation is ' +std12, ';', 'The percentiles are ([25%, 50%, 75%], respectively) ' +per12, ';', 'The range is ' +range12)

        #initiates creation of graph
        fig, ax = plt.subplots()

        #establishes what is x and y axis and teh label and marker for data points
        ax.plot(x, y, linewidth=0, marker='s', label='Data points')

        #names the x axis
        ax.set_xlabel('Date (Year-Month-Day)')

        #names the y axis
        ax.set_ylabel('Stock Value')

        #colors the background to white
        ax.legend(facecolor='white')

        #plots the graph using matplotlib and tells us which plot it is in case user forgot
        print('This is the plot of the Open data.', plt.show())

#if user chose High column
if val == '2':

        #note that the comments of the interior of the if function will be the same as in the first if function
        y = [92.083726, 96.291285, 109.078914, 112.799771, 110.59579, 128.645891, 139.25568, 150.389668, 188.700981, 186.051209, 229.990454, 232.251945, 217.320007, 216.209503]
        x = ['2017-12', '2018-3', '2018-6', '2018-9', '2018-12', '2019-3', '2019-6', '2019-9', '2019-12', '2020-3', '2020-6', '2020-9', '2020-12-01', '2020-12-13']
        mean11 = statistics.mean(y)
        mean12 = str(mean11)
        median11 = statistics.median(y)
        median12 = str(median11)
        mode11 = statistics.mode(y)
        mode12 = str(mode11)
        var11 = statistics.variance(y)
        var12 = str(var11)
        std11 = statistics.stdev(y)
        std12 = str(std11)
        per11 = statistics.quantiles(y, n=4)
        per12 = str(per11)
        range11 = max(y) - min(y)
        range12 = str(range11)
        print('The mean is ' +mean12, ';', 'The median is ' +median12, ';', 'The mode is ' +mode12, ';', 'The variance is ' +var12, ';', 'The sample standard deviation is ' +std12, ';', 'The percentiles are ([25%, 50%, 75%], respectively) ' +per12, ';', 'The range is ' +range12)
        fig, ax = plt.subplots()
        ax.plot(x, y, linewidth=0, marker='s', label='Data points')
        ax.set_xlabel('Date (Year-Month-Day)')
        ax.set_ylabel('Stock Value')
        ax.legend(facecolor='white')
        print('This is the plot of the High data.', plt.show())

#if the user chose the Low column
if val == '3':

        #note that the comments of the interior of the if function will be the same as in the first if function
        y = [80.351608, 83.85884, 94.068253, 96.459434, 91.620354, 106.543913, 116.9736, 131.376470, 145.112733, 131.489028, 180.440283, 195.737542, 209.110001, 212.885696]
        x = ['2017-12', '2018-3', '2018-6', '2018-9', '2018-12', '2019-3', '2019-6', '2019-9', '2019-12', '2020-3', '2020-6', '2020-9', '2020-12-01', '2020-12-13']
        mean11 = statistics.mean(y)
        mean12 = str(mean11)
        median11 = statistics.median(y)
        median12 = str(median11)
        mode11 = statistics.mode(y)
        mode12 = str(mode11)
        var11 = statistics.variance(y)
        var12 = str(var11)
        std11 = statistics.stdev(y)
        std12 = str(std11)
        per11 = statistics.quantiles(y, n=4)
        per12 = str(per11)
        range11 = max(y) - min(y)
        range12 = str(range11)
        print('The mean is ' +mean12, ';', 'The median is ' +median12, ';', 'The mode is ' +mode12, ';', 'The variance is ' +var12, ';', 'The sample standard deviation is ' +std12, ';', 'The percentiles are ([25%, 50%, 75%], respectively) ' +per12, ';', 'The range is ' +range12)
        fig, ax = plt.subplots()
        ax.plot(x, y, linewidth=0, marker='s', label='Data points')
        ax.set_xlabel('Date (Year-Month-Day)')
        ax.set_ylabel('Stock Value')
        ax.legend(facecolor='white')
        print('This is the plot of the Low data.', plt.show())

#if the user chose the Close column
if val == '4':

        #note that the comments of the interior of the if function will be the same as in the first if function
        y = [89.879158, 95.183823, 108.643684, 107.663681, 109.240402, 121.115356, 135.501053, 149.285172, 160.311722, 181.824356, 224.398651, 213.511017, 214.199997, 214.199997]
        x = ['2017-12', '2018-3', '2018-6', '2018-9', '2018-12', '2019-3', '2019-6', '2019-9', '2019-12', '2020-3', '2020-6', '2020-9', '2020-12-01', '2020-12-13']
        mean11 = statistics.mean(y)
        mean12 = str(mean11)
        median11 = statistics.median(y)
        median12 = str(median11)
        mode11 = statistics.mode(y)
        mode12 = str(mode11)
        var11 = statistics.variance(y)
        var12 = str(var11)
        std11 = statistics.stdev(y)
        std12 = str(std11)
        per11 = statistics.quantiles(y, n=4)
        per12 = str(per11)
        range11 = max(y) - min(y)
        range12 = str(range11)
        print('The mean is ' +mean12, ';', 'The median is ' +median12, ';', 'The mode is ' +mode12, ';', 'The variance is ' +var12, ';', 'The sample standard deviation is ' +std12, ';', 'The percentiles are ([25%, 50%, 75%], respectively) ' +per12, ';', 'The range is ' +range12)
        fig, ax = plt.subplots()
        ax.plot(x, y, linewidth=0, marker='s', label='Data points')
        ax.set_xlabel('Date (Year-Month-Day)')
        ax.set_ylabel('Stock Value')
        ax.legend(facecolor='white')
        print('This is the plot of the Close data.', plt.show())

#This was my python project showing the statistics of microsoft stocks and this is how the code will close once you are done viewing the graph
print('Hopefully you enjoyed viewing the statistics of Microsoft Stocks over the last 3 years!')
