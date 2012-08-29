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
		#self.l_truth_type_mu = utils.newArray('f', 50)
		#self.tree_mu.SetBranchAddress('l_truth_type', self.l_truth_type_mu)

		self.l_tag_mu = utils.newArray('i', 50)		

	#####################################################################

	def Loop(self, mc_RunNumber, mc_weight, grl):

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

		ETABINS_XXbins = array.array('f', [-2.47, -2.37, -2.01, -1.81, -1.52, -1.37, -1.15, -0.8, -0.6, -0.1, 0,
                    0.1, 0.6, 0.8, 1.15, 1.37, 1.52, 1.81, 2.01, 2.37, 2.47])


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

		heUntagZee_eta = ROOT.TH1F('heUntagZee_eta', 'heUntagZee_eta', len(ETABINS_XXbins) - 1, ETABINS_XXbins)
		heUntagZeeCaloIsoOk_eta = ROOT.TH1F('heUntagZeeCaloIsoOk_eta', 'heUntagZeeCaloIsoOk_eta', len(ETABINS_XXbins) - 1, ETABINS_XXbins)
		heUntagZeeTrkIsoOk_eta = ROOT.TH1F('heUntagZeeTrkIsoOk_eta', 'heUntagZeeTrkIsoOk_eta', len(ETABINS_XXbins) - 1, ETABINS_XXbins)
		heUntagZeed0Ok_eta = ROOT.TH1F('heUntagZeed0Ok_eta', 'heUntagZeed0Ok_eta', len(ETABINS_XXbins) - 1, ETABINS_XXbins)
		heUntagZeeAllOk_eta = ROOT.TH1F('heUntagZeeAllOk_eta', 'heUntagZeeAllOk_eta', len(ETABINS_XXbins) - 1, ETABINS_XXbins)

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

		huUntagZee_eta = ROOT.TH1F('huUntagZee_eta', 'huUntagZee_eta', len(ETABINS_XXbins) - 1, ETABINS_XXbins)
		huUntagZeeCaloIsoOk_eta = ROOT.TH1F('huUntagZeeCaloIsoOk_eta', 'huUntagZeeCaloIsoOk_eta', len(ETABINS_XXbins) - 1, ETABINS_XXbins)
		huUntagZeeTrkIsoOk_eta = ROOT.TH1F('huUntagZeeTrkIsoOk_eta', 'huUntagZeeTrkIsoOk_eta', len(ETABINS_XXbins) - 1, ETABINS_XXbins)
		huUntagZeed0Ok_eta = ROOT.TH1F('huUntagZeed0Ok_eta', 'huUntagZeed0Ok_eta', len(ETABINS_XXbins) - 1, ETABINS_XXbins)
		huUntagZeeAllOk_eta = ROOT.TH1F('huUntagZeeAllOk_eta', 'huUntagZeeAllOk_eta', len(ETABINS_XXbins) - 1, ETABINS_XXbins)

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
		heTagZee_eta = ROOT.TH1F('heTagZee_eta', 'heTagZee_eta', len(ETABINS_XXbins) - 1, ETABINS_XXbins)
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

		heUntagZuu_eta = ROOT.TH1F('heUntagZuu_eta', 'heUntagZuu_eta', len(ETABINS_XXbins) - 1, ETABINS_XXbins)
		heUntagZuuCaloIsoOk_eta = ROOT.TH1F('heUntagZuuCaloIsoOk_eta', 'heUntagZuuCaloIsoOk_eta', len(ETABINS_XXbins) - 1, ETABINS_XXbins)
		heUntagZuuTrkIsoOk_eta = ROOT.TH1F('heUntagZuuTrkIsoOk_eta', 'heUntagZuuTrkIsoOk_eta', len(ETABINS_XXbins) - 1, ETABINS_XXbins)
		heUntagZuud0Ok_eta = ROOT.TH1F('heUntagZuud0Ok_eta', 'heUntagZuud0Ok_eta', len(ETABINS_XXbins) - 1, ETABINS_XXbins)
		heUntagZuuAllOk_eta = ROOT.TH1F('heUntagZuuAllOk_eta', 'heUntagZuuAllOk_eta', len(ETABINS_XXbins) - 1, ETABINS_XXbins)

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

		huUntagZuu_eta = ROOT.TH1F('huUntagZuu_eta', 'huUntagZuu_eta', len(ETABINS_XXbins) - 1, ETABINS_XXbins)
		huUntagZuuCaloIsoOk_eta = ROOT.TH1F('huUntagZuuCaloIsoOk_eta', 'huUntagZuuCaloIsoOk_eta', len(ETABINS_XXbins) - 1, ETABINS_XXbins)
		huUntagZuuTrkIsoOk_eta = ROOT.TH1F('huUntagZuuTrkIsoOk_eta', 'huUntagZuuTrkIsoOk_eta', len(ETABINS_XXbins) - 1, ETABINS_XXbins)
		huUntagZuud0Ok_eta = ROOT.TH1F('huUntagZuud0Ok_eta', 'huUntagZuud0Ok_eta', len(ETABINS_XXbins) - 1, ETABINS_XXbins)
		huUntagZuuAllOk_eta = ROOT.TH1F('huUntagZuuAllOk_eta', 'huUntagZuuAllOk_eta', len(ETABINS_XXbins) - 1, ETABINS_XXbins)

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
		huTagZuu_eta = ROOT.TH1F('huTagZuu_eta', 'huTagZuu_eta', len(ETABINS_XXbins) - 1, ETABINS_XXbins)
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
				for j in xrange(i + 1, self.n_ele[0]):
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
					if mc_RunNumber < 0:
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

					# IS MC
					if mc_RunNumber > 0:
						if self.RunNumber_ele[0] == 180164:
							hZee_rate.Fill(0, evt_weight * weight )
							hZee_rate.Fill(1, evt_weight * weight )

						elif self.RunNumber_ele[0] == 183003:
							hZee_rate.Fill(2, evt_weight * weight)
							hZee_rate.Fill(3, evt_weight * weight)
							hZee_rate.Fill(4, evt_weight * weight)
							hZee_rate.Fill(5, evt_weight * weight)

						elif self.RunNumber_ele[0] == 186169:
							hZee_rate.Fill(6, evt_weight * weight)
							hZee_rate.Fill(7, evt_weight * weight)
							hZee_rate.Fill(8, evt_weight * weight)

						elif self.RunNumber_ele[0] == 189751:
							hZee_rate.Fill(9, evt_weight * weight)
							hZee_rate.Fill(10, evt_weight * weight)

			#####################################################
			#	Count number of Z recontructed 		    #
			#	with independent mu			    #
			#####################################################

			ZuuEvtList = []

			L_Zuu = []
			I_Zuu = []

			for i in xrange(0 + 0, self.n_mu[0]):
				for j in xrange(i + 1, self.n_mu[0]):
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

			for l_index in xrange(len(I_Zuu)):				ZuubestMassR = 999999.0
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
					if mc_RunNumber < 0:
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

					# IS MC
					if mc_RunNumber > 0:
						if self.RunNumber_ele[0] == 180164:
							hZuu_rate.Fill(0, evt_weight * weight)
							hZuu_rate.Fill(1, evt_weight * weight)

						elif self.RunNumber_ele[0] == 183003:
							hZuu_rate.Fill(2, evt_weight * weight)
							hZuu_rate.Fill(3, evt_weight * weight)
							hZuu_rate.Fill(4, evt_weight * weight)
							hZuu_rate.Fill(5, evt_weight * weight)

						elif self.RunNumber_ele[0] == 186169:
							hZuu_rate.Fill(6, evt_weight * weight)
							hZuu_rate.Fill(7, evt_weight * weight)
							hZuu_rate.Fill(8, evt_weight * weight)

						elif self.RunNumber_ele[0] == 189751:
							hZuu_rate.Fill(9, evt_weight * weight)
							hZuu_rate.Fill(10, evt_weight * weight)


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

						#####################
						# IsoCuts on Z ele  #
						#####################

						if self.l_clIso20_ele[i] < 0.30:
							NeTagZee_CaloIsoOk += 1
							NeTagZee_CaloIsoOk_Weighted += weight
						if self.l_tkIso20_ele[i] < 0.15:
							NeTagZee_TrkIsoOk += 1
							NeTagZee_TrkIsoOk_Weighted += weight
						if self.l_d0sigma_ele[i] < 6.5:
							NeTagZee_d0Ok += 1
							NeTagZee_d0Ok_Weighted += weight
						if self.l_clIso20_ele[i] < 0.30\
						and			\
						self.l_tkIso20_ele[i] < 0.15\
						and			\
						self.l_d0sigma_ele[i] < 6.5:
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

							#####################
							# IsoCuts add ele   #
							#####################

							if self.l_clIso20_ele[i] < 0.30:
								NeUntagZee_CaloIsoOk += 1
								NeUntagZee_CaloIsoOk_Weighted += weight
								heUntagZeeCaloIsoOk_eta.Fill(self.l_eta_ele[i], weight)
								heUntagZeeCaloIsoOk_pt.Fill(self.l_pt_ele[i] / 1000.0, weight)

							if self.l_tkIso20_ele[i] < 0.15:
								NeUntagZee_TrkIsoOk += 1
								NeUntagZee_TrkIsoOk_Weighted += weight
								heUntagZeeTrkIsoOk_eta.Fill(self.l_eta_ele[i], weight)
								heUntagZeeTrkIsoOk_pt.Fill(self.l_pt_ele[i] / 1000.0, weight)
							if self.l_d0sigma_ele[i] < 6.5:
								NeUntagZee_d0Ok += 1
								NeUntagZee_d0Ok_Weighted += weight
								heUntagZeed0Ok_eta.Fill(self.l_eta_ele[i], weight)
								heUntagZeed0Ok_pt.Fill(self.l_pt_ele[i] / 1000.0, weight)
							if self.l_clIso20_ele[i] < 0.30\
							and			\
							self.l_tkIso20_ele[i] < 0.15\
							and			\
							self.l_d0sigma_ele[i] < 6.5:
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

							if self.l_clIso20_mu[i] < 0.30:
								NuUntagZee_CaloIsoOk += 1
								NuUntagZee_CaloIsoOk_Weighted += weight
								huUntagZeeCaloIsoOk_eta.Fill(self.l_eta_mu[i], weight)
								huUntagZeeCaloIsoOk_pt.Fill(self.l_pt_mu[i] / 1000.0, weight)
							if self.l_tkIso20_mu[i] < 0.15:
								NuUntagZee_TrkIsoOk += 1
								NuUntagZee_TrkIsoOk_Weighted += weight
								huUntagZeeTrkIsoOk_eta.Fill(self.l_eta_mu[i], weight)
								huUntagZeeTrkIsoOk_pt.Fill(self.l_pt_mu[i] / 1000.0, weight)
							if self.l_d0sigma_mu[i] < 3.5:
								NuUntagZee_d0Ok += 1
								NuUntagZee_d0Ok_Weighted += weight
								huUntagZeed0Ok_eta.Fill(self.l_eta_mu[i], weight)
								huUntagZeed0Ok_pt.Fill(self.l_pt_mu[i] / 1000.0, weight)
							if self.l_clIso20_mu[i] < 0.30\
							and			\
							self.l_tkIso20_mu[i] < 0.15\
							and			\
							self.l_d0sigma_mu[i] < 3.5:
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

						if self.l_clIso20_mu[i] < 0.30:
							NuTagZuu_CaloIsoOk += 1
							NuTagZuu_CaloIsoOk_Weighted += weight
						if self.l_tkIso20_mu[i] < 0.15:
							NuTagZuu_TrkIsoOk += 1
							NuTagZuu_TrkIsoOk_Weighted += weight
						if self.l_d0sigma_mu[i] < 3.5:
							NuTagZuu_d0Ok += 1
							NuTagZuu_d0Ok_Weighted += weight
						if self.l_clIso20_mu[i] < 0.30\
						and			\
						self.l_tkIso20_mu[i] < 0.15\
						and			\
						self.l_d0sigma_mu[i] < 3.5:
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
										Nb_tag_ele_passDeltaR += 1
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

							#####################
							# IsoCuts Add ele   #
							#####################

							if self.l_clIso20_ele[i] < 0.30:
								NeUntagZuu_CaloIsoOk += 1
								NeUntagZuu_CaloIsoOk_Weighted += weight
								heUntagZuuCaloIsoOk_eta.Fill(self.l_eta_ele[i], weight)
								heUntagZuuCaloIsoOk_pt.Fill(self.l_pt_ele[i] / 1000.0, weight)
							if self.l_tkIso20_ele[i] < 0.15:
								NeUntagZuu_TrkIsoOk += 1
								NeUntagZuu_TrkIsoOk_Weighted += weight
								heUntagZuuTrkIsoOk_eta.Fill(self.l_eta_ele[i], weight)
								heUntagZuuTrkIsoOk_pt.Fill(self.l_pt_ele[i] / 1000.0, weight)
							if self.l_d0sigma_ele[i] < 6.5:
								NeUntagZuu_d0Ok += 1
								NeUntagZuu_d0Ok_Weighted += weight
								heUntagZuud0Ok_eta.Fill(self.l_eta_ele[i], weight)
								heUntagZuud0Ok_pt.Fill(self.l_pt_ele[i] / 1000.0, weight)
							if self.l_clIso20_ele[i] < 0.30\
							and			\
							self.l_tkIso20_ele[i] < 0.15\
							and			\
							self.l_d0sigma_ele[i] < 6.5:
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
										Nb_tag_ele_passDeltaR += 1
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

							if self.l_clIso20_mu[i] < 0.30:
								NuUntagZuu_CaloIsoOk += 1
								NuUntagZuu_CaloIsoOk_Weighted += weight
								huUntagZuuCaloIsoOk_eta.Fill(self.l_eta_mu[i], weight)
								huUntagZuuCaloIsoOk_pt.Fill(self.l_pt_mu[i] / 1000.0, weight)
							if self.l_tkIso20_mu[i] < 0.15:
								NuUntagZuu_TrkIsoOk += 1
								NuUntagZuu_TrkIsoOk_Weighted += weight
								huUntagZuuTrkIsoOk_eta.Fill(self.l_eta_mu[i], weight)
								huUntagZuuTrkIsoOk_pt.Fill(self.l_pt_mu[i] / 1000.0, weight)
							if self.l_d0sigma_mu[i] < 3.5:
								NuUntagZuu_d0Ok += 1
								NuUntagZuu_d0Ok_Weighted += weight
								huUntagZuud0Ok_eta.Fill(self.l_eta_mu[i], weight)
								huUntagZuud0Ok_pt.Fill(self.l_pt_mu[i] / 1000.0, weight)
							if self.l_clIso20_mu[i] < 0.30\
							and			\
							self.l_tkIso20_mu[i] < 0.15\
							and			\
							self.l_d0sigma_mu[i] < 3.5:
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

		f = ROOT.TFile('output/Zuu_DATA.root', 'RECREATE')
		#f = ROOT.TFile('output/Zuu_MC_%d.root' % mc_RunNumber, 'RECREATE')
		#f = ROOT.TFile('output/Zee_DATA.root', 'RECREATE')
		#f = ROOT.TFile('output/Zee_MC_%d.root' % mc_RunNumber, 'RECREATE')

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

lumi = 4.807 #Zuu
#lumi = 4.910 #Zee

import BkgCrossSection

def load(fileName, RunNumber, nbrOfEvent, grl):
	chain1 = utils.localLoader(fileName, 'elSTACO')
	chain2 = utils.localLoader(fileName, 'muSTACO')

	if RunNumber > 0 and nbrOfEvent > 0:
		weight = BkgCrossSection.GetBkgCrossSection7TeV(RunNumber) * lumi / nbrOfEvent
	else:
		weight = 1.0000000000000000000000000000000000000000000000000000000000000000000

	BkgCrossSection.GetBkgCrossSection7TeV(RunNumber)

	algo = TZLTree(chain1, chain2)
	algo.Loop(RunNumber, weight, grl)

#############################################################################
# INIT									    #
#############################################################################

def reco(fileNameList, RunNumberList, nbrOfEventList, grl):
	l1 = len(fileNameList)
	l2 = len(RunNumberList)
	l3 = len(nbrOfEventList)

	if (l1 != l2) or (l1 != l3):
		print('Error: len(fileNameList) != len(RunNumberList) != len(nbrOfEventList) !')
		return False

	for i in xrange((l1 + l2 + l3) / 3):
		load(fileNameList[i], RunNumberList[i], nbrOfEventList[i], grl)

	return True

#############################################################################

import GRLEgamma
import GRLMuons

atlas.init()
#reco(['input/2011/egamma.txt'], [-1], [-1], GRLEgamma)
reco(['input/2011/muons.txt'], [-1], [-1], GRLMuons)

#reco(['input/2011/mc11.107650.AlpgenJimmyZeeNp0_pt20.txt'], [107650], [6618284], GRLEgamma)
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
 
#reco(['input/2011/mc11.107660.AlpgenJimmyZmumuNp0_pt20.txt'], [107660], [6615230], GRLEgamma)
#reco(['input/2011/mc11.107661.AlpgenJimmyZmumuNp1_pt20.txt'], [107661], [1334296], GRLEgamma)
#reco(['input/2011/mc11.107662.AlpgenJimmyZmumuNp2_pt20.txt'], [107662], [1999941], GRLEgamma)
#reco(['input/2011/mc11.107663.AlpgenJimmyZmumuNp3_pt20.txt'], [107663], [549896], GRLEgamma)
#reco(['input/2011/mc11.107664.AlpgenJimmyZmumuNp4_pt20.txt'], [107664], [150000], GRLEgamma)
#reco(['input/2011/mc11.107665.AlpgenJimmyZmumuNp5_pt20.txt'], [107665], [50000], GRLEgamma)
#reco(['input/2011/mc11.116955.AlpgenHWfZmumubbNp0_Veto4LepM_Pass3Lep.txt'], [116955], [249950], GRLEgamma)
#reco(['input/2011/mc11.116956.AlpgenHWfZmumubbNp1_Veto4LepM_Pass3Lep.txt'], [116956], [149950], GRLEgamma)
#reco(['input/2011/mc11.116957.AlpgenHWfZmumubbNp2_Veto4LepM_Pass3Lep.txt'], [116957], [79999], GRLEgamma)
#reco(['input/2011/mc11.116958.AlpgenHWfZmumubbNp3_Veto4LepM_Pass3Lep.txt'], [116958], [20000], GRLEgamma)
#reco(['input/2011/mc11.116965.AlpgenHWfZmumubbNp0_4LepM.txt'], [116965], [149500], GRLEgamma)#reco(['input/2011/mc11.116966.AlpgenHWfZmumubbNp1_4LepM.txt'], [116966], [90000], GRLEgamma)
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

