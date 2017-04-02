#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Wed Apr 25 08:48:53 2012
##################################################

from gnuradio import audio
from gnuradio import blks2
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio import window
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class top_block(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Top Block")

		##################################################
		# Variables
		##################################################
		self.tranwidth = tranwidth = 10000
		self.tau = tau = 50e-6
		self.gain = gain = 20
		self.freq = freq = 100.0e6
		self.decim = decim = 80
		self.cutoff = cutoff = 100000

		##################################################
		# Blocks
		##################################################
		self._tranwidth_text_box = forms.text_box(
			parent=self.GetWin(),
			value=self.tranwidth,
			callback=self.set_tranwidth,
			label="tranwidth",
			converter=forms.float_converter(),
		)
		self.GridAdd(self._tranwidth_text_box, 1, 1, 1, 1)
		_tau_sizer = wx.BoxSizer(wx.VERTICAL)
		self._tau_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_tau_sizer,
			value=self.tau,
			callback=self.set_tau,
			label="Zeitkonstante (Tau)",
			converter=forms.float_converter(),
			proportion=0,
		)
		self._tau_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_tau_sizer,
			value=self.tau,
			callback=self.set_tau,
			minimum=0,
			maximum=100e-6,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_tau_sizer)
		_gain_sizer = wx.BoxSizer(wx.VERTICAL)
		self._gain_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_gain_sizer,
			value=self.gain,
			callback=self.set_gain,
			label="Gain [dB]",
			converter=forms.float_converter(),
			proportion=0,
		)
		self._gain_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_gain_sizer,
			value=self.gain,
			callback=self.set_gain,
			minimum=0,
			maximum=30,
			num_steps=60,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_gain_sizer)
		_freq_sizer = wx.BoxSizer(wx.VERTICAL)
		self._freq_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_freq_sizer,
			value=self.freq,
			callback=self.set_freq,
			label="Frequenz (UKW)",
			converter=forms.float_converter(),
			proportion=0,
		)
		self._freq_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_freq_sizer,
			value=self.freq,
			callback=self.set_freq,
			minimum=87.5e6,
			maximum=108e6,
			num_steps=205,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.GridAdd(_freq_sizer, 0, 0, 1, 1)
		self._decim_text_box = forms.text_box(
			parent=self.GetWin(),
			value=self.decim,
			callback=self.set_decim,
			label="Decimation",
			converter=forms.float_converter(),
		)
		self.GridAdd(self._decim_text_box, 1, 0, 1, 1)
		self._cutoff_text_box = forms.text_box(
			parent=self.GetWin(),
			value=self.cutoff,
			callback=self.set_cutoff,
			label="Cutoff",
			converter=forms.float_converter(),
		)
		self.GridAdd(self._cutoff_text_box, 0, 1, 1, 1)
		self.wxgui_fftsink2_0 = fftsink2.fft_sink_f(
			self.GetWin(),
			baseband_freq=0,
			y_per_div=10,
			y_divs=10,
			ref_level=0,
			ref_scale=2.0,
			sample_rate=64000000/decim,
			fft_size=1024,
			fft_rate=15,
			average=False,
			avg_alpha=None,
			title="FFT Plot",
			peak_hold=False,
		)
		self.Add(self.wxgui_fftsink2_0.win)
		self.uhd_usrp_source_0 = uhd.usrp_source(
			device_addr="type=usrp1",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_source_0.set_subdev_spec("B:0", 0)
		self.uhd_usrp_source_0.set_samp_rate(64000000/decim)
		self.uhd_usrp_source_0.set_center_freq(freq, 0)
		self.uhd_usrp_source_0.set_gain(gain, 0)
		self.low_pass_filter_0_0 = gr.fir_filter_fff(1, firdes.low_pass(
			1, 44100, 15000, tranwidth, firdes.WIN_HAMMING, 6.76))
		self.low_pass_filter_0 = gr.fir_filter_ccf(1, firdes.low_pass(
			1, 64000000/decim, cutoff, tranwidth, firdes.WIN_HAMMING, 6.76))
		self.gr_multiply_xx_0 = gr.multiply_vcc(1)
		self.gr_iir_filter_ffd_1 = gr.iir_filter_ffd(((1.0/(1+tau*2*800000), 1.0/(1+tau*2*800000))), ((1, -(1-tau*2*800000)/(1+tau*2*800000))))
		self.gr_delay_0 = gr.delay(gr.sizeof_gr_complex*1, 1)
		self.gr_conjugate_cc_0 = gr.conjugate_cc()
		self.gr_complex_to_arg_0 = gr.complex_to_arg(1)
		self.blks2_rational_resampler_xxx_0 = blks2.rational_resampler_fff(
			interpolation=44100,
			decimation=64000000/decim,
			taps=None,
			fractional_bw=None,
		)
		self.audio_sink_0 = audio.sink(44100, "", True)

		##################################################
		# Connections
		##################################################
		self.connect((self.uhd_usrp_source_0, 0), (self.low_pass_filter_0, 0))
		self.connect((self.low_pass_filter_0, 0), (self.gr_delay_0, 0))
		self.connect((self.low_pass_filter_0, 0), (self.gr_multiply_xx_0, 0))
		self.connect((self.gr_delay_0, 0), (self.gr_conjugate_cc_0, 0))
		self.connect((self.gr_conjugate_cc_0, 0), (self.gr_multiply_xx_0, 1))
		self.connect((self.gr_multiply_xx_0, 0), (self.gr_complex_to_arg_0, 0))
		self.connect((self.gr_complex_to_arg_0, 0), (self.blks2_rational_resampler_xxx_0, 0))
		self.connect((self.blks2_rational_resampler_xxx_0, 0), (self.low_pass_filter_0_0, 0))
		self.connect((self.low_pass_filter_0_0, 0), (self.gr_iir_filter_ffd_1, 0))
		self.connect((self.gr_iir_filter_ffd_1, 0), (self.audio_sink_0, 0))
		self.connect((self.gr_complex_to_arg_0, 0), (self.wxgui_fftsink2_0, 0))

	def get_tranwidth(self):
		return self.tranwidth

	def set_tranwidth(self, tranwidth):
		self.tranwidth = tranwidth
		self.low_pass_filter_0.set_taps(firdes.low_pass(1, 64000000/self.decim, self.cutoff, self.tranwidth, firdes.WIN_HAMMING, 6.76))
		self._tranwidth_text_box.set_value(self.tranwidth)
		self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, 44100, 15000, self.tranwidth, firdes.WIN_HAMMING, 6.76))

	def get_tau(self):
		return self.tau

	def set_tau(self, tau):
		self.tau = tau
		self._tau_slider.set_value(self.tau)
		self._tau_text_box.set_value(self.tau)
		self.gr_iir_filter_ffd_1.set_taps(((1.0/(1+self.tau*2*800000), 1.0/(1+self.tau*2*800000))), ((1, -(1-self.tau*2*800000)/(1+self.tau*2*800000))))

	def get_gain(self):
		return self.gain

	def set_gain(self, gain):
		self.gain = gain
		self._gain_slider.set_value(self.gain)
		self._gain_text_box.set_value(self.gain)
		self.uhd_usrp_source_0.set_gain(self.gain, 0)

	def get_freq(self):
		return self.freq

	def set_freq(self, freq):
		self.freq = freq
		self._freq_slider.set_value(self.freq)
		self._freq_text_box.set_value(self.freq)
		self.uhd_usrp_source_0.set_center_freq(self.freq, 0)

	def get_decim(self):
		return self.decim

	def set_decim(self, decim):
		self.decim = decim
		self._decim_text_box.set_value(self.decim)
		self.low_pass_filter_0.set_taps(firdes.low_pass(1, 64000000/self.decim, self.cutoff, self.tranwidth, firdes.WIN_HAMMING, 6.76))
		self.uhd_usrp_source_0.set_samp_rate(64000000/self.decim)
		self.wxgui_fftsink2_0.set_sample_rate(64000000/self.decim)

	def get_cutoff(self):
		return self.cutoff

	def set_cutoff(self, cutoff):
		self.cutoff = cutoff
		self._cutoff_text_box.set_value(self.cutoff)
		self.low_pass_filter_0.set_taps(firdes.low_pass(1, 64000000/self.decim, self.cutoff, self.tranwidth, firdes.WIN_HAMMING, 6.76))

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

