#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#############################################################################
# Author  : Jerome ODIER, Tiouchichine Elodie
# Email   : jerome.odier@cern.ch, elodie.tiouchihine@cern.ch
#
# Version : 1.0 (2011-2012)
#
#############################################################################

import math, ROOT, utils, atlas, array

Zmass = 91.1876

#############################################################################
# TZLTree								    #
#############################################################################

class TZLTree:
	#####################################################################

	def __init__(self, tree_ele, tree_mu):

		self.tree_ele = tree_ele

		#########################
		# Event			#
		#########################

		self.RunNumber_ele = utils.newArray('i', 1)
		self.tree_ele.SetBranchAddress('RunNumber', self.RunNumber_ele)
		self.EventNumber_ele = utils.newArray('i', 1)
		self.tree_ele.SetBranchAddress('EventNumber', self.EventNumber_ele)
		self.LumiBlock_ele = utils.newArray('i', 1)
		self.tree_ele.SetBranchAddress('LumiBlock', self.LumiBlock_ele)

		self.nPV2_ele = utils.newArray('i', 1)
		self.tree_ele.SetBranchAddress('nPV2', self.nPV2_ele)
		self.nIntPerXing_ele = utils.newArray('f', 1)
		self.tree_ele.SetBranchAddress('nIntPerXing', self.nIntPerXing_ele)

		self.elTrigger_ele = utils.newArray('i', 1)
		self.tree_ele.SetBranchAddress('elTrigger', self.elTrigger_ele)
		self.muTrigger_ele = utils.newArray('i', 1)
		self.tree_ele.SetBranchAddress('muTrigger', self.muTrigger_ele)

		#########################
		# Electrons		#
		#########################

		self.n_ele = utils.newArray('i', 1)
		self.tree_ele.SetBranchAddress('n', self.n_ele)

		self.weight1_ele = utils.newArray('f', 50)
		self.tree_ele.SetBranchAddress('weight1', self.weight1_ele)# poids mc
		self.weight2_ele = utils.newArray('f', 50)
		self.tree_ele.SetBranchAddress('weight2', self.weight2_ele)# pileupreweighting
		self.weight3_ele = utils.newArray('f', 50)
		self.tree_ele.SetBranchAddress('weight3', self.weight3_ele)# sf id + reco
		
		self.l_tight_ele = utils.newArray('i', 50)
		self.tree_ele.SetBranchAddress('l_tight', self.l_tight_ele)
		self.l_triggerMatch_ele = utils.newArray('i', 50)
		self.tree_ele.SetBranchAddress('l_triggerMatch', self.l_triggerMatch_ele)
		self.l_lepton_ele = utils.newArray('i', 50)
		self.tree_ele.SetBranchAddress('l_lepton', self.l_lepton_ele)

		self.l_charge_ele = utils.newArray('f', 50)
		self.tree_ele.SetBranchAddress('l_charge', self.l_charge_ele)
		self.l_e_ele = utils.newArray('f', 50)
		self.tree_ele.SetBranchAddress('l_e', self.l_e_ele)
		self.l_pt_ele = utils.newArray('f', 50)
		self.tree_ele.SetBranchAddress('l_pt', self.l_pt_ele)
		self.l_eta_ele = utils.newArray('f', 50)
		self.tree_ele.SetBranchAddress('l_eta', self.l_eta_ele)
		self.l_phi_ele = utils.newArray('f', 50)
		self.tree_ele.SetBranchAddress('l_phi', self.l_phi_ele)
		self.l_z0_ele = utils.newArray('f', 50)
		self.tree_ele.SetBranchAddress('l_z0', self.l_z0_ele)
		self.l_d0_ele = utils.newArray('f', 50)
		self.tree_ele.SetBranchAddress('l_d0', self.l_d0_ele)
		self.l_tkIso20_ele = utils.newArray('f', 50)
		self.tree_ele.SetBranchAddress('l_tkIso20', self.l_tkIso20_ele)
		self.l_clIso20_ele = utils.newArray('f', 50)
		self.tree_ele.SetBranchAddress('l_clIso20', self.l_clIso20_ele)
		self.l_d0sigma_ele = utils.newArray('f', 50)
		self.tree_ele.SetBranchAddress('l_d0sigma', self.l_d0sigma_ele)

		#self.l_f1_ele = utils.newArray('f', 50)
		#self.tree_ele.SetBranchAddress('l_f1', self.l_f1_ele)
		#self.l_rphi_ele = utils.newArray('f', 50)
		#self.tree_ele.SetBranchAddress('l_rphi', self.l_rphi_ele)
		self.l_nBlayerHits_ele = utils.newArray('i', 50)
		self.tree_ele.SetBranchAddress('l_nBlayerHits', self.l_nBlayerHits_ele)
		#self.l_nPixelHits_ele = utils.newArray('i', 50)
		#self.tree_ele.SetBranchAddress('l_nPixelHits', self.l_nPixelHits_ele)
		#self.l_rTRT_ele = utils.newArray('f', 50)
		#self.tree_ele.SetBranchAddress('l_rTRT', self.l_rTRT_ele)
		
		self.l_type_ele = utils.newArray('f', 50)
		self.tree_ele.SetBranchAddress('l_type', self.l_type_ele)
		self.l_origin_ele = utils.newArray('f', 50)
		self.tree_ele.SetBranchAddress('l_origin', self.l_origin_ele)
		self.l_typebkg_ele = utils.newArray('f', 50)
		self.tree_ele.SetBranchAddress('l_typebkg', self.l_typebkg_ele)
		self.l_originbkg_ele = utils.newArray('f', 50)
		self.tree_ele.SetBranchAddress('l_originbkg', self.l_originbkg_ele)
		self.l_truth_type_ele = utils.newArray('f', 50)
		self.tree_ele.SetBranchAddress('l_truth_type', self.l_truth_type_ele)

		self.l_tag_ele = utils.newArray('i', 50)
		
		#############################################################

		self.tree_mu = tree_mu

		#########################
		# Event			#
		#########################

		self.RunNumber_mu = utils.newArray('i', 1)
		self.tree_mu.SetBranchAddress('RunNumber', self.RunNumber_mu)
		self.EventNumber_mu = utils.newArray('i', 1)
		self.tree_mu.SetBranchAddress('EventNumber', self.EventNumber_mu)
		self.LumiBlock_mu = utils.newArray('i', 1)
		self.tree_mu.SetBranchAddress('LumiBlock', self.LumiBlock_mu)

		self.nPV2_mu = utils.newArray('i', 1)
		self.tree_mu.SetBranchAddress('nPV2', self.nPV2_mu)
		self.nIntPerXing_mu = utils.newArray('f', 1)
		self.tree_mu.SetBranchAddress('nIntPerXing', self.nIntPerXing_mu)

		self.elTrigger_mu = utils.newArray('i', 1)
		self.tree_mu.SetBranchAddress('elTrigger', self.elTrigger_mu)
		self.muTrigger_mu = utils.newArray('i', 1)
		self.tree_mu.SetBranchAddress('muTrigger', self.muTrigger_mu)

		#########################
		# Muons			#
		#########################

		self.n_mu = utils.newArray('i', 1)
		self.tree_mu.SetBranchAddress('n', self.n_mu)

		self.weight1_mu = utils.newArray('f', 50)
		self.tree_mu.SetBranchAddress('weight1', self.weight1_mu)# poids mc
		self.weight2_mu = utils.newArray('f', 50)
		self.tree_mu.SetBranchAddress('weight2', self.weight2_mu)# pileupreweighting
		self.weight3_mu = utils.newArray('f', 50)
		self.tree_mu.SetBranchAddress('weight3', self.weight3_mu)# sf id + reco
		
		self.l_tight_mu = utils.newArray('i', 50)
		self.tree_mu.SetBranchAddress('l_tight', self.l_tight_mu)
		self.l_triggerMatch_mu = utils.newArray('i', 50)
		self.tree_mu.SetBranchAddress('l_triggerMatch', self.l_triggerMatch_mu)
		self.l_lepton_mu = utils.newArray('i', 50)
		self.tree_mu.SetBranchAddress('l_lepton', self.l_lepton_mu)

		self.l_charge_mu = utils.newArray('f', 50)
		self.tree_mu.SetBranchAddress('l_charge', self.l_charge_mu)
		self.l_e_mu = utils.newArray('f', 50)
		self.tree_mu.SetBranchAddress('l_e', self.l_e_mu)
		self.l_pt_mu = utils.newArray('f', 50)
		self.tree_mu.SetBranchAddress('l_pt', self.l_pt_mu)
		self.l_eta_mu = utils.newArray('f', 50)
		self.tree_mu.SetBranchAddress('l_eta', self.l_eta_mu)
		self.l_phi_mu = utils.newArray('f', 50)
		self.tree_mu.SetBranchAddress('l_phi', self.l_phi_mu)
		self.l_z0_mu = utils.newArray('f', 50)
		self.tree_mu.SetBranchAddress('l_z0', self.l_z0_mu)
		self.l_d0_mu = utils.newArray('f', 50)
		self.tree_mu.SetBranchAddress('l_d0', self.l_d0_mu)
		self.l_tkIso20_mu = utils.newArray('f', 50)
		self.tree_mu.SetBranchAddress('l_tkIso20', self.l_tkIso20_mu)
		self.l_clIso20_mu = utils.newArray('f', 50)
		self.tree_mu.SetBranchAddress('l_clIso20', self.l_clIso20_mu)
		self.l_d0sigma_mu = utils.newArray('f', 50)
		self.tree_mu.SetBranchAddress('l_d0sigma', self.l_d0sigma_mu)

		#self.l_f1_mu = utils.newArray('f', 50)
		#self.tree_mu.SetBranchAddress('l_f1', self.l_f1_mu)
		#self.l_rphi_mu = utils.newArray('f', 50)
		#self.tree_mu.SetBranchAddress('l_rphi', self.l_rphi_mu)
		self.l_nBlayerHits_mu = utils.newArray('i', 50)
		self.tree_mu.SetBranchAddress('l_nBlayerHits', self.l_nBlayerHits_mu)
		#self.l_nPixelHits_mu = utils.newArray('i', 50)
		#self.tree_mu.SetBranchAddress('l_nPixelHits', self.l_nPixelHits_mu)
		#self.l_rTRT_mu = utils.newArray('f', 50)
		#self.tree_mu.SetBranchAddress('l_rTRT', self.l_rTRT_mu)
		
		#self.l_type_mu = utils.newArray('f', 50)
		#self.tree_mu.SetBranchAddress('l_type', self.l_type_mu)
		#self.l_origin_mu = utils.newArray('f', 50)
		#self.tree_mu.SetBranchAddress('l_origin', self.l_origin_mu)
		#self.l_typebkg_mu = utils.newArray('f', 50)
		#self.tree_mu.SetBranchAddress('l_typebkg', self.l_typebkg_mu)
		#self.l_originbkg_mu = utils.newArray('f', 50)
		#self.tree_mu.SetBranchAddress('l_originbkg', self.l_originbkg_mu)
		#self.l_truth_type_mu = utils.newArray('f', 50)
		#self.tree_mu.SetBranchAddress('l_truth_type', self.l_truth_type_mu)

		self.l_tag_mu = utils.newArray('i', 50)		

	#####################################################################

	def Loop(self, Year, mc_RunNumber, mc_weight, grl):

		eventNr1 = self.tree_ele.GetEntries()
		eventNr2 = self.tree_mu.GetEntries()

		if eventNr1 != eventNr2:
			print ('Oula!')
			return

		nZee = 0
		nZeeZee = 0
		nZeeZuu = 0

		nZeeN0e0u = 0

		nZeeN1e0u = 0
		nZeeN2e0u = 0
		nZeeN3e0u = 0

		nZeeN0e1u = 0
		nZeeN0e2u = 0
		nZeeN0e3u = 0

		nZeeN1e1u = 0
		nZeeN1e2u = 0
		nZeeN2e1u = 0

		# Tagged electron coming from Z when there is just one Z

		NeTagZee = 0 

		NeTagZee_CaloIsoOk = 0
		NeTagZee_TrkIsoOk = 0
		NeTagZee_d0Ok = 0
		NeTagZee_AllOk = 0

		# Additional electrons

		NeUntagZee = 0

		NeUntagZee_CaloIsoOk = 0
		NeUntagZee_TrkIsoOk = 0
		NeUntagZee_d0Ok = 0
		NeUntagZee_AllOk = 0

		# Additional muons

		NuUntagZee = 0

		NuUntagZee_CaloIsoOk = 0
		NuUntagZee_TrkIsoOk = 0
		NuUntagZee_d0Ok = 0
		NuUntagZee_AllOk = 0

		##########  Weighted counters ##########

		nZee_Weighted = 0
		nZeeZee_Weighted = 0
		nZeeZuu_Weighted = 0

		nZeeN0e0u_Weighted = 0

		nZeeN1e0u_Weighted = 0
		nZeeN2e0u_Weighted = 0
		nZeeN3e0u_Weighted = 0

		nZeeN0e1u_Weighted = 0
		nZeeN0e2u_Weighted = 0
		nZeeN0e3u_Weighted = 0

		nZeeN1e1u_Weighted = 0
		nZeeN1e2u_Weighted = 0
		nZeeN2e1u_Weighted = 0

		# Tagged electron from Z with one Z only

		NeTagZee_Weighted = 0 

		NeTagZee_CaloIsoOk_Weighted = 0
		NeTagZee_TrkIsoOk_Weighted = 0
		NeTagZee_d0Ok_Weighted = 0
		NeTagZee_AllOk_Weighted = 0

		# Additional electrons

		NeUntagZee_Weighted = 0

		NeUntagZee_CaloIsoOk_Weighted = 0
		NeUntagZee_TrkIsoOk_Weighted = 0
		NeUntagZee_d0Ok_Weighted = 0
		NeUntagZee_AllOk_Weighted = 0

		#Additional muons

		NuUntagZee_Weighted = 0

		NuUntagZee_CaloIsoOk_Weighted = 0
		NuUntagZee_TrkIsoOk_Weighted = 0
		NuUntagZee_d0Ok_Weighted = 0
		NuUntagZee_AllOk_Weighted = 0

		nZuu = 0
		nZuuZuu = 0
		nZuuZee = 0

		nZuuN0e0u = 0

		nZuuN1e0u = 0
		nZuuN2e0u = 0
		nZuuN3e0u = 0

		nZuuN0e1u = 0
		nZuuN0e2u = 0
		nZuuN0e3u = 0

		nZuuN1e1u = 0
		nZuuN2e1u = 0
		nZuuN1e2u = 0

		#Tagged muons coming from Z->uu when there is just one Z->uu
		NuTagZuu = 0

		NuTagZuu_CaloIsoOk = 0
		NuTagZuu_TrkIsoOk = 0
		NuTagZuu_d0Ok = 0
		NuTagZuu_AllOk = 0

		#Additional muons
		NuUntagZuu = 0

		NuUntagZuu_CaloIsoOk = 0
		NuUntagZuu_TrkIsoOk = 0
		NuUntagZuu_d0Ok = 0
		NuUntagZuu_AllOk = 0

		#Additional electrons 
		NeUntagZuu = 0

		NeUntagZuu_CaloIsoOk = 0
		NeUntagZuu_TrkIsoOk = 0
		NeUntagZuu_d0Ok = 0
		NeUntagZuu_AllOk = 0

		###########   Counter weighted ############

		nZuu_Weighted = 0
		nZuuZuu_Weighted = 0
		nZuuZee_Weighted = 0

		nZuuN0e0u_Weighted = 0

		nZuuN1e0u_Weighted = 0
		nZuuN2e0u_Weighted = 0
		nZuuN3e0u_Weighted = 0

		nZuuN0e1u_Weighted = 0
		nZuuN0e2u_Weighted = 0
		nZuuN0e3u_Weighted = 0

		nZuuN1e1u_Weighted = 0
		nZuuN2e1u_Weighted = 0
		nZuuN1e2u_Weighted = 0

		#Tagged muons coming from Z->uu when there is just one Z->uu
		NuTagZuu_Weighted = 0

		NuTagZuu_CaloIsoOk_Weighted = 0
		NuTagZuu_TrkIsoOk_Weighted = 0
		NuTagZuu_d0Ok_Weighted = 0
		NuTagZuu_AllOk_Weighted = 0

		#Additional muons
		NuUntagZuu_Weighted = 0

		NuUntagZuu_CaloIsoOk_Weighted = 0
		NuUntagZuu_TrkIsoOk_Weighted = 0
		NuUntagZuu_d0Ok_Weighted = 0
		NuUntagZuu_AllOk_Weighted = 0

		#Additional electrons 
		NeUntagZuu_Weighted = 0

		NeUntagZuu_CaloIsoOk_Weighted = 0
		NeUntagZuu_TrkIsoOk_Weighted = 0
		NeUntagZuu_d0Ok_Weighted = 0
		NeUntagZuu_AllOk_Weighted = 0
		############################################

		heTag_type = ROOT.TH1D('eTag_type', 'eTag_type', 23, 0, 23)
		heUntag_typeZee = ROOT.TH1D('eUntag_typeZee', 'eUntag_typeZee', 23, 0, 23)
		heUntag_typeZuu = ROOT.TH1D('eUntag_typeZuu', 'eUntag_typeZuu', 23, 0, 23)

		############################################
		# Z rate per period			   #
		############################################

		hZee_rate = ROOT.TH1D('Zee_rate', 'Zee_rate', 11, 0, 11)
		hZuu_rate = ROOT.TH1D('Zuu_rate', 'Zuu_rate', 11, 0, 11)

		############################################
		#Invariante mass of Z candidates ee and uu #
		############################################

		hMass_uu = ROOT.TH1F('hMass_uu', 'Mass_uu', 40, 70, 110)
		hMass_ee = ROOT.TH1F('hMass_ee', 'Mass_ee', 40, 70, 110)

		####################################
		# Additional leptons control plots #
		####################################

		hZeeEleUntag = ROOT.TH1F('hZeeEleUntag', 'ZeeEleUntag', 7, 0, 7)

		heUntagZee_eta = ROOT.TH1F('heUntagZee_eta', 'heUntagZee_eta', 540, -2.70, 2.70)
		heUntagZeeCaloIsoOk_eta = ROOT.TH1F('heUntagZeeCaloIsoOk_eta', 'heUntagZeeCaloIsoOk_eta', 540, -2.70, 2.70)
		heUntagZeeTrkIsoOk_eta = ROOT.TH1F('heUntagZeeTrkIsoOk_eta', 'heUntagZeeTrkIsoOk_eta', 540, -2.70, 2.70)
		heUntagZeed0Ok_eta = ROOT.TH1F('heUntagZeed0Ok_eta', 'heUntagZeed0Ok_eta', 540, -2.70, 2.70)
		heUntagZeeAllOk_eta = ROOT.TH1F('heUntagZeeAllOk_eta', 'heUntagZeeAllOk_eta', 540, -2.70, 2.70)

		heUntagZee_pt = ROOT.TH1F('heUntagZee_pt', 'heUntagZee_pt', 1000, 0, 1000)
		heUntagZeeCaloIsoOk_pt = ROOT.TH1F('heUntagZeeCaloIsoOk_pt', 'heUntagZeeCaloIsoOk_pt', 1000, 0, 1000)
		heUntagZeeTrkIsoOk_pt = ROOT.TH1F('heUntagZeeTrkIsoOk_pt', 'heUntagZeeTrkIsoOk_pt', 1000, 0, 1000)
		heUntagZeed0Ok_pt = ROOT.TH1F('heUntagZeed0Ok_pt', 'heUntagZeed0Ok_pt', 1000, 0, 1000)
		heUntagZeeAllOk_pt = ROOT.TH1F('heUntagZeeAllOk_pt', 'heUntagZeeAllOk_pt', 1000, 0, 1000)


		heUntagCrackZee_pt = ROOT.TH1F('heUntagCrackZee_pt', 'heUntagCrackZee_pt', 1000, 0, 1000)
		heUntagNoCrackZee_pt = ROOT.TH1F('heUntagNoCrackZee_pt', 'heUntagNoCrackZee_pt', 1000, 0, 1000)
		heUntagZee_phi = ROOT.TH1F('heUntagZee_phi', 'heUntagZee_phi', 20, -3.14, 3.14)
		heUntagZee_d0 = ROOT.TH1F('heUntagZee_d0', 'heUntagZee_d0', 20, -20, 20)
		heUntagZee_z0 = ROOT.TH1F('heUntagZee_z0', 'heUntagZee_z0', 20, -20, 20)
		heUntagZee_CaloIso = ROOT.TH1F('heUntagZee_CaloIso', 'heUntagZee_CaloIso', 100, -1, 1)
		heUntagZee_TrkIso = ROOT.TH1F('heUntagZee_TrkIso', 'heUntagZee_TrkIso', 100, -1, 1)
		heUntagZee_d0Sig = ROOT.TH1F('heUntagZee_d0Sig', 'heUntagZee_d0Sig', 30, 0,30)

		##

		hZeeMuUntag = ROOT.TH1F('hZeeMuUntag', 'ZeeMuUntag', 7, 0, 7)

		huUntagZee_eta = ROOT.TH1F('huUntagZee_eta', 'huUntagZee_eta', 540, -2.70, 2.70)
		huUntagZeeCaloIsoOk_eta = ROOT.TH1F('huUntagZeeCaloIsoOk_eta', 'huUntagZeeCaloIsoOk_eta', 540, -2.70, 2.70)
		huUntagZeeTrkIsoOk_eta = ROOT.TH1F('huUntagZeeTrkIsoOk_eta', 'huUntagZeeTrkIsoOk_eta', 540, -2.70, 2.70)
		huUntagZeed0Ok_eta = ROOT.TH1F('huUntagZeed0Ok_eta', 'huUntagZeed0Ok_eta', 540, -2.70, 2.70)
		huUntagZeeAllOk_eta = ROOT.TH1F('huUntagZeeAllOk_eta', 'huUntagZeeAllOk_eta', 540, -2.70, 2.70)

		huUntagZee_pt = ROOT.TH1F('huUntagZee_pt', 'huUntagZee_pt', 1000, 0, 1000)
		huUntagZeeCaloIsoOk_pt = ROOT.TH1F('huUntagZeeCaloIsoOk_pt', 'huUntagZeeCaloIsoOk_pt', 1000, 0, 1000)
		huUntagZeeTrkIsoOk_pt = ROOT.TH1F('huUntagZeeTrkIsoOk_pt', 'huUntagZeeTrkIsoOk_pt', 1000, 0, 1000)
		huUntagZeed0Ok_pt = ROOT.TH1F('huUntagZeed0Ok_pt', 'huUntagZeed0Ok_pt', 1000, 0, 1000)
		huUntagZeeAllOk_pt = ROOT.TH1F('huUntagZeeAllOk_pt', 'huUntagZeeAllOk_pt', 1000, 0, 1000)

		huUntagZee_phi = ROOT.TH1F('huUntagZee_phi', 'huUntagZee_phi', 20, -3.14, 3.14)
		huUntagZee_d0 = ROOT.TH1F('huUntagZee_d0', 'huUntagZee_d0', 20, -20, 20)
		huUntagZee_z0 = ROOT.TH1F('huUntagZee_z0', 'huUntagZee_z0', 20, -20, 20)
		huUntagZee_CaloIso = ROOT.TH1F('huUntagZee_CaloIso', 'huUntagZee_CaloIso', 100, -1, 1)
		huUntagZee_TrkIso = ROOT.TH1F('huUntagZee_TrkIso', 'huUntagZee_TrkIso', 100, -1, 1)
		huUntagZee_d0Sig = ROOT.TH1F('huUntagZee_d0Sig', 'huUntagZee_d0Sig', 30, 0,30)

		####################################
		# Z leptons control plots  	   #
		####################################

		heTagZee_phi = ROOT.TH1F('heTagZee_phi', 'heTagZee_phi', 20, -3.14, 3.14)
		heFEBMissingTagZee_phi = ROOT.TH1F('heFEBMissingTagZee_phi', 'heFEBMissingTagZee_phi', 20, -3.14, 3.14)
		heFEBRecoverTagZee_phi = ROOT.TH1F('heFEBRecoverTagZee_phi', 'heFEBRecoverTagZee_phi', 20, -3.14, 3.14)
		heTagZee_eta = ROOT.TH1F('heTagZee_eta', 'heTagZee_eta', 540, -2.70, 2.70)
		heTagZee_pt = ROOT.TH1F('heTagZee_pt', 'heTagZee_pt', 1000, 0, 1000)
		heTagZee_d0 = ROOT.TH1F('heTagZee_d0', 'heTagZee_d0', 20, -20, 20)
		heTagZee_z0 = ROOT.TH1F('heTagZee_z0', 'heTagZee_z0', 20, -20, 20)
		heTagZee_CaloIso = ROOT.TH1F('heTagZee_CaloIso', 'heTagZee_CaloIso', 100, -1, 1)
		heTagZee_TrkIso = ROOT.TH1F('heTagZee_TrkIso', 'heTagZee_TrkIso', 100, -1, 1)
		heTagZee_d0Sig = ROOT.TH1F('heTagZee_d0Sig', 'heTagZee_d0Sig', 30, 0,30)

		####################################
		#Additional leptons control plots  #
		####################################

		hZuuEleUntag = ROOT.TH1F('hZuuEleUntag', 'ZuuEleUntag', 7, 0, 7)

		heUntagZuu_eta = ROOT.TH1F('heUntagZuu_eta', 'heUntagZuu_eta', 540, -2.70, 2.70)
		heUntagZuuCaloIsoOk_eta = ROOT.TH1F('heUntagZuuCaloIsoOk_eta', 'heUntagZuuCaloIsoOk_eta', 540, -2.70, 2.70)
		heUntagZuuTrkIsoOk_eta = ROOT.TH1F('heUntagZuuTrkIsoOk_eta', 'heUntagZuuTrkIsoOk_eta',540, -2.70, 2.70)
		heUntagZuud0Ok_eta = ROOT.TH1F('heUntagZuud0Ok_eta', 'heUntagZuud0Ok_eta', 540, -2.70, 2.70)
		heUntagZuuAllOk_eta = ROOT.TH1F('heUntagZuuAllOk_eta', 'heUntagZuuAllOk_eta', 540, -2.70, 2.70)

		heUntagZuu_pt = ROOT.TH1F('heUntagZuu_pt', 'heUntagZuu_pt', 1000, 0, 1000)
		heUntagZuuCaloIsoOk_pt = ROOT.TH1F('heUntagZuuCaloIsoOk_pt', 'heUntagZuuCaloIsoOk_pt', 1000, 0, 1000)
		heUntagZuuTrkIsoOk_pt = ROOT.TH1F('heUntagZuuTrkIsoOk_pt', 'heUntagZuuTrkIsoOk_pt', 1000, 0, 1000)
		heUntagZuud0Ok_pt = ROOT.TH1F('heUntagZuud0Ok_pt', 'heUntagZuud0Ok_pt', 1000, 0, 1000)
		heUntagZuuAllOk_pt = ROOT.TH1F('heUntagZuuAllOk_pt', 'heUntagZuuAllOk_pt', 1000, 0, 1000)

		heUntagZuu_phi = ROOT.TH1F('heUntagZuu_phi', 'heUntagZuu_phi', 20, -3.14, 3.14)
		heUntagCrackZuu_pt = ROOT.TH1F('heUntagCrackZuu_pt', 'heUntagCrackZuu_pt', 1000, 0, 1000)
		heUntagNoCrackZuu_pt = ROOT.TH1F('heUntagNoCrackZuu_pt', 'heUntagNoCrackZuu_pt', 1000, 0, 1000)
		heUntagZuu_d0 = ROOT.TH1F('heUntagZuu_d0', 'heUntagZuu_d0', 20, -20, 20)
		heUntagZuu_z0 = ROOT.TH1F('heUntagZuu_z0', 'heUntagZuu_z0', 20, -20, 20)
		heUntagZuu_CaloIso = ROOT.TH1F('heUntagZuu_CaloIso', 'heUntagZuu_CaloIso', 20, -20, 20)
		heUntagZuu_TrkIso = ROOT.TH1F('heUntagZuu_TrkIso', 'heUntagZuu_TrkIso', 20, -20, 20)
		heUntagZuu_d0Sig = ROOT.TH1F('heUntagZuu_d0Sig', 'heUntagZuu_d0Sig', 30, 0,30)

		hZuuMuUntag = ROOT.TH1F('hZuuMuUntag', 'ZuuMuUntag', 7, 0, 7)

		huUntagZuu_eta = ROOT.TH1F('huUntagZuu_eta', 'huUntagZuu_eta', 540, -2.70, 2.70)
		huUntagZuuCaloIsoOk_eta = ROOT.TH1F('huUntagZuuCaloIsoOk_eta', 'huUntagZuuCaloIsoOk_eta', 540, -2.70, 2.70)
		huUntagZuuTrkIsoOk_eta = ROOT.TH1F('huUntagZuuTrkIsoOk_eta', 'huUntagZuuTrkIsoOk_eta',540, -2.70, 2.70)
		huUntagZuud0Ok_eta = ROOT.TH1F('huUntagZuud0Ok_eta', 'huUntagZuud0Ok_eta',540, -2.70, 2.70)
		huUntagZuuAllOk_eta = ROOT.TH1F('huUntagZuuAllOk_eta', 'huUntagZuuAllOk_eta',540, -2.70, 2.70)

		huUntagZuu_pt = ROOT.TH1F('huUntagZuu_pt', 'huUntagZuu_pt', 1000, 0, 1000)
		huUntagZuuCaloIsoOk_pt = ROOT.TH1F('huUntagZuuCaloIsoOk_pt', 'huUntagZuuCaloIsoOk_pt', 1000, 0, 1000)
		huUntagZuuTrkIsoOk_pt = ROOT.TH1F('huUntagZuuTrkIsoOk_pt', 'huUntagZuuTrkIsoOk_pt', 1000, 0, 1000)
		huUntagZuud0Ok_pt = ROOT.TH1F('huUntagZuud0Ok_pt', 'huUntagZuud0Ok_pt', 1000, 0, 1000)
		huUntagZuuAllOk_pt = ROOT.TH1F('huUntagZuuAllOk_pt', 'huUntagZuuAllOk_pt', 1000, 0, 1000)

		huUntagZuu_phi = ROOT.TH1F('huUntagZuu_phi', 'huUntagZuu_phi', 20, -3.14, 3.14)
		huUntagZuu_d0 = ROOT.TH1F('huUntagZuu_d0', 'huUntagZuu_d0', 20, -20, 20)
		huUntagZuu_z0 = ROOT.TH1F('huUntagZuu_z0', 'huUntagZuu_z0', 20, -20, 20)
		huUntagZuu_CaloIso = ROOT.TH1F('huUntagZuu_CaloIso', 'huUntagZuu_CaloIso', 20, -20, 20)
		huUntagZuu_TrkIso = ROOT.TH1F('huUntagZuu_TrkIso', 'huUntagZuu_TrkIso', 20, -20, 20)
		huUntagZuu_d0Sig = ROOT.TH1F('huUntagZuu_d0Sig', 'huUntagZuu_d0Sig', 30, 0,30)

		####################################
		#Z leptons control plots  	   #
		####################################

		huTagZuu_phi = ROOT.TH1F('huTagZuu_phi', 'huTagZuu_phi', 20, -3.14, 3.14)
		huTagZuu_eta = ROOT.TH1F('huTagZuu_eta', 'huTagZuu_eta',540, -2.70, 2.70)
		huTagZuu_pt = ROOT.TH1F('huTagZuu_pt', 'huTagZuu_pt', 1000, 0, 1000)

		for event in xrange(eventNr1):

			#####################################################

			if self.tree_ele.GetEntry(event) == 0:
				break
			if self.tree_mu.GetEntry(event) == 0:
				break

			#####################################################

			if mc_RunNumber < 0:
				if grl.check(self.RunNumber_ele[0], self.LumiBlock_ele[0]) == False:
					continue

			#####################################################

			for i in xrange(self.n_ele[0]):
				self.l_tag_ele[i] = 0
			for i in xrange(self.n_mu[0]):
				self.l_tag_mu[i] = 0

			#####################################################

			evt_weight = 0

			if self.n_ele[0] != 0:
 				evt_weight = mc_weight * self.weight1_ele[0] * self.weight2_ele[0]

			if self.n_mu[0] != 0:
				evt_weight = mc_weight * self.weight1_mu[0] * self.weight2_mu[0]

			#####################################################
			#	Count number of Z recontructed 		    #
			#	with independent electron		    #
			#####################################################

			ZeeEvtList=[]

			L_Zee = [] #List of 2 index and mass reconstructed between this two index
			I_Zee = [] #list of all the index implicated in the Z reconstructed

			for i in xrange(0 + 0, self.n_ele[0]):
				if utils.isLeptonPassCuts(2012, True, True, True, self.l_lepton_ele[i], self.l_clIso20_ele[i], self.l_tkIso20_ele[i], self.l_d0sigma_ele[i]) == False:
					continue

				for j in xrange(i + 1, self.n_ele[0]):
					if utils.isLeptonPassCuts(2012, True, True, True, self.l_lepton_ele[j], self.l_clIso20_ele[j], self.l_tkIso20_ele[j], self.l_d0sigma_ele[j]) == False:
						continue

					if (self.l_charge_ele[i] * self.l_charge_ele[j]) < 0 \
					    and \
					    (self.l_pt_ele[i] > 20000 and self.l_pt_ele[j] > 20000) \
					    and \
					    (self.l_triggerMatch_ele[i] > 0 or self.l_triggerMatch_ele[j] > 0)\
					    and \
					    (utils.dR(self.l_eta_ele[i], self.l_eta_ele[j], self.l_phi_ele[i], self.l_phi_ele[j]) > 0.1):
						pi = ROOT.TLorentzVector()
						pj = ROOT.TLorentzVector()
						pi.SetPtEtaPhiE(self.l_pt_ele[i], self.l_eta_ele[i], self.l_phi_ele[i], self.l_e_ele[i])
						pj.SetPtEtaPhiE(self.l_pt_ele[j], self.l_eta_ele[j], self.l_phi_ele[j], self.l_e_ele[j])
						z = pi + pj
						if math.fabs(z.M()/1000.0 - Zmass ) < 15:
							L_Zee.append([i, j, z.M()/1000.0])
							if not i in I_Zee:
								I_Zee.append(i)
							if not j in I_Zee:
								I_Zee.append(j)

			for l_index in xrange(len(I_Zee)):
				ZeebestMassR = 999999.0
				ZeebestIndex = 999999
				for z_index in xrange(len(L_Zee)):
					if self.l_tag_ele[L_Zee[z_index][0]] == 0\
					   and				     \
					   self.l_tag_ele[L_Zee[z_index][1]] == 0:
						if I_Zee[l_index] == L_Zee[z_index][0] or I_Zee[l_index] == L_Zee[z_index][1]:
							massR = math.fabs(Zmass - L_Zee[z_index][2])
							if massR < ZeebestMassR:
								ZeebestMassR = massR
								ZeebestIndex = z_index

				if ZeebestIndex != 999999:
					self.l_tag_ele[L_Zee[ZeebestIndex][0]] = 1
					self.l_tag_ele[L_Zee[ZeebestIndex][1]] = 1

					weight = self.weight3_ele[L_Zee[ZeebestIndex][0]] \
						* self.weight3_ele[L_Zee[ZeebestIndex][1]]

					ZeeEvtList.append(weight)
					hMass_ee.Fill(L_Zee[ZeebestIndex][2],evt_weight * weight)

					
					# IS DATA
					if mc_RunNumber < 0 and Year == 2011:
						if self.RunNumber_ele[0] >= 177986 and self.RunNumber_ele[0] <= 178109:
							hZee_rate.Fill(0,evt_weight * weight)
						if self.RunNumber_ele[0] >= 179710 and self.RunNumber_ele[0] <= 180481:
							hZee_rate.Fill(1,evt_weight * weight)
						if self.RunNumber_ele[0] >= 180614 and self.RunNumber_ele[0] <= 180776:
							hZee_rate.Fill(2,evt_weight * weight)
						if self.RunNumber_ele[0] >= 182013 and self.RunNumber_ele[0] <= 182519:
							hZee_rate.Fill(3,evt_weight * weight)
						if self.RunNumber_ele[0] >= 182726 and self.RunNumber_ele[0] <= 183462:
							hZee_rate.Fill(4,evt_weight * weight)
						if self.RunNumber_ele[0] >= 183544 and self.RunNumber_ele[0] <= 184169:
							hZee_rate.Fill(5,evt_weight * weight)
						if self.RunNumber_ele[0] >= 185353 and self.RunNumber_ele[0] <= 186493:
							hZee_rate.Fill(6,evt_weight * weight)
						if self.RunNumber_ele[0] >= 186516 and self.RunNumber_ele[0] <= 186755:
							hZee_rate.Fill(7,evt_weight * weight)
						if self.RunNumber_ele[0] >= 186873 and self.RunNumber_ele[0] <= 187815:
							hZee_rate.Fill(8,evt_weight * weight)
						if self.RunNumber_ele[0] >= 188902 and self.RunNumber_ele[0] <= 190343:
							hZee_rate.Fill(9,evt_weight * weight)
						if self.RunNumber_ele[0] >= 190503 and self.RunNumber_ele[0] <= 191933:
							hZee_rate.Fill(10,evt_weight * weight)

					# IS DATA
					if mc_RunNumber < 0 and Year == 2012:
						if self.RunNumber_ele[0] >= 200804 and self.RunNumber_ele[0] <= 201556:
							hZee_rate.Fill(0,evt_weight * weight)
						if self.RunNumber_ele[0] >= 202660 and self.RunNumber_ele[0] <= 205113:
							hZee_rate.Fill(1,evt_weight * weight)
						if self.RunNumber_ele[0] >= 206248 and self.RunNumber_ele[0] <= 207397:
							hZee_rate.Fill(2,evt_weight * weight)
						if self.RunNumber_ele[0] >= 207447 and self.RunNumber_ele[0] <= 209025:
							hZee_rate.Fill(3,evt_weight * weight)
						if self.RunNumber_ele[0] >= 209074 and self.RunNumber_ele[0] <= 210308:
							hZee_rate.Fill(4,evt_weight * weight)

					# IS MC
					if mc_RunNumber > 0 and Year == 2012:
							hZee_rate.Fill(0, evt_weight * weight / 5.0)
							hZee_rate.Fill(1, evt_weight * weight / 5.0)
							hZee_rate.Fill(2, evt_weight * weight / 5.0)
							hZee_rate.Fill(3, evt_weight * weight / 5.0)
							hZee_rate.Fill(4, evt_weight * weight / 5.0)



			#####################################################
			#	Count number of Z recontructed 		    #
			#	with independent mu			    #
			#####################################################

			ZuuEvtList = []

			L_Zuu = []
			I_Zuu = []

			for i in xrange(0 + 0, self.n_mu[0]):
				if utils.isLeptonPassCuts(2012, True, True, True, self.l_lepton_mu[i], self.l_clIso20_mu[i], self.l_tkIso20_mu[i], self.l_d0sigma_mu[i]) == False:
					continue

				for j in xrange(i + 1, self.n_mu[0]):
					if utils.isLeptonPassCuts(2012, True, True, True, self.l_lepton_mu[j], self.l_clIso20_mu[j], self.l_tkIso20_mu[j], self.l_d0sigma_mu[j]) == False:
						continue

					if (self.l_charge_mu[i] * self.l_charge_mu[j]) < 0 \
					    and \
					   (self.l_pt_mu[i] > 20000 and self.l_pt_mu[j] > 20000) \
					    and \
					   (self.l_triggerMatch_mu[i] > 0 or self.l_triggerMatch_mu[j] > 0)\
					    and \
					   (utils.dR(self.l_eta_mu[i], self.l_eta_mu[j], self.l_phi_mu[i], self.l_phi_mu[j]) > 0.1):
						pi = ROOT.TLorentzVector()
						pj = ROOT.TLorentzVector()
						pi.SetPtEtaPhiE(self.l_pt_mu[i], self.l_eta_mu[i], self.l_phi_mu[i], self.l_e_mu[i])
						pj.SetPtEtaPhiE(self.l_pt_mu[j], self.l_eta_mu[j], self.l_phi_mu[j], self.l_e_mu[j])
						z = pi + pj
						if math.fabs(z.M()/1000.0 - Zmass ) < 15:
							L_Zuu.append([i, j, z.M()/1000.0])
							if not i in I_Zuu:
								I_Zuu.append(i)
							if not j in I_Zuu:
								I_Zuu.append(j)

			for l_index in xrange(len(I_Zuu)):
				ZuubestMassR = 999999.0
				ZuubestIndex = 999999
				for z_index in xrange(len(L_Zuu)):
					if self.l_tag_mu[L_Zuu[z_index][0]] == 0\
					   and				     \
					   self.l_tag_mu[L_Zuu[z_index][1]] == 0:

						if I_Zuu[l_index] == L_Zuu[z_index][0] or I_Zuu[l_index] == L_Zuu[z_index][1]:
							massR = math.fabs(Zmass - L_Zuu[z_index][2])
							if massR < ZuubestMassR:
								ZuubestMassR = massR
								ZuubestIndex = z_index

				if ZuubestIndex != 999999:
					self.l_tag_mu[L_Zuu[ZuubestIndex][0]] = 1
					self.l_tag_mu[L_Zuu[ZuubestIndex][1]] = 1
					weight = self.weight3_mu[L_Zuu[ZuubestIndex][0]] \
						* self.weight3_mu[L_Zuu[ZuubestIndex][1]]

					ZuuEvtList.append(weight)
					hMass_uu.Fill(L_Zuu[ZuubestIndex][2],evt_weight * weight)
					
					# IS DATA
					if mc_RunNumber < 0 and Year == 2011:
						if self.RunNumber_ele[0] >= 177986 and self.RunNumber_ele[0] <= 178109:
							hZuu_rate.Fill(0,evt_weight * weight)
						if self.RunNumber_ele[0] >= 179710 and self.RunNumber_ele[0] <= 180481:
							hZuu_rate.Fill(1,evt_weight * weight)
						if self.RunNumber_ele[0] >= 180614 and self.RunNumber_ele[0] <= 180776:
							hZuu_rate.Fill(2,evt_weight * weight)
						if self.RunNumber_ele[0] >= 182013 and self.RunNumber_ele[0] <= 182519:
							hZuu_rate.Fill(3,evt_weight * weight)
						if self.RunNumber_ele[0] >= 182726 and self.RunNumber_ele[0] <= 183462:
							hZuu_rate.Fill(4,evt_weight * weight)
						if self.RunNumber_ele[0] >= 183544 and self.RunNumber_ele[0] <= 184169:
							hZuu_rate.Fill(5,evt_weight * weight)
						if self.RunNumber_ele[0] >= 185353 and self.RunNumber_ele[0] <= 186493:
							hZuu_rate.Fill(6,evt_weight * weight)
						if self.RunNumber_ele[0] >= 186516 and self.RunNumber_ele[0] <= 186755:
							hZuu_rate.Fill(7,evt_weight * weight)
						if self.RunNumber_ele[0] >= 186873 and self.RunNumber_ele[0] <= 187815:
							hZuu_rate.Fill(8,evt_weight * weight)
						if self.RunNumber_ele[0] >= 188902 and self.RunNumber_ele[0] <= 190343:
							hZuu_rate.Fill(9,evt_weight * weight)
						if self.RunNumber_ele[0] >= 190503 and self.RunNumber_ele[0] <= 191933:
							hZuu_rate.Fill(10,evt_weight * weight)

					# IS DATA
					if mc_RunNumber < 0 and Year == 2012:
						if self.RunNumber_ele[0] >= 200804 and self.RunNumber_ele[0] <= 201556:
							hZuu_rate.Fill(0,evt_weight * weight)
						if self.RunNumber_ele[0] >= 202660 and self.RunNumber_ele[0] <= 205113:
							hZuu_rate.Fill(1,evt_weight * weight)
						if self.RunNumber_ele[0] >= 206248 and self.RunNumber_ele[0] <= 207397:
							hZuu_rate.Fill(2,evt_weight * weight)
						if self.RunNumber_ele[0] >= 207447 and self.RunNumber_ele[0] <= 209025:
							hZuu_rate.Fill(3,evt_weight * weight)
						if self.RunNumber_ele[0] >= 209074 and self.RunNumber_ele[0] <= 210308:
							hZuu_rate.Fill(4,evt_weight * weight)

					# IS MC
					if mc_RunNumber > 0 and Year == 2012:
							hZuu_rate.Fill(0, evt_weight * weight / 5.0)
							hZuu_rate.Fill(1, evt_weight * weight / 5.0)
							hZuu_rate.Fill(2, evt_weight * weight / 5.0)
							hZuu_rate.Fill(3, evt_weight * weight / 5.0)
							hZuu_rate.Fill(4, evt_weight * weight / 5.0)


			#####################################################
			# If no Z reconstructed	continue		    #
			#####################################################

			if len(ZeeEvtList) == 0 and len(ZuuEvtList) == 0:
				continue

			#####################################################
			# Count number of lepton Untag in the event	    #
			#####################################################

			NeUntagEventWeighted = 0
			NuUntagEventWeighted = 0

			EleUntagPerEvtList = []
			MuUntagPerEvtList = []

			for i in xrange(0, self.n_ele[0]):
				if self.l_tag_ele[i] == 0:

					Nb_tag_ele = 0
					Nb_tag_ele_passDeltaR = 0
					for j in xrange(0, self.n_ele[0]):
						if self.l_tag_ele[j] == 1:
							Nb_tag_ele += 1
							if(utils.dR(self.l_eta_ele[i], self.l_eta_ele[j], self.l_phi_ele[i], self.l_phi_ele[j]) > 0.1):
								Nb_tag_ele_passDeltaR += 1

					Nb_tag_mu = 0
					Nb_tag_mu_passDeltaR = 0
					for j in xrange(0, self.n_mu[0]):
						if self.l_tag_mu[j] == 1:
							Nb_tag_mu += 1
							if(utils.dR(self.l_eta_ele[i], self.l_eta_mu[j], self.l_phi_ele[i], self.l_phi_mu[j]) > 0.2):
								Nb_tag_mu_passDeltaR += 1

					if(Nb_tag_ele == Nb_tag_ele_passDeltaR \
				  	   and \
				  	   Nb_tag_mu == Nb_tag_mu_passDeltaR):
						EleUntagPerEvtList.append(self.weight3_ele[i])

			for i in xrange(0, self.n_mu[0]):
				if self.l_tag_mu[i] == 0:
					Nb_tag_ele = 0
					Nb_tag_ele_passDeltaR = 0
					for j in xrange(0, self.n_ele[0]):
						if self.l_tag_ele[j] == 1:
							Nb_tag_ele += 1
							if(utils.dR(self.l_eta_mu[i], self.l_eta_ele[j], self.l_phi_mu[i], self.l_phi_ele[j]) > 0.2):
								Nb_tag_ele_passDeltaR += 1
					Nb_tag_mu = 0
					Nb_tag_mu_passDeltaR = 0
					for j in xrange(0, self.n_mu[0]):
						if self.l_tag_mu[j] == 1:
							Nb_tag_mu += 1
							if(utils.dR(self.l_eta_mu[i], self.l_eta_mu[j], self.l_phi_mu[i], self.l_phi_mu[j]) > 0.1):
								Nb_tag_mu_passDeltaR += 1

					if(Nb_tag_ele == Nb_tag_ele_passDeltaR \
				  	   and \
				  	   Nb_tag_mu == Nb_tag_mu_passDeltaR):
						MuUntagPerEvtList.append(self.weight3_mu[i])

			for w in EleUntagPerEvtList:
				NeUntagEventWeighted += w

			for w in MuUntagPerEvtList:
				NuUntagEventWeighted += w

			#####################################################
			# When we reconstruct exactly 1 Z->ee		    #
			#####################################################

			if len(ZeeEvtList) == 1 and len(ZuuEvtList) == 0:
				nZee += 1
				nZee_Weighted += evt_weight * ZeeEvtList[0]

				hZeeEleUntag.Fill(evt_weight * NeUntagEventWeighted * ZeeEvtList[0])
				hZeeMuUntag.Fill(evt_weight * NuUntagEventWeighted * ZeeEvtList[0])

				#############################################
				# electron coming from Z		    #
				#############################################

				for i in xrange(0, self.n_ele[0]):
					if self.l_tag_ele[i] == 1:
						weight = evt_weight * self.weight3_ele[i]

						NeTagZee += 1
						NeTagZee_Weighted += weight

						heTagZee_phi.Fill(self.l_phi_ele[i], weight)
						if self.RunNumber_ele[0] >= 180614 \
					 	  and \
					  	 self.RunNumber_ele[0] < 185353 : 
							heFEBMissingTagZee_phi.Fill(self.l_phi_ele[i], weight)
						else:
							heFEBRecoverTagZee_phi.Fill(self.l_phi_ele[i], weight)
						heTagZee_eta.Fill(self.l_eta_ele[i], weight)
						heTagZee_pt.Fill(self.l_pt_ele[i] / 1000.0, weight)
						heTagZee_d0.Fill(self.l_d0_ele[i], weight)
						heTagZee_z0.Fill(self.l_z0_ele[i], weight)
						heTagZee_CaloIso.Fill(self.l_clIso20_ele[i], weight)
						heTagZee_TrkIso.Fill(self.l_tkIso20_ele[i], weight)
						heTagZee_d0Sig.Fill(self.l_d0sigma_ele[i], weight)

						heTag_type.Fill(self.l_type_ele[i], weight)

						#####################
						# IsoCuts on Z ele  #
						#####################

						if utils.isLeptonPassCuts(2012, True, False, False, self.l_lepton_ele[i], self.l_clIso20_ele[i], self.l_tkIso20_ele[i], self.l_d0sigma_ele[i]) == True:
							NeTagZee_CaloIsoOk += 1
							NeTagZee_CaloIsoOk_Weighted += weight
						if utils.isLeptonPassCuts(2012, False, True, False, self.l_lepton_ele[i], self.l_clIso20_ele[i], self.l_tkIso20_ele[i], self.l_d0sigma_ele[i]) == True:
							NeTagZee_TrkIsoOk += 1
							NeTagZee_TrkIsoOk_Weighted += weight
						if utils.isLeptonPassCuts(2012, False, False, True, self.l_lepton_ele[i], self.l_clIso20_ele[i], self.l_tkIso20_ele[i], self.l_d0sigma_ele[i]) == True:
							NeTagZee_d0Ok += 1
							NeTagZee_d0Ok_Weighted += weight
						if utils.isLeptonPassCuts(2012, True, True, True, self.l_lepton_ele[i], self.l_clIso20_ele[i], self.l_tkIso20_ele[i], self.l_d0sigma_ele[i]) == True:
							NeTagZee_AllOk += 1
							NeTagZee_AllOk_Weighted += weight

				#############################################
				#############################################
				# There are electron Untag		    #
				#############################################
				#############################################

				if len(EleUntagPerEvtList) > 0:
					for i in xrange(0, self.n_ele[0]):
						if self.l_tag_ele[i] == 0:
							Nb_tag_ele = 0
							Nb_tag_ele_passDeltaR = 0
							for j in xrange(0, self.n_ele[0]):
								if self.l_tag_ele[j] == 1:
									Nb_tag_ele += 1
									if(utils.dR(self.l_eta_ele[i], self.l_eta_ele[j], self.l_phi_ele[i], self.l_phi_ele[j]) > 0.1):
										Nb_tag_ele_passDeltaR += 1
							if(Nb_tag_ele != Nb_tag_ele_passDeltaR): continue


							weight = evt_weight * ZeeEvtList[0] * self.weight3_ele[i]

							NeUntagZee += 1
							NeUntagZee_Weighted += weight

							heUntagZee_eta.Fill(self.l_eta_ele[i], weight)
							heUntagZee_pt.Fill(self.l_pt_ele[i] / 1000.0, weight)
							heUntagZee_phi.Fill(self.l_phi_ele[i], weight)

							if math.fabs(self.l_eta_ele[i]) <= 1.37\
							or					\
							math.fabs(self.l_eta_ele[i]) >= 1.52:
								heUntagNoCrackZee_pt.Fill(self.l_pt_ele[i] / 1000.0, weight)
							if math.fabs(self.l_eta_ele[i]) >= 1.37\
							and					\
							math.fabs(self.l_eta_ele[i]) <= 1.52:
								heUntagCrackZee_pt.Fill(self.l_pt_ele[i] / 1000.0, weight)

							heUntagZee_d0.Fill(self.l_d0_ele[i], weight)
							heUntagZee_z0.Fill(self.l_z0_ele[i], weight)
							heUntagZee_CaloIso.Fill(self.l_clIso20_ele[i], weight)
							heUntagZee_TrkIso.Fill(self.l_tkIso20_ele[i], weight)
							heUntagZee_d0Sig.Fill(self.l_d0sigma_ele[i], weight)

							heUntag_typeZee.Fill(self.l_type_ele[i], weight)

							#####################
							# IsoCuts add ele   #
							#####################

							if utils.isLeptonPassCuts(2012, True, False, False, self.l_lepton_ele[i], self.l_clIso20_ele[i], self.l_tkIso20_ele[i], self.l_d0sigma_ele[i]) == True:
								NeUntagZee_CaloIsoOk += 1
								NeUntagZee_CaloIsoOk_Weighted += weight
								heUntagZeeCaloIsoOk_eta.Fill(self.l_eta_ele[i], weight)
								heUntagZeeCaloIsoOk_pt.Fill(self.l_pt_ele[i] / 1000.0, weight)

							if utils.isLeptonPassCuts(2012, False, True, False, self.l_lepton_ele[i], self.l_clIso20_ele[i], self.l_tkIso20_ele[i], self.l_d0sigma_ele[i]) == True:
								NeUntagZee_TrkIsoOk += 1
								NeUntagZee_TrkIsoOk_Weighted += weight
								heUntagZeeTrkIsoOk_eta.Fill(self.l_eta_ele[i], weight)
								heUntagZeeTrkIsoOk_pt.Fill(self.l_pt_ele[i] / 1000.0, weight)
							if utils.isLeptonPassCuts(2012, False, False, True, self.l_lepton_ele[i], self.l_clIso20_ele[i], self.l_tkIso20_ele[i], self.l_d0sigma_ele[i]) == True:
								NeUntagZee_d0Ok += 1
								NeUntagZee_d0Ok_Weighted += weight
								heUntagZeed0Ok_eta.Fill(self.l_eta_ele[i], weight)
								heUntagZeed0Ok_pt.Fill(self.l_pt_ele[i] / 1000.0, weight)
							if utils.isLeptonPassCuts(2012, True, True, True, self.l_lepton_ele[i], self.l_clIso20_ele[i], self.l_tkIso20_ele[i], self.l_d0sigma_ele[i]) == True:
								NeUntagZee_AllOk += 1
								NeUntagZee_AllOk_Weighted += weight
								heUntagZeeAllOk_eta.Fill(self.l_eta_ele[i], weight)
								heUntagZeeAllOk_pt.Fill(self.l_pt_ele[i] / 1000.0, weight)
				#############################################
				# There are muon Untag			    #
				#############################################

				if len(MuUntagPerEvtList) > 0:
					for i in xrange(0, self.n_mu[0]):
						if self.l_tag_mu[i] == 0:

							Nb_tag_ele = 0
							Nb_tag_ele_passDeltaR = 0
							for j in xrange(0, self.n_ele[0]):
								if self.l_tag_ele[j] == 1:
									Nb_tag_ele += 1
									if(utils.dR(self.l_eta_mu[i], self.l_eta_ele[j], self.l_phi_mu[i], self.l_phi_ele[j]) > 0.2):
										Nb_tag_ele_passDeltaR += 1
							if(Nb_tag_ele != Nb_tag_ele_passDeltaR): continue

							weight = evt_weight * ZeeEvtList[0] * self.weight3_mu[i] 

							NuUntagZee += 1
							NuUntagZee_Weighted += weight
							huUntagZee_phi.Fill(self.l_phi_mu[i], weight)
							huUntagZee_eta.Fill(self.l_eta_mu[i], weight)
							huUntagZee_pt.Fill(self.l_pt_mu[i] / 1000.0, weight)
							huUntagZee_d0.Fill(self.l_d0_mu[i], weight)
							huUntagZee_z0.Fill(self.l_z0_mu[i], weight)
							huUntagZee_CaloIso.Fill(self.l_clIso20_mu[i], weight)
							huUntagZee_TrkIso.Fill(self.l_tkIso20_mu[i], weight)
							huUntagZee_d0Sig.Fill(self.l_d0sigma_mu[i], weight)

							#####################
							# IsoCuts on mu add#
							#####################

							if utils.isLeptonPassCuts(2012, True, False, False, self.l_lepton_mu[i], self.l_clIso20_mu[i], self.l_tkIso20_mu[i], self.l_d0sigma_mu[i]) == True:
								NuUntagZee_CaloIsoOk += 1
								NuUntagZee_CaloIsoOk_Weighted += weight
								huUntagZeeCaloIsoOk_eta.Fill(self.l_eta_mu[i], weight)
								huUntagZeeCaloIsoOk_pt.Fill(self.l_pt_mu[i] / 1000.0, weight)
							if utils.isLeptonPassCuts(2012, False, True, False, self.l_lepton_mu[i], self.l_clIso20_mu[i], self.l_tkIso20_mu[i], self.l_d0sigma_mu[i]) == True:
								NuUntagZee_TrkIsoOk += 1
								NuUntagZee_TrkIsoOk_Weighted += weight
								huUntagZeeTrkIsoOk_eta.Fill(self.l_eta_mu[i], weight)
								huUntagZeeTrkIsoOk_pt.Fill(self.l_pt_mu[i] / 1000.0, weight)
							if utils.isLeptonPassCuts(2012, False, False, True, self.l_lepton_mu[i], self.l_clIso20_mu[i], self.l_tkIso20_mu[i], self.l_d0sigma_mu[i]) == True:
								NuUntagZee_d0Ok += 1
								NuUntagZee_d0Ok_Weighted += weight
								huUntagZeed0Ok_eta.Fill(self.l_eta_mu[i], weight)
								huUntagZeed0Ok_pt.Fill(self.l_pt_mu[i] / 1000.0, weight)

							if utils.isLeptonPassCuts(2012, True, True, True, self.l_lepton_mu[i], self.l_clIso20_mu[i], self.l_tkIso20_mu[i], self.l_d0sigma_mu[i]) == True:
								NuUntagZee_AllOk += 1
								NuUntagZee_AllOk_Weighted += weight
								huUntagZeeAllOk_eta.Fill(self.l_eta_mu[i], weight)
								huUntagZeeAllOk_pt.Fill(self.l_pt_mu[i] / 1000.0, weight)

				#############################################

				if len(EleUntagPerEvtList) == 0 and len(MuUntagPerEvtList) == 0:
					nZeeN0e0u += 1
					nZeeN0e0u_Weighted += evt_weight * ZeeEvtList[0]
				##

				if len(EleUntagPerEvtList) == 1 and len(MuUntagPerEvtList) == 0:
					nZeeN1e0u += 1
					nZeeN1e0u_Weighted += evt_weight * ZeeEvtList[0] * EleUntagPerEvtList[0]
				##

				if len(EleUntagPerEvtList) == 2 and len(MuUntagPerEvtList) == 0:
					nZeeN2e0u += 1
					nZeeN2e0u_Weighted += evt_weight * ZeeEvtList[0] * EleUntagPerEvtList[0] * EleUntagPerEvtList[1]
				##

				if len(EleUntagPerEvtList) >= 3 and len(MuUntagPerEvtList) == 0:
					nZeeN3e0u += 1
					nZeeN3e0u_Weighted += evt_weight * ZeeEvtList[0] * EleUntagPerEvtList[0] * EleUntagPerEvtList[1] * EleUntagPerEvtList[2]
				##

				if len(MuUntagPerEvtList) == 1 and len(EleUntagPerEvtList) == 0:
					nZeeN0e1u += 1
					nZeeN0e1u_Weighted += evt_weight * ZeeEvtList[0] * MuUntagPerEvtList[0]
				##

				if len(MuUntagPerEvtList) == 2 and len(EleUntagPerEvtList) == 0:
					nZeeN0e2u += 1
					nZeeN0e2u_Weighted += evt_weight * ZeeEvtList[0] * MuUntagPerEvtList[0] * MuUntagPerEvtList[1]
				##

				if len(MuUntagPerEvtList) >= 3 and len(EleUntagPerEvtList) == 0:
					nZeeN0e3u += 1
					nZeeN0e3u_Weighted += evt_weight * ZeeEvtList[0] * MuUntagPerEvtList[0] * MuUntagPerEvtList[1] * MuUntagPerEvtList[2]
				##

				if len(MuUntagPerEvtList) == 1 and len(EleUntagPerEvtList) == 1:
					nZeeN1e1u += 1
					nZeeN1e1u_Weighted += evt_weight * ZeeEvtList[0] * EleUntagPerEvtList[0] * MuUntagPerEvtList[0]
				##

				if len(MuUntagPerEvtList) == 1 and len(EleUntagPerEvtList) == 2:
					nZeeN2e1u += 1
					nZeeN2e1u_Weighted += evt_weight * ZeeEvtList[0] * EleUntagPerEvtList[0] * EleUntagPerEvtList[1] * MuUntagPerEvtList[0]
				##

				if len(MuUntagPerEvtList) == 2 and len(EleUntagPerEvtList) == 1:
					nZeeN1e2u += 1
					nZeeN1e2u_Weighted += evt_weight * ZeeEvtList[0] * EleUntagPerEvtList[0] * MuUntagPerEvtList[0] * MuUntagPerEvtList[1]


			#####################################################
			# When we reconstruct exactly 1 Z->uu		    #
			#####################################################
			if len(ZuuEvtList) == 1 and len(ZeeEvtList) == 0:
				nZuu += 1
				nZuu_Weighted += evt_weight * ZuuEvtList[0]

				hZuuEleUntag.Fill(evt_weight * ZuuEvtList[0] * NeUntagEventWeighted)
				hZuuMuUntag.Fill(evt_weight * ZuuEvtList[0] * NuUntagEventWeighted)

				#############################################
				# muons coming from Z			    #
				#############################################

				for i in xrange(0, self.n_mu[0]):
					if self.l_tag_mu[i] == 1:
						weight = evt_weight * self.weight3_mu[i] 

						NuTagZuu += 1
						NuTagZuu_Weighted += weight
						huTagZuu_phi.Fill(self.l_phi_mu[i], weight)
						huTagZuu_eta.Fill(self.l_eta_mu[i], weight)
						huTagZuu_pt.Fill(self.l_pt_mu[i] / 1000.0, weight)

						#####################
						# IsoCuts on Z mu   #
						#####################

						if utils.isLeptonPassCuts(2012, True, False, False, self.l_lepton_mu[i], self.l_clIso20_mu[i], self.l_tkIso20_mu[i], self.l_d0sigma_mu[i]) == True:
							NuTagZuu_CaloIsoOk += 1
							NuTagZuu_CaloIsoOk_Weighted += weight
						if utils.isLeptonPassCuts(2012, False, True, False, self.l_lepton_mu[i], self.l_clIso20_mu[i], self.l_tkIso20_mu[i], self.l_d0sigma_mu[i]) == True:
							NuTagZuu_TrkIsoOk += 1
							NuTagZuu_TrkIsoOk_Weighted += weight
						if utils.isLeptonPassCuts(2012, False, False, True, self.l_lepton_mu[i], self.l_clIso20_mu[i], self.l_tkIso20_mu[i], self.l_d0sigma_mu[i]) == True:
							NuTagZuu_d0Ok += 1
							NuTagZuu_d0Ok_Weighted += weight

						if utils.isLeptonPassCuts(2012, True, True, True, self.l_lepton_mu[i], self.l_clIso20_mu[i], self.l_tkIso20_mu[i], self.l_d0sigma_mu[i]) == True:
							NuTagZuu_AllOk += 1
							NuTagZuu_AllOk_Weighted += weight

				#############################################
				# There are electron Untag		    #
				#############################################
				if len(EleUntagPerEvtList) > 0:
					for i in xrange(0, self.n_ele[0]):
						if self.l_tag_ele[i] == 0:

							Nb_tag_mu = 0
							Nb_tag_mu_passDeltaR = 0
							for j in xrange(0, self.n_mu[0]):
								if self.l_tag_mu[j] == 1:
									Nb_tag_mu += 1
									if(utils.dR(self.l_eta_ele[i], self.l_eta_mu[j], self.l_phi_ele[i], self.l_phi_mu[j]) > 0.2):
										Nb_tag_mu_passDeltaR += 1
							if(Nb_tag_mu != Nb_tag_mu_passDeltaR): continue

							weight = evt_weight * ZuuEvtList[0] * self.weight3_ele[i]
							NeUntagZuu += 1
							NeUntagZuu_Weighted += weight

							heUntagZuu_phi.Fill(self.l_phi_ele[i], weight)
							heUntagZuu_eta.Fill(self.l_eta_ele[i], weight)
							heUntagZuu_pt.Fill(self.l_pt_ele[i] / 1000.0, weight)

							if math.fabs(self.l_eta_ele[i]) <= 1.37\
						 	  or					\
						 	  math.fabs(self.l_eta_ele[i]) >= 1.52:
								heUntagNoCrackZuu_pt.Fill(self.l_pt_ele[i] / 1000.0, weight)
							if math.fabs(self.l_eta_ele[i]) >= 1.37\
						  	 and					\
						  	 math.fabs(self.l_eta_ele[i]) <= 1.52:
								heUntagCrackZuu_pt.Fill(self.l_pt_ele[i] / 1000.0, weight)

							heUntagZuu_d0.Fill(self.l_d0_ele[i], weight)
							heUntagZuu_z0.Fill(self.l_z0_ele[i], weight)
							heUntagZuu_CaloIso.Fill(self.l_clIso20_ele[i], weight)
							heUntagZuu_TrkIso.Fill(self.l_tkIso20_ele[i], weight)
							heUntagZuu_d0Sig.Fill(self.l_d0sigma_ele[i], weight)

							heUntag_typeZuu.Fill(self.l_type_ele[i], weight)

							#####################
							# IsoCuts Add ele   #
							#####################

							if utils.isLeptonPassCuts(2012, True, False, False, self.l_lepton_ele[i], self.l_clIso20_ele[i], self.l_tkIso20_ele[i], self.l_d0sigma_ele[i]) == True:
								NeUntagZuu_CaloIsoOk += 1
								NeUntagZuu_CaloIsoOk_Weighted += weight
								heUntagZuuCaloIsoOk_eta.Fill(self.l_eta_ele[i], weight)
								heUntagZuuCaloIsoOk_pt.Fill(self.l_pt_ele[i] / 1000.0, weight)
							if utils.isLeptonPassCuts(2012, False, True, False, self.l_lepton_ele[i], self.l_clIso20_ele[i], self.l_tkIso20_ele[i], self.l_d0sigma_ele[i]) == True:
								NeUntagZuu_TrkIsoOk += 1
								NeUntagZuu_TrkIsoOk_Weighted += weight
								heUntagZuuTrkIsoOk_eta.Fill(self.l_eta_ele[i], weight)
								heUntagZuuTrkIsoOk_pt.Fill(self.l_pt_ele[i] / 1000.0, weight)
							if utils.isLeptonPassCuts(2012, False, False, True, self.l_lepton_ele[i], self.l_clIso20_ele[i], self.l_tkIso20_ele[i], self.l_d0sigma_ele[i]) == True:
								NeUntagZuu_d0Ok += 1
								NeUntagZuu_d0Ok_Weighted += weight
								heUntagZuud0Ok_eta.Fill(self.l_eta_ele[i], weight)
								heUntagZuud0Ok_pt.Fill(self.l_pt_ele[i] / 1000.0, weight)
							if utils.isLeptonPassCuts(2012, True, True, True, self.l_lepton_ele[i], self.l_clIso20_ele[i], self.l_tkIso20_ele[i], self.l_d0sigma_ele[i]) == True:
								NeUntagZuu_AllOk += 1
								NeUntagZuu_AllOk_Weighted += weight
								heUntagZuuAllOk_eta.Fill(self.l_eta_ele[i], weight)
								heUntagZuuAllOk_pt.Fill(self.l_pt_ele[i] / 1000.0, weight)

				#############################################
				# There are muon Untag			    #
				#############################################
				if len(MuUntagPerEvtList) > 0:
					for i in xrange(0, self.n_mu[0]):
						if self.l_tag_mu[i] == 0:

							Nb_tag_mu = 0
							Nb_tag_mu_passDeltaR = 0
							for j in xrange(0, self.n_mu[0]):
								if self.l_tag_mu[j] == 1:
									Nb_tag_mu += 1
									if(utils.dR(self.l_eta_mu[i], self.l_eta_mu[j], self.l_phi_mu[i], self.l_phi_mu[j]) > 0.1):
										Nb_tag_mu_passDeltaR += 1
							if(Nb_tag_mu != Nb_tag_mu_passDeltaR): continue
							weight = evt_weight * ZuuEvtList[0] * self.weight3_mu[i] 

							NuUntagZuu += 1
							NuUntagZuu_Weighted += weight

							huUntagZuu_phi.Fill(self.l_phi_mu[i], weight)
							huUntagZuu_eta.Fill(self.l_eta_mu[i], weight)
							huUntagZuu_pt.Fill(self.l_pt_mu[i] / 1000.0, weight)
							huUntagZuu_d0.Fill(self.l_d0_mu[i], weight)
							huUntagZuu_z0.Fill(self.l_z0_mu[i], weight)
							huUntagZuu_CaloIso.Fill(self.l_clIso20_mu[i], weight)
							huUntagZuu_TrkIso.Fill(self.l_tkIso20_mu[i], weight)
							huUntagZuu_d0Sig.Fill(self.l_d0sigma_mu[i], weight)

							#####################
							# IsoCuts Add mu    #
							#####################

							if utils.isLeptonPassCuts(2012, True, False, False, self.l_lepton_mu[i], self.l_clIso20_mu[i], self.l_tkIso20_mu[i], self.l_d0sigma_mu[i]) == True:
								NuUntagZuu_CaloIsoOk += 1
								NuUntagZuu_CaloIsoOk_Weighted += weight
								huUntagZuuCaloIsoOk_eta.Fill(self.l_eta_mu[i], weight)
								huUntagZuuCaloIsoOk_pt.Fill(self.l_pt_mu[i] / 1000.0, weight)
							if utils.isLeptonPassCuts(2012, False, True, False, self.l_lepton_mu[i], self.l_clIso20_mu[i], self.l_tkIso20_mu[i], self.l_d0sigma_mu[i]) == True:
								NuUntagZuu_TrkIsoOk += 1
								NuUntagZuu_TrkIsoOk_Weighted += weight
								huUntagZuuTrkIsoOk_eta.Fill(self.l_eta_mu[i], weight)
								huUntagZuuTrkIsoOk_pt.Fill(self.l_pt_mu[i] / 1000.0, weight)
							if utils.isLeptonPassCuts(2012, False, False, True, self.l_lepton_mu[i], self.l_clIso20_mu[i], self.l_tkIso20_mu[i], self.l_d0sigma_mu[i]) == True:
								NuUntagZuu_d0Ok += 1
								NuUntagZuu_d0Ok_Weighted += weight
								huUntagZuud0Ok_eta.Fill(self.l_eta_mu[i], weight)
								huUntagZuud0Ok_pt.Fill(self.l_pt_mu[i] / 1000.0, weight)

							if utils.isLeptonPassCuts(2012, True, True, True, self.l_lepton_mu[i], self.l_clIso20_mu[i], self.l_tkIso20_mu[i], self.l_d0sigma_mu[i]) == True:
								NuUntagZuu_AllOk += 1
								NuUntagZuu_AllOk_Weighted += weight
								huUntagZuuAllOk_eta.Fill(self.l_eta_mu[i], weight)
								huUntagZuuAllOk_pt.Fill(self.l_pt_mu[i] / 1000.0, weight)

				#############################################

				if len(EleUntagPerEvtList) == 0 and len(MuUntagPerEvtList) == 0:
					nZuuN0e0u += 1
					nZuuN0e0u_Weighted += evt_weight * ZuuEvtList[0]
				##

				if len(EleUntagPerEvtList) == 1 and len(MuUntagPerEvtList) == 0:
					nZuuN1e0u += 1
					nZuuN1e0u_Weighted += evt_weight * ZuuEvtList[0] * EleUntagPerEvtList[0]
				##

				if len(EleUntagPerEvtList) == 2 and len(MuUntagPerEvtList) == 0:
					nZuuN2e0u += 1
					nZuuN2e0u_Weighted += evt_weight * ZuuEvtList[0] * EleUntagPerEvtList[0] * EleUntagPerEvtList[1]
				##

				if len(EleUntagPerEvtList) >= 3 and len(MuUntagPerEvtList) == 0:
					nZuuN3e0u += 1
					nZuuN3e0u_Weighted += evt_weight * ZuuEvtList[0] * EleUntagPerEvtList[0] * EleUntagPerEvtList[1] * EleUntagPerEvtList[2]
				##

				if len(EleUntagPerEvtList) == 0 and len(MuUntagPerEvtList) == 1:
					nZuuN0e1u += 1
					nZuuN0e1u_Weighted += evt_weight * ZuuEvtList[0] * MuUntagPerEvtList[0]
				##

				if len(EleUntagPerEvtList) == 0 and len(MuUntagPerEvtList) == 2:
					nZuuN0e2u += 1
					nZuuN0e2u_Weighted += evt_weight * ZuuEvtList[0] * MuUntagPerEvtList[0] * MuUntagPerEvtList[1]
				##

				if len(EleUntagPerEvtList) == 0 and len(MuUntagPerEvtList) >= 3:
					nZuuN0e3u += 1
					nZuuN0e3u_Weighted += evt_weight * ZuuEvtList[0] * MuUntagPerEvtList[0] * MuUntagPerEvtList[1] * MuUntagPerEvtList[2]
				##

				if len(EleUntagPerEvtList) == 1 and len(MuUntagPerEvtList) == 1:
					nZuuN1e1u += 1
					nZuuN1e1u_Weighted += evt_weight * ZuuEvtList[0] * EleUntagPerEvtList[0] * MuUntagPerEvtList[0]
				##

				if len(EleUntagPerEvtList) == 2 and len(MuUntagPerEvtList) == 1:
					nZuuN2e1u += 1
					nZuuN2e1u_Weighted += evt_weight * ZuuEvtList[0] * EleUntagPerEvtList[0] * EleUntagPerEvtList[1] * MuUntagPerEvtList[0]
				##

				if len(EleUntagPerEvtList) == 1 and len(MuUntagPerEvtList) == 2:
					nZuuN1e2u += 1
					nZuuN1e2u_Weighted += evt_weight * ZuuEvtList[0] * EleUntagPerEvtList[0] * MuUntagPerEvtList[0] * MuUntagPerEvtList[1]


			#####################################################
			# When we reconstruct exactly 2 Z->ee		    #
			#####################################################

			if len(ZeeEvtList) == 2 and len(ZuuEvtList) == 0:
				nZeeZee += 1
				nZeeZee_Weighted += evt_weight * ZeeEvtList[0] * ZeeEvtList[1]

			#####################################################
			# When we reconstruct exactly 2 Z->uu		    #
			#####################################################
			if len(ZuuEvtList) == 2 and len(ZeeEvtList) == 0:
				nZuuZuu += 1
				nZuuZuu_Weighted += evt_weight * ZuuEvtList[0] * ZuuEvtList[1]

			#####################################################
			# When we reconstruct exactly 1 Z->ee and 1 Z->uu   #
			#####################################################

			if len(ZeeEvtList) == 1 and len(ZuuEvtList) == 1:
				nZeeZuu += 1
				nZeeZuu_Weighted += evt_weight * ZeeEvtList[0] * ZuuEvtList[0]

		#############################################################

		#f = ROOT.TFile('output/%d/Zee_DATA.root' %Year, 'RECREATE')
		f = ROOT.TFile('output/%d/Zuu_DATA.root' %Year, 'RECREATE')

		#f = ROOT.TFile('output/%d/Zee_MC_%d.root' %(Year, mc_RunNumber), 'RECREATE')
		#f = ROOT.TFile('output/%d/Zuu_MC_%d.root' %(Year, mc_RunNumber), 'RECREATE')


		#f = ROOT.TFile('output/%d/Z_MC_%d.root' %(Year, mc_RunNumber), 'RECREATE')

		#f = ROOT.TFile('output/test.root', 'RECREATE')
		f.cd()

		tree = ROOT.TTree('result', 'result')

		dic = {
			'nZee_Weighted': nZee_Weighted,
			'nZeeZee_Weighted': nZeeZee_Weighted,
			'nZeeZuu_Weighted': nZeeZuu_Weighted,
			'nZeeN0e0u_Weighted': nZeeN0e0u_Weighted,
			'nZeeN1e0u_Weighted': nZeeN1e0u_Weighted,
			'nZeeN2e0u_Weighted': nZeeN2e0u_Weighted,
			'nZeeN3e0u_Weighted': nZeeN3e0u_Weighted,
			'nZeeN0e1u_Weighted': nZeeN0e1u_Weighted,
			'nZeeN0e2u_Weighted': nZeeN0e2u_Weighted,
			'nZeeN0e3u_Weighted': nZeeN0e3u_Weighted,
			'nZeeN1e1u_Weighted': nZeeN1e1u_Weighted,
			'nZeeN1e2u_Weighted': nZeeN1e2u_Weighted,
			'nZeeN2e1u_Weighted': nZeeN2e1u_Weighted,
			'NeTagZee_Weighted': NeTagZee_Weighted,
			'NeTagZee_CaloIsoOk_Weighted': NeTagZee_CaloIsoOk_Weighted,
			'NeTagZee_TrkIsoOk_Weighted': NeTagZee_TrkIsoOk_Weighted,
			'NeTagZee_d0Ok_Weighted': NeTagZee_d0Ok_Weighted,
			'NeTagZee_AllOk_Weighted': NeTagZee_AllOk_Weighted,
			'NeUntagZee_Weighted': NeUntagZee_Weighted,
			'NeUntagZee_CaloIsoOk_Weighted': NeUntagZee_CaloIsoOk_Weighted,
			'NeUntagZee_TrkIsoOk_Weighted': NeUntagZee_TrkIsoOk_Weighted,
			'NeUntagZee_d0Ok_Weighted': NeUntagZee_d0Ok_Weighted,
			'NeUntagZee_AllOk_Weighted': NeUntagZee_AllOk_Weighted,
			'NuUntagZee_Weighted': NuUntagZee_Weighted,
			'NuUntagZee_CaloIsoOk_Weighted': NuUntagZee_CaloIsoOk_Weighted,
			'NuUntagZee_TrkIsoOk_Weighted': NuUntagZee_TrkIsoOk_Weighted,
			'NuUntagZee_d0Ok_Weighted': NuUntagZee_d0Ok_Weighted,
			'NuUntagZee_AllOk_Weighted': NuUntagZee_AllOk_Weighted,
			'nZuu_Weighted': nZuu_Weighted,
			'nZuuZuu_Weighted': nZuuZuu_Weighted,
			'nZeeZuu_Weighted': nZeeZuu_Weighted,
			'nZuuN0e0u_Weighted': nZuuN0e0u_Weighted,
			'nZuuN1e0u_Weighted': nZuuN1e0u_Weighted,
			'nZuuN2e0u_Weighted': nZuuN2e0u_Weighted,
			'nZuuN3e0u_Weighted': nZuuN3e0u_Weighted,
			'nZuuN0e1u_Weighted': nZuuN0e1u_Weighted,
			'nZuuN0e2u_Weighted': nZuuN0e2u_Weighted,
			'nZuuN0e3u_Weighted': nZuuN0e3u_Weighted,
			'nZuuN1e1u_Weighted': nZuuN1e1u_Weighted,
			'nZuuN1e2u_Weighted': nZuuN1e2u_Weighted,
			'nZuuN2e1u_Weighted': nZuuN2e1u_Weighted,
			'NuTagZuu_Weighted': NuTagZuu_Weighted,
			'NuTagZuu_CaloIsoOk_Weighted': NuTagZuu_CaloIsoOk_Weighted,
			'NuTagZuu_TrkIsoOk_Weighted': NuTagZuu_TrkIsoOk_Weighted,
			'NuTagZuu_d0Ok_Weighted': NuTagZuu_d0Ok_Weighted,
			'NuTagZuu_AllOk_Weighted': NuTagZuu_AllOk_Weighted,
			'NeUntagZuu_Weighted': NeUntagZuu_Weighted,
			'NeUntagZuu_CaloIsoOk_Weighted': NeUntagZuu_CaloIsoOk_Weighted,
			'NeUntagZuu_TrkIsoOk_Weighted': NeUntagZuu_TrkIsoOk_Weighted,
			'NeUntagZuu_d0Ok_Weighted': NeUntagZuu_d0Ok_Weighted,
			'NeUntagZuu_AllOk_Weighted': NeUntagZuu_AllOk_Weighted,
			'NuUntagZuu_Weighted': NuUntagZuu_Weighted,
			'NuUntagZuu_CaloIsoOk_Weighted': NuUntagZuu_CaloIsoOk_Weighted,
			'NuUntagZuu_TrkIsoOk_Weighted': NuUntagZuu_TrkIsoOk_Weighted,
			'NuUntagZuu_d0Ok_Weighted': NuUntagZuu_d0Ok_Weighted,
			'NuUntagZuu_AllOk_Weighted': NuUntagZuu_AllOk_Weighted,
		}

		utils.fillTreeFromDict(tree, dic)
		tree.Write()

		hZee_rate.Write()
		hZuu_rate.Write()

		hMass_ee.Write()
		hMass_uu.Write()

		####################################
		#Additional leptons control plots  #
		####################################

		hZeeEleUntag.Write()
		hZeeMuUntag.Write()

		heUntagZee_eta.Write()
		heUntagZeeCaloIsoOk_eta.Write()
		heUntagZeeTrkIsoOk_eta.Write()
		heUntagZeed0Ok_eta.Write()
		heUntagZeeAllOk_eta.Write()

		heUntagZee_pt.Write()
		heUntagZeeCaloIsoOk_pt.Write()
		heUntagZeeTrkIsoOk_pt.Write()
		heUntagZeed0Ok_pt.Write()
		heUntagZeeAllOk_pt.Write()

		heUntagZee_phi.Write()
		heUntagCrackZee_pt.Write()
		heUntagNoCrackZee_pt.Write()
		heUntagZee_d0.Write()
		heUntagZee_z0.Write()
		heUntagZee_CaloIso.Write()
		heUntagZee_TrkIso.Write()
		heUntagZee_d0Sig.Write()

		huUntagZee_eta.Write()
		huUntagZeeCaloIsoOk_eta.Write()
		huUntagZeeTrkIsoOk_eta.Write()
		huUntagZeed0Ok_eta.Write()
		huUntagZeeAllOk_eta.Write()

		huUntagZee_pt.Write()
		huUntagZeeCaloIsoOk_pt.Write()
		huUntagZeeTrkIsoOk_pt.Write()
		huUntagZeed0Ok_pt.Write()
		huUntagZeeAllOk_pt.Write()

		huUntagZee_phi.Write()
		huUntagZee_d0.Write()
		huUntagZee_z0.Write()
		huUntagZee_CaloIso.Write()
		huUntagZee_TrkIso.Write()
		huUntagZee_d0Sig.Write()

		####################################
		#Z leptons control plots  	   #
		####################################

		heTagZee_phi.Write()
		heFEBMissingTagZee_phi.Write()
		heFEBRecoverTagZee_phi.Write()
		heTagZee_eta.Write()
		heTagZee_pt.Write()
		heTagZee_d0.Write()
		heTagZee_z0.Write()
		heTagZee_CaloIso.Write()
		heTagZee_TrkIso.Write()
		heTagZee_d0Sig.Write()

		####################################
		hZuuEleUntag.Write()
		hZuuMuUntag.Write()

		heUntagZuu_eta.Write()
		heUntagZuuCaloIsoOk_eta.Write()
		heUntagZuuTrkIsoOk_eta.Write()
		heUntagZuud0Ok_eta.Write()
		heUntagZuuAllOk_eta.Write()

		heUntagZuu_pt.Write()
		heUntagZuuCaloIsoOk_pt.Write()
		heUntagZuuTrkIsoOk_pt.Write()
		heUntagZuud0Ok_pt.Write()
		heUntagZuuAllOk_pt.Write()

		heUntagZuu_phi.Write()
		heUntagCrackZuu_pt.Write()
		heUntagNoCrackZuu_pt.Write()
		heUntagZuu_d0.Write()
		heUntagZuu_z0.Write()
		heUntagZuu_CaloIso.Write()
		heUntagZuu_TrkIso.Write()
		heUntagZuu_d0Sig.Write()

		huUntagZuu_eta.Write()
		huUntagZuuCaloIsoOk_eta.Write()
		huUntagZuuTrkIsoOk_eta.Write()
		huUntagZuud0Ok_eta.Write()
		huUntagZuuAllOk_eta.Write()

		huUntagZuu_pt.Write()
		huUntagZuuCaloIsoOk_pt.Write()
		huUntagZuuTrkIsoOk_pt.Write()
		huUntagZuud0Ok_pt.Write()
		huUntagZuuAllOk_pt.Write()

		huUntagZuu_phi.Write()
		huUntagZuu_d0.Write()
		huUntagZuu_z0.Write()
		huUntagZuu_CaloIso.Write()
		huUntagZuu_TrkIso.Write()
		huUntagZuu_d0Sig.Write()

		####################################
		#Z leptons control plots  	   #
		####################################

		huTagZuu_phi.Write()
		huTagZuu_eta.Write()
		huTagZuu_pt.Write()

		f.Close()

		#############################################################

#############################################################################
# LOAD									    #
#############################################################################

import BkgCrossSection

def load(fileName, Year, RunNumber, nbrOfEvent, grl):

	chain1 = utils.localLoader(fileName, 'el')
	chain2 = utils.localLoader(fileName, 'mu')

	if RunNumber > 0 and nbrOfEvent > 0:
		if Year == 2011:
			#lumi = 4.807 #Zuu
			lumi = 4.910 #Zee
			weight = BkgCrossSection.GetBkgCrossSection7TeV(RunNumber) * lumi / nbrOfEvent
		if Year == 2012:
			lumi = 13.0 #AllGood
			weight = BkgCrossSection.GetBkgCrossSection8TeV(RunNumber) * lumi / nbrOfEvent
	else:
		weight = 1.0000000000000000000000000000000000000000000000000000000000000000000

	#BkgCrossSection.GetBkgCrossSection7TeV(RunNumber)

	algo = TZLTree(chain1, chain2)
	algo.Loop(Year, RunNumber, weight, grl)

#############################################################################
# INIT									    #
#############################################################################

def reco(fileNameList, Year, RunNumberList, nbrOfEventList, grl):
	l1 = len(fileNameList)
	l2 = len(RunNumberList)
	l3 = len(nbrOfEventList)

	if (l1 != l2) or (l1 != l3):
		print('Error: len(fileNameList) != len(RunNumberList) != len(nbrOfEventList) !')
		return False

	for i in xrange((l1 + l2 + l3) / 3):
		load(fileNameList[i], Year, RunNumberList[i], nbrOfEventList[i], grl)

	return True

#############################################################################

import GRLEgamma
import GRLMuons
import GRL2012_ALLGOOD
atlas.init()

#############################################################################
#				2011
#############################################################################
#DATA

#reco(['input/2011/egamma_AllYear.txt'], 2011, [-1], [-1], GRLEgamma)
#reco(['input/2011/muon_AllYear.txt'], 2011, [-1], [-1], GRLMuons)

#MC
#reco(['input/2011/mc11.107650.AlpgenJimmyZeeNp0_pt20.txt'], 2011, [107650], [6618284], GRLEgamma)
#reco(['input/2011/mc11.107660.AlpgenJimmyZmumuNp0_pt20.txt'], 2011, [107660], [6615230], GRLEgamma)



#reco(['input/2011/mc11.107651.AlpgenJimmyZeeNp1_pt20.txt'], [107651], [1334897], GRLEgamma)
#reco(['input/2011/mc11.107652.AlpgenJimmyZeeNp2_pt20.txt'], [107652], [2004195], GRLEgamma)
#reco(['input/2011/mc11.107653.AlpgenJimmyZeeNp3_pt20.txt'], [107653], [549949], GRLEgamma)
#reco(['input/2011/mc11.107654.AlpgenJimmyZeeNp4_pt20.txt'], [107654], [149948], GRLEgamma)
#reco(['input/2011/mc11.107655.AlpgenJimmyZeeNp5_pt20.txt'], [107655], [50000], GRLEgamma)
#reco(['input/2011/mc11.116950.AlpgenHWfZeebbNp0_Veto4LepM_Pass3Lep.txt'], [116950], [249999], GRLEgamma)
#reco(['input/2011/mc11.116951.AlpgenHWfZeebbNp1_Veto4LepM_Pass3Lep.txt'], [116951], [149999], GRLEgamma)
#reco(['input/2011/mc11.116952.AlpgenHWfZeebbNp2_Veto4LepM_Pass3Lep.txt'], [116952], [80000], GRLEgamma)
#reco(['input/2011/mc11.116953.AlpgenHWfZeebbNp3_Veto4LepM_Pass3Lep.txt'], [116953], [20000], GRLEgamma)
#reco(['input/2011/mc11.116960.AlpgenHWfZeebbNp0_4LepM.txt'], [116960], [150000], GRLEgamma)
#reco(['input/2011/mc11.116961.AlpgenHWfZeebbNp1_4LepM.txt'], [116961], [90000], GRLEgamma)
#reco(['input/2011/mc11.116962.AlpgenHWfZeebbNp2_4LepM.txt'], [116962], [11500], GRLEgamma)
#reco(['input/2011/mc11.116963.AlpgenHWfZeebbNp3_4LepM.txt'], [116963], [1500], GRLEgamma)
 

#reco(['input/2011/mc11.107661.AlpgenJimmyZmumuNp1_pt20.txt'], [107661], [1334296], GRLEgamma)
#reco(['input/2011/mc11.107662.AlpgenJimmyZmumuNp2_pt20.txt'], [107662], [1999941], GRLEgamma)
#reco(['input/2011/mc11.107663.AlpgenJimmyZmumuNp3_pt20.txt'], [107663], [549896], GRLEgamma)
#reco(['input/2011/mc11.107664.AlpgenJimmyZmumuNp4_pt20.txt'], [107664], [150000], GRLEgamma)
#reco(['input/2011/mc11.107665.AlpgenJimmyZmumuNp5_pt20.txt'], [107665], [50000], GRLEgamma)
#reco(['input/2011/mc11.116955.AlpgenHWfZmumubbNp0_Veto4LepM_Pass3Lep.txt'], [116955], [249950], GRLEgamma)
#reco(['input/2011/mc11.116956.AlpgenHWfZmumubbNp1_Veto4LepM_Pass3Lep.txt'], [116956], [149950], GRLEgamma)
#reco(['input/2011/mc11.116957.AlpgenHWfZmumubbNp2_Veto4LepM_Pass3Lep.txt'], [116957], [79999], GRLEgamma)
#reco(['input/2011/mc11.116958.AlpgenHWfZmumubbNp3_Veto4LepM_Pass3Lep.txt'], [116958], [20000], GRLEgamma)
#reco(['input/2011/mc11.116965.AlpgenHWfZmumubbNp0_4LepM.txt'], [116965], [149500], GRLEgamma)
#reco(['input/2011/mc11.116966.AlpgenHWfZmumubbNp1_4LepM.txt'], [116966], [90000], GRLEgamma)
#reco(['input/2011/mc11.116967.AlpgenHWfZmumubbNp2_4LepM.txt'], [116967], [11500], GRLEgamma)
#reco(['input/2011/mc11.116968.AlpgenHWfZmumubbNp3_4LepM.txt'], [116968], [1500], GRLEgamma)

#reco(['input/2011/mc11.128971.PythiaWZ_inclusive.txt'], [128971], [49999], GRLEgamma)
#reco(['input/2011/mc11.105200.T1_McAtNlo_Jimmy.txt'], [105200], [14983835], GRLEgamma)

#reco(['input/2011/mc11.116601.gg2ZZ_JIMMY_ZZ4e.txt'], [116601], [61999], GRLEgamma)
#reco(['input/2011/mc11.116602.gg2ZZ_JIMMY_ZZ4mu.txt'], [116602], [65000], GRLEgamma)
#reco(['input/2011/mc11.116603.gg2ZZ_JIMMY_ZZ2e2mu.txt'], [116603], [65000], GRLEgamma)
#reco(['input/2011/mc11.126859.PowHegZZ_4e_trilep5GeV_Pythia.txt'], [126859], [100000], GRLEgamma)
#reco(['input/2011/mc11.126860.PowHegZZ_4mu_trilep5GeV_Pythia.txt'], [126860], [100000], GRLEgamma)
#reco(['input/2011/mc11.126861.PowHegZZ_2e2mu_trilep5GeV_Pythia.txt'], [126861], [199900], GRLEgamma)
#reco(['input/2011/mc11.126862.PowHegZZ_2mu2tau_trilep5GeV_Pythia.txt'], [126862], [199899], GRLEgamma)
#reco(['input/2011/mc11.126863.PowHegZZ_2e2tau_trilep5GeV_Pythia.txt'], [126863], [199999], GRLEgamma)
#reco(['input/2011/mc11.126864.PowHegZZ_4tau_trilep5GeV_Pythia.txt'], [126864], [99999], GRLEgamma)

#############################################################################
#				2012
#############################################################################

#------------------------- > DATA

#reco(['input/2012/data12_periodA-E_Egamma.txt'], 2012, [-1], [-1], GRL2012_ALLGOOD)
reco(['input/2012/data12_periodA-E_Muons.txt'], 2012, [-1], [-1], GRL2012_ALLGOOD)

#------------------------- > MC
#ttbar
#reco(['input/2012/mc12.105200.McAtNloJimmy_CT10_ttbar_LeptonFilter.txt'], 2012, [105200], [14983835], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.146369.McAtNloJimmy_CT10_ttbar_4LepMass_Mll40GeV12GeV.txt'], 2012, [146369], [399098], GRL2012_ALLGOOD)

#Z+jet
#reco(['input/2012/mc12.107650.AlpgenJimmy_AUET2CTEQ6L1_ZeeNp0.txt'], 2012, [107650], [6604283], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.107651.AlpgenJimmy_AUET2CTEQ6L1_ZeeNp1.txt'], 2012, [107651], [1329994], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.107652.AlpgenJimmy_AUET2CTEQ6L1_ZeeNp2.txt'], 2012, [107652], [404798], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.107653.AlpgenJimmy_AUET2CTEQ6L1_ZeeNp3.txt'], 2012, [107653], [109998], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.107654.AlpgenJimmy_AUET2CTEQ6L1_ZeeNp4.txt'], 2012, [107654], [30000], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.107655.AlpgenJimmy_AUET2CTEQ6L1_ZeeNp5.txt'], 2012, [107655], [10000], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.107660.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp0.txt'], 2012, [107660], [6609982], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.107661.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp1.txt'], 2012, [107661], [1334897], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.107662.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp2.txt'], 2012, [107662], [404897], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.107663.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp3.txt'], 2012, [107663], [110000], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.107664.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp4.txt'], 2012, [107664], [29999], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.107665.AlpgenJimmy_AUET2CTEQ6L1_ZmumuNp5.txt'], 2012, [107665], [10000], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.107670.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp0.txt'], 2012, [107670], [6607086], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.107671.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp1.txt'], 2012, [107671], [1334896], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.107672.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp2.txt'], 2012, [107672], [404900], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.107673.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp3.txt'], 2012, [107673], [110000], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.107674.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp4.txt'], 2012, [107674], [28999], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.107675.AlpgenJimmy_AUET2CTEQ6L1_ZtautauNp5.txt'], 2012, [107675], [10000], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.146830.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZeeNp0Excl_Mll10to60.txt'], 2012, [146830], [999496], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.146831.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZeeNp1Excl_Mll10to60.txt'], 2012, [146831], [299498], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.146832.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZeeNp2Excl_Mll10to60.txt'], 2012, [146832], [396499], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.146833.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZeeNp3Excl_Mll10to60.txt'], 2012, [146833], [145399], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.146834.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZeeNp4Excl_Mll10to60.txt'], 2012, [146834], [37500], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.146840.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZmumuNp0Excl_Mll10to60.txt'], 2012, [146840], [997896], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.146841.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZmumuNp1Excl_Mll10to60.txt'], 2012, [146841], [300000], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.146842.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZmumuNp2Excl_Mll10to60.txt'], 2012, [146842], [396499], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.146843.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZmumuNp3Excl_Mll10to60.txt'], 2012, [146843], [145499], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.146844.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZmumuNp4Excl_Mll10to60.txt'], 2012, [146844], [37400], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.146850.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZtautauNp0Excl_Mll10to60.txt'], 2012, [146850], [999896], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.146851.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZtautauNp1Excl_Mll10to60.txt'], 2012, [146851], [298899], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.146852.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZtautauNp2Excl_Mll10to60.txt'], 2012, [146852], [397500], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.146853.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZtautauNp3Excl_Mll10to60.txt'], 2012, [146853], [145400], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.146854.AlpgenJimmy_Auto_AUET2CTEQ6L1_ZtautauNp4Excl_Mll10to60.txt'], 2012, [146854], [365497], GRL2012_ALLGOOD)

#Zbb+jet
#reco(['input/2012/mc12.146980.AlpgenJimmy_Auto_AUET2CTEQ6L1_4lFilter_ZeeNp0.txt'], 2012, [146980], [217099], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.146981.AlpgenJimmy_Auto_AUET2CTEQ6L1_4lFilter_ZeeNp1.txt'], 2012, [146981], [105199], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.146982.AlpgenJimmy_Auto_AUET2CTEQ6L1_4lFilter_ZbbeeNp2.txt'], 2012, [146982], [23500], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.146985.AlpgenJimmy_Auto_AUET2CTEQ6L1_4lFilter_ZmumuNp0.txt'], 2012, [146985], [213299], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.146986.AlpgenJimmy_Auto_AUET2CTEQ6L1_4lFilter_ZmumuNp1.txt'], 2012, [146986], [105600], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.146987.AlpgenJimmy_Auto_AUET2CTEQ6L1_4lFilter_ZbbmumuNp2.txt'], 2012, [146987], [23300], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.146990.AlpgenJimmy_Auto_AUET2CTEQ6L1_3lFilter_4lVeto_ZeeNp0.txt'], 2012, [146990], [275700], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.146991.AlpgenJimmy_Auto_AUET2CTEQ6L1_3lFilter_4lVeto_ZeeNp1.txt'], 2012, [146991], [164000], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.146992.AlpgenJimmy_Auto_AUET2CTEQ6L1_3lFilter_4lVeto_ZbbeeNp2.txt'], 2012, [146992], [78498], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.146995.AlpgenJimmy_Auto_AUET2CTEQ6L1_3lFilter_4lVeto_ZmumuNp0.txt'], 2012, [146995], [275700], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.146996.AlpgenJimmy_Auto_AUET2CTEQ6L1_3lFilter_4lVeto_ZmumuNp1.txt'], 2012, [146996], [163300], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.146997.AlpgenJimmy_Auto_AUET2CTEQ6L1_3lFilter_4lVeto_ZbbmumuNp2.txt'], 2012, [146997], [77200], GRL2012_ALLGOOD)

#WZ
#reco(['input/2012/mc12.161961.Sherpa_CT10_lllnu_WZ.txt'], 2012, [161961], [599600], GRL2012_ALLGOOD)

#ZZ
#reco(['input/2012/mc12.116601.gg2ZZJimmy_AUET2CT10_ZZ4e.txt'], 2012, [116601], [90000], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.116602.gg2ZZJimmy_AUET2CT10_ZZ4mu.txt'], 2012, [116602], [89699], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.116603.gg2ZZJimmy_AUET2CT10_ZZ2e2mu.txt'], 2012, [116603], [89899], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.126937.PowhegPythia8_AU2CT10_ZZ_4e_mll4_2pt5.txt'], 2012, [126937], [599998], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.126938.PowhegPythia8_AU2CT10_ZZ_2e2mu_mll4_2pt5.txt'], 2012, [126938], [599799], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.126939.PowhegPythia8_AU2CT10_ZZ_2e2tau_mll4_2pt5.txt'], 2012, [126939], [599899], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.126940.PowhegPythia8_AU2CT10_ZZ_4mu_mll4_2pt5.txt'], 2012, [126940], [600000], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.126941.PowhegPythia8_AU2CT10_ZZ_2mu2tau_mll4_2pt5.txt'], 2012, [126941], [600000], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.126942.PowhegPythia8_AU2CT10_ZZ_4tau_mll4_2pt5.txt'], 2012, [126942], [300000], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.167162.PowhegPythia8_AU2CT10_ZZ_4e_m4l100_150_mll4_4pt3.txt'], 2012, [167162], [249999], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.167163.PowhegPythia8_AU2CT10_ZZ_2e2mu_m4l100_150_mll4_4pt3.txt'], 2012, [167163], [499900], GRL2012_ALLGOOD)
#reco(['input/2012/mc12.167165.PowhegPythia8_AU2CT10_ZZ_4mu_m4l100_150_mll4_4pt3.txt'], 2012, [167165], [250000], GRL2012_ALLGOOD)

