#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Wed Apr 27 11:55:39 2016
##################################################

from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx

class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.vol = vol = 100
        self.tau = tau = 50e-6
        self.samp_rate = samp_rate = 1000000
        self.rx_gain = rx_gain = 20
        self.freq = freq = 107.2e6
        self.decim = decim = 80
        self.b_signal = b_signal = 50e3

        ##################################################
        # Blocks
        ##################################################
        _vol_sizer = wx.BoxSizer(wx.VERTICAL)
        self._vol_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_vol_sizer,
        	value=self.vol,
        	callback=self.set_vol,
        	label="Volume L",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._vol_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_vol_sizer,
        	value=self.vol,
        	callback=self.set_vol,
        	minimum=0,
        	maximum=300,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_vol_sizer, 2, 0, 1, 1)
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
        self.GridAdd(_tau_sizer, 0, 1, 1, 1)
        self._samp_rate_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.samp_rate,
        	callback=self.set_samp_rate,
        	label="Sampling Rate",
        	converter=forms.float_converter(),
        )
        self.GridAdd(self._samp_rate_text_box, 1, 0, 1, 1)
        _rx_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._rx_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_rx_gain_sizer,
        	value=self.rx_gain,
        	callback=self.set_rx_gain,
        	label="Receiver Gain",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._rx_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_rx_gain_sizer,
        	value=self.rx_gain,
        	callback=self.set_rx_gain,
        	minimum=0,
        	maximum=50,
        	num_steps=50,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_rx_gain_sizer, 2, 2, 1, 1)
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
        	minimum=80e6,
        	maximum=230e6,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_freq_sizer, 0, 0, 1, 1)
        _b_signal_sizer = wx.BoxSizer(wx.VERTICAL)
        self._b_signal_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_b_signal_sizer,
        	value=self.b_signal,
        	callback=self.set_b_signal,
        	label="Signalbandbreite",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._b_signal_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_b_signal_sizer,
        	value=self.b_signal,
        	callback=self.set_b_signal,
        	minimum=1e3,
        	maximum=400e3,
        	num_steps=399,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_b_signal_sizer, 1, 1, 1, 1)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=500,
                decimation=480,
                taps=None,
                fractional_bw=None,
        )
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(freq, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(2, 0)
        self.osmosdr_source_0.set_gain_mode(True, 0)
        self.osmosdr_source_0.set_gain(rx_gain, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna("", 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
          
        self.notebook_0 = self.notebook_0 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Audio L (FFT)")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Audio R (FFT)")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Audio L (Scope)")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Audio R (Scope)")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "MPX-Signal (FFT)")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "RX FFT")
        self.GridAdd(self.notebook_0, 3, 0, 1, 3)
        self.low_pass_filter_2_1_0_0 = filter.fir_filter_fff(20, firdes.low_pass(
        	1, samp_rate, 15000, 500, firdes.WIN_HANN, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, b_signal, 2000, firdes.WIN_HANN, 6.76))
        self.iir_filter_xxx_0 = filter.iir_filter_ffd(((1.0/(1+tau*2*samp_rate), 1.0/(1+tau*2*samp_rate))), ((1, -(1-tau*2*samp_rate)/(1+tau*2*samp_rate))), True)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((vol/100, ))
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, 1)
        self.blocks_complex_to_arg_0 = blocks.complex_to_arg(1)
        self.audio_sink_0 = audio.sink(48000, "", True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_conjugate_cc_0, 1))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_multiply_conjugate_cc_0, 0))
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.blocks_complex_to_arg_0, 0))
        self.connect((self.low_pass_filter_2_1_0_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_complex_to_arg_0, 0), (self.iir_filter_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.iir_filter_xxx_0, 0), (self.low_pass_filter_2_1_0_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.wxgui_fftsink2_0, 0))



    def get_vol(self):
        return self.vol

    def set_vol(self, vol):
        self.vol = vol
        self.blocks_multiply_const_vxx_0_0.set_k((self.vol/100, ))
        self._vol_slider.set_value(self.vol)
        self._vol_text_box.set_value(self.vol)

    def get_tau(self):
        return self.tau

    def set_tau(self, tau):
        self.tau = tau
        self._tau_slider.set_value(self.tau)
        self._tau_text_box.set_value(self.tau)
        self.iir_filter_xxx_0.set_taps(((1.0/(1+self.tau*2*self.samp_rate), 1.0/(1+self.tau*2*self.samp_rate))), ((1, -(1-self.tau*2*self.samp_rate)/(1+self.tau*2*self.samp_rate))))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self._samp_rate_text_box.set_value(self.samp_rate)
        self.iir_filter_xxx_0.set_taps(((1.0/(1+self.tau*2*self.samp_rate), 1.0/(1+self.tau*2*self.samp_rate))), ((1, -(1-self.tau*2*self.samp_rate)/(1+self.tau*2*self.samp_rate))))
        self.low_pass_filter_2_1_0_0.set_taps(firdes.low_pass(1, self.samp_rate, 15000, 500, firdes.WIN_HANN, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.b_signal, 2000, firdes.WIN_HANN, 6.76))
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        self._rx_gain_slider.set_value(self.rx_gain)
        self._rx_gain_text_box.set_value(self.rx_gain)
        self.osmosdr_source_0.set_gain(self.rx_gain, 0)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self._freq_slider.set_value(self.freq)
        self._freq_text_box.set_value(self.freq)
        self.osmosdr_source_0.set_center_freq(self.freq, 0)

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim

    def get_b_signal(self):
        return self.b_signal

    def set_b_signal(self, b_signal):
        self.b_signal = b_signal
        self._b_signal_slider.set_value(self.b_signal)
        self._b_signal_text_box.set_value(self.b_signal)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.b_signal, 2000, firdes.WIN_HANN, 6.76))

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = top_block()
    tb.Start(True)
    tb.Wait()
