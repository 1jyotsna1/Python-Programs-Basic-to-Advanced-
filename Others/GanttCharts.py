import numpy as np
import pandas as pd
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go

tls.set_credentials_file(username='1jyotsna1' ,api_key='adSffv3YL8CdBCCj1TSd')

a=np.linspace(start=0, stop=36,num=36)
np.random.seed(25)
b=np.random.uniform(low=0.0, high=1.0, size=36)
##trace=go.scatter(x=a,y=b)
##data=trace
py.iplot(b, filename='basic-chart')
