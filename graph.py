import pandas as pd
import plotly.graph_objects as go
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from collections import defaultdict
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
##################################################################
##CASES OVERALL
#df = pd.read_csv('cases-overall.csv')
#fig1 = go.Figure(go.Scatter(x = df['districtid'], y = df['cases'],
#                  name='overall cases'))
#fig1.update_layout(title='OVERALL CASES',
#                   plot_bgcolor='rgb(230, 230,230)',
#                   showlegend=True)
#fig1.show()
###################################################################

##NEIGHBOR MEAN
#df = pd.read_csv('neighbor-overall.csv')
#fig2 = go.Figure(go.Scatter(x = df['districtid'], y = df['neighbormean'],
#                  name='NEIGHBOR MEAN'))
#fig2.update_layout(title='NEIGHBOR OVERALL OBSERVATION',
#                   plot_bgcolor='rgb(230, 230,230)',
#                   showlegend=True)
#fig2.show()


###################################################################

##STATE MEAN
#df = pd.read_csv('state-overall.csv')
#fig3 = go.Figure(go.Scatter(x = df['districtid'], y = df['statemean'],
#                  name='STATE MEAN'))
#fig3.update_layout(title='STATE OVERALL OBSERVATION',
#                   plot_bgcolor='rgb(230, 230,230)',
#                   showlegend=True)
#fig3.show()

##################################################################
#
##NEIGHBORHOOD ZSCORE OVERALL
#df = pd.read_csv('zscore-overall.csv')
#fig4 = go.Figure(go.Scatter(x = df['districtid'], y = df['neighborhoodzscore'],
#                  name='NEIGHBORHOOD ZSCORE'))
#fig4.update_layout(title='NEIGHBORHOOD ZSCORE',
#                   plot_bgcolor='rgb(230, 230,230)',
#                   showlegend=True)
#fig4.show()
#
###################################################################
#
##STATE ZSCORE OVERALL
df = pd.read_csv('zscore-overall.csv')
fig5 = go.Figure(go.Scatter(x = df['districtid'], y = df['statezscore'],
                  name='STATE ZSCORE'))
fig5.update_layout(title='STATE ZSCORE',
                   plot_bgcolor='rgb(230, 230,230)',
                   showlegend=True)
fig5.show()
#
###################################################################