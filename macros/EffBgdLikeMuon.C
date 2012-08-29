
#include "utils.C"

void EffBgdLikeMuon(void)
{
	//--------------------------------------//
	// ATLAS STYLE				//
	//--------------------------------------//

	gROOT->LoadMacro("~/Root/atlasstyle-00-03-01/AtlasStyle.C");
  	gROOT->LoadMacro("~/Root/atlasstyle-00-03-01/AtlasLabels.C");
  	AtlasStyle();
  	TStyle* atlasStyle = AtlasStyle();
  	gROOT->SetStyle("ATLAS");
  	gROOT->ForceStyle();
	gStyle->SetOptStat("emri");
	//gStyle->SetOptStat("enmriou");
	gStyle->SetPalette(1);



	//--------------------------------------//
	// execute				//
	//--------------------------------------//
	Eff_uUntag_eta(true,  true, true, true);
	Eff_uUntag_pt(true,  true, true, true);
}

//--------------------------------------------------------------------------//

void Eff_uUntag_eta(bool PlotCaloIso, bool PlotTrkIso, bool Plotd0sig, bool PlotAll)
{
	//--------------------------------------//
	// Data					//
	//--------------------------------------//

	TFile *fileData_Zee = new TFile("../output/Zee_DATA.root");
	TFile *fileData_Zuu = new TFile("../output/Zuu_DATA.root");

	TH1F *huUntagZee_eta = (TH1F *) fileData_Zee->Get("huUntagZee_eta");
	TH1F *huUntagZeeCaloIsoOk_eta = (TH1F *) fileData_Zee->Get("huUntagZeeCaloIsoOk_eta");
	TH1F *huUntagZeeTrkIsoOk_eta = (TH1F *) fileData_Zee->Get("huUntagZeeTrkIsoOk_eta");
	TH1F *huUntagZeed0Ok_eta = (TH1F *) fileData_Zee->Get("huUntagZeed0Ok_eta");
	TH1F *huUntagZeeAllOk_eta = (TH1F *) fileData_Zee->Get("huUntagZeeAllOk_eta");

	TH1F *huUntagZuu_eta = (TH1F *) fileData_Zuu->Get("huUntagZuu_eta");
	TH1F *huUntagZuuCaloIsoOk_eta = (TH1F *) fileData_Zuu->Get("huUntagZuuCaloIsoOk_eta");
	TH1F *huUntagZuuTrkIsoOk_eta = (TH1F *) fileData_Zuu->Get("huUntagZuuTrkIsoOk_eta");
	TH1F *huUntagZuud0Ok_eta = (TH1F *) fileData_Zuu->Get("huUntagZuud0Ok_eta");
	TH1F *huUntagZuuAllOk_eta = (TH1F *) fileData_Zuu->Get("huUntagZuuAllOk_eta");


	double Eff_ZeeCaloIsoOk_eta[20];
	double Eff_ZeeCaloIsoOk_eta_err[20];
	double Eff_ZeeTrkIsoOk_eta[20];
	double Eff_ZeeTrkIsoOk_eta_err[20];
	double Eff_Zeed0Ok_eta[20];
	double Eff_Zeed0Ok_eta_err[20];
	double Eff_ZeeAllOk_eta[20];
	double Eff_ZeeAllOk_eta_err[20];

	double Eff_ZuuCaloIsoOk_eta[20];
	double Eff_ZuuCaloIsoOk_eta_err[20];
	double Eff_ZuuTrkIsoOk_eta[20];
	double Eff_ZuuTrkIsoOk_eta_err[20];
	double Eff_Zuud0Ok_eta[20];
	double Eff_Zuud0Ok_eta_err[20];
	double Eff_ZuuAllOk_eta[20];
	double Eff_ZuuAllOk_eta_err[20];

	for (int i = 0; i < 20; i++){
		Eff_ZeeCaloIsoOk_eta[i] = huUntagZeeCaloIsoOk_eta->TH1::GetBinContent(i + 1) 
						/ huUntagZee_eta->TH1::GetBinContent(i + 1) * 100.0;
		Eff_ZeeCaloIsoOk_eta_err[i] = error(huUntagZeeCaloIsoOk_eta->TH1::GetBinContent(i + 1), huUntagZee_eta->TH1::GetBinContent(i + 1)) * 100.0;
		Eff_ZeeTrkIsoOk_eta[i] = huUntagZeeTrkIsoOk_eta->TH1::GetBinContent(i + 1) 
						/ huUntagZee_eta->TH1::GetBinContent(i + 1) * 100.0;
		Eff_ZeeTrkIsoOk_eta_err[i] = error(huUntagZeeTrkIsoOk_eta->TH1::GetBinContent(i + 1), huUntagZee_eta->TH1::GetBinContent(i + 1)) * 100.0;
		Eff_Zeed0Ok_eta[i] = huUntagZeed0Ok_eta->TH1::GetBinContent(i + 1) 
						/ huUntagZee_eta->TH1::GetBinContent(i + 1) * 100.0;
		Eff_Zeed0Ok_eta_err[i] = error(huUntagZeed0Ok_eta->TH1::GetBinContent(i + 1), huUntagZee_eta->TH1::GetBinContent(i + 1)) * 100.0;
		Eff_ZeeAllOk_eta[i] = huUntagZeeAllOk_eta->TH1::GetBinContent(i + 1) 
						/ huUntagZee_eta->TH1::GetBinContent(i + 1) * 100.0;
		Eff_ZeeAllOk_eta_err[i] = error(huUntagZeeAllOk_eta->TH1::GetBinContent(i + 1), huUntagZee_eta->TH1::GetBinContent(i + 1)) * 100.0;

		Eff_ZuuCaloIsoOk_eta[i] = huUntagZuuCaloIsoOk_eta->TH1::GetBinContent(i + 1) 
						/ huUntagZuu_eta->TH1::GetBinContent(i + 1) * 100.0;
		Eff_ZuuCaloIsoOk_eta_err[i] = error(huUntagZuuCaloIsoOk_eta->TH1::GetBinContent(i + 1), huUntagZuu_eta->TH1::GetBinContent(i + 1)) * 100.0;
		Eff_ZuuTrkIsoOk_eta[i] = huUntagZuuTrkIsoOk_eta->TH1::GetBinContent(i + 1) 
						/ huUntagZuu_eta->TH1::GetBinContent(i + 1) * 100.0;
		Eff_ZuuTrkIsoOk_eta_err[i] = error(huUntagZuuTrkIsoOk_eta->TH1::GetBinContent(i + 1), huUntagZuu_eta->TH1::GetBinContent(i + 1)) * 100.0;
		Eff_Zuud0Ok_eta[i] = huUntagZuud0Ok_eta->TH1::GetBinContent(i + 1) 
						/ huUntagZuu_eta->TH1::GetBinContent(i + 1) * 100.0;
		Eff_Zuud0Ok_eta_err[i] = error(huUntagZuud0Ok_eta->TH1::GetBinContent(i + 1), huUntagZuu_eta->TH1::GetBinContent(i + 1)) * 100.0;
		Eff_ZuuAllOk_eta[i] = huUntagZuuAllOk_eta->TH1::GetBinContent(i + 1) 
						/ huUntagZuu_eta->TH1::GetBinContent(i + 1) * 100.0;
		Eff_ZuuAllOk_eta_err[i] = error(huUntagZuuAllOk_eta->TH1::GetBinContent(i + 1), huUntagZuu_eta->TH1::GetBinContent(i + 1)) * 100.0;

	}
	//--------------------------------------//
	// MC Zee				//
	//--------------------------------------//

	Int_t mc_RunNumber[] = {107650,107651,107652,107653,107654,107655,               //Zee + light jets
				107660,107661,107662,107663,107664,107665, 		 //Zuu + light jets
				116950,116951,116952,116953,116960,116961,116962,116963, //Zeebb 4LepM + bgdVeto4LepM
				116955,116956,116957,116958,116965,116966,116967,116968,  //Zuubb 4LepM + bgdVeto4LepM
				128971,							 //PythiaWZ_inclusive
				105200,							 //T1_McAtNlo_Jimmy
				116601,116602,116603,126859,126860,126861,126862,126863,126864//ZZ
				};
	const double etaBins[]={-2.47, -2.37, -2.01, -1.81, -1.52, -1.37, -1.15, -0.8, -0.6, -0.1, 0,
                    0.1, 0.6, 0.8, 1.15, 1.37, 1.52, 1.81, 2.01, 2.37, 2.47};


	TFile *fileMC_Zee = new TFile(Form("../output/Zee_MC_%d.root",mc_RunNumber[0]));
	TFile *fileMC_Zuu = new TFile(Form("../output/Zuu_MC_%d.root",mc_RunNumber[0]));

	TH1F *hAllMC_uUntagZee_eta= (TH1F *) fileMC_Zee->Get("huUntagZee_eta");
	TH1F *hAllMC_uUntagZeeCaloIsoOk_eta= (TH1F *) fileMC_Zee->Get("huUntagZeeCaloIsoOk_eta");
	TH1F *hAllMC_uUntagZeeTrkIsoOk_eta= (TH1F *) fileMC_Zee->Get("huUntagZeeTrkIsoOk_eta");
	TH1F *hAllMC_uUntagZeed0Ok_eta= (TH1F *) fileMC_Zee->Get("huUntagZeed0Ok_eta");
	TH1F *hAllMC_uUntagZeeAllOk_eta= (TH1F *) fileMC_Zee->Get("huUntagZeeAllOk_eta");

	TH1F *hAllMC_uUntagZuu_eta= (TH1F *) fileMC_Zuu->Get("huUntagZuu_eta");
	TH1F *hAllMC_uUntagZuuCaloIsoOk_eta= (TH1F *) fileMC_Zuu->Get("huUntagZuuCaloIsoOk_eta");
	TH1F *hAllMC_uUntagZuuTrkIsoOk_eta= (TH1F *) fileMC_Zuu->Get("huUntagZuuTrkIsoOk_eta");
	TH1F *hAllMC_uUntagZuud0Ok_eta= (TH1F *) fileMC_Zuu->Get("huUntagZuud0Ok_eta");
	TH1F *hAllMC_uUntagZuuAllOk_eta= (TH1F *) fileMC_Zuu->Get("huUntagZuuAllOk_eta");

	for(int i =  1; i < 39; i++){  
		TFile *fileMC_Zee = new TFile(Form("../output/Zee_MC_%d.root",mc_RunNumber[i]));
		TFile *fileMC_Zuu = new TFile(Form("../output/Zuu_MC_%d.root",mc_RunNumber[i]));

		TH1F *h0= (TH1F *) fileMC_Zee->Get("huUntagZee_eta");
		TH1F *h1= (TH1F *) fileMC_Zee->Get("huUntagZeeCaloIsoOk_eta");
		TH1F *h2= (TH1F *) fileMC_Zee->Get("huUntagZeeTrkIsoOk_eta");
		TH1F *h3= (TH1F *) fileMC_Zee->Get("huUntagZeed0Ok_eta");
		TH1F *h4= (TH1F *) fileMC_Zee->Get("huUntagZeeAllOk_eta");

		TH1F *h5= (TH1F *) fileMC_Zuu->Get("huUntagZuu_eta");
		TH1F *h6= (TH1F *) fileMC_Zuu->Get("huUntagZuuCaloIsoOk_eta");
		TH1F *h7= (TH1F *) fileMC_Zuu->Get("huUntagZuuTrkIsoOk_eta");
		TH1F *h8= (TH1F *) fileMC_Zuu->Get("huUntagZuud0Ok_eta");
		TH1F *h9= (TH1F *) fileMC_Zuu->Get("huUntagZuuAllOk_eta");

		hAllMC_uUntagZee_eta->Add(h0);
		hAllMC_uUntagZeeCaloIsoOk_eta->Add(h1);
		hAllMC_uUntagZeeTrkIsoOk_eta->Add(h2);
		hAllMC_uUntagZeed0Ok_eta->Add(h3);
		hAllMC_uUntagZeeAllOk_eta->Add(h4);

		hAllMC_uUntagZuu_eta->Add(h5);
		hAllMC_uUntagZuuCaloIsoOk_eta->Add(h6);
		hAllMC_uUntagZuuTrkIsoOk_eta->Add(h7);
		hAllMC_uUntagZuud0Ok_eta->Add(h8);
		hAllMC_uUntagZuuAllOk_eta->Add(h9);
	}

	double MC_Eff_ZeeCaloIsoOk_eta[20];
	double MC_Eff_ZeeCaloIsoOk_eta_err[20];
	double MC_Eff_ZeeTrkIsoOk_eta[20];
	double MC_Eff_ZeeTrkIsoOk_eta_err[20];
	double MC_Eff_Zeed0Ok_eta[20];
	double MC_Eff_Zeed0Ok_eta_err[20];
	double MC_Eff_ZeeAllOk_eta[20];
	double MC_Eff_ZeeAllOk_eta_err[20];

	double MC_Eff_ZuuCaloIsoOk_eta[20];
	double MC_Eff_ZuuCaloIsoOk_eta_err[20];
	double MC_Eff_ZuuTrkIsoOk_eta[20];
	double MC_Eff_ZuuTrkIsoOk_eta_err[20];
	double MC_Eff_Zuud0Ok_eta[20];
	double MC_Eff_Zuud0Ok_eta_err[20];
	double MC_Eff_ZuuAllOk_eta[20];
	double MC_Eff_ZuuAllOk_eta_err[20];

	for (int i = 0; i < 20; i++){
		MC_Eff_ZeeCaloIsoOk_eta[i] = hAllMC_uUntagZeeCaloIsoOk_eta->TH1::GetBinContent(i + 1) 
						/ hAllMC_uUntagZee_eta->TH1::GetBinContent(i + 1) * 100.0;
		MC_Eff_ZeeCaloIsoOk_eta_err[i] = error(hAllMC_uUntagZeeCaloIsoOk_eta->TH1::GetBinContent(i + 1), hAllMC_uUntagZee_eta->TH1::GetBinContent(i + 1)) * 100.0;
		MC_Eff_ZeeTrkIsoOk_eta[i] = hAllMC_uUntagZeeTrkIsoOk_eta->TH1::GetBinContent(i + 1) 
						/ hAllMC_uUntagZee_eta->TH1::GetBinContent(i + 1) * 100.0;
		MC_Eff_ZeeTrkIsoOk_eta_err[i] = error(hAllMC_uUntagZeeTrkIsoOk_eta->TH1::GetBinContent(i + 1), hAllMC_uUntagZee_eta->TH1::GetBinContent(i + 1)) * 100.0;
		MC_Eff_Zeed0Ok_eta[i] = hAllMC_uUntagZeed0Ok_eta->TH1::GetBinContent(i + 1) 
						/ hAllMC_uUntagZee_eta->TH1::GetBinContent(i + 1) * 100.0;
		MC_Eff_Zeed0Ok_eta_err[i] = error(hAllMC_uUntagZeed0Ok_eta->TH1::GetBinContent(i + 1), hAllMC_uUntagZee_eta->TH1::GetBinContent(i + 1)) * 100.0;
		MC_Eff_ZeeAllOk_eta[i] = hAllMC_uUntagZeeAllOk_eta->TH1::GetBinContent(i + 1) 
						/ hAllMC_uUntagZee_eta->TH1::GetBinContent(i + 1) * 100.0;
		MC_Eff_ZeeAllOk_eta_err[i] = error(hAllMC_uUntagZeeAllOk_eta->TH1::GetBinContent(i + 1), hAllMC_uUntagZee_eta->TH1::GetBinContent(i + 1)) * 100.0;

		MC_Eff_ZuuCaloIsoOk_eta[i] = hAllMC_uUntagZuuCaloIsoOk_eta->TH1::GetBinContent(i + 1) 
						/ hAllMC_uUntagZuu_eta->TH1::GetBinContent(i + 1) * 100.0;
		MC_Eff_ZuuCaloIsoOk_eta_err[i] = error(hAllMC_uUntagZuuCaloIsoOk_eta->TH1::GetBinContent(i + 1), hAllMC_uUntagZuu_eta->TH1::GetBinContent(i + 1)) * 100.0;
		MC_Eff_ZuuTrkIsoOk_eta[i] = hAllMC_uUntagZuuTrkIsoOk_eta->TH1::GetBinContent(i + 1) 
						/ hAllMC_uUntagZuu_eta->TH1::GetBinContent(i + 1) * 100.0;
		MC_Eff_ZuuTrkIsoOk_eta_err[i] = error(hAllMC_uUntagZuuTrkIsoOk_eta->TH1::GetBinContent(i + 1), hAllMC_uUntagZuu_eta->TH1::GetBinContent(i + 1)) * 100.0;
		MC_Eff_Zuud0Ok_eta[i] = hAllMC_uUntagZuud0Ok_eta->TH1::GetBinContent(i + 1) 
						/ hAllMC_uUntagZuu_eta->TH1::GetBinContent(i + 1) * 100.0;
		MC_Eff_Zuud0Ok_eta_err[i] = error(hAllMC_uUntagZuud0Ok_eta->TH1::GetBinContent(i + 1), hAllMC_uUntagZuu_eta->TH1::GetBinContent(i + 1)) * 100.0;
		MC_Eff_ZuuAllOk_eta[i] = hAllMC_uUntagZuuAllOk_eta->TH1::GetBinContent(i + 1) 
						/ hAllMC_uUntagZuu_eta->TH1::GetBinContent(i + 1) * 100.0;
		MC_Eff_ZuuAllOk_eta_err[i] = error(hAllMC_uUntagZuuAllOk_eta->TH1::GetBinContent(i + 1), hAllMC_uUntagZuu_eta->TH1::GetBinContent(i + 1)) * 100.0;

	}

	//--------------------------------------//
	// Draw Graph	- Calo Iso		//
	//--------------------------------------//
	if(PlotCaloIso){
		TGraphErrors*geData_CaloIso_Zee= new TGraphErrors;
		TGraphErrors*geMc_CaloIso_Zee= new TGraphErrors;
		TGraphErrors*geData_CaloIso_Zuu= new TGraphErrors;
		TGraphErrors*geMc_CaloIso_Zuu= new TGraphErrors;

		const int nbins=sizeof(Eff_ZeeCaloIsoOk_eta)/sizeof(double);
		for(int i=0;i<nbins;i++)
		{
			double x_data = 0.5*(etaBins[i]+etaBins[i+1]);
			double x_mc = x_data;

			geData_CaloIso_Zee->SetPoint(i,x_data,Eff_ZeeCaloIsoOk_eta[i]);
			geData_CaloIso_Zee->SetPointError(i,0,Eff_ZeeCaloIsoOk_eta_err[i]);
			geMc_CaloIso_Zee->SetPoint(i,x_mc,MC_Eff_ZeeCaloIsoOk_eta[i]);
			geMc_CaloIso_Zee->SetPointError(i,0,MC_Eff_ZeeCaloIsoOk_eta_err[i]);

			geData_CaloIso_Zuu->SetPoint(i,x_data,Eff_ZuuCaloIsoOk_eta[i]);
			geData_CaloIso_Zuu->SetPointError(i,0,Eff_ZuuCaloIsoOk_eta_err[i]);
			geMc_CaloIso_Zuu->SetPoint(i,x_mc,MC_Eff_ZuuCaloIsoOk_eta[i]);
			geMc_CaloIso_Zuu->SetPointError(i,0,MC_Eff_ZuuCaloIsoOk_eta_err[i]);
		
		}

		SetGraphStyle(geData_CaloIso_Zee,20,kRed,1,kRed,0);
		SetGraphStyle(geMc_CaloIso_Zee,20,kBlue,1,kBlue,0);

		SetGraphStyle(geData_CaloIso_Zuu,20,kGreen,1,kGreen,0);
		SetGraphStyle(geMc_CaloIso_Zuu,20,kMagenta,1,kMagenta,0);
	
		TCanvas*cnvs_CaloIso =new TCanvas;
		TH1F*hFrame=cnvs_CaloIso->DrawFrame(-2.47,0,2.47,100);
		hFrame->SetXTitle("#eta_{additional muon}");
		hFrame->SetYTitle("Calo Iso efficiency [%]");
		cnvs_CaloIso->SetGridy();
		DrawGridx(hFrame,etaBins,nbins);
		geMc_CaloIso_Zee->Draw("PE same");
		geData_CaloIso_Zee->Draw("PE same");
		geMc_CaloIso_Zuu->Draw("PE same");
		geData_CaloIso_Zuu->Draw("PE same");
	
		TLegend*leg1CaloIso=new TLegend(0.30,0.70,0.60,0.90);
		leg1CaloIso->SetFillColor(0);
		leg1CaloIso->SetShadowColor(0);
		leg1CaloIso->SetBorderSize(0);
		leg1CaloIso->SetHeader("Z#rightarrow ee #int L dt #approx 4.9 fb^{-1}");
		leg1CaloIso->AddEntry(geData_CaloIso_Zee,"2011 data ","lp");
		leg1CaloIso->AddEntry(geMc_CaloIso_Zee,"MC11c","lp");
		leg1CaloIso->Draw();

		TLegend*leg2CaloIso=new TLegend(0.55,0.73,0.85,0.90);
		leg2CaloIso->SetFillColor(0);
		leg2CaloIso->SetShadowColor(0);
		leg2CaloIso->SetBorderSize(0);
		leg2CaloIso->SetHeader("Z#rightarrow #mu#mu #int L dt #approx 4.8 fb^{-1}");
		leg2CaloIso->AddEntry(geData_CaloIso_Zuu,"2011 data ","lp");
		leg2CaloIso->AddEntry(geMc_CaloIso_Zuu,"MC11c","lp");
		leg2CaloIso->Draw();

		cnvs_CaloIso->SaveAs("eff_CaloIso_uUntagetaBin2011.png");
	}
	//--------------------------------------//
	// Draw Graph	- Track Iso		//
	//--------------------------------------//
	if(PlotTrkIso){
		TGraphErrors*geData_TrkIso_Zee= new TGraphErrors;
		TGraphErrors*geMc_TrkIso_Zee= new TGraphErrors;
		TGraphErrors*geData_TrkIso_Zuu= new TGraphErrors;
		TGraphErrors*geMc_TrkIso_Zuu= new TGraphErrors;

		const int nbins=sizeof(Eff_ZeeTrkIsoOk_eta)/sizeof(double);
		for(int i=0;i<nbins;i++)
		{
			double x_data = 0.5*(etaBins[i]+etaBins[i+1]);
			double x_mc = x_data;

			geData_TrkIso_Zee->SetPoint(i,x_data,Eff_ZeeTrkIsoOk_eta[i]);
			geData_TrkIso_Zee->SetPointError(i,0,Eff_ZeeTrkIsoOk_eta_err[i]);
			geMc_TrkIso_Zee->SetPoint(i,x_mc,MC_Eff_ZeeTrkIsoOk_eta[i]);
			geMc_TrkIso_Zee->SetPointError(i,0,MC_Eff_ZeeTrkIsoOk_eta_err[i]);

			geData_TrkIso_Zuu->SetPoint(i,x_data,Eff_ZuuTrkIsoOk_eta[i]);
			geData_TrkIso_Zuu->SetPointError(i,0,Eff_ZuuTrkIsoOk_eta_err[i]);
			geMc_TrkIso_Zuu->SetPoint(i,x_mc,MC_Eff_ZuuTrkIsoOk_eta[i]);
			geMc_TrkIso_Zuu->SetPointError(i,0,MC_Eff_ZuuTrkIsoOk_eta_err[i]);
		
		}

		SetGraphStyle(geData_TrkIso_Zee,20,kRed,1,kRed,0);
		SetGraphStyle(geMc_TrkIso_Zee,20,kBlue,1,kBlue,0);

		SetGraphStyle(geData_TrkIso_Zuu,20,kGreen,1,kGreen,0);
		SetGraphStyle(geMc_TrkIso_Zuu,20,kMagenta,1,kMagenta,0);
	
		TCanvas*cnvs_TrkIso =new TCanvas;
		TH1F*hFrame=cnvs_TrkIso->DrawFrame(-2.47,0,2.47,100);
		hFrame->SetXTitle("#eta_{additional muon}");
		hFrame->SetYTitle("Track Iso efficiency [%]");
		cnvs_TrkIso->SetGridy();
		DrawGridx(hFrame,etaBins,nbins);
		geMc_TrkIso_Zee->Draw("PE same");
		geData_TrkIso_Zee->Draw("PE same");
		geMc_TrkIso_Zuu->Draw("PE same");
		geData_TrkIso_Zuu->Draw("PE same");
	
		TLegend*leg1TrkIso=new TLegend(0.30,0.70,0.60,0.90);
		leg1TrkIso->SetFillColor(0);
		leg1TrkIso->SetShadowColor(0);
		leg1TrkIso->SetBorderSize(0);
		leg1TrkIso->SetHeader("Z#rightarrow ee #int L dt #approx 4.9 fb^{-1}");
		leg1TrkIso->AddEntry(geData_TrkIso_Zee,"2011 data","lp");
		leg1TrkIso->AddEntry(geMc_TrkIso_Zee,"MC11c","lp");
		leg1TrkIso->Draw();

		TLegend*leg2TrkIso=new TLegend(0.55,0.73,0.85,0.90);
		leg2TrkIso->SetFillColor(0);
		leg2TrkIso->SetShadowColor(0);
		leg2TrkIso->SetBorderSize(0);
		leg2TrkIso->SetHeader("Z#rightarrow #mu#mu #int L dt #approx 4.8 fb^{-1}");
		leg2TrkIso->AddEntry(geData_TrkIso_Zuu,"2011 data ","lp");
		leg2TrkIso->AddEntry(geMc_TrkIso_Zuu,"MC11c","lp");
		leg2TrkIso->Draw();

		cnvs_TrkIso->SaveAs("eff_TrkIso_uUntagetaBin2011.png");
	}

	//--------------------------------------//
	// Draw Graph	- d0 significance	//
	//--------------------------------------//
	if(Plotd0sig){
		TGraphErrors*geData_d0_Zee= new TGraphErrors;
		TGraphErrors*geMc_d0_Zee= new TGraphErrors;	
		TGraphErrors*geData_d0_Zuu= new TGraphErrors;
		TGraphErrors*geMc_d0_Zuu= new TGraphErrors;

		const int nbins=sizeof(Eff_Zeed0Ok_eta)/sizeof(double);
		for(int i=0;i<nbins;i++)
		{
			double x_data = 0.5*(etaBins[i]+etaBins[i+1]);
			double x_mc = x_data;

			geData_d0_Zee->SetPoint(i,x_data,Eff_Zeed0Ok_eta[i]);
			geData_d0_Zee->SetPointError(i,0,Eff_Zeed0Ok_eta_err[i]);
			geMc_d0_Zee->SetPoint(i,x_mc,MC_Eff_Zeed0Ok_eta[i]);
			geMc_d0_Zee->SetPointError(i,0,MC_Eff_Zeed0Ok_eta_err[i]);

			geData_d0_Zuu->SetPoint(i,x_data,Eff_Zuud0Ok_eta[i]);
			geData_d0_Zuu->SetPointError(i,0,Eff_Zuud0Ok_eta_err[i]);
			geMc_d0_Zuu->SetPoint(i,x_mc,MC_Eff_Zuud0Ok_eta[i]);
			geMc_d0_Zuu->SetPointError(i,0,MC_Eff_Zuud0Ok_eta_err[i]);
		}

		SetGraphStyle(geData_d0_Zee,20,kRed,1,kRed,0);
		SetGraphStyle(geMc_d0_Zee,20,kBlue,1,kBlue,0);
		SetGraphStyle(geData_d0_Zuu,20,kGreen,1,kGreen,0);
		SetGraphStyle(geMc_d0_Zuu,20,kMagenta,1,kMagenta,0);
	
		TCanvas*cnvs_d0 =new TCanvas;
		TH1F*hFrame=cnvs_d0->DrawFrame(-2.47,0,2.47,100);
		hFrame->SetXTitle("#eta_{additional muon}");
		hFrame->SetYTitle("d0 significance efficiency [%]");
		cnvs_d0->SetGridy();
		DrawGridx(hFrame,etaBins,nbins);
		geMc_d0_Zee->Draw("PE same");
		geData_d0_Zee->Draw("PE same");
		geMc_d0_Zuu->Draw("PE same");
		geData_d0_Zuu->Draw("PE same");
	
		TLegend*leg1d0=new TLegend(0.30,0.30,0.60,0.50);
		leg1d0->SetFillColor(0);
		leg1d0->SetShadowColor(0);
		leg1d0->SetBorderSize(0);
		leg1d0->SetHeader("Z#rightarrow ee #int L dt #approx 4.9 fb^{-1}");
		leg1d0->AddEntry(geData_d0_Zee,"2011 data","lp");
		leg1d0->AddEntry(geMc_d0_Zee,"MC11c","lp");
		leg1d0->Draw();

		TLegend*leg2d0=new TLegend(0.60,0.30,0.90,0.50);
		leg2d0->SetFillColor(0);
		leg2d0->SetShadowColor(0);
		leg2d0->SetBorderSize(0);
		leg2d0->SetHeader("Z#rightarrow #mu#mu #int L dt #approx 4.8 fb^{-1}");
		leg2d0->AddEntry(geData_d0_Zuu,"2011 data ","lp");
		leg2d0->AddEntry(geMc_d0_Zuu,"MC11c","lp");
		leg2d0->Draw();

		cnvs_d0->SaveAs("eff_d0_uUntagetaBin2011.png");
	}

	//--------------------------------------//
	// Draw Graph	- All 			//
	//--------------------------------------//
	if(PlotAll){
		TGraphErrors*geData_All_Zee= new TGraphErrors;
		TGraphErrors*geMc_All_Zee= new TGraphErrors;
		TGraphErrors*geData_All_Zuu= new TGraphErrors;
		TGraphErrors*geMc_All_Zuu= new TGraphErrors;
		const int nbins=sizeof(Eff_ZeeAllOk_eta)/sizeof(double);

		for(int i=0;i<nbins;i++)
		{
			double x_data = 0.5*(etaBins[i]+etaBins[i+1]);
			double x_mc = x_data;

			geData_All_Zee->SetPoint(i,x_data,Eff_ZeeAllOk_eta[i]);
			geData_All_Zee->SetPointError(i,0,Eff_ZeeAllOk_eta_err[i]);
			geMc_All_Zee->SetPoint(i,x_mc,MC_Eff_ZeeAllOk_eta[i]);
			geMc_All_Zee->SetPointError(i,0,MC_Eff_ZeeAllOk_eta_err[i]);

			geData_All_Zuu->SetPoint(i,x_data,Eff_ZuuAllOk_eta[i]);
			geData_All_Zuu->SetPointError(i,0,Eff_ZuuAllOk_eta_err[i]);
			geMc_All_Zuu->SetPoint(i,x_mc,MC_Eff_ZuuAllOk_eta[i]);
			geMc_All_Zuu->SetPointError(i,0,MC_Eff_ZuuAllOk_eta_err[i]);	
		}

		SetGraphStyle(geData_All_Zee,20,kRed,1,kRed,0);
		SetGraphStyle(geMc_All_Zee,20,kBlue,1,kBlue,0);
		SetGraphStyle(geData_All_Zuu,20,kGreen,1,kGreen,0);
		SetGraphStyle(geMc_All_Zuu,20,kMagenta,1,kMagenta,0);
	
		TCanvas*cnvs_All =new TCanvas;
		TH1F*hFrame=cnvs_All->DrawFrame(-2.47,0,2.47,100);
		hFrame->SetXTitle("#eta_{additional muon}");
		hFrame->SetYTitle("All cuts efficiency [%]");
		cnvs_All->SetGridy();
		DrawGridx(hFrame,etaBins,nbins);
		geMc_All_Zee->Draw("PE same");
		geData_All_Zee->Draw("PE same");
		geMc_All_Zuu->Draw("PE same");
		geData_All_Zuu->Draw("PE same");
	
		TLegend*leg1All=new TLegend(0.30,0.70,0.60,0.90);
		leg1All->SetFillColor(0);
		leg1All->SetShadowColor(0);
		leg1All->SetBorderSize(0);
		leg1All->SetHeader("Z#rightarrow ee #int L dt #approx 4.9 fb^{-1}");
		leg1All->AddEntry(geData_All_Zee,"2011 data","lp");
		leg1All->AddEntry(geMc_All_Zee,"MC11c","lp");
		leg1All->Draw();

		TLegend*leg2All=new TLegend(0.55,0.73,0.85,0.90);
		leg2All->SetFillColor(0);
		leg2All->SetShadowColor(0);
		leg2All->SetBorderSize(0);
		leg2All->SetHeader("Z#rightarrow #mu#mu #int L dt #approx 4.8 fb^{-1}");
		leg2All->AddEntry(geData_All_Zuu,"2011 data ","lp");
		leg2All->AddEntry(geMc_All_Zuu,"MC11c","lp");
		leg2All->Draw();

		cnvs_All->SaveAs("eff_All_uUntagetaBin2011.png");
	}
}

//--------------------------------------------------------------------------//

void Eff_uUntag_pt(bool PlotCaloIso, bool PlotTrkIso, bool Plotd0sig, bool PlotAll)
{
	//--------------------------------------//
	// Data					//
	//--------------------------------------//

	TFile *fileData_Zee = new TFile("../output/Zee_DATA.root");
	TFile *fileData_Zuu = new TFile("../output/Zuu_DATA.root");

	const double ptBins[]={7, 12, 15, 20, 25, 30, 35, 40, 45, 50};

	TH1F *huUntagZee_pt = (TH1F *) fileData_Zee->Get("huUntagZee_pt");
	TH1F *huUntagZeeCaloIsoOk_pt = (TH1F *) fileData_Zee->Get("huUntagZeeCaloIsoOk_pt");
	TH1F *huUntagZeeTrkIsoOk_pt = (TH1F *) fileData_Zee->Get("huUntagZeeTrkIsoOk_pt");
	TH1F *huUntagZeed0Ok_pt = (TH1F *) fileData_Zee->Get("huUntagZeed0Ok_pt");
	TH1F *huUntagZeeAllOk_pt = (TH1F *) fileData_Zee->Get("huUntagZeeAllOk_pt");

	TH1F *huUntagZuu_pt = (TH1F *) fileData_Zuu->Get("huUntagZuu_pt");
	TH1F *huUntagZuuCaloIsoOk_pt = (TH1F *) fileData_Zuu->Get("huUntagZuuCaloIsoOk_pt");
	TH1F *huUntagZuuTrkIsoOk_pt = (TH1F *) fileData_Zuu->Get("huUntagZuuTrkIsoOk_pt");
	TH1F *huUntagZuud0Ok_pt = (TH1F *) fileData_Zuu->Get("huUntagZuud0Ok_pt");
	TH1F *huUntagZuuAllOk_pt = (TH1F *) fileData_Zuu->Get("huUntagZuuAllOk_pt");

	double Eff_ZeeCaloIsoOk_pt[9];
	double Eff_ZeeCaloIsoOk_pt_err[9];
	double Eff_ZeeTrkIsoOk_pt[9];
	double Eff_ZeeTrkIsoOk_pt_err[9];
	double Eff_Zeed0Ok_pt[9];
	double Eff_Zeed0Ok_pt_err[9];
	double Eff_ZeeAllOk_pt[9];
	double Eff_ZeeAllOk_pt_err[9];

	double Eff_ZuuCaloIsoOk_pt[9];
	double Eff_ZuuCaloIsoOk_pt_err[9];
	double Eff_ZuuTrkIsoOk_pt[9];
	double Eff_ZuuTrkIsoOk_pt_err[9];
	double Eff_Zuud0Ok_pt[9];
	double Eff_Zuud0Ok_pt_err[9];
	double Eff_ZuuAllOk_pt[9];
	double Eff_ZuuAllOk_pt_err[9];

	const int nbins=sizeof(Eff_ZeeCaloIsoOk_pt)/sizeof(double);

	std::cout<< nbins <<endl;

	for (int i = 0; i < nbins; i++){
		Eff_ZeeCaloIsoOk_pt[i] = huUntagZeeCaloIsoOk_pt->TH1::Integral(huUntagZeeCaloIsoOk_pt->FindBin(ptBins[i]),huUntagZeeCaloIsoOk_pt->FindBin(ptBins[i+1])) 
						/ huUntagZee_pt->TH1::Integral(huUntagZeeCaloIsoOk_pt->FindBin(ptBins[i]),huUntagZeeCaloIsoOk_pt->FindBin(ptBins[i+1])) * 100.0;
		Eff_ZeeCaloIsoOk_pt_err[i] = error(huUntagZeeCaloIsoOk_pt->TH1::Integral(huUntagZeeCaloIsoOk_pt->FindBin(ptBins[i]),huUntagZeeCaloIsoOk_pt->FindBin(ptBins[i+1])), huUntagZee_pt->TH1::Integral(huUntagZeeCaloIsoOk_pt->FindBin(ptBins[i]),huUntagZeeCaloIsoOk_pt->FindBin(ptBins[i+1]))) * 100.0;

		Eff_ZeeTrkIsoOk_pt[i] = huUntagZeeTrkIsoOk_pt->TH1::Integral(huUntagZeeTrkIsoOk_pt->FindBin(ptBins[i]),huUntagZeeTrkIsoOk_pt->FindBin(ptBins[i+1])) 
						/ huUntagZee_pt->TH1::Integral(huUntagZeeTrkIsoOk_pt->FindBin(ptBins[i]),huUntagZeeTrkIsoOk_pt->FindBin(ptBins[i+1])) * 100.0;
		Eff_ZeeTrkIsoOk_pt_err[i] = error(huUntagZeeTrkIsoOk_pt->TH1::Integral(huUntagZeeTrkIsoOk_pt->FindBin(ptBins[i]),huUntagZeeTrkIsoOk_pt->FindBin(ptBins[i+1])), huUntagZee_pt->TH1::Integral(huUntagZeeTrkIsoOk_pt->FindBin(ptBins[i]),huUntagZeeTrkIsoOk_pt->FindBin(ptBins[i+1]))) * 100.0;

		Eff_Zeed0Ok_pt[i] = huUntagZeed0Ok_pt->TH1::Integral(huUntagZeed0Ok_pt->FindBin(ptBins[i]),huUntagZeed0Ok_pt->FindBin(ptBins[i+1])) 
						/ huUntagZee_pt->TH1::Integral(huUntagZeed0Ok_pt->FindBin(ptBins[i]),huUntagZeed0Ok_pt->FindBin(ptBins[i+1])) * 100.0;
		Eff_Zeed0Ok_pt_err[i] = error(huUntagZeed0Ok_pt->TH1::Integral(huUntagZeed0Ok_pt->FindBin(ptBins[i]),huUntagZeed0Ok_pt->FindBin(ptBins[i+1])), huUntagZee_pt->TH1::Integral(huUntagZeed0Ok_pt->FindBin(ptBins[i]),huUntagZeed0Ok_pt->FindBin(ptBins[i+1]))) * 100.0;

		Eff_ZeeAllOk_pt[i] = huUntagZeeAllOk_pt->TH1::Integral(huUntagZeeAllOk_pt->FindBin(ptBins[i]),huUntagZeeAllOk_pt->FindBin(ptBins[i+1])) 
						/ huUntagZee_pt->TH1::Integral(huUntagZeeAllOk_pt->FindBin(ptBins[i]),huUntagZeeAllOk_pt->FindBin(ptBins[i+1])) * 100.0;
		Eff_ZeeAllOk_pt_err[i] = error(huUntagZeeAllOk_pt->TH1::Integral(huUntagZeeAllOk_pt->FindBin(ptBins[i]),huUntagZeeAllOk_pt->FindBin(ptBins[i+1])), huUntagZee_pt->TH1::Integral(huUntagZeeAllOk_pt->FindBin(ptBins[i]),huUntagZeeAllOk_pt->FindBin(ptBins[i+1]))) * 100.0;

		Eff_ZuuCaloIsoOk_pt[i] = huUntagZuuCaloIsoOk_pt->TH1::Integral(huUntagZuuCaloIsoOk_pt->FindBin(ptBins[i]),huUntagZuuCaloIsoOk_pt->FindBin(ptBins[i+1])) 
						/ huUntagZuu_pt->TH1::Integral(huUntagZuuCaloIsoOk_pt->FindBin(ptBins[i]),huUntagZuuCaloIsoOk_pt->FindBin(ptBins[i+1])) * 100.0;
		Eff_ZuuCaloIsoOk_pt_err[i] = error(huUntagZuuCaloIsoOk_pt->TH1::Integral(huUntagZuuCaloIsoOk_pt->FindBin(ptBins[i]),huUntagZuuCaloIsoOk_pt->FindBin(ptBins[i+1])), huUntagZuu_pt->TH1::Integral(huUntagZuuCaloIsoOk_pt->FindBin(ptBins[i]),huUntagZuuCaloIsoOk_pt->FindBin(ptBins[i+1]))) * 100.0;

		Eff_ZuuTrkIsoOk_pt[i] = huUntagZuuTrkIsoOk_pt->TH1::Integral(huUntagZuuTrkIsoOk_pt->FindBin(ptBins[i]),huUntagZuuTrkIsoOk_pt->FindBin(ptBins[i+1])) 
						/ huUntagZuu_pt->TH1::Integral(huUntagZuuTrkIsoOk_pt->FindBin(ptBins[i]),huUntagZuuTrkIsoOk_pt->FindBin(ptBins[i+1])) * 100.0;
		Eff_ZuuTrkIsoOk_pt_err[i] = error(huUntagZuuTrkIsoOk_pt->TH1::Integral(huUntagZuuTrkIsoOk_pt->FindBin(ptBins[i]),huUntagZuuTrkIsoOk_pt->FindBin(ptBins[i+1])), huUntagZuu_pt->TH1::Integral(huUntagZuuTrkIsoOk_pt->FindBin(ptBins[i]),huUntagZuuTrkIsoOk_pt->FindBin(ptBins[i+1]))) * 100.0;

		Eff_Zuud0Ok_pt[i] = huUntagZuud0Ok_pt->TH1::Integral(huUntagZuud0Ok_pt->FindBin(ptBins[i]),huUntagZuud0Ok_pt->FindBin(ptBins[i+1])) 
						/ huUntagZuu_pt->TH1::Integral(huUntagZuud0Ok_pt->FindBin(ptBins[i]),huUntagZuud0Ok_pt->FindBin(ptBins[i+1])) * 100.0;
		Eff_Zuud0Ok_pt_err[i] = error(huUntagZuud0Ok_pt->TH1::Integral(huUntagZuud0Ok_pt->FindBin(ptBins[i]),huUntagZuud0Ok_pt->FindBin(ptBins[i+1])), huUntagZuu_pt->TH1::Integral(huUntagZuud0Ok_pt->FindBin(ptBins[i]),huUntagZuud0Ok_pt->FindBin(ptBins[i+1]))) * 100.0;

		Eff_ZuuAllOk_pt[i] = huUntagZuuAllOk_pt->TH1::Integral(huUntagZuuAllOk_pt->FindBin(ptBins[i]),huUntagZuuAllOk_pt->FindBin(ptBins[i+1])) 
						/ huUntagZuu_pt->TH1::Integral(huUntagZuuAllOk_pt->FindBin(ptBins[i]),huUntagZuuAllOk_pt->FindBin(ptBins[i+1])) * 100.0;
		Eff_ZuuAllOk_pt_err[i] = error(huUntagZuuAllOk_pt->TH1::Integral(huUntagZuuAllOk_pt->FindBin(ptBins[i]),huUntagZuuAllOk_pt->FindBin(ptBins[i+1])), huUntagZuu_pt->TH1::Integral(huUntagZuuAllOk_pt->FindBin(ptBins[i]),huUntagZuuAllOk_pt->FindBin(ptBins[i+1]))) * 100.0;

	}
	//--------------------------------------//
	// MC 					//
	//--------------------------------------//

	Int_t mc_RunNumber[] = {107650,107651,107652,107653,107654,107655,               //Zee + light jets
				107660,107661,107662,107663,107664,107665, 		 //Zuu + light jets
				116950,116951,116952,116953,116960,116961,116962,116963, //Zeebb 4LepM + bgdVeto4LepM
				116955,116956,116957,116958,116965,116966,116967,116968,  //Zuubb 4LepM + bgdVeto4LepM
				128971,							 //PythiaWZ_inclusive
				105200,							 //T1_McAtNlo_Jimmy
				116601,116602,116603,126859,126860,126861,126862,126863,126864//ZZ
				};



	TFile *fileMC_Zee = new TFile(Form("../output/Zee_MC_%d.root",mc_RunNumber[0]));
	TFile *fileMC_Zuu = new TFile(Form("../output/Zuu_MC_%d.root",mc_RunNumber[0]));

	TH1F *hAllMC_uUntagZee_pt= (TH1F *) fileMC_Zee->Get("huUntagZee_pt");
	TH1F *hAllMC_uUntagZeeCaloIsoOk_pt= (TH1F *) fileMC_Zee->Get("huUntagZeeCaloIsoOk_pt");
	TH1F *hAllMC_uUntagZeeTrkIsoOk_pt= (TH1F *) fileMC_Zee->Get("huUntagZeeTrkIsoOk_pt");
	TH1F *hAllMC_uUntagZeed0Ok_pt= (TH1F *) fileMC_Zee->Get("huUntagZeed0Ok_pt");
	TH1F *hAllMC_uUntagZeeAllOk_pt= (TH1F *) fileMC_Zee->Get("huUntagZeeAllOk_pt");

	TH1F *hAllMC_uUntagZuu_pt= (TH1F *) fileMC_Zuu->Get("huUntagZuu_pt");
	TH1F *hAllMC_uUntagZuuCaloIsoOk_pt= (TH1F *) fileMC_Zuu->Get("huUntagZuuCaloIsoOk_pt");
	TH1F *hAllMC_uUntagZuuTrkIsoOk_pt= (TH1F *) fileMC_Zuu->Get("huUntagZuuTrkIsoOk_pt");
	TH1F *hAllMC_uUntagZuud0Ok_pt= (TH1F *) fileMC_Zuu->Get("huUntagZuud0Ok_pt");
	TH1F *hAllMC_uUntagZuuAllOk_pt= (TH1F *) fileMC_Zuu->Get("huUntagZuuAllOk_pt");

	for(int i =  1; i < 39; i++){  
		TFile *fileMC_Zee = new TFile(Form("../output/Zee_MC_%d.root",mc_RunNumber[i]));
		TFile *fileMC_Zuu = new TFile(Form("../output/Zuu_MC_%d.root",mc_RunNumber[i]));

		TH1F *h0= (TH1F *) fileMC_Zee->Get("huUntagZee_pt");
		TH1F *h1= (TH1F *) fileMC_Zee->Get("huUntagZeeCaloIsoOk_pt");
		TH1F *h2= (TH1F *) fileMC_Zee->Get("huUntagZeeTrkIsoOk_pt");
		TH1F *h3= (TH1F *) fileMC_Zee->Get("huUntagZeed0Ok_pt");
		TH1F *h4= (TH1F *) fileMC_Zee->Get("huUntagZeeAllOk_pt");

		TH1F *h5= (TH1F *) fileMC_Zuu->Get("huUntagZuu_pt");
		TH1F *h6= (TH1F *) fileMC_Zuu->Get("huUntagZuuCaloIsoOk_pt");
		TH1F *h7= (TH1F *) fileMC_Zuu->Get("huUntagZuuTrkIsoOk_pt");
		TH1F *h8= (TH1F *) fileMC_Zuu->Get("huUntagZuud0Ok_pt");
		TH1F *h9= (TH1F *) fileMC_Zuu->Get("huUntagZuuAllOk_pt");

		hAllMC_uUntagZee_pt->Add(h0);
		hAllMC_uUntagZeeCaloIsoOk_pt->Add(h1);
		hAllMC_uUntagZeeTrkIsoOk_pt->Add(h2);
		hAllMC_uUntagZeed0Ok_pt->Add(h3);
		hAllMC_uUntagZeeAllOk_pt->Add(h4);

		hAllMC_uUntagZuu_pt->Add(h5);
		hAllMC_uUntagZuuCaloIsoOk_pt->Add(h6);
		hAllMC_uUntagZuuTrkIsoOk_pt->Add(h7);
		hAllMC_uUntagZuud0Ok_pt->Add(h8);
		hAllMC_uUntagZuuAllOk_pt->Add(h9);
	}

	double MC_Eff_ZeeCaloIsoOk_pt[9];
	double MC_Eff_ZeeCaloIsoOk_pt_err[9];
	double MC_Eff_ZeeTrkIsoOk_pt[9];
	double MC_Eff_ZeeTrkIsoOk_pt_err[9];
	double MC_Eff_Zeed0Ok_pt[9];
	double MC_Eff_Zeed0Ok_pt_err[9];
	double MC_Eff_ZeeAllOk_pt[9];
	double MC_Eff_ZeeAllOk_pt_err[9];

	double MC_Eff_ZuuCaloIsoOk_pt[9];
	double MC_Eff_ZuuCaloIsoOk_pt_err[9];
	double MC_Eff_ZuuTrkIsoOk_pt[9];
	double MC_Eff_ZuuTrkIsoOk_pt_err[9];
	double MC_Eff_Zuud0Ok_pt[9];
	double MC_Eff_Zuud0Ok_pt_err[9];
	double MC_Eff_ZuuAllOk_pt[9];
	double MC_Eff_ZuuAllOk_pt_err[9];

	for (int i = 0; i < nbins; i++){
		MC_Eff_ZeeCaloIsoOk_pt[i] = hAllMC_uUntagZeeCaloIsoOk_pt->TH1::Integral(hAllMC_uUntagZeeCaloIsoOk_pt->FindBin(ptBins[i]),hAllMC_uUntagZeeCaloIsoOk_pt->FindBin(ptBins[i+1])) 
						/ hAllMC_uUntagZee_pt->TH1::Integral(hAllMC_uUntagZeeCaloIsoOk_pt->FindBin(ptBins[i]),hAllMC_uUntagZeeCaloIsoOk_pt->FindBin(ptBins[i+1])) * 100.0;
		MC_Eff_ZeeCaloIsoOk_pt_err[i] = error(hAllMC_uUntagZeeCaloIsoOk_pt->TH1::Integral(hAllMC_uUntagZeeCaloIsoOk_pt->FindBin(ptBins[i]),hAllMC_uUntagZeeCaloIsoOk_pt->FindBin(ptBins[i+1])), hAllMC_uUntagZee_pt->TH1::Integral(hAllMC_uUntagZeeCaloIsoOk_pt->FindBin(ptBins[i]),hAllMC_uUntagZeeCaloIsoOk_pt->FindBin(ptBins[i+1]))) * 100.0;

		MC_Eff_ZeeTrkIsoOk_pt[i] = hAllMC_uUntagZeeTrkIsoOk_pt->TH1::Integral(hAllMC_uUntagZeeTrkIsoOk_pt->FindBin(ptBins[i]),hAllMC_uUntagZeeTrkIsoOk_pt->FindBin(ptBins[i+1])) 
						/ hAllMC_uUntagZee_pt->TH1::Integral(hAllMC_uUntagZeeTrkIsoOk_pt->FindBin(ptBins[i]),hAllMC_uUntagZeeTrkIsoOk_pt->FindBin(ptBins[i+1])) * 100.0;
		MC_Eff_ZeeTrkIsoOk_pt_err[i] = error(hAllMC_uUntagZeeTrkIsoOk_pt->TH1::Integral(hAllMC_uUntagZeeTrkIsoOk_pt->FindBin(ptBins[i]),hAllMC_uUntagZeeTrkIsoOk_pt->FindBin(ptBins[i+1])), hAllMC_uUntagZee_pt->TH1::Integral(hAllMC_uUntagZeeTrkIsoOk_pt->FindBin(ptBins[i]),hAllMC_uUntagZeeTrkIsoOk_pt->FindBin(ptBins[i+1]))) * 100.0;

		MC_Eff_Zeed0Ok_pt[i] = hAllMC_uUntagZeed0Ok_pt->TH1::Integral(hAllMC_uUntagZeed0Ok_pt->FindBin(ptBins[i]),hAllMC_uUntagZeed0Ok_pt->FindBin(ptBins[i+1])) 
						/ hAllMC_uUntagZee_pt->TH1::Integral(hAllMC_uUntagZeed0Ok_pt->FindBin(ptBins[i]),hAllMC_uUntagZeed0Ok_pt->FindBin(ptBins[i+1])) * 100.0;
		MC_Eff_Zeed0Ok_pt_err[i] = error(hAllMC_uUntagZeed0Ok_pt->TH1::Integral(hAllMC_uUntagZeed0Ok_pt->FindBin(ptBins[i]),hAllMC_uUntagZeed0Ok_pt->FindBin(ptBins[i+1])), hAllMC_uUntagZee_pt->TH1::Integral(hAllMC_uUntagZeed0Ok_pt->FindBin(ptBins[i]),hAllMC_uUntagZeed0Ok_pt->FindBin(ptBins[i+1])) )* 100.0;

		MC_Eff_ZeeAllOk_pt[i] = hAllMC_uUntagZeeAllOk_pt->TH1::Integral(hAllMC_uUntagZeeAllOk_pt->FindBin(ptBins[i]),hAllMC_uUntagZeeAllOk_pt->FindBin(ptBins[i+1])) 
						/ hAllMC_uUntagZee_pt->TH1::Integral(hAllMC_uUntagZeeAllOk_pt->FindBin(ptBins[i]),hAllMC_uUntagZeeAllOk_pt->FindBin(ptBins[i+1])) * 100.0;
		MC_Eff_ZeeAllOk_pt_err[i] = error(hAllMC_uUntagZeeAllOk_pt->TH1::Integral(hAllMC_uUntagZeeAllOk_pt->FindBin(ptBins[i]),hAllMC_uUntagZeeAllOk_pt->FindBin(ptBins[i+1])), hAllMC_uUntagZee_pt->TH1::Integral(hAllMC_uUntagZeeAllOk_pt->FindBin(ptBins[i]),hAllMC_uUntagZeeAllOk_pt->FindBin(ptBins[i+1]))) * 100.0;

		MC_Eff_ZuuCaloIsoOk_pt[i] = hAllMC_uUntagZuuCaloIsoOk_pt->TH1::Integral(hAllMC_uUntagZuuCaloIsoOk_pt->FindBin(ptBins[i]),hAllMC_uUntagZuuCaloIsoOk_pt->FindBin(ptBins[i+1])) 
						/ hAllMC_uUntagZuu_pt->TH1::Integral(hAllMC_uUntagZuuCaloIsoOk_pt->FindBin(ptBins[i]),hAllMC_uUntagZuuCaloIsoOk_pt->FindBin(ptBins[i+1])) * 100.0;
		MC_Eff_ZuuCaloIsoOk_pt_err[i] = error(hAllMC_uUntagZuuCaloIsoOk_pt->TH1::Integral(hAllMC_uUntagZuuCaloIsoOk_pt->FindBin(ptBins[i]),hAllMC_uUntagZuuCaloIsoOk_pt->FindBin(ptBins[i+1])), hAllMC_uUntagZuu_pt->TH1::Integral(hAllMC_uUntagZuuCaloIsoOk_pt->FindBin(ptBins[i]),hAllMC_uUntagZuuCaloIsoOk_pt->FindBin(ptBins[i+1]))) * 100.0;

		MC_Eff_ZuuTrkIsoOk_pt[i] = hAllMC_uUntagZuuTrkIsoOk_pt->TH1::Integral(hAllMC_uUntagZuuTrkIsoOk_pt->FindBin(ptBins[i]),hAllMC_uUntagZuuTrkIsoOk_pt->FindBin(ptBins[i+1])) 
						/ hAllMC_uUntagZuu_pt->TH1::Integral(hAllMC_uUntagZuuTrkIsoOk_pt->FindBin(ptBins[i]),hAllMC_uUntagZuuTrkIsoOk_pt->FindBin(ptBins[i+1])) * 100.0;
		MC_Eff_ZuuTrkIsoOk_pt_err[i] = error(hAllMC_uUntagZuuTrkIsoOk_pt->TH1::Integral(hAllMC_uUntagZuuTrkIsoOk_pt->FindBin(ptBins[i]),hAllMC_uUntagZuuTrkIsoOk_pt->FindBin(ptBins[i+1])), hAllMC_uUntagZuu_pt->TH1::Integral(hAllMC_uUntagZuuTrkIsoOk_pt->FindBin(ptBins[i]),hAllMC_uUntagZuuTrkIsoOk_pt->FindBin(ptBins[i+1]))) * 100.0;

		MC_Eff_Zuud0Ok_pt[i] = hAllMC_uUntagZuud0Ok_pt->TH1::Integral(hAllMC_uUntagZuud0Ok_pt->FindBin(ptBins[i]),hAllMC_uUntagZuud0Ok_pt->FindBin(ptBins[i+1])) 
						/ hAllMC_uUntagZuu_pt->TH1::Integral(hAllMC_uUntagZuud0Ok_pt->FindBin(ptBins[i]),hAllMC_uUntagZuud0Ok_pt->FindBin(ptBins[i+1])) * 100.0;
		MC_Eff_Zuud0Ok_pt_err[i] = error(hAllMC_uUntagZuud0Ok_pt->TH1::Integral(hAllMC_uUntagZuud0Ok_pt->FindBin(ptBins[i]),hAllMC_uUntagZuud0Ok_pt->FindBin(ptBins[i+1])), hAllMC_uUntagZuu_pt->TH1::Integral(hAllMC_uUntagZuud0Ok_pt->FindBin(ptBins[i]),hAllMC_uUntagZuud0Ok_pt->FindBin(ptBins[i+1]))) * 100.0;

		MC_Eff_ZuuAllOk_pt[i] = hAllMC_uUntagZuuAllOk_pt->TH1::Integral(hAllMC_uUntagZuuAllOk_pt->FindBin(ptBins[i]),hAllMC_uUntagZuuAllOk_pt->FindBin(ptBins[i+1])) 
						/ hAllMC_uUntagZuu_pt->TH1::Integral(hAllMC_uUntagZuuAllOk_pt->FindBin(ptBins[i]),hAllMC_uUntagZuuAllOk_pt->FindBin(ptBins[i+1])) * 100.0;
		MC_Eff_ZuuAllOk_pt_err[i] = error(hAllMC_uUntagZuuAllOk_pt->TH1::Integral(hAllMC_uUntagZuuAllOk_pt->FindBin(ptBins[i]),hAllMC_uUntagZuuAllOk_pt->FindBin(ptBins[i+1])), hAllMC_uUntagZuu_pt->TH1::Integral(hAllMC_uUntagZuuAllOk_pt->FindBin(ptBins[i]),hAllMC_uUntagZuuAllOk_pt->FindBin(ptBins[i+1]))) * 100.0;

	}

	//--------------------------------------//
	// Draw Graph	- Calo Iso		//
	//--------------------------------------//
	if(PlotCaloIso){
		TGraphErrors*geData_CaloIso_Zee= new TGraphErrors;
		TGraphErrors*geMc_CaloIso_Zee= new TGraphErrors;
		TGraphErrors*geData_CaloIso_Zuu= new TGraphErrors;
		TGraphErrors*geMc_CaloIso_Zuu= new TGraphErrors;

		for(int i=0;i<nbins;i++)
		{
			double x_data = 0.5*(ptBins[i]+ptBins[i+1]);
			double x_mc = x_data;

			geData_CaloIso_Zee->SetPoint(i,x_data,Eff_ZeeCaloIsoOk_pt[i]);
			geData_CaloIso_Zee->SetPointError(i,0,Eff_ZeeCaloIsoOk_pt_err[i]);
			geMc_CaloIso_Zee->SetPoint(i,x_mc,MC_Eff_ZeeCaloIsoOk_pt[i]);
			geMc_CaloIso_Zee->SetPointError(i,0,MC_Eff_ZeeCaloIsoOk_pt_err[i]);

			geData_CaloIso_Zuu->SetPoint(i,x_data,Eff_ZuuCaloIsoOk_pt[i]);
			geData_CaloIso_Zuu->SetPointError(i,0,Eff_ZuuCaloIsoOk_pt_err[i]);
			geMc_CaloIso_Zuu->SetPoint(i,x_mc,MC_Eff_ZuuCaloIsoOk_pt[i]);
			geMc_CaloIso_Zuu->SetPointError(i,0,MC_Eff_ZuuCaloIsoOk_pt_err[i]);
		
		}

		SetGraphStyle(geData_CaloIso_Zee,20,kRed,1,kRed,0);
		SetGraphStyle(geMc_CaloIso_Zee,20,kBlue,1,kBlue,0);

		SetGraphStyle(geData_CaloIso_Zuu,20,kGreen,1,kGreen,0);
		SetGraphStyle(geMc_CaloIso_Zuu,20,kMagenta,1,kMagenta,0);
	
		TCanvas*cnvs_CaloIso =new TCanvas;
		TH1F*hFrame=cnvs_CaloIso->DrawFrame(0,0,50,100);
		hFrame->SetXTitle("Pt_{additional muon}");
		hFrame->SetYTitle("Calo Iso efficiency [%]");
		cnvs_CaloIso->SetGridy();
		DrawGridx(hFrame,ptBins,nbins);
		geMc_CaloIso_Zee->Draw("PE same");
		geData_CaloIso_Zee->Draw("PE same");
		geMc_CaloIso_Zuu->Draw("PE same");
		geData_CaloIso_Zuu->Draw("PE same");
	
		TLegend*leg1CaloIso=new TLegend(0.25,0.7,0.55,0.9);
		leg1CaloIso->SetFillColor(0);
		leg1CaloIso->SetShadowColor(0);
		leg1CaloIso->SetBorderSize(0);
		leg1CaloIso->SetHeader("Z#rightarrow ee #int L dt #approx 4.9 fb^{-1}");
		leg1CaloIso->AddEntry(geData_CaloIso_Zee,"2011 data ","lp");
		leg1CaloIso->AddEntry(geMc_CaloIso_Zee,"MC11c","lp");
		leg1CaloIso->Draw();

		TLegend*leg2CaloIso=new TLegend(0.50,0.7,0.8,0.9);
		leg2CaloIso->SetFillColor(0);
		leg2CaloIso->SetShadowColor(0);
		leg2CaloIso->SetBorderSize(0);
		leg2CaloIso->SetHeader("Z#rightarrow #mu#mu #int L dt #approx 4.8 fb^{-1}");
		leg2CaloIso->AddEntry(geData_CaloIso_Zuu,"2011 data ","lp");
		leg2CaloIso->AddEntry(geMc_CaloIso_Zuu,"MC11c","lp");
		leg2CaloIso->Draw();

		cnvs_CaloIso->SaveAs("eff_CaloIso_uUntagptBin2011.png");
	}
	//--------------------------------------//
	// Draw Graph	- Track Iso		//
	//--------------------------------------//
	if(PlotTrkIso){
		TGraphErrors*geData_TrkIso_Zee= new TGraphErrors;
		TGraphErrors*geMc_TrkIso_Zee= new TGraphErrors;
		TGraphErrors*geData_TrkIso_Zuu= new TGraphErrors;
		TGraphErrors*geMc_TrkIso_Zuu= new TGraphErrors;

		const int nbins=sizeof(Eff_ZeeTrkIsoOk_pt)/sizeof(double);
		for(int i=0;i<nbins;i++)
		{
			double x_data = 0.5*(ptBins[i]+ptBins[i+1]);
			double x_mc = x_data;

			geData_TrkIso_Zee->SetPoint(i,x_data,Eff_ZeeTrkIsoOk_pt[i]);
			geData_TrkIso_Zee->SetPointError(i,0,Eff_ZeeTrkIsoOk_pt_err[i]);
			geMc_TrkIso_Zee->SetPoint(i,x_mc,MC_Eff_ZeeTrkIsoOk_pt[i]);
			geMc_TrkIso_Zee->SetPointError(i,0,MC_Eff_ZeeTrkIsoOk_pt_err[i]);

			geData_TrkIso_Zuu->SetPoint(i,x_data,Eff_ZuuTrkIsoOk_pt[i]);
			geData_TrkIso_Zuu->SetPointError(i,0,Eff_ZuuTrkIsoOk_pt_err[i]);
			geMc_TrkIso_Zuu->SetPoint(i,x_mc,MC_Eff_ZuuTrkIsoOk_pt[i]);
			geMc_TrkIso_Zuu->SetPointError(i,0,MC_Eff_ZuuTrkIsoOk_pt_err[i]);
		
		}

		SetGraphStyle(geData_TrkIso_Zee,20,kRed,1,kRed,0);
		SetGraphStyle(geMc_TrkIso_Zee,20,kBlue,1,kBlue,0);

		SetGraphStyle(geData_TrkIso_Zuu,20,kGreen,1,kGreen,0);
		SetGraphStyle(geMc_TrkIso_Zuu,20,kMagenta,1,kMagenta,0);
	
		TCanvas*cnvs_TrkIso =new TCanvas;
		TH1F*hFrame=cnvs_TrkIso->DrawFrame(0,0,50,100);
		hFrame->SetXTitle("Pt_{additional muon}");
		hFrame->SetYTitle("Track Iso efficiency [%]");
		cnvs_TrkIso->SetGridy();
		DrawGridx(hFrame,ptBins,nbins);
		geMc_TrkIso_Zee->Draw("PE same");
		geData_TrkIso_Zee->Draw("PE same");
		geMc_TrkIso_Zuu->Draw("PE same");
		geData_TrkIso_Zuu->Draw("PE same");
	
		TLegend*leg1TrkIso=new TLegend(0.30,0.7,0.60,0.9);
		leg1TrkIso->SetFillColor(0);
		leg1TrkIso->SetShadowColor(0);
		leg1TrkIso->SetBorderSize(0);
		leg1TrkIso->SetHeader("Z#rightarrow ee #int L dt #approx 4.9 fb^{-1}");
		leg1TrkIso->AddEntry(geData_TrkIso_Zee,"2011 data","lp");
		leg1TrkIso->AddEntry(geMc_TrkIso_Zee,"MC11c","lp");
		leg1TrkIso->Draw();

		TLegend*leg2TrkIso=new TLegend(0.55,0.7,0.85,0.9);
		leg2TrkIso->SetFillColor(0);
		leg2TrkIso->SetShadowColor(0);
		leg2TrkIso->SetBorderSize(0);
		leg2TrkIso->SetHeader("Z#rightarrow #mu#mu #int L dt #approx 4.8 fb^{-1}");
		leg2TrkIso->AddEntry(geData_TrkIso_Zuu,"2011 data ","lp");
		leg2TrkIso->AddEntry(geMc_TrkIso_Zuu,"MC11c","lp");
		leg2TrkIso->Draw();

		cnvs_TrkIso->SaveAs("eff_TrkIso_uUntagptBin2011.png");
	}

	//--------------------------------------//
	// Draw Graph	- d0 significance	//
	//--------------------------------------//
	if(Plotd0sig){
		TGraphErrors*geData_d0_Zee= new TGraphErrors;
		TGraphErrors*geMc_d0_Zee= new TGraphErrors;	
		TGraphErrors*geData_d0_Zuu= new TGraphErrors;
		TGraphErrors*geMc_d0_Zuu= new TGraphErrors;

		const int nbins=sizeof(Eff_Zeed0Ok_pt)/sizeof(double);
		for(int i=0;i<nbins;i++)
		{
			double x_data = 0.5*(ptBins[i]+ptBins[i+1]);
			double x_mc = x_data;

			geData_d0_Zee->SetPoint(i,x_data,Eff_Zeed0Ok_pt[i]);
			geData_d0_Zee->SetPointError(i,0,Eff_Zeed0Ok_pt_err[i]);
			geMc_d0_Zee->SetPoint(i,x_mc,MC_Eff_Zeed0Ok_pt[i]);
			geMc_d0_Zee->SetPointError(i,0,MC_Eff_Zeed0Ok_pt_err[i]);

			geData_d0_Zuu->SetPoint(i,x_data,Eff_Zuud0Ok_pt[i]);
			geData_d0_Zuu->SetPointError(i,0,Eff_Zuud0Ok_pt_err[i]);
			geMc_d0_Zuu->SetPoint(i,x_mc,MC_Eff_Zuud0Ok_pt[i]);
			geMc_d0_Zuu->SetPointError(i,0,MC_Eff_Zuud0Ok_pt_err[i]);
		}

		SetGraphStyle(geData_d0_Zee,20,kRed,1,kRed,0);
		SetGraphStyle(geMc_d0_Zee,20,kBlue,1,kBlue,0);
		SetGraphStyle(geData_d0_Zuu,20,kGreen,1,kGreen,0);
		SetGraphStyle(geMc_d0_Zuu,20,kMagenta,1,kMagenta,0);
	
		TCanvas*cnvs_d0 =new TCanvas;
		TH1F*hFrame=cnvs_d0->DrawFrame(0,0,50,100);
		hFrame->SetXTitle("Pt_{additional muon}");
		hFrame->SetYTitle("d0 significance efficiency [%]");
		cnvs_d0->SetGridy();
		DrawGridx(hFrame,ptBins,nbins);
		geMc_d0_Zee->Draw("PE same");
		geData_d0_Zee->Draw("PE same");
		geMc_d0_Zuu->Draw("PE same");
		geData_d0_Zuu->Draw("PE same");
	
		TLegend*leg1d0=new TLegend(0.30,0.28,0.60,0.48);
		leg1d0->SetFillColor(0);
		leg1d0->SetShadowColor(0);
		leg1d0->SetBorderSize(0);
		leg1d0->SetHeader("Z#rightarrow ee #int L dt #approx 4.9 fb^{-1}");
		leg1d0->AddEntry(geData_d0_Zee,"2011 data","lp");
		leg1d0->AddEntry(geMc_d0_Zee,"MC11c","lp");
		leg1d0->Draw();

		TLegend*leg2d0=new TLegend(0.55,0.28,0.85,0.48);
		leg2d0->SetFillColor(0);
		leg2d0->SetShadowColor(0);
		leg2d0->SetBorderSize(0);
		leg2d0->SetHeader("Z#rightarrow #mu#mu #int L dt #approx 4.8 fb^{-1}");
		leg2d0->AddEntry(geData_d0_Zuu,"2011 data ","lp");
		leg2d0->AddEntry(geMc_d0_Zuu,"MC11c","lp");
		leg2d0->Draw();

		cnvs_d0->SaveAs("eff_d0_uUntagptBin2011.png");
	}

	//--------------------------------------//
	// Draw Graph	- All 			//
	//--------------------------------------//
	if(PlotAll){
		TGraphErrors*geData_All_Zee= new TGraphErrors;
		TGraphErrors*geMc_All_Zee= new TGraphErrors;
		TGraphErrors*geData_All_Zuu= new TGraphErrors;
		TGraphErrors*geMc_All_Zuu= new TGraphErrors;
		const int nbins=sizeof(Eff_ZeeAllOk_pt)/sizeof(double);

		for(int i=0;i<nbins;i++)
		{
			double x_data = 0.5*(ptBins[i]+ptBins[i+1]);
			double x_mc = x_data;

			geData_All_Zee->SetPoint(i,x_data,Eff_ZeeAllOk_pt[i]);
			geData_All_Zee->SetPointError(i,0,Eff_ZeeAllOk_pt_err[i]);
			geMc_All_Zee->SetPoint(i,x_mc,MC_Eff_ZeeAllOk_pt[i]);
			geMc_All_Zee->SetPointError(i,0,MC_Eff_ZeeAllOk_pt_err[i]);

			geData_All_Zuu->SetPoint(i,x_data,Eff_ZuuAllOk_pt[i]);
			geData_All_Zuu->SetPointError(i,0,Eff_ZuuAllOk_pt_err[i]);
			geMc_All_Zuu->SetPoint(i,x_mc,MC_Eff_ZuuAllOk_pt[i]);
			geMc_All_Zuu->SetPointError(i,0,MC_Eff_ZuuAllOk_pt_err[i]);	
		}

		SetGraphStyle(geData_All_Zee,20,kRed,1,kRed,0);
		SetGraphStyle(geMc_All_Zee,20,kBlue,1,kBlue,0);
		SetGraphStyle(geData_All_Zuu,20,kGreen,1,kGreen,0);
		SetGraphStyle(geMc_All_Zuu,20,kMagenta,1,kMagenta,0);
	
		TCanvas*cnvs_All =new TCanvas;
		TH1F*hFrame=cnvs_All->DrawFrame(0,0,50,100);
		hFrame->SetXTitle("Pt_{additional muon}");
		hFrame->SetYTitle("All cuts efficiency [%]");
		cnvs_All->SetGridy();
		DrawGridx(hFrame,ptBins,nbins);
		geMc_All_Zee->Draw("PE same");
		geData_All_Zee->Draw("PE same");
		geMc_All_Zuu->Draw("PE same");
		geData_All_Zuu->Draw("PE same");
	
		TLegend*leg1All=new TLegend(0.30,0.70,0.60,0.90);
		leg1All->SetFillColor(0);
		leg1All->SetShadowColor(0);
		leg1All->SetBorderSize(0);
		leg1All->SetHeader("Z#rightarrow ee #int L dt #approx 4.9 fb^{-1}");
		leg1All->AddEntry(geData_All_Zee,"2011 data","lp");
		leg1All->AddEntry(geMc_All_Zee,"MC11c","lp");
		leg1All->Draw();

		TLegend*leg2All=new TLegend(0.55,0.73,0.85,0.90);
		leg2All->SetFillColor(0);
		leg2All->SetShadowColor(0);
		leg2All->SetBorderSize(0);
		leg2All->SetHeader("Z#rightarrow #mu#mu #int L dt #approx 4.8 fb^{-1}");
		leg2All->AddEntry(geData_All_Zuu,"2011 data ","lp");
		leg2All->AddEntry(geMc_All_Zuu,"MC11c","lp");
		leg2All->Draw();

		cnvs_All->SaveAs("eff_All_uUntagptBin2011.png");
	}

}


