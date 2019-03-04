import os, subprocess
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
b=r'C:\Users\cho2n\PycharmProjects\projcode\Scripts\python.exe C:\Users\cho2n\Desktop\Masters Thesis\projcode\backend\FMMSysApi\manage.py graph_models -a -g -o model.png'

subprocess.run(b,shell=True)