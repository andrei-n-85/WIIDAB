% One OFDM symbol; DAB-Transmission Mode 1
close all, clear all, clc
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% SENDER
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Generate bits
bits_to_map = randi(2,3072,1)-1; % random bits
%bits_to_map = zeros(3072,1); % zeros

% Modulation: 4-QAM
h = modem.qammod('M',4,'InputType','bit'); % Initialization
z = modulate(h,bits_to_map);
%scatterplot(z); title('QAM-Symbols at Sender'); xlabel('Real Part (Inphase)'); ylabel('Imaginary Part (Quadrature)'); xlim([-10 10]); ylim([-10 10]);

% OFDM-Modulation
CP_duration = 504; % Duration of Cyclic Prefix


z_input = [zeros(256,1); z(1:768); 0; z(769:1536); zeros(255,1)]; % include zeros for oversampling; include 0 at DC (Gleichanteil)
figure, plot(abs(z_input));
ofdm_symbol_wo_cp = ifft(ifftshift(z_input)); % Ofdm Symbol without Cyclic Prefix
demod_onspot = fftshift(fft(ofdm_symbol_wo_cp));
hold on, plot(abs(demod_onspot),'r'), hold off;
ofdm_symbol_wo_cp = ofdm_symbol_wo_cp.';
ofdm_symbol = [ofdm_symbol_wo_cp((end-CP_duration+1):end) ofdm_symbol_wo_cp]; %add cyclic prefix

s_TP = ofdm_symbol/sqrt(mean(abs(ofdm_symbol).^2)); %scale to average power of 1
figure; plot(abs(s_TP)); title('Absolute Value of Transmitted signal'); xlabel('Time (samples)'); ylabel('Absolute value');


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Channel
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Path 1
a_1 = 1; % attenuation of path 1
tau_1 = 1; % delay of path 1 (number of samples)

% Path 2
a_2 = 0.3; % attenuation of path 2
tau_2 = 10; % delay of path 2 (number of samples) % tau_2 has to be larger or equal than tau_1

% Noise
noise_var = 0;
noise = sqrt(noise_var/2)*(randn(1,length(s_TP)+tau_2) + 1i*randn(1,length(s_TP)+tau_2));


s_TP_shifted1 = [zeros(1,tau_1) s_TP zeros(1,tau_2-tau_1)];
s_TP_shifted2 = [zeros(1,tau_2) s_TP];
r_TP = a_1 * s_TP_shifted1 + a_2 * s_TP_shifted2 + noise;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Receiver
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% APPOINTMENT 2: IMPLEMENTATION OF YOUR RECEIVER

%% SOLUTION 
%remove cyclic prefix
r_TP_wo_cp = r_TP(CP_duration+1:end-tau_2);
%get channel freq domain transfer function
H = fftshift(fft(impz([[zeros(1,tau_1) a_1 zeros(1,tau_2-tau_1)]+[zeros(1,tau_1) zeros(1,tau_2-tau_1) a_2]]),2048)).';
%demod FFT 
s = fftshift(fft(r_TP_wo_cp))*sqrt(mean(abs(ofdm_symbol).^2));
figure, plot(abs(s)), hold on , plot(abs(H),'r'),hold off;
scatterplot(s),title('QAM-Symbols at Receiver'); xlabel('Real Part (Inphase)'); ylabel('Imaginary Part (Quadrature)'); xlim([-10 10]); ylim([-10 10]);
%One tap equalization
s2 = s./H;
plot(abs(s2),'m'), hold off
%find zeros and eliminate them
idx = (z_input ~= 0);
s1 = s2(idx==1);
modObj = modem.qamdemod('M', 4, 'OutputType', 'Bit') ;
scatterplot(s1); title('QAM-Symbols at Receiver'); xlabel('Real Part (Inphase)'); ylabel('Imaginary Part (Quadrature)'); xlim([-10 10]); ylim([-10 10]);
e_bit = demodulate(modObj,s1);
r_bits_to_map = reshape(e_bit,3072,1);
%END SOLUTION



disp('**************************************');
disp('number of total bits');
disp(length(bits_to_map));
disp('number of bit errors');
disp(sum(abs(r_bits_to_map - bits_to_map)));
disp('Signal-to-Noise Ratio in dB');
SNR = mean(abs(a_1 * s_TP_shifted1 + a_2 * s_TP_shifted2).^2)/mean(abs(noise).^2);
disp(10*log10(SNR));

