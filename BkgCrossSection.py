#############################################################################

def GetBkgCrossSection7TeV(RunNumber):

	process = ''
	crossSection = -1.0
	
	if   RunNumber ==  107650:
		process = 'Alpgen+Jimmy Zee + 0 partons'
		crossSection = 827375.0
	elif RunNumber ==  107651:
		process = 'Alpgen+Jimmy Zee + 1 partons'
		crossSection = 166625.0
	elif RunNumber ==  107652:
		process = 'Alpgen+Jimmy Zee + 2 partons'
		crossSection = 50375.0
	elif RunNumber ==  107653:
		process = 'Alpgen+Jimmy Zee + 3 partons'
		crossSection = 14000.0
	elif RunNumber ==  107654:
		process = 'Alpgen+Jimmy Zee + 4 partons'
		crossSection = 3375.0
	elif RunNumber ==  107655:
		process = 'Alpgen+Jimmy Zee + 5 partons'
		crossSection = 1000.0
	elif RunNumber ==  107660:
		process = 'Alpgen+Jimmy Zmumu + 0 partons'
		crossSection = 822125
	elif RunNumber ==  107661:
		process = 'Alpgen+Jimmy Zmumu + 1 partons'
		crossSection = 166000.0
	elif RunNumber ==  107662:
		process = 'Alpgen+Jimmy Zmumu + 2 partons'
		crossSection = 49500.0
	elif RunNumber ==  107663:
		process = 'Alpgen+Jimmy Zmumu + 3 partons' 
		crossSection = 13875.0
	elif RunNumber ==  107664:
		process = 'Alpgen+Jimmy Zmumu + 4 partons'
		crossSection = 3500.0
	elif RunNumber ==  107665:
		process = 'Alpgen+Jimmy Zmumu + 5 partons'
		crossSection = 1000.0
	elif RunNumber ==  107670:
		process = 'Alpgen+Jimmy Ztautau + 0 partons'
		crossSection = 828125.0
	elif RunNumber ==  107671:
		process = 'Alpgen+Jimmy Ztautau + 1 partons'
		crossSection = 167375.0
	elif RunNumber ==  107672:
		process = 'Alpgen+Jimmy Ztautau + 2 partons'
		crossSection = 50375.0
	elif RunNumber ==  107673:
		process = 'Alpgen+Jimmy Ztautau + 3 partons'
		crossSection = 13750
	elif RunNumber ==  107674:
		process = 'Alpgen+Jimmy Ztautau + 4 partons'
		crossSection = 3500.0
	elif RunNumber ==  107675:
		process = 'Alpgen+Jimmy Ztautau + 5 partons'
		crossSection = 1000.0
	elif RunNumber ==  116960:
		process = 'Zbb, Z->ee (ll > 30 !GeV) + 0 parton [m_4l 60/12 !GeV]'
		crossSection = 20.701 * 1.4
	elif RunNumber ==  116961:
		process = 'Zbb, Z->ee (ll > 30 !GeV) + 1 parton [m_4l 60/12 !GeV]'
		crossSection = 18.8029 * 1.4
	elif RunNumber ==  116962:
		process = 'Zbb, Z->ee (ll > 30 !GeV) + 2 parton [m_4l 60/12 !GeV]'
		crossSection = 10.505 * 1.4
	elif RunNumber ==  116963:
		process = 'Zbb, Z->ee (ll > 30 !GeV) + 3 parton [m_4l 60/12 !GeV]'
		crossSection = 7.30463 * 1.4
	elif RunNumber ==  116965:
		process = 'Zbb, Z->mumu (ll > 30 !GeV) + 0 parton [m_4l 60/12 !GeV]'
		crossSection = 21.516 * 1.4
	elif RunNumber ==  116966: 
		process = 'Zbb, Z->mumu (ll > 30 !GeV) + 1 parton [m_4l 60/12 !GeV]'
		crossSection = 19.6674 * 1.4
	elif RunNumber ==  116967:
		process = 'Zbb, Z->mumu (ll > 30 !GeV) + 2 parton [m_4l 60/12 !GeV]'
		crossSection = 10.516 * 1.4
	elif RunNumber ==  116968:
		process = 'Zbb, Z->mumu (ll > 30 !GeV) + 3 parton [m_4l 60/12 !GeV]'
		crossSection = 7.93834 * 1.4
	elif RunNumber ==  116950:
		process = 'Zbb, Z->ee (ll > 30 !GeV) + 0 parton 3l filter, veto on m_4l 60/12 !GeV'
		crossSection = 756.32 * 1.4
	elif RunNumber ==  116951:
		process = 'Zbb, Z->ee (ll > 30 !GeV) + 1 parton 3l filter, veto on m_4l 60/12 !GeV'
		crossSection = 432.25 * 1.4
	elif RunNumber ==  116952:
		process = 'Zbb, Z->ee (ll > 30 !GeV) + 2 parton 3l filter, veto on m_4l 60/12 !GeV'
		crossSection = 176 * 1.4
	elif RunNumber ==  116953: 
		process = 'Zbb, Z->ee (ll > 30 !GeV) + 3 parton 3l filter, veto on m_4l 60/12 !GeV'
		crossSection = 96.75 * 1.4
	elif RunNumber ==  116955: 
		process = 'Zbb, Z->mumu (ll > 30 !GeV) + 0 parton 3l filter, veto on m_4l 60/12 !GeV'
		crossSection = 730.24 * 1.4
	elif RunNumber ==  116956: 
		process = 'Zbb, Z->mumu (ll > 30 !GeV) + 1 parton 3l filter, veto on m_4l 60/12 !GeV'
		crossSection = 432.25 * 1.4
	elif RunNumber ==  116957: 
		process = 'Zbb, Z->mumu (ll > 30 !GeV) + 2 parton 3l filter, veto on m_4l 60/12 !GeV'
		crossSection = 179.3 * 1.4
	elif RunNumber ==  116958: 
		process = 'Zbb, Z->mumu (ll > 30 !GeV) + 3 parton 3l filter, veto on m_4l 60/12 !GeV'
		crossSection = 92.3962 * 1.4
	elif RunNumber ==  128130: 
		process = 'AlpgenJimmyLowMassDYeebbNp0_nofilter'
		crossSection = 11675 * 1.25 * 1.4
	elif RunNumber ==  128131: 
		process = 'AlpgenJimmyLowMassDYeebbNp1_nofilter'
		crossSection = 1856.6 * 1.25 * 1.4
	elif RunNumber ==  128132: 
		process = 'AlpgenJimmyLowMassDYeebbNp2_nofilter'
		crossSection = 692.62 * 1.25 * 1.4
	elif RunNumber ==  128133: 
		process = 'AlpgenJimmyLowMassDYeebbNp3_nofilter'
		crossSection = 333.27 * 1.25 * 1.4
	elif RunNumber ==  128135: 
		process = 'AlpgenJimmyLowMassDYmumubbNp0_nofilter'
		crossSection = 11675 * 1.25 * 1.4
	elif RunNumber ==  128136: 
		process = 'AlpgenJimmyLowMassDYmumubbNp1_nofilter'
		crossSection = 1856.6 * 1.25 * 1.4
	elif RunNumber ==  128137: 
		process = 'AlpgenJimmyLowMassDYmumubbNp2_nofilter'
		crossSection = 692.62 * 1.25 * 1.4
	elif RunNumber ==  128138: 
		process = 'AlpgenJimmyLowMassDYmumubbNp3_nofilter'
		crossSection = 333.27 * 1.25 * 1.4
	elif RunNumber ==  128140: 
		process = 'AlpgenJimmyLowMassDYtautaubbNp0_nofilter'
		crossSection = 11675 * 1.25 * 1.4
	elif RunNumber ==  128141: 
		process = 'AlpgenJimmyLowMassDYtautaubbNp1_nofilter'
		crossSection = 1856.6 * 1.25 * 1.4
	elif RunNumber ==  128142: 
		process = 'AlpgenJimmyLowMassDYtautaubbNp2_nofilter'
		crossSection = 692.62 * 1.25 * 1.4
	elif RunNumber ==  128143: 
		process = 'AlpgenJimmyLowMassDYtautaubbNp3_nofilter'
		crossSection = 333.27 * 1.25 * 1.4
	elif RunNumber ==  105200: 
		process = 'ttbar (at least 1lepton filter)'
		crossSection = 91550.6
	elif RunNumber ==  109345: 
		process = 'ttbar (with Mll > 60 !GeV filter)'
		crossSection = 12707.2
	elif RunNumber ==  109346: 
		process = 'ttbar (with Mll > 60 !GeV filter and Mll > 12 !GeV)'
		crossSection = 515.2
	elif RunNumber ==  109292: 
		process = 'ZZ->4l 3LepFilter'
		crossSection = 91.54
	elif RunNumber ==  126399: 
		process = 'PowHegBoxZZeemm_Pythia_mll025_m4l40'
		crossSection = -1 # don't use this sample
	elif RunNumber ==  126400: 
		process = 'PowHegBoxZZeeee_Pythia_mll025_m4l40'
		crossSection = -1 # don't use this sample
	elif RunNumber ==  126401: 
		process = 'PowHegBoxZmmmm_Pythia_mll025_m4l40'
		crossSection = -1 # don't use this sample
	elif RunNumber ==  126859: 
		process = 'PowHegZZ_4e_trilep5GeV_Pythia'
		crossSection = 46.6
	elif RunNumber == 126860: 
		process = 'PowHegZZ_4mu_trilep5GeV_Pythia'
		crossSection = 46.6 
	elif RunNumber ==  126861: 
		process = 'PowHegZZ_2e2mu_trilep5GeV_Pythia'
		crossSection = 99.1 
	elif RunNumber ==  126862: 
		process = 'PowHegZZ_2mu2tau_trilep5GeV_Pythia'
		crossSection = 99.1 
	elif RunNumber ==  126863: 
		process = 'PowHegZZ_2e2tau_trilep5GeV_Pythia'
		crossSection = 99.1 
	elif RunNumber ==  126864: 
		process = 'PowHegZZ_4tau_trilep5GeV_Pythia'
		crossSection = 44.6 
	elif RunNumber ==  128813: 
		process = 'SherpaZZllll'
		crossSection = -1
	elif RunNumber ==  116600: 
		process = 'gg2ZZ_JIMMY_ZZ4lep [2e2mu,2e2tau,2mu2tau] (gg2ZZv2.0)'
		crossSection = -1 # don't use this sample - check 116601,116602,116603
	elif RunNumber ==  116601: 
		process = 'gg2ZZ_JIMMY_ZZ4lep [4e] (gg2ZZv2.0)'
		crossSection = 0.86 / 2.0
	elif RunNumber ==  116602: 
		process = 'gg2ZZ_JIMMY_ZZ4lep [4mu] (gg2ZZv2.0)'
		crossSection = 0.86 / 2.0
	elif RunNumber ==  116603: 
		process = 'gg2ZZ_JIMMY_ZZ4lep [2e2mu] (gg2ZZv2.0)'
		crossSection = 0.86
	elif RunNumber ==  128593: 
		process = 'PythiaZZall_EF_15_5'
		crossSection = -1
	elif RunNumber ==  109300: 
		process = 'AlpgenJimmyZeebbNp0_nofilter'
		crossSection = 6520 * 1.25 * 1.4
	elif RunNumber ==  109301: 
		process = 'AlpgenJimmyZeebbNp1_nofilter'
		crossSection = 2470 * 1.25 * 1.4
	elif RunNumber ==  109302: 
		process = 'AlpgenJimmyZeebbNp2_nofilter'
		crossSection = 880 * 1.25 * 1.4
	elif RunNumber ==  109303: 
		process = 'AlpgenJimmyZeebbNp3_nofilter'
		crossSection = 387 * 1.25 * 1.4
	elif RunNumber ==  109305: 
		process = 'AlpgenJimmyZmumubbNp0_nofilter'
		crossSection = 6520 * 1.25 * 1.4
	elif RunNumber ==  109306: 
		process = 'AlpgenJimmyZmumubbNp1_nofilter'
		crossSection = 2470 * 1.25 * 1.4
	elif RunNumber ==  109307: 
		process = 'AlpgenJimmyZmumubbNp2_nofilter'
		crossSection = 880 * 1.25 * 1.4
	elif RunNumber ==  109308: 
		process = 'AlpgenJimmyZmumubbNp3_nofilter'
		crossSection = 387 * 1.25 * 1.4
	elif RunNumber ==  109310: 
		process = 'AlpgenJimmyZtautaubbNp0_nofilter'
		crossSection = 6520 * 1.25 * 1.4
	elif RunNumber ==  109311: 
		process = 'AlpgenJimmyZtautaubbNp1_nofilter'
		crossSection = 2470 * 1.25 * 1.4
	elif RunNumber ==  109312: 
		process = 'AlpgenJimmyZtautaubbNp2_nofilter'
		crossSection = 880 * 1.25 * 1.4
	elif RunNumber ==  109313: 
		process = 'AlpgenJimmyZtautaubbNp3_nofilter'
		crossSection = 387 * 1.25 * 1.4
	elif RunNumber ==  116250: 
		process = 'ZeeNp0 M10to40 pt20'
		crossSection = 3051620 * 1.22
	elif RunNumber ==  116251: 
		process = 'ZeeNp1 M10to40 pt20'
		crossSection = 87870 * 1.22
	elif RunNumber ==  116252: 
		process = 'ZeeNp2 M10to40 pt20'
		crossSection = 41100 * 1.22
	elif RunNumber ==  116253: 
		process = 'ZeeNp3 M10to40 pt20'
		crossSection = 8460 * 1.22
	elif RunNumber ==  116254: 
		process = 'ZeeNp4 M10to40 pt20'
		crossSection = 1840 * 1.22
	elif RunNumber ==  116255: 
		process = 'ZeeNp5 M10to40 pt20'
		crossSection = 460 * 1.22
	elif RunNumber ==  116260: 
		process = 'ZmumuNp0 M10to40 pt20'
		crossSection = 3051620 * 1.22
	elif RunNumber ==  116261: 
		process = 'ZmumuNp1 M10to40 pt20'
		crossSection = 87870 * 1.22
	elif RunNumber ==  116262: 
		process = 'ZmumuNp2 M10to40 pt20'
		crossSection = 40950 * 1.22
	elif RunNumber ==  116263: 
		process = 'ZmumuNp3 M10to40 pt20'
		crossSection = 8410 * 1.22
	elif RunNumber ==  116264: 
		process = 'ZmumuNp4 M10to40 pt20'
		crossSection = 1850 * 1.22
	elif RunNumber ==  116265: 
		process = 'ZmumuNp5 M10to40 pt20'
		crossSection = 460 * 1.22
	elif RunNumber ==  116270: 
		process = 'ZtautauNp0 M10to40 pt20'
		crossSection = 3051620 * 1.22
	elif RunNumber ==  116271: 
		process = 'ZtautauNp1 M10to40 pt20'
		crossSection = 87870 * 1.22
	elif RunNumber ==  116272: 
		process = 'ZtautauNp2 M10to40 pt20'
		crossSection = 41100 * 1.22
	elif RunNumber ==  116273: 
		process = 'ZtautauNp3 M10to40 pt20'
		crossSection = 8460 * 1.22
	elif RunNumber ==  116274: 
		process = 'ZtautauNp4 M10to40 pt20'
		crossSection = 1840 * 1.22
	elif RunNumber ==  116275: 
		process = 'ZtautauNp5 M10to40 pt20'
		crossSection = 460 * 1.22
	elif RunNumber ==  128971: 
		process = 'PythiaWZ_inclusive'
		crossSection = 4190.0
	print('RunNumber: %d, Process: %s, Cross section x Branching Ratio: %f fb^-1' % (RunNumber, process, crossSection))

	return crossSection

#############################################################################

def GetBkgCrossSection8TeV(RunNumber):

	process = ''
	crossSection = -1.0
	
	if   RunNumber == 105200:
		process = 'McAtNloJimmy_CT10_ttbar_LeptonFilter'
		crossSection = 238.06e3 * 0.648
	elif RunNumber == 110001:
		process = 'McAtNloJimmy_CT10_ttbar_dilepton'
		crossSection = 238.06e3 * 0.1045
	elif RunNumber == 146369:
		process = 'ttbar_4LepMass_Mll50GeV12GeV'
		crossSection = 238.06e3 * 0.1045 * 0.0306
	elif RunNumber == 126937:
		process = 'PowhegPythia8_AU2CT10_ZZ_4e_mll4_2pt5'
		crossSection = 69.75
	elif RunNumber == 126938:
		process = 'PowhegPythia8_AU2CT10_ZZ_2e2mu_mll4_2pt5'
		crossSection = 145.37
	elif RunNumber == 126939:
		process = 'PowhegPythia8_AU2CT10_ZZ_2e2tau_mll4_2pt5'
		crossSection = 103.06
	elif RunNumber == 126940:
		process = 'PowhegPythia8_AU2CT10_ZZ_4mu_mll4_2pt5'
		crossSection = 69.75
	elif RunNumber == 126941:
		process = 'PowhegPythia8_AU2CT10_ZZ_2mu2tau_mll4_2pt5'
		crossSection = 103.06
	elif RunNumber == 126942:
		process = 'PowhegPythia8_AU2CT10_ZZ_4tau_mll4_2pt5'
		crossSection = 8.15
	elif RunNumber == 116601:
		process = 'gg2ZZJimmy_AUET2CT10_ZZ4e'
		crossSection = 1.14 / 2.0
	elif RunNumber == 116602:
		process = 'gg2ZZJimmy_AUET2CT10_ZZ4mu'
		crossSection = 1.14 / 2.0
	elif RunNumber == 116603:
		process = 'gg2ZZJimmy_AUET2CT10_ZZ2e2mu'
		crossSection = 1.14
	elif RunNumber == 107650:
		process = 'AlpgenJimmy_AUET2CTEQ6L1_ZeeNp0'
		crossSection = 712000. * 1.23
	elif RunNumber == 107651:
		process = 'AlpgenJimmy_AUET2CTEQ6L1_ZeeNp1'
		crossSection = 155000. * 1.23
	elif RunNumber == 107652:
		process = 'AlpgenJimmy_AUET2CTEQ6L1_ZeeNp2'
		crossSection = 48800. * 1.23
	elif RunNumber == 107653:
		process = 'AlpgenJimmy_AUET2CTEQ6L1_ZeeNp3'
		crossSection = 14200. * 1.23
	elif RunNumber == 107654:
		process = 'AlpgenJimmy_AUET2CTEQ6L1_ZeeNp4'
		crossSection = 3770. * 1.23
	elif RunNumber == 107655:
		process = 'AlpgenJimmy_AUET2CTEQ6L1_ZeeNp5'
		crossSection = 1120. * 1.23
	elif RunNumber == 107660:
		process = 'AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp0'
		crossSection = 712000. * 1.23
	elif RunNumber == 107661:
		process = 'AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp1'
		crossSection = 155000. * 1.23
	elif RunNumber == 107662:
		process = 'AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp2'
		crossSection = 48800. * 1.23
	elif RunNumber == 107663:
		process = 'AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp3'
		crossSection = 14200. * 1.23
	elif RunNumber == 107664:
		process = 'AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp4'
		crossSection = 3770. * 1.23
	elif RunNumber == 107665:
		process = 'AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp5'
		crossSection = 1120. * 1.23
	elif RunNumber == 107670:
		process = 'AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp0'
		crossSection = 712000. * 1.23
	elif RunNumber == 107671:
		process = 'AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp1'
		crossSection = 155000. * 1.23
	elif RunNumber == 107672:
		process = 'AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp2'
		crossSection = 48800. * 1.23
	elif RunNumber == 107673:
		process = 'AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp3'
		crossSection = 14200. * 1.23
	elif RunNumber == 107674:
		process = 'AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp4'
		crossSection = 3770. * 1.23
	elif RunNumber == 107675:
		process = 'AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp5'
		crossSection = 1120. * 1.23
	elif RunNumber == 147808:
		process = 'PowhegPythia8_AU2CT10_Ztautau'
		crossSection = 1.109e6 * 1.04
	elif RunNumber == 147807:
		process = 'PowhegPythia8_AU2CT10_Zmumu'
		crossSection = 1.109e6 * 1.04
	elif RunNumber == 147806:
		process = 'PowhegPythia8_AU2CT10_Zee'
		crossSection = 1.109e6 * 1.04

	print('RunNumber: %d, Process: %s, Cross section x Branching Ratio: %f fb^-1' % (RunNumber, process, crossSection))

	return crossSection

#############################################################################

