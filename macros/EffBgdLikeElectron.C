
#include "utils.C"

void EffBgdLikeElectron(void)
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
	Eff_eUntag_eta(true,  true, true, true);
	Eff_eUntag_pt(true, true, true, true );
}

//--------------------------------------------------------------------------//

void Eff_eUntag_eta(bool PlotCaloIso, bool PlotTrkIso, bool Plotd0sig, bool PlotAll)
{
	//--------------------------------------//
	// Data					//
	//--------------------------------------//

	TFile *fileData_Zee = new TFile("../output/Zee_DATA.root");
	TFile *fileData_Zuu = new TFile("../output/Zuu_DATA.root");

	TH1F *heUntagZee_eta = (TH1F *) fileData_Zee->Get("heUntagZee_eta");
	TH1F *heUntagZeeCaloIsoOk_eta = (TH1F *) fileData_Zee->Get("heUntagZeeCaloIsoOk_eta");
	TH1F *heUntagZeeTrkIsoOk_eta = (TH1F *) fileData_Zee->Get("heUntagZeeTrkIsoOk_eta");
	TH1F *heUntagZeed0Ok_eta = (TH1F *) fileData_Zee->Get("heUntagZeed0Ok_eta");
	TH1F *heUntagZeeAllOk_eta = (TH1F *) fileData_Zee->Get("heUntagZeeAllOk_eta");

	TH1F *heUntagZuu_eta = (TH1F *) fileData_Zuu->Get("heUntagZuu_eta");
	TH1F *heUntagZuuCaloIsoOk_eta = (TH1F *) fileData_Zuu->Get("heUntagZuuCaloIsoOk_eta");
	TH1F *heUntagZuuTrkIsoOk_eta = (TH1F *) fileData_Zuu->Get("heUntagZuuTrkIsoOk_eta");
	TH1F *heUntagZuud0Ok_eta = (TH1F *) fileData_Zuu->Get("heUntagZuud0Ok_eta");
	TH1F *heUntagZuuAllOk_eta = (TH1F *) fileData_Zuu->Get("heUntagZuuAllOk_eta");


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
		Eff_ZeeCaloIsoOk_eta[i] = heUntagZeeCaloIsoOk_eta->TH1::GetBinContent(i + 1) 
						/ heUntagZee_eta->TH1::GetBinContent(i + 1) * 100.0;
		Eff_ZeeCaloIsoOk_eta_err[i] = error(heUntagZeeCaloIsoOk_eta->TH1::GetBinContent(i + 1), heUntagZee_eta->TH1::GetBinContent(i + 1)) * 100.0;
		Eff_ZeeTrkIsoOk_eta[i] = heUntagZeeTrkIsoOk_eta->TH1::GetBinContent(i + 1) 
						/ heUntagZee_eta->TH1::GetBinContent(i + 1) * 100.0;
		Eff_ZeeTrkIsoOk_eta_err[i] = error(heUntagZeeTrkIsoOk_eta->TH1::GetBinContent(i + 1), heUntagZee_eta->TH1::GetBinContent(i + 1)) * 100.0;
		Eff_Zeed0Ok_eta[i] = heUntagZeed0Ok_eta->TH1::GetBinContent(i + 1) 
						/ heUntagZee_eta->TH1::GetBinContent(i + 1) * 100.0;
		Eff_Zeed0Ok_eta_err[i] = error(heUntagZeed0Ok_eta->TH1::GetBinContent(i + 1), heUntagZee_eta->TH1::GetBinContent(i + 1)) * 100.0;
		Eff_ZeeAllOk_eta[i] = heUntagZeeAllOk_eta->TH1::GetBinContent(i + 1) 
						/ heUntagZee_eta->TH1::GetBinContent(i + 1) * 100.0;
		Eff_ZeeAllOk_eta_err[i] = error(heUntagZeeAllOk_eta->TH1::GetBinContent(i + 1), heUntagZee_eta->TH1::GetBinContent(i + 1)) * 100.0;

		Eff_ZuuCaloIsoOk_eta[i] = heUntagZuuCaloIsoOk_eta->TH1::GetBinContent(i + 1) 
						/ heUntagZuu_eta->TH1::GetBinContent(i + 1) * 100.0;
		Eff_ZuuCaloIsoOk_eta_err[i] = error(heUntagZuuCaloIsoOk_eta->TH1::GetBinContent(i + 1), heUntagZuu_eta->TH1::GetBinContent(i + 1)) * 100.0;
		Eff_ZuuTrkIsoOk_eta[i] = heUntagZuuTrkIsoOk_eta->TH1::GetBinContent(i + 1) 
						/ heUntagZuu_eta->TH1::GetBinContent(i + 1) * 100.0;
		Eff_ZuuTrkIsoOk_eta_err[i] = error(heUntagZuuTrkIsoOk_eta->TH1::GetBinContent(i + 1), heUntagZuu_eta->TH1::GetBinContent(i + 1)) * 100.0;
		Eff_Zuud0Ok_eta[i] = heUntagZuud0Ok_eta->TH1::GetBinContent(i + 1) 
						/ heUntagZuu_eta->TH1::GetBinContent(i + 1) * 100.0;
		Eff_Zuud0Ok_eta_err[i] = error(heUntagZuud0Ok_eta->TH1::GetBinContent(i + 1), heUntagZuu_eta->TH1::GetBinContent(i + 1)) * 100.0;
		Eff_ZuuAllOk_eta[i] = heUntagZuuAllOk_eta->TH1::GetBinContent(i + 1) 
						/ heUntagZuu_eta->TH1::GetBinContent(i + 1) * 100.0;
		Eff_ZuuAllOk_eta_err[i] = error(heUntagZuuAllOk_eta->TH1::GetBinContent(i + 1), heUntagZuu_eta->TH1::GetBinContent(i + 1)) * 100.0;

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

	TH1F *hAllMC_eUntagZee_eta= (TH1F *) fileMC_Zee->Get("heUntagZee_eta");
	TH1F *hAllMC_eUntagZeeCaloIsoOk_eta= (TH1F *) fileMC_Zee->Get("heUntagZeeCaloIsoOk_eta");
	TH1F *hAllMC_eUntagZeeTrkIsoOk_eta= (TH1F *) fileMC_Zee->Get("heUntagZeeTrkIsoOk_eta");
	TH1F *hAllMC_eUntagZeed0Ok_eta= (TH1F *) fileMC_Zee->Get("heUntagZeed0Ok_eta");
	TH1F *hAllMC_eUntagZeeAllOk_eta= (TH1F *) fileMC_Zee->Get("heUntagZeeAllOk_eta");

	TH1F *hAllMC_eUntagZuu_eta= (TH1F *) fileMC_Zuu->Get("heUntagZuu_eta");
	TH1F *hAllMC_eUntagZuuCaloIsoOk_eta= (TH1F *) fileMC_Zuu->Get("heUntagZuuCaloIsoOk_eta");
	TH1F *hAllMC_eUntagZuuTrkIsoOk_eta= (TH1F *) fileMC_Zuu->Get("heUntagZuuTrkIsoOk_eta");
	TH1F *hAllMC_eUntagZuud0Ok_eta= (TH1F *) fileMC_Zuu->Get("heUntagZuud0Ok_eta");
	TH1F *hAllMC_eUntagZuuAllOk_eta= (TH1F *) fileMC_Zuu->Get("heUntagZuuAllOk_eta");

	for(int i =  1; i < 39; i++){  
		TFile *fileMC_Zee = new TFile(Form("../output/Zee_MC_%d.root",mc_RunNumber[i]));
		TFile *fileMC_Zuu = new TFile(Form("../output/Zuu_MC_%d.root",mc_RunNumber[i]));

		TH1F *h0= (TH1F *) fileMC_Zee->Get("heUntagZee_eta");
		TH1F *h1= (TH1F *) fileMC_Zee->Get("heUntagZeeCaloIsoOk_eta");
		TH1F *h2= (TH1F *) fileMC_Zee->Get("heUntagZeeTrkIsoOk_eta");
		TH1F *h3= (TH1F *) fileMC_Zee->Get("heUntagZeed0Ok_eta");
		TH1F *h4= (TH1F *) fileMC_Zee->Get("heUntagZeeAllOk_eta");

		TH1F *h5= (TH1F *) fileMC_Zuu->Get("heUntagZuu_eta");
		TH1F *h6= (TH1F *) fileMC_Zuu->Get("heUntagZuuCaloIsoOk_eta");
		TH1F *h7= (TH1F *) fileMC_Zuu->Get("heUntagZuuTrkIsoOk_eta");
		TH1F *h8= (TH1F *) fileMC_Zuu->Get("heUntagZuud0Ok_eta");
		TH1F *h9= (TH1F *) fileMC_Zuu->Get("heUntagZuuAllOk_eta");

		hAllMC_eUntagZee_eta->Add(h0);
		hAllMC_eUntagZeeCaloIsoOk_eta->Add(h1);
		hAllMC_eUntagZeeTrkIsoOk_eta->Add(h2);
		hAllMC_eUntagZeed0Ok_eta->Add(h3);
		hAllMC_eUntagZeeAllOk_eta->Add(h4);

		hAllMC_eUntagZuu_eta->Add(h5);
		hAllMC_eUntagZuuCaloIsoOk_eta->Add(h6);
		hAllMC_eUntagZuuTrkIsoOk_eta->Add(h7);
		hAllMC_eUntagZuud0Ok_eta->Add(h8);
		hAllMC_eUntagZuuAllOk_eta->Add(h9);
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
		MC_Eff_ZeeCaloIsoOk_eta[i] = hAllMC_eUntagZeeCaloIsoOk_eta->TH1::GetBinContent(i + 1) 
						/ hAllMC_eUntagZee_eta->TH1::GetBinContent(i + 1) * 100.0;
		MC_Eff_ZeeCaloIsoOk_eta_err[i] = error(hAllMC_eUntagZeeCaloIsoOk_eta->TH1::GetBinContent(i + 1), hAllMC_eUntagZee_eta->TH1::GetBinContent(i + 1)) * 100.0;
		MC_Eff_ZeeTrkIsoOk_eta[i] = hAllMC_eUntagZeeTrkIsoOk_eta->TH1::GetBinContent(i + 1) 
						/ hAllMC_eUntagZee_eta->TH1::GetBinContent(i + 1) * 100.0;
		MC_Eff_ZeeTrkIsoOk_eta_err[i] = error(hAllMC_eUntagZeeTrkIsoOk_eta->TH1::GetBinContent(i + 1), hAllMC_eUntagZee_eta->TH1::GetBinContent(i + 1)) * 100.0;
		MC_Eff_Zeed0Ok_eta[i] = hAllMC_eUntagZeed0Ok_eta->TH1::GetBinContent(i + 1) 
						/ hAllMC_eUntagZee_eta->TH1::GetBinContent(i + 1) * 100.0;
		MC_Eff_Zeed0Ok_eta_err[i] = error(hAllMC_eUntagZeed0Ok_eta->TH1::GetBinContent(i + 1), hAllMC_eUntagZee_eta->TH1::GetBinContent(i + 1)) * 100.0;
		MC_Eff_ZeeAllOk_eta[i] = hAllMC_eUntagZeeAllOk_eta->TH1::GetBinContent(i + 1) 
						/ hAllMC_eUntagZee_eta->TH1::GetBinContent(i + 1) * 100.0;
		MC_Eff_ZeeAllOk_eta_err[i] = error(hAllMC_eUntagZeeAllOk_eta->TH1::GetBinContent(i + 1), hAllMC_eUntagZee_eta->TH1::GetBinContent(i + 1)) * 100.0;

		MC_Eff_ZuuCaloIsoOk_eta[i] = hAllMC_eUntagZuuCaloIsoOk_eta->TH1::GetBinContent(i + 1) 
						/ hAllMC_eUntagZuu_eta->TH1::GetBinContent(i + 1) * 100.0;
		MC_Eff_ZuuCaloIsoOk_eta_err[i] = error(hAllMC_eUntagZuuCaloIsoOk_eta->TH1::GetBinContent(i + 1), hAllMC_eUntagZuu_eta->TH1::GetBinContent(i + 1)) * 100.0;
		MC_Eff_ZuuTrkIsoOk_eta[i] = hAllMC_eUntagZuuTrkIsoOk_eta->TH1::GetBinContent(i + 1) 
						/ hAllMC_eUntagZuu_eta->TH1::GetBinContent(i + 1) * 100.0;
		MC_Eff_ZuuTrkIsoOk_eta_err[i] = error(hAllMC_eUntagZuuTrkIsoOk_eta->TH1::GetBinContent(i + 1), hAllMC_eUntagZuu_eta->TH1::GetBinContent(i + 1)) * 100.0;
		MC_Eff_Zuud0Ok_eta[i] = hAllMC_eUntagZuud0Ok_eta->TH1::GetBinContent(i + 1) 
						/ hAllMC_eUntagZuu_eta->TH1::GetBinContent(i + 1) * 100.0;
		MC_Eff_Zuud0Ok_eta_err[i] = error(hAllMC_eUntagZuud0Ok_eta->TH1::GetBinContent(i + 1), hAllMC_eUntagZuu_eta->TH1::GetBinContent(i + 1)) * 100.0;
		MC_Eff_ZuuAllOk_eta[i] = hAllMC_eUntagZuuAllOk_eta->TH1::GetBinContent(i + 1) 
						/ hAllMC_eUntagZuu_eta->TH1::GetBinContent(i + 1) * 100.0;
		MC_Eff_ZuuAllOk_eta_err[i] = error(hAllMC_eUntagZuuAllOk_eta->TH1::GetBinContent(i + 1), hAllMC_eUntagZuu_eta->TH1::GetBinContent(i + 1)) * 100.0;

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
		hFrame->SetXTitle("#eta_{additional electron}");
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

		cnvs_CaloIso->SaveAs("eff_CaloIso_eUntagetaBin2011.png");
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
		hFrame->SetXTitle("#eta_{additional electron}");
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

		cnvs_TrkIso->SaveAs("eff_TrkIso_eUntagetaBin2011.png");
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
		hFrame->SetXTitle("#eta_{additional electron}");
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

		cnvs_d0->SaveAs("eff_d0_eUntagetaBin2011.png");
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
		hFrame->SetXTitle("#eta_{additional electron}");
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

		cnvs_All->SaveAs("eff_All_eUntagetaBin2011.png");
	}
}

//--------------------------------------------------------------------------//

void Eff_eUntag_pt(bool PlotCaloIso, bool PlotTrkIso, bool Plotd0sig, bool PlotAll)
{
	//--------------------------------------//
	// Data					//
	//--------------------------------------//

	TFile *fileData_Zee = new TFile("../output/Zee_DATA.root");
	TFile *fileData_Zuu = new TFile("../output/Zuu_DATA.root");

	const double ptBins[]={7, 12, 15, 20, 25, 30, 35, 40, 45, 50};

	TH1F *heUntagZee_pt = (TH1F *) fileData_Zee->Get("heUntagZee_pt");
	TH1F *heUntagZeeCaloIsoOk_pt = (TH1F *) fileData_Zee->Get("heUntagZeeCaloIsoOk_pt");
	TH1F *heUntagZeeTrkIsoOk_pt = (TH1F *) fileData_Zee->Get("heUntagZeeTrkIsoOk_pt");
	TH1F *heUntagZeed0Ok_pt = (TH1F *) fileData_Zee->Get("heUntagZeed0Ok_pt");
	TH1F *heUntagZeeAllOk_pt = (TH1F *) fileData_Zee->Get("heUntagZeeAllOk_pt");

	TH1F *heUntagZuu_pt = (TH1F *) fileData_Zuu->Get("heUntagZuu_pt");
	TH1F *heUntagZuuCaloIsoOk_pt = (TH1F *) fileData_Zuu->Get("heUntagZuuCaloIsoOk_pt");
	TH1F *heUntagZuuTrkIsoOk_pt = (TH1F *) fileData_Zuu->Get("heUntagZuuTrkIsoOk_pt");
	TH1F *heUntagZuud0Ok_pt = (TH1F *) fileData_Zuu->Get("heUntagZuud0Ok_pt");
	TH1F *heUntagZuuAllOk_pt = (TH1F *) fileData_Zuu->Get("heUntagZuuAllOk_pt");

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
		Eff_ZeeCaloIsoOk_pt[i] = heUntagZeeCaloIsoOk_pt->TH1::Integral(heUntagZeeCaloIsoOk_pt->FindBin(ptBins[i]),heUntagZeeCaloIsoOk_pt->FindBin(ptBins[i+1])) 
						/ heUntagZee_pt->TH1::Integral(heUntagZeeCaloIsoOk_pt->FindBin(ptBins[i]),heUntagZeeCaloIsoOk_pt->FindBin(ptBins[i+1])) * 100.0;
		Eff_ZeeCaloIsoOk_pt_err[i] = error(heUntagZeeCaloIsoOk_pt->TH1::Integral(heUntagZeeCaloIsoOk_pt->FindBin(ptBins[i]),heUntagZeeCaloIsoOk_pt->FindBin(ptBins[i+1])), heUntagZee_pt->TH1::Integral(heUntagZeeCaloIsoOk_pt->FindBin(ptBins[i]),heUntagZeeCaloIsoOk_pt->FindBin(ptBins[i+1]))) * 100.0;

		Eff_ZeeTrkIsoOk_pt[i] = heUntagZeeTrkIsoOk_pt->TH1::Integral(heUntagZeeTrkIsoOk_pt->FindBin(ptBins[i]),heUntagZeeTrkIsoOk_pt->FindBin(ptBins[i+1])) 
						/ heUntagZee_pt->TH1::Integral(heUntagZeeTrkIsoOk_pt->FindBin(ptBins[i]),heUntagZeeTrkIsoOk_pt->FindBin(ptBins[i+1])) * 100.0;
		Eff_ZeeTrkIsoOk_pt_err[i] = error(heUntagZeeTrkIsoOk_pt->TH1::Integral(heUntagZeeTrkIsoOk_pt->FindBin(ptBins[i]),heUntagZeeTrkIsoOk_pt->FindBin(ptBins[i+1])), heUntagZee_pt->TH1::Integral(heUntagZeeTrkIsoOk_pt->FindBin(ptBins[i]),heUntagZeeTrkIsoOk_pt->FindBin(ptBins[i+1]))) * 100.0;

		Eff_Zeed0Ok_pt[i] = heUntagZeed0Ok_pt->TH1::Integral(heUntagZeed0Ok_pt->FindBin(ptBins[i]),heUntagZeed0Ok_pt->FindBin(ptBins[i+1])) 
						/ heUntagZee_pt->TH1::Integral(heUntagZeed0Ok_pt->FindBin(ptBins[i]),heUntagZeed0Ok_pt->FindBin(ptBins[i+1])) * 100.0;
		Eff_Zeed0Ok_pt_err[i] = error(heUntagZeed0Ok_pt->TH1::Integral(heUntagZeed0Ok_pt->FindBin(ptBins[i]),heUntagZeed0Ok_pt->FindBin(ptBins[i+1])), heUntagZee_pt->TH1::Integral(heUntagZeed0Ok_pt->FindBin(ptBins[i]),heUntagZeed0Ok_pt->FindBin(ptBins[i+1]))) * 100.0;

		Eff_ZeeAllOk_pt[i] = heUntagZeeAllOk_pt->TH1::Integral(heUntagZeeAllOk_pt->FindBin(ptBins[i]),heUntagZeeAllOk_pt->FindBin(ptBins[i+1])) 
						/ heUntagZee_pt->TH1::Integral(heUntagZeeAllOk_pt->FindBin(ptBins[i]),heUntagZeeAllOk_pt->FindBin(ptBins[i+1])) * 100.0;
		Eff_ZeeAllOk_pt_err[i] = error(heUntagZeeAllOk_pt->TH1::Integral(heUntagZeeAllOk_pt->FindBin(ptBins[i]),heUntagZeeAllOk_pt->FindBin(ptBins[i+1])), heUntagZee_pt->TH1::Integral(heUntagZeeAllOk_pt->FindBin(ptBins[i]),heUntagZeeAllOk_pt->FindBin(ptBins[i+1]))) * 100.0;

		Eff_ZuuCaloIsoOk_pt[i] = heUntagZuuCaloIsoOk_pt->TH1::Integral(heUntagZuuCaloIsoOk_pt->FindBin(ptBins[i]),heUntagZuuCaloIsoOk_pt->FindBin(ptBins[i+1])) 
						/ heUntagZuu_pt->TH1::Integral(heUntagZuuCaloIsoOk_pt->FindBin(ptBins[i]),heUntagZuuCaloIsoOk_pt->FindBin(ptBins[i+1])) * 100.0;
		Eff_ZuuCaloIsoOk_pt_err[i] = error(heUntagZuuCaloIsoOk_pt->TH1::Integral(heUntagZuuCaloIsoOk_pt->FindBin(ptBins[i]),heUntagZuuCaloIsoOk_pt->FindBin(ptBins[i+1])), heUntagZuu_pt->TH1::Integral(heUntagZuuCaloIsoOk_pt->FindBin(ptBins[i]),heUntagZuuCaloIsoOk_pt->FindBin(ptBins[i+1]))) * 100.0;

		Eff_ZuuTrkIsoOk_pt[i] = heUntagZuuTrkIsoOk_pt->TH1::Integral(heUntagZuuTrkIsoOk_pt->FindBin(ptBins[i]),heUntagZuuTrkIsoOk_pt->FindBin(ptBins[i+1])) 
						/ heUntagZuu_pt->TH1::Integral(heUntagZuuTrkIsoOk_pt->FindBin(ptBins[i]),heUntagZuuTrkIsoOk_pt->FindBin(ptBins[i+1])) * 100.0;
		Eff_ZuuTrkIsoOk_pt_err[i] = error(heUntagZuuTrkIsoOk_pt->TH1::Integral(heUntagZuuTrkIsoOk_pt->FindBin(ptBins[i]),heUntagZuuTrkIsoOk_pt->FindBin(ptBins[i+1])), heUntagZuu_pt->TH1::Integral(heUntagZuuTrkIsoOk_pt->FindBin(ptBins[i]),heUntagZuuTrkIsoOk_pt->FindBin(ptBins[i+1]))) * 100.0;

		Eff_Zuud0Ok_pt[i] = heUntagZuud0Ok_pt->TH1::Integral(heUntagZuud0Ok_pt->FindBin(ptBins[i]),heUntagZuud0Ok_pt->FindBin(ptBins[i+1])) 
						/ heUntagZuu_pt->TH1::Integral(heUntagZuud0Ok_pt->FindBin(ptBins[i]),heUntagZuud0Ok_pt->FindBin(ptBins[i+1])) * 100.0;
		Eff_Zuud0Ok_pt_err[i] = error(heUntagZuud0Ok_pt->TH1::Integral(heUntagZuud0Ok_pt->FindBin(ptBins[i]),heUntagZuud0Ok_pt->FindBin(ptBins[i+1])), heUntagZuu_pt->TH1::Integral(heUntagZuud0Ok_pt->FindBin(ptBins[i]),heUntagZuud0Ok_pt->FindBin(ptBins[i+1]))) * 100.0;

		Eff_ZuuAllOk_pt[i] = heUntagZuuAllOk_pt->TH1::Integral(heUntagZuuAllOk_pt->FindBin(ptBins[i]),heUntagZuuAllOk_pt->FindBin(ptBins[i+1])) 
						/ heUntagZuu_pt->TH1::Integral(heUntagZuuAllOk_pt->FindBin(ptBins[i]),heUntagZuuAllOk_pt->FindBin(ptBins[i+1])) * 100.0;
		Eff_ZuuAllOk_pt_err[i] = error(heUntagZuuAllOk_pt->TH1::Integral(heUntagZuuAllOk_pt->FindBin(ptBins[i]),heUntagZuuAllOk_pt->FindBin(ptBins[i+1])), heUntagZuu_pt->TH1::Integral(heUntagZuuAllOk_pt->FindBin(ptBins[i]),heUntagZuuAllOk_pt->FindBin(ptBins[i+1]))) * 100.0;

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

	TH1F *hAllMC_eUntagZee_pt= (TH1F *) fileMC_Zee->Get("heUntagZee_pt");
	TH1F *hAllMC_eUntagZeeCaloIsoOk_pt= (TH1F *) fileMC_Zee->Get("heUntagZeeCaloIsoOk_pt");
	TH1F *hAllMC_eUntagZeeTrkIsoOk_pt= (TH1F *) fileMC_Zee->Get("heUntagZeeTrkIsoOk_pt");
	TH1F *hAllMC_eUntagZeed0Ok_pt= (TH1F *) fileMC_Zee->Get("heUntagZeed0Ok_pt");
	TH1F *hAllMC_eUntagZeeAllOk_pt= (TH1F *) fileMC_Zee->Get("heUntagZeeAllOk_pt");

	TH1F *hAllMC_eUntagZuu_pt= (TH1F *) fileMC_Zuu->Get("heUntagZuu_pt");
	TH1F *hAllMC_eUntagZuuCaloIsoOk_pt= (TH1F *) fileMC_Zuu->Get("heUntagZuuCaloIsoOk_pt");
	TH1F *hAllMC_eUntagZuuTrkIsoOk_pt= (TH1F *) fileMC_Zuu->Get("heUntagZuuTrkIsoOk_pt");
	TH1F *hAllMC_eUntagZuud0Ok_pt= (TH1F *) fileMC_Zuu->Get("heUntagZuud0Ok_pt");
	TH1F *hAllMC_eUntagZuuAllOk_pt= (TH1F *) fileMC_Zuu->Get("heUntagZuuAllOk_pt");

	for(int i =  1; i < 39; i++){  
		TFile *fileMC_Zee = new TFile(Form("../output/Zee_MC_%d.root",mc_RunNumber[i]));
		TFile *fileMC_Zuu = new TFile(Form("../output/Zuu_MC_%d.root",mc_RunNumber[i]));

		TH1F *h0= (TH1F *) fileMC_Zee->Get("heUntagZee_pt");
		TH1F *h1= (TH1F *) fileMC_Zee->Get("heUntagZeeCaloIsoOk_pt");
		TH1F *h2= (TH1F *) fileMC_Zee->Get("heUntagZeeTrkIsoOk_pt");
		TH1F *h3= (TH1F *) fileMC_Zee->Get("heUntagZeed0Ok_pt");
		TH1F *h4= (TH1F *) fileMC_Zee->Get("heUntagZeeAllOk_pt");

		TH1F *h5= (TH1F *) fileMC_Zuu->Get("heUntagZuu_pt");
		TH1F *h6= (TH1F *) fileMC_Zuu->Get("heUntagZuuCaloIsoOk_pt");
		TH1F *h7= (TH1F *) fileMC_Zuu->Get("heUntagZuuTrkIsoOk_pt");
		TH1F *h8= (TH1F *) fileMC_Zuu->Get("heUntagZuud0Ok_pt");
		TH1F *h9= (TH1F *) fileMC_Zuu->Get("heUntagZuuAllOk_pt");

		hAllMC_eUntagZee_pt->Add(h0);
		hAllMC_eUntagZeeCaloIsoOk_pt->Add(h1);
		hAllMC_eUntagZeeTrkIsoOk_pt->Add(h2);
		hAllMC_eUntagZeed0Ok_pt->Add(h3);
		hAllMC_eUntagZeeAllOk_pt->Add(h4);

		hAllMC_eUntagZuu_pt->Add(h5);
		hAllMC_eUntagZuuCaloIsoOk_pt->Add(h6);
		hAllMC_eUntagZuuTrkIsoOk_pt->Add(h7);
		hAllMC_eUntagZuud0Ok_pt->Add(h8);
		hAllMC_eUntagZuuAllOk_pt->Add(h9);
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
		MC_Eff_ZeeCaloIsoOk_pt[i] = hAllMC_eUntagZeeCaloIsoOk_pt->TH1::Integral(hAllMC_eUntagZeeCaloIsoOk_pt->FindBin(ptBins[i]),hAllMC_eUntagZeeCaloIsoOk_pt->FindBin(ptBins[i+1])) 
						/ hAllMC_eUntagZee_pt->TH1::Integral(hAllMC_eUntagZeeCaloIsoOk_pt->FindBin(ptBins[i]),hAllMC_eUntagZeeCaloIsoOk_pt->FindBin(ptBins[i+1])) * 100.0;
		MC_Eff_ZeeCaloIsoOk_pt_err[i] = error(hAllMC_eUntagZeeCaloIsoOk_pt->TH1::Integral(hAllMC_eUntagZeeCaloIsoOk_pt->FindBin(ptBins[i]),hAllMC_eUntagZeeCaloIsoOk_pt->FindBin(ptBins[i+1])), hAllMC_eUntagZee_pt->TH1::Integral(hAllMC_eUntagZeeCaloIsoOk_pt->FindBin(ptBins[i]),hAllMC_eUntagZeeCaloIsoOk_pt->FindBin(ptBins[i+1]))) * 100.0;

		MC_Eff_ZeeTrkIsoOk_pt[i] = hAllMC_eUntagZeeTrkIsoOk_pt->TH1::Integral(hAllMC_eUntagZeeTrkIsoOk_pt->FindBin(ptBins[i]),hAllMC_eUntagZeeTrkIsoOk_pt->FindBin(ptBins[i+1])) 
						/ hAllMC_eUntagZee_pt->TH1::Integral(hAllMC_eUntagZeeTrkIsoOk_pt->FindBin(ptBins[i]),hAllMC_eUntagZeeTrkIsoOk_pt->FindBin(ptBins[i+1])) * 100.0;
		MC_Eff_ZeeTrkIsoOk_pt_err[i] = error(hAllMC_eUntagZeeTrkIsoOk_pt->TH1::Integral(hAllMC_eUntagZeeTrkIsoOk_pt->FindBin(ptBins[i]),hAllMC_eUntagZeeTrkIsoOk_pt->FindBin(ptBins[i+1])), hAllMC_eUntagZee_pt->TH1::Integral(hAllMC_eUntagZeeTrkIsoOk_pt->FindBin(ptBins[i]),hAllMC_eUntagZeeTrkIsoOk_pt->FindBin(ptBins[i+1]))) * 100.0;

		MC_Eff_Zeed0Ok_pt[i] = hAllMC_eUntagZeed0Ok_pt->TH1::Integral(hAllMC_eUntagZeed0Ok_pt->FindBin(ptBins[i]),hAllMC_eUntagZeed0Ok_pt->FindBin(ptBins[i+1])) 
						/ hAllMC_eUntagZee_pt->TH1::Integral(hAllMC_eUntagZeed0Ok_pt->FindBin(ptBins[i]),hAllMC_eUntagZeed0Ok_pt->FindBin(ptBins[i+1])) * 100.0;
		MC_Eff_Zeed0Ok_pt_err[i] = error(hAllMC_eUntagZeed0Ok_pt->TH1::Integral(hAllMC_eUntagZeed0Ok_pt->FindBin(ptBins[i]),hAllMC_eUntagZeed0Ok_pt->FindBin(ptBins[i+1])), hAllMC_eUntagZee_pt->TH1::Integral(hAllMC_eUntagZeed0Ok_pt->FindBin(ptBins[i]),hAllMC_eUntagZeed0Ok_pt->FindBin(ptBins[i+1])) )* 100.0;

		MC_Eff_ZeeAllOk_pt[i] = hAllMC_eUntagZeeAllOk_pt->TH1::Integral(hAllMC_eUntagZeeAllOk_pt->FindBin(ptBins[i]),hAllMC_eUntagZeeAllOk_pt->FindBin(ptBins[i+1])) 
						/ hAllMC_eUntagZee_pt->TH1::Integral(hAllMC_eUntagZeeAllOk_pt->FindBin(ptBins[i]),hAllMC_eUntagZeeAllOk_pt->FindBin(ptBins[i+1])) * 100.0;
		MC_Eff_ZeeAllOk_pt_err[i] = error(hAllMC_eUntagZeeAllOk_pt->TH1::Integral(hAllMC_eUntagZeeAllOk_pt->FindBin(ptBins[i]),hAllMC_eUntagZeeAllOk_pt->FindBin(ptBins[i+1])), hAllMC_eUntagZee_pt->TH1::Integral(hAllMC_eUntagZeeAllOk_pt->FindBin(ptBins[i]),hAllMC_eUntagZeeAllOk_pt->FindBin(ptBins[i+1]))) * 100.0;

		MC_Eff_ZuuCaloIsoOk_pt[i] = hAllMC_eUntagZuuCaloIsoOk_pt->TH1::Integral(hAllMC_eUntagZuuCaloIsoOk_pt->FindBin(ptBins[i]),hAllMC_eUntagZuuCaloIsoOk_pt->FindBin(ptBins[i+1])) 
						/ hAllMC_eUntagZuu_pt->TH1::Integral(hAllMC_eUntagZuuCaloIsoOk_pt->FindBin(ptBins[i]),hAllMC_eUntagZuuCaloIsoOk_pt->FindBin(ptBins[i+1])) * 100.0;
		MC_Eff_ZuuCaloIsoOk_pt_err[i] = error(hAllMC_eUntagZuuCaloIsoOk_pt->TH1::Integral(hAllMC_eUntagZuuCaloIsoOk_pt->FindBin(ptBins[i]),hAllMC_eUntagZuuCaloIsoOk_pt->FindBin(ptBins[i+1])), hAllMC_eUntagZuu_pt->TH1::Integral(hAllMC_eUntagZuuCaloIsoOk_pt->FindBin(ptBins[i]),hAllMC_eUntagZuuCaloIsoOk_pt->FindBin(ptBins[i+1]))) * 100.0;

		MC_Eff_ZuuTrkIsoOk_pt[i] = hAllMC_eUntagZuuTrkIsoOk_pt->TH1::Integral(hAllMC_eUntagZuuTrkIsoOk_pt->FindBin(ptBins[i]),hAllMC_eUntagZuuTrkIsoOk_pt->FindBin(ptBins[i+1])) 
						/ hAllMC_eUntagZuu_pt->TH1::Integral(hAllMC_eUntagZuuTrkIsoOk_pt->FindBin(ptBins[i]),hAllMC_eUntagZuuTrkIsoOk_pt->FindBin(ptBins[i+1])) * 100.0;
		MC_Eff_ZuuTrkIsoOk_pt_err[i] = error(hAllMC_eUntagZuuTrkIsoOk_pt->TH1::Integral(hAllMC_eUntagZuuTrkIsoOk_pt->FindBin(ptBins[i]),hAllMC_eUntagZuuTrkIsoOk_pt->FindBin(ptBins[i+1])), hAllMC_eUntagZuu_pt->TH1::Integral(hAllMC_eUntagZuuTrkIsoOk_pt->FindBin(ptBins[i]),hAllMC_eUntagZuuTrkIsoOk_pt->FindBin(ptBins[i+1]))) * 100.0;

		MC_Eff_Zuud0Ok_pt[i] = hAllMC_eUntagZuud0Ok_pt->TH1::Integral(hAllMC_eUntagZuud0Ok_pt->FindBin(ptBins[i]),hAllMC_eUntagZuud0Ok_pt->FindBin(ptBins[i+1])) 
						/ hAllMC_eUntagZuu_pt->TH1::Integral(hAllMC_eUntagZuud0Ok_pt->FindBin(ptBins[i]),hAllMC_eUntagZuud0Ok_pt->FindBin(ptBins[i+1])) * 100.0;
		MC_Eff_Zuud0Ok_pt_err[i] = error(hAllMC_eUntagZuud0Ok_pt->TH1::Integral(hAllMC_eUntagZuud0Ok_pt->FindBin(ptBins[i]),hAllMC_eUntagZuud0Ok_pt->FindBin(ptBins[i+1])), hAllMC_eUntagZuu_pt->TH1::Integral(hAllMC_eUntagZuud0Ok_pt->FindBin(ptBins[i]),hAllMC_eUntagZuud0Ok_pt->FindBin(ptBins[i+1]))) * 100.0;

		MC_Eff_ZuuAllOk_pt[i] = hAllMC_eUntagZuuAllOk_pt->TH1::Integral(hAllMC_eUntagZuuAllOk_pt->FindBin(ptBins[i]),hAllMC_eUntagZuuAllOk_pt->FindBin(ptBins[i+1])) 
						/ hAllMC_eUntagZuu_pt->TH1::Integral(hAllMC_eUntagZuuAllOk_pt->FindBin(ptBins[i]),hAllMC_eUntagZuuAllOk_pt->FindBin(ptBins[i+1])) * 100.0;
		MC_Eff_ZuuAllOk_pt_err[i] = error(hAllMC_eUntagZuuAllOk_pt->TH1::Integral(hAllMC_eUntagZuuAllOk_pt->FindBin(ptBins[i]),hAllMC_eUntagZuuAllOk_pt->FindBin(ptBins[i+1])), hAllMC_eUntagZuu_pt->TH1::Integral(hAllMC_eUntagZuuAllOk_pt->FindBin(ptBins[i]),hAllMC_eUntagZuuAllOk_pt->FindBin(ptBins[i+1]))) * 100.0;

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
		hFrame->SetXTitle("Pt_{additional electron}");
		hFrame->SetYTitle("Calo Iso efficiency [%]");
		cnvs_CaloIso->SetGridy();
		DrawGridx(hFrame,ptBins,nbins);
		geMc_CaloIso_Zee->Draw("PE same");
		geData_CaloIso_Zee->Draw("PE same");
		geMc_CaloIso_Zuu->Draw("PE same");
		geData_CaloIso_Zuu->Draw("PE same");
	
		TLegend*leg1CaloIso=new TLegend(0.30,0.28,0.60,0.48);
		leg1CaloIso->SetFillColor(0);
		leg1CaloIso->SetShadowColor(0);
		leg1CaloIso->SetBorderSize(0);
		leg1CaloIso->SetHeader("Z#rightarrow ee #int L dt #approx 4.9 fb^{-1}");
		leg1CaloIso->AddEntry(geData_CaloIso_Zee,"2011 data ","lp");
		leg1CaloIso->AddEntry(geMc_CaloIso_Zee,"MC11c","lp");
		leg1CaloIso->Draw();

		TLegend*leg2CaloIso=new TLegend(0.55,0.28,0.85,0.48);
		leg2CaloIso->SetFillColor(0);
		leg2CaloIso->SetShadowColor(0);
		leg2CaloIso->SetBorderSize(0);
		leg2CaloIso->SetHeader("Z#rightarrow #mu#mu #int L dt #approx 4.8 fb^{-1}");
		leg2CaloIso->AddEntry(geData_CaloIso_Zuu,"2011 data ","lp");
		leg2CaloIso->AddEntry(geMc_CaloIso_Zuu,"MC11c","lp");
		leg2CaloIso->Draw();

		cnvs_CaloIso->SaveAs("eff_CaloIso_eUntagptBin2011.png");
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
		hFrame->SetXTitle("Pt_{additional electron}");
		hFrame->SetYTitle("Track Iso efficiency [%]");
		cnvs_TrkIso->SetGridy();
		DrawGridx(hFrame,ptBins,nbins);
		geMc_TrkIso_Zee->Draw("PE same");
		geData_TrkIso_Zee->Draw("PE same");
		geMc_TrkIso_Zuu->Draw("PE same");
		geData_TrkIso_Zuu->Draw("PE same");
	
		TLegend*leg1TrkIso=new TLegend(0.30,0.28,0.60,0.48);
		leg1TrkIso->SetFillColor(0);
		leg1TrkIso->SetShadowColor(0);
		leg1TrkIso->SetBorderSize(0);
		leg1TrkIso->SetHeader("Z#rightarrow ee #int L dt #approx 4.9 fb^{-1}");
		leg1TrkIso->AddEntry(geData_TrkIso_Zee,"2011 data","lp");
		leg1TrkIso->AddEntry(geMc_TrkIso_Zee,"MC11c","lp");
		leg1TrkIso->Draw();

		TLegend*leg2TrkIso=new TLegend(0.55,0.28,0.85,0.48);
		leg2TrkIso->SetFillColor(0);
		leg2TrkIso->SetShadowColor(0);
		leg2TrkIso->SetBorderSize(0);
		leg2TrkIso->SetHeader("Z#rightarrow #mu#mu #int L dt #approx 4.8 fb^{-1}");
		leg2TrkIso->AddEntry(geData_TrkIso_Zuu,"2011 data ","lp");
		leg2TrkIso->AddEntry(geMc_TrkIso_Zuu,"MC11c","lp");
		leg2TrkIso->Draw();

		cnvs_TrkIso->SaveAs("eff_TrkIso_eUntagptBin2011.png");
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
		hFrame->SetXTitle("Pt_{additional electron}");
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

		cnvs_d0->SaveAs("eff_d0_eUntagptBin2011.png");
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
		hFrame->SetXTitle("Pt_{additional electron}");
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

		cnvs_All->SaveAs("eff_All_eUntagptBin2011.png");
	}

}


