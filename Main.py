import random 
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
list1 = []
count1 = []
for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    list1.append(dice1+dice2)
mean = sum(list1)/len(list1)
st_div = statistics.stdev(list1)
print(mean)
print(st_div)
median = statistics.median(list1)
mode = statistics.mode(list1)
print(median)
print(mode)
fstd_start, fstd_stop = mean - st_div, mean + st_div
sstd_start, sstd_stop = mean - 2*(st_div), mean + 2*(st_div)
tstd_start, tstd_stop = mean - 3*(st_div), mean + 3*(st_div)
list_of_data1 = [result for result in list1 if result>fstd_start and result<fstd_stop]
list_of_data2 = [result for result in list1 if result>sstd_start and result<sstd_stop]
list_of_data3 = [result for result in list1 if result>tstd_start and result<tstd_stop]
print(len(list_of_data1)*100/len(list1))
print(len(list_of_data2)*100/len(list1))
print(len(list_of_data3)*100/len(list1))
graph = ff.create_distplot([list1],['result'],show_hist=False)
graph.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name='Mean'))
graph.add_trace(go.Scatter(x=[fstd_start,fstd_start],y=[0,0.17],mode='lines',name='First standard deviation'))
graph.add_trace(go.Scatter(x=[fstd_stop,fstd_stop],y=[0,0.17],mode='lines',name='First standard deviation'))
graph.add_trace(go.Scatter(x=[sstd_start,sstd_start],y=[0,0.17],mode='lines',name='Second standard deviation'))
graph.add_trace(go.Scatter(x=[sstd_stop,sstd_stop],y=[0,0.17],mode='lines',name='Second standard deviation'))
graph.add_trace(go.Scatter(x=[tstd_start,tstd_start],y=[0,0.17],mode='lines',name='Third standard deviation'))
graph.add_trace(go.Scatter(x=[tstd_stop,tstd_stop],y=[0,0.17],mode='lines',name='Third standard deviation'))
graph.show()