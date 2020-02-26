import matplotlib.pyplot
import os

colours = {'red'     :(198.0/255.0, 62.0/255.0, 98.0/255.0),
			'reddish': (198/255,131/255,136/255),
			'blue'    :(0.0/255.0, 70.0/255.0, 127.0/255.0),
			'grayblue'  :(145./255.0, 148./255.0, 182./255.0),
			'purple'  :(126.0/255.0, 29.0/255.0, 123.0/255.0),
			'purpley'  :(200./255.0, 130./255.0, 199./255.0),
			'sand'  :(244./255.0, 234./255.0, 168./255.0),
			'sandy'  :(200./255.0, 191./255.0, 130./255.0),
			'green'   :(45.0/255.0, 159.0/255.0, 60.0/255.0),
			'greenish':(130/255,200/255,139/255)}

def plot_style(style=None):
	'''
	Simple function to change plot style to one of the JQC ones.

	available styles are:
	 'single column',
	 'two column',
	 'half column',
	 'large two column'
	 'full page',
	  thesis',
	 'large thesis'

	The default is 'single column'.
	'''
	
	cwd = os.path.dirname(os.path.abspath(__file__))

	fpath = os.path.join(cwd,"StyleFiles","")

	if style != None:
		style = style.lower()
		if style in ["two column","twocolumn","wide"]:
			stylefile = 'Wide.mplstyle'

		elif style in ["large two column","largetwocolumn","largewide",
						"large wide"]:
			stylefile = 'LargeWide.mplstyle'

		elif style in ["half column","halfcolumn","small"]:
			stylefile = 'small.mplstyle'

		elif style in ["full page","fullpage"]:
			stylefile = 'FullPage.mplstyle'

		elif style =="thesis":
			stylefile = 'Thesis.mplstyle'

		elif style in ["largethesis", "large thesis","large"]:
			stylefile = 'BigThesis.mplstyle'

		elif style in ["normal" or "single column" or "default"]:
			stylefile='default.mplstyle'

		else:
			print("available styles are 'single column', 'two column',"+\
				" 'half column', 'full page', 'thesis', 'large thesis'. The"+\
				" default is 'single column'. ")
	else:
		print("available styles are 'single column', 'two column',"+\
				" 'half column', 'full page', 'thesis', 'large thesis'. The"+\
				" default is 'single column'. ")
	matplotlib.pyplot.style.use(fpath+stylefile)
