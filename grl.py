#!/usr/bin/python

#############################################################################
# Author  : Jerome ODIER
#
# Email   : jerome.odier@cern.ch
#
# Version : 2.0 (2010-2011)
#
#############################################################################

import sys, xml.dom.minidom

#############################################################################

if __name__ == '__main__':
	try:
		MyGRLRoot = xml.dom.minidom.parse(sys.argv[1])

	except (IndexError, IOError), e:
		print('Syntax: grl.py grl.xml')
		sys.exit(1)

	i = 0

	print('def check(RunNumber, LumiBlock):')
	print('')
	print('\tresult = False')
	print('')

	for LumiRange in MyGRLRoot.getElementsByTagName('NamedLumiRange'):

		for LumiBlock in LumiRange.getElementsByTagName('LumiBlockCollection'):

			Run = None
			LBRangeStart = []
			LBRangeEnd = []

			for theRun in LumiBlock.getElementsByTagName('Run'):
				for node in theRun.childNodes:
					Run = node.nodeValue.strip()

			for theLBRange in LumiBlock.getElementsByTagName('LBRange'):
				LBRangeStart.append(theLBRange.getAttribute('Start'))
				LBRangeEnd.append(theLBRange.getAttribute('End'))

			if not Run is None:

				nr = (len(LBRangeStart) + len(LBRangeEnd)) / 2

				if i == 0:
					print('\tif RunNumber == %s and (' % Run)
				else:
					print('\telif RunNumber == %s and (' % Run)

				for j in xrange(nr):
					print('\t\t(LumiBlock >= 0x%04X and LumiBlock <= 0x%04X)' % (int(LBRangeStart[j]), int(LBRangeEnd[j])))

					if j < (nr - 1):
						print('\t\tor')

				print('\t ): result = True')

				i = i + 1

	print('')
	print('\treturn result\n')

#############################################################################

