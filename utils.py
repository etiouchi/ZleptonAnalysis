#############################################################################

import math, ROOT, array

#############################################################################

def newArray(type, size):
	return array.array(type, [0 for i in xrange(size)])

#############################################################################

def localLoader(fName, name):

	result = ROOT.TChain(name)

	try:
		fp = open(fName, 'rt')

		for line in fp.readlines():

			line = line.strip()

			if len(line) > 0:
				result.Add(line)

		fp.close()

	except IOError:
		print('Could not open \'%s\' !' % fName)

	return result

#############################################################################

def fillTreeFromDict(tree, item):
	#####################################################################
	# INIT								    #
	#####################################################################

	if tree.__dict__.has_key('dict') == False:

		tree.dict = {}

		for variable in item:

			T = type(item[variable]).__name__

			if T == 'str': pass

			elif T == 'int':
				tree.dict[variable] = array.array('i', [0x0])
				tree.Branch(variable, tree.dict[variable], '%s/I' % variable)

			elif T == 'long':
				tree.dict[variable] = array.array('I', [0x0])
				tree.Branch(variable, tree.dict[variable], '%s/i' % variable)

			elif T == 'float':
				tree.dict[variable] = array.array('f', [0.0])
				tree.Branch(variable, tree.dict[variable], '%s/F' % variable)

			elif T == 'bool':
				tree.dict[variable] = array.array('i', [0x0])
				tree.Branch(variable, tree.dict[variable], '%s/I' % variable)

			else:
				print('Unsupported type \'%s\' for branch \'%s\' !' % (T, variable))

	#####################################################################
	# FILL								    #
	#####################################################################

	for variable in item:

		if tree.dict.has_key(variable):

			tree.dict[variable][0] = item[variable]

	tree.Fill()

#############################################################################

def getBounds(signal):
	bin = signal.GetMaximumBin()

	window = 3.0 * signal.GetRMS() / signal.GetXaxis().GetBinWidth(1)

	a = bin - window
	b = bin + window

	if a - math.floor(a) < 0.5:
		a = int(a) + 0
	else:
		a = int(a) + 1

	if b - math.floor(b) < 0.5:
		b = int(b) + 0
	else:
		b = int(b) + 1

#	print('bin: %d, win: %d, min: %d, max: %d' % (bin, window, a, b))

	return a, b

#############################################################################

def getSignificance(signal, bkgd):
	a, b = getBounds(signal)

	s = signal.Integral(a, b)
	b =  bkgd .Integral(a, b)

	return math.sqrt(2.0 * ((s + b) * math.log(1.0 + s / b) - s))

#############################################################################

def getSignalToNoiseRatio(signal, bkgd):
	a, b = getBounds(signal)

	I1 = signal.Integral(a, b)
	I2 =  bkgd .Integral(a, b)

	return I1 / I2

#############################################################################

def getEfficiencyError(x, y):

	return math.sqrt(1.0 * x * (y - x)/(y * y * y))

#############################################################################

def dR(eta1, eta2, phi1, phi2):
	dEta = eta1 - eta2
	dPhi = phi1 - phi2
	M_PI = 3.14159265

	while(dPhi < -M_PI):
		dPhi += 2.0 * M_PI
	while(dPhi >= +M_PI):
		dPhi -= 2.0 * M_PI

	return math.sqrt(dEta * dEta + dPhi * dPhi)

