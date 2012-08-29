#############################################################################

import math, time, ROOT

#############################################################################

def init():
	ROOT.gStyle.SetFrameBorderMode(0)
	ROOT.gStyle.SetFrameFillColor(0)
	ROOT.gStyle.SetCanvasBorderMode(0)
	ROOT.gStyle.SetCanvasColor(0)
	ROOT.gStyle.SetPadBorderMode(0)
	ROOT.gStyle.SetPadColor(0)

	ROOT.gStyle.SetPaperSize(20, 26)

	ROOT.gStyle.SetPadTopMargin(0.05)
	ROOT.gStyle.SetPadRightMargin(0.05)
	ROOT.gStyle.SetPadBottomMargin(0.16)
	ROOT.gStyle.SetPadLeftMargin(0.16)

	ROOT.gStyle.SetTitleXOffset(1.4)
	ROOT.gStyle.SetTitleYOffset(1.4)

	ROOT.gStyle.SetTextFont(42)
	ROOT.gStyle.SetLabelFont(42, 'x')
	ROOT.gStyle.SetTitleFont(42, 'x')
	ROOT.gStyle.SetLabelFont(42, 'y')
	ROOT.gStyle.SetTitleFont(42, 'y')
	ROOT.gStyle.SetLabelFont(42, 'z')
	ROOT.gStyle.SetTitleFont(42, 'z')

	ROOT.gStyle.SetTextSize(0.05)
	ROOT.gStyle.SetLabelSize(0.05, 'x')
	ROOT.gStyle.SetTitleSize(0.05, 'x')
	ROOT.gStyle.SetLabelSize(0.05, 'y')
	ROOT.gStyle.SetTitleSize(0.05, 'y')
	ROOT.gStyle.SetLabelSize(0.05, 'z')
	ROOT.gStyle.SetTitleSize(0.05, 'z')

	ROOT.gStyle.SetEndErrorSize(2.5)

	ROOT.gStyle.SetPadTickX(1)
	ROOT.gStyle.SetPadTickY(1)

#############################################################################

def drawFrame(xmin, xmax, ymin, ymax, title = '', option = '', nr = 1):

	dummy = ROOT.TH1F('dummy%f' % time.time(), title, nr, xmin, xmax);

	dummy.SetMinimum(ymin);
	dummy.SetMaximum(ymax);

	dummy.SetStats(False);
	dummy.Draw(option);

	return dummy

#############################################################################

def drawLegend(x, y, n = 2.0):

	legend = ROOT.TLegend()
	legend.SetFillColor(0)
	legend.SetBorderSize(0)
	legend.SetTextSize(0.04)

	delx = (1.0 * ROOT.gPad.GetWh()) / (1.0 * ROOT.gPad.GetWw())

	legend.SetX1NDC(x)
	legend.SetX2NDC(x + 0.6 * 0.2)
	legend.SetY1NDC(y)
	legend.SetY2NDC(y + 0.6 * (0.055 * n / delx))

	return legend

#############################################################################

def drawAtlasLabel1(x, y, msg = "Work in progress"):
	l = ROOT.TLatex()
	l.SetNDC()
	l.SetTextFont(72)
	l.SetTextColor(ROOT.kBlack)
	l.DrawLatex(x + 0x00, y, "ATLAS")

	delx = 0.115 * (696.0 * ROOT.gPad.GetWh()) / (472.0 * ROOT.gPad.GetWw())

	l = ROOT.TLatex()
	l.SetNDC()
	l.SetTextFont(42)
	l.SetTextColor(ROOT.kBlack)
	l.DrawLatex(x + delx, y, msg)

#############################################################################

def drawAtlasLabel2(x, y, msg = "Preliminary"):
	l = ROOT.TLatex()
	l.SetNDC()
	l.SetTextFont(72)
	l.SetTextColor(ROOT.kBlack)
	l.DrawLatex(x + 0x00, y, "ATLAS")

	delx = 0.115 * (696.0 * ROOT.gPad.GetWh()) / (472.0 * ROOT.gPad.GetWw())

	l = ROOT.TLatex()
	l.SetNDC()
	l.SetTextFont(42)
	l.SetTextColor(ROOT.kBlack)
	l.DrawLatex(x + delx, y, msg)

#############################################################################

def getGraphFromHisto(hist, error):
	i_point = 0

	if error != False:
		graph = ROOT.TGraphAsymmErrors()
	else:

		graph = ROOT.     TGraph      ()

	for i in xrange(1, hist.GetNbinsX() + 1):

		if hist.GetBinContent(i) != 0:

			graph.SetPoint(
				i_point
				,
				hist.GetBinCenter(i)
				,
				hist.GetBinContent(i)
			)

			if error != False:

				graph.SetPointError(
					i_point
					,
					0.0
					,
					0.0
					,
					(-0.5 + math.sqrt(hist.GetBinContent(i) + 0.25)) * 1.2
					,
					(+0.5 + math.sqrt(hist.GetBinContent(i) + 0.25)) * 1.2
				)

			i_point += 1

	graph.SetMarkerSize(1.0)
	graph.SetMarkerStyle( 8 )
	graph.SetMarkerColor(ROOT.kBlack)

	graph.SetLineWidth(2)
	graph.SetLineColor(ROOT.kBlack)

	graph.SetTitle(hist.GetTitle())

	return graph

#############################################################################

def CDF(hist):
	th1 = hist.Clone()
	th2 = hist.Clone()

	normalize(th1)

	for i in xrange(th1.GetXaxis().GetFirst(), th1.GetXaxis().GetLast() + 1):

		th2.SetBinContent(i, hist.Integral(0, i))

	return th2

#############################################################################

def CDF_inv(hist):
	th1 = hist.Clone()
	th2 = hist.Clone()

	normalize(th1)

	for i in xrange(th1.GetXaxis().GetFirst(), th1.GetXaxis().GetLast() + 1):

		th2.SetBinContent(i, 1.0 - hist.Integral(0, i))

	return th2

#############################################################################

def normalize(hist):
	I = hist.Integral('width')

	if I != 0.0:
		hist.Scale(1.0 / I)

#############################################################################

