void ZuuRate(void){

	
	//--------------------------------------//
	// ATLAS STYLE				//
	//--------------------------------------//

	gROOT->LoadMacro("~/Root/atlasstyle-00-03-01/AtlasStyle.C");
  	gROOT->LoadMacro("~/Root/atlasstyle-00-03-01/AtlasLabels.C");
  	AtlasStyle();
  	TStyle* atlasStyle = AtlasStyle();
  	gROOT->SetStyle("ATLAS");
  	gROOT->ForceStyle();
	//gStyle->SetOptStat("enmriou");
	gStyle->SetPalette(1);

	Int_t mc_RunNumber[] = {107650,107651,107652,107653,107654,107655,               //Zee + light jets
				107660,107661,107662,107663,107664,107665, 		 //Zuu + light jets
				116950,116951,116952,116953,116960,116961,116962,116963, //Zeebb 4LepM + bgdVeto4LepM
				116955,116956,116957,116958,116965,116966,116967,116968,  //Zuubb 4LepM + bgdVeto4LepM
				128971,							 //PythiaWZ_inclusive
				105200,							 //T1_McAtNlo_Jimmy
				116601,116602,116603,126859,126860,126861,126862,126863,126864//ZZ
				};

	TFile *file0 = new TFile("../output/Zuu_DATA.root");
	TH1D *hData = (TH1D *) file0->Get("Zuu_rate");

	TH1D *hZjets = new TH1D("", "", 11, 0, 11);
	for(int i =  0; i <  12 ; i++){  //Z + light jets bgd
		TFile *file = new TFile(Form("../output/Zuu_MC_%d.root",mc_RunNumber[i]));
		TH1D *h = (TH1D *) file->Get("Zuu_rate");
		hZjets->Add(h);
		delete h;
		delete file;
	}

	TH1D *hZbbjets = new TH1D("", "", 11, 0, 11);
	for(int i = 12; i < 28 ; i++){  //Zbb 4LepM + bgdVeto4LepM
		TFile *file = new TFile(Form("../output/Zuu_MC_%d.root",mc_RunNumber[i]));
		TH1D *h = (TH1D *) file->Get("Zuu_rate");
		hZbbjets->Add(h);
		delete h;
		delete file;
	}

	TH1D *hWZ = new TH1D("", "", 11, 0, 11);
	for(int i = 28; i < 29 ; i++){  //PythiaWZ_inclusive
		TFile *file = new TFile(Form("../output/Zuu_MC_%d.root",mc_RunNumber[i]));
		TH1D *h = (TH1D *) file->Get("Zuu_rate");
		hWZ->Add(h);
		delete h;
		delete file;
	}

	TH1D *httbar = new TH1D("", "", 11, 0, 11);
	for(int i = 29; i < 30 ; i++){  //T1_McAtNlo_Jimmy
		TFile *file = new TFile(Form("../output/Zuu_MC_%d.root",mc_RunNumber[i]));
		TH1D *h = (TH1D *) file->Get("Zuu_rate");
		httbar->Add(h);
		delete h;
		delete file;
	}

	TH1D *hZZ = new TH1D("", "", 11, 0, 11);
	for(int i = 30; i < 39 ; i++){  //ZZ
		TFile *file = new TFile(Form("../output/Zuu_MC_%d.root",mc_RunNumber[i]));
		TH1D *h = (TH1D *) file->Get("Zuu_rate");
		hZZ->Add(h);
		delete h;
		delete file;
	}
	/*-----------------------------------------------------------------*/
/*	hData->Sumw2();
	hZjets->Sumw2();
	hZbbjets->Sumw2();
	hWZ->Sumw2();
	httbar->Sumw2();
	hZZ->Sumw2();
*/
	/*-----------------------------------------------------------------*/

	const Float_t LumiPeriod[] = {
		11.74, 166.77,
		48.70, 142.56, 537.54, 259.46,
		386.23, 226.46, 600.07,
		1401.87, 1025.62
	};

	const Float_t LumiPeriodMC[] = {
		LumiPeriod[0] + LumiPeriod[1],
		LumiPeriod[2] + LumiPeriod[3] + LumiPeriod[4] + LumiPeriod[5],
		LumiPeriod[6] + LumiPeriod[7] + LumiPeriod[8],
		LumiPeriod[9] + LumiPeriod[10]
	};

	/*-----------------------------------------------------------------*/

	if(1)
	{
		// MC : Z+jets //
		hZjets->TH1::SetBinContent(1,  hZjets->TH1::GetBinContent(1)  / (float)LumiPeriodMC[0]);
		hZjets->TH1::SetBinContent(2,  hZjets->TH1::GetBinContent(2)  / (float)LumiPeriodMC[0]);

		hZjets->TH1::SetBinContent(3,  hZjets->TH1::GetBinContent(3)  / (float)LumiPeriodMC[1]);
		hZjets->TH1::SetBinContent(4,  hZjets->TH1::GetBinContent(4)  / (float)LumiPeriodMC[1]);
		hZjets->TH1::SetBinContent(5,  hZjets->TH1::GetBinContent(5)  / (float)LumiPeriodMC[1]);
		hZjets->TH1::SetBinContent(6,  hZjets->TH1::GetBinContent(6)  / (float)LumiPeriodMC[1]);

		hZjets->TH1::SetBinContent(7,  hZjets->TH1::GetBinContent(7)  / (float)LumiPeriodMC[2]);
		hZjets->TH1::SetBinContent(8,  hZjets->TH1::GetBinContent(8)  / (float)LumiPeriodMC[2]);
		hZjets->TH1::SetBinContent(9,  hZjets->TH1::GetBinContent(9)  / (float)LumiPeriodMC[2]);

		hZjets->TH1::SetBinContent(10, hZjets->TH1::GetBinContent(10) / (float)LumiPeriodMC[3]);
		hZjets->TH1::SetBinContent(11, hZjets->TH1::GetBinContent(11) / (float)LumiPeriodMC[3]);

		// MC : Zbb+jets //
		hZbbjets->TH1::SetBinContent(1,  hZbbjets->TH1::GetBinContent(1)  / (float)LumiPeriodMC[0]);
		hZbbjets->TH1::SetBinContent(2,  hZbbjets->TH1::GetBinContent(2)  / (float)LumiPeriodMC[0]);

		hZbbjets->TH1::SetBinContent(3,  hZbbjets->TH1::GetBinContent(3)  / (float)LumiPeriodMC[1]);
		hZbbjets->TH1::SetBinContent(4,  hZbbjets->TH1::GetBinContent(4)  / (float)LumiPeriodMC[1]);
		hZbbjets->TH1::SetBinContent(5,  hZbbjets->TH1::GetBinContent(5)  / (float)LumiPeriodMC[1]);
		hZbbjets->TH1::SetBinContent(6,  hZbbjets->TH1::GetBinContent(6)  / (float)LumiPeriodMC[1]);

		hZbbjets->TH1::SetBinContent(7,  hZbbjets->TH1::GetBinContent(7)  / (float)LumiPeriodMC[2]);
		hZbbjets->TH1::SetBinContent(8,  hZbbjets->TH1::GetBinContent(8)  / (float)LumiPeriodMC[2]);
		hZbbjets->TH1::SetBinContent(9,  hZbbjets->TH1::GetBinContent(9)  / (float)LumiPeriodMC[2]);

		hZbbjets->TH1::SetBinContent(10, hZbbjets->TH1::GetBinContent(10) / (float)LumiPeriodMC[3]);
		hZbbjets->TH1::SetBinContent(11, hZbbjets->TH1::GetBinContent(11) / (float)LumiPeriodMC[3]);

		// MC : WZ //
		hWZ->TH1::SetBinContent(1,  hWZ->TH1::GetBinContent(1)  / (float)LumiPeriodMC[0]);
		hWZ->TH1::SetBinContent(2,  hWZ->TH1::GetBinContent(2)  / (float)LumiPeriodMC[0]);

		hWZ->TH1::SetBinContent(3,  hWZ->TH1::GetBinContent(3)  / (float)LumiPeriodMC[1]);
		hWZ->TH1::SetBinContent(4,  hWZ->TH1::GetBinContent(4)  / (float)LumiPeriodMC[1]);
		hWZ->TH1::SetBinContent(5,  hWZ->TH1::GetBinContent(5)  / (float)LumiPeriodMC[1]);
		hWZ->TH1::SetBinContent(6,  hWZ->TH1::GetBinContent(6)  / (float)LumiPeriodMC[1]);

		hWZ->TH1::SetBinContent(7,  hWZ->TH1::GetBinContent(7)  / (float)LumiPeriodMC[2]);
		hWZ->TH1::SetBinContent(8,  hWZ->TH1::GetBinContent(8)  / (float)LumiPeriodMC[2]);
		hWZ->TH1::SetBinContent(9,  hWZ->TH1::GetBinContent(9)  / (float)LumiPeriodMC[2]);

		hWZ->TH1::SetBinContent(10, hWZ->TH1::GetBinContent(10) / (float)LumiPeriodMC[3]);
		hWZ->TH1::SetBinContent(11, hWZ->TH1::GetBinContent(11) / (float)LumiPeriodMC[3]);

		// MC : ttbar //
		httbar->TH1::SetBinContent(1,  httbar->TH1::GetBinContent(1)  / (float)LumiPeriodMC[0]);
		httbar->TH1::SetBinContent(2,  httbar->TH1::GetBinContent(2)  / (float)LumiPeriodMC[0]);

		httbar->TH1::SetBinContent(3,  httbar->TH1::GetBinContent(3)  / (float)LumiPeriodMC[1]);
		httbar->TH1::SetBinContent(4,  httbar->TH1::GetBinContent(4)  / (float)LumiPeriodMC[1]);
		httbar->TH1::SetBinContent(5,  httbar->TH1::GetBinContent(5)  / (float)LumiPeriodMC[1]);
		httbar->TH1::SetBinContent(6,  httbar->TH1::GetBinContent(6)  / (float)LumiPeriodMC[1]);

		httbar->TH1::SetBinContent(7,  httbar->TH1::GetBinContent(7)  / (float)LumiPeriodMC[2]);
		httbar->TH1::SetBinContent(8,  httbar->TH1::GetBinContent(8)  / (float)LumiPeriodMC[2]);
		httbar->TH1::SetBinContent(9,  httbar->TH1::GetBinContent(9)  / (float)LumiPeriodMC[2]);

		httbar->TH1::SetBinContent(10, httbar->TH1::GetBinContent(10) / (float)LumiPeriodMC[3]);
		httbar->TH1::SetBinContent(11, httbar->TH1::GetBinContent(11) / (float)LumiPeriodMC[3]);

		// MC : ZZ //
		hZZ->TH1::SetBinContent(1,  hZZ->TH1::GetBinContent(1)  / (float)LumiPeriodMC[0]);
		hZZ->TH1::SetBinContent(2,  hZZ->TH1::GetBinContent(2)  / (float)LumiPeriodMC[0]);

		hZZ->TH1::SetBinContent(3,  hZZ->TH1::GetBinContent(3)  / (float)LumiPeriodMC[1]);
		hZZ->TH1::SetBinContent(4,  hZZ->TH1::GetBinContent(4)  / (float)LumiPeriodMC[1]);
		hZZ->TH1::SetBinContent(5,  hZZ->TH1::GetBinContent(5)  / (float)LumiPeriodMC[1]);
		hZZ->TH1::SetBinContent(6,  hZZ->TH1::GetBinContent(6)  / (float)LumiPeriodMC[1]);

		hZZ->TH1::SetBinContent(7,  hZZ->TH1::GetBinContent(7)  / (float)LumiPeriodMC[2]);
		hZZ->TH1::SetBinContent(8,  hZZ->TH1::GetBinContent(8)  / (float)LumiPeriodMC[2]);
		hZZ->TH1::SetBinContent(9,  hZZ->TH1::GetBinContent(9)  / (float)LumiPeriodMC[2]);

		hZZ->TH1::SetBinContent(10, hZZ->TH1::GetBinContent(10) / (float)LumiPeriodMC[3]);
		hZZ->TH1::SetBinContent(11, hZZ->TH1::GetBinContent(11) / (float)LumiPeriodMC[3]);

		// DATA //

		Int_t DataNb_B = hData->TH1::GetBinContent(1);
		Int_t DataNb_D = hData->TH1::GetBinContent(2);
		Int_t DataNb_E = hData->TH1::GetBinContent(3);
		Int_t DataNb_F = hData->TH1::GetBinContent(4);
		Int_t DataNb_G = hData->TH1::GetBinContent(5);
		Int_t DataNb_H = hData->TH1::GetBinContent(6);
		Int_t DataNb_I = hData->TH1::GetBinContent(7);
		Int_t DataNb_J = hData->TH1::GetBinContent(8);
		Int_t DataNb_K = hData->TH1::GetBinContent(9);
		Int_t DataNb_L = hData->TH1::GetBinContent(10);
		Int_t DataNb_M = hData->TH1::GetBinContent(11);

		hData->TH1::SetBinContent(1,  (float)DataNb_B / (float)LumiPeriod[0]);
		hData->TH1::SetBinContent(2,  (float)DataNb_D / (float)LumiPeriod[1]);

		hData->TH1::SetBinContent(3,  (float)DataNb_E / (float)LumiPeriod[2]);
		hData->TH1::SetBinContent(4,  (float)DataNb_F / (float)LumiPeriod[3]);
		hData->TH1::SetBinContent(5,  (float)DataNb_G / (float)LumiPeriod[4]);
		hData->TH1::SetBinContent(6,  (float)DataNb_H / (float)LumiPeriod[5]);

		hData->TH1::SetBinContent(7,  (float)DataNb_I / (float)LumiPeriod[6]);
		hData->TH1::SetBinContent(8,  (float)DataNb_J / (float)LumiPeriod[7]);
		hData->TH1::SetBinContent(9,  (float)DataNb_K / (float)LumiPeriod[8]);

		hData->TH1::SetBinContent(10, (float)DataNb_L / (float)LumiPeriod[9]);
		hData->TH1::SetBinContent(11, (float)DataNb_M / (float)LumiPeriod[10]);
	}


	hData->SetMarkerStyle(20);
	hZjets->SetFillColor(kBlue);
	hZbbjets->SetFillColor(kRed);
	hWZ->SetFillColor(kYellow);
	httbar->SetFillColor(kGreen);
	hZZ->SetFillColor(kCyan - 7);

	const char *names[] = {
			"B", "D",
			"E", "F", "G", "H",
			"I", "J", "K",
			"L", "M"
		};
	TAxis *axis1 = hData->GetXaxis();

	for(int i = 1; i < 12; i++)
	{
		axis1->SetBinLabel(i - 0, names[i - 1]);
	}
	hData->SetXTitle("2011 Periods");
	hData->SetYTitle("Z#rightarrow #mu#mu candidats / Luminosity [pb]");
	THStack* hresult = new THStack("hresults","hresult");

	hresult->Add(hZZ);
	hresult->Add(hWZ); 
	hresult->Add(httbar);
	hresult->Add(hZbbjets);
	hresult->Add(hZjets);

	TCanvas *c = new TCanvas("c","c");
	c->SetLogy();
	hData->TH1::SetMinimum(0.01);
	hData->TH1::SetMaximum(100000);
	hData->Draw("EP");
	hresult->Draw("SAME");

	TLegend*leg1=new TLegend(0.25,0.75,0.50,0.9);
	leg1->SetFillColor(0);
	leg1->SetShadowColor(0);
	leg1->SetBorderSize(0);
	leg1->AddEntry(httbar,"t#bar{t}","f");
	leg1->AddEntry(hWZ,"WZ","f");
	leg1->AddEntry(hZZ,"ZZ","f");
	leg1->Draw();

	TLegend*leg2=new TLegend(0.40,0.75,0.60,0.9);
	leg2->SetFillColor(0);
	leg2->SetShadowColor(0);
	leg2->SetBorderSize(0);
	leg2->AddEntry(hData,"Data","ep");
	leg2->AddEntry(hZjets,"Z light jets","f");
	leg2->AddEntry(hZbbjets,"Zbb","f");
	leg2->Draw();

	TLatex l2;
	l2.SetNDC();
	l2.DrawLatex(0.65, 0.8, "#int L dt  #approx 4.8 fb^{-1}");

	c->SaveAs("2011_ZuuRate.png");


}
