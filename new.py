import csv
import plotly.figure_factory as pff
import statistics
import pandas as pd
import plotly.graph_objects as pgo

df = pd.read_csv("data.csv")
data = df["reading"].tolist()
mean = statistics.mean(data)
print(mean)
sd = statistics.stdev(data)
print(sd)

figure = pff.create_distplot([data],["mean"],show_hist=False)
figure.show()

fsdstart , fsdend = mean-sd, mean+sd
ssdstart,ssdend = mean-(2*sd),mean+(2*sd)
tsdstart,tsdend = mean-(3*sd),mean+(3*sd)
figure.add_trace(pgo.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))

figure.add_trace(pgo.Scatter(x=[fsdstart,fsdstart],y=[0,0.17],mode="lines",name="first"))
figure.add_trace(pgo.Scatter(x=[fsdend,fsdend],y=[0,0.17],mode="lines",name="end"))

figure.add_trace(pgo.Scatter(x=[ssdstart,ssdstart],y=[0,0.17],mode="lines",name="second"))
figure.add_trace(pgo.Scatter(x=[ssdend,ssdend],y=[0,0.17],mode="lines",name="2end"))

figure.add_trace(pgo.Scatter(x=[tsdstart,tsdstart],y=[0,0.17],mode="lines",name="third"))
figure.add_trace(pgo.Scatter(x=[tsdend,tsdend],y=[0,0.17],mode="lines",name="3end"))

figure.show()

data1 = [result for result in mean if result > fsdstart and result < fsdend]
data2 = [result for result in mean if result > ssdstart and result < ssdend]
data3 = [result for result in mean if result > tsdstart and result < tsdend]
print("{}% of data lies within first standard diviation".format(len(data1)*100/len(mean)))
print("{}% of data lies within second standard diviation".format(len(data2)*100/len(mean)))
print("{}% of data lies within third standard diviation".format(len(data3)*100/len(mean)))
