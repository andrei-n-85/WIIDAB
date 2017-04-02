%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% additional_files/create_fixed_vars.m                                    %
%                                                                         %
% Requires: no requirements                                               %
% Returns: - fixed_vars (struct)                                          %
%-------------------------------------------------------------------------%
% This function creates variable necessary to create a DAB transmission.  %
% The values never change and are called therefore fixed variables.       %
%                                                                         %
%-------------------------------------------------------------------------%
% MASTER THESIS: CHRISTOPHER TSCHISCHKA                                   %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function fixed_vars = create_fixed_vars

    % Number of sub carriers in TM1
    fixed_vars.K = 1536;

    % Frequency permutation vector for TM1
    fixed_vars.freq_perm = frequency_permutation;

    % TFPR symbol for TM1
    fixed_vars.TFPR = TFPR_generation;

    % PRBS for energy dispersial and CIF pdding bits
    fixed_vars.PRBS = PRBS_generation;

     % For convolitional coding
    fixed_vars.tre = poly2trellis(7, [133, 171, 145, 133]); 

    % Puncturing vector for UEP
    fixed_vars.punct_vectors = logical( [ 1 1 0 0 1 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 ; % PI 01 
                                          1 1 0 0 1 0 0 0 1 0 0 0 1 0 0 0 1 1 0 0 1 0 0 0 1 0 0 0 1 0 0 0 ; % PI 02
                                          1 1 0 0 1 0 0 0 1 1 0 0 1 0 0 0 1 1 0 0 1 0 0 0 1 0 0 0 1 0 0 0 ; % PI 03
                                          1 1 0 0 1 0 0 0 1 1 0 0 1 0 0 0 1 1 0 0 1 0 0 0 1 1 0 0 1 0 0 0 ; % PI 04
                                          1 1 0 0 1 1 0 0 1 1 0 0 1 0 0 0 1 1 0 0 1 0 0 0 1 1 0 0 1 0 0 0 ; % PI 05
                                          1 1 0 0 1 1 0 0 1 1 0 0 1 0 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 0 0 0 ; % PI 06
                                          1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 0 0 0 ; % PI 07           
                                          1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 ; % PI 08
                                          1 1 1 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 ; % PI 09
                                          1 1 1 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 1 0 1 1 0 0 1 1 0 0 1 1 0 0 ; % PI 10
                                          1 1 1 0 1 1 0 0 1 1 1 0 1 1 0 0 1 1 1 0 1 1 0 0 1 1 0 0 1 1 0 0 ; % PI 11
                                          1 1 1 0 1 1 0 0 1 1 1 0 1 1 0 0 1 1 1 0 1 1 0 0 1 1 1 0 1 1 0 0 ; % PI 12
                                          1 1 1 0 1 1 1 0 1 1 1 0 1 1 0 0 1 1 1 0 1 1 0 0 1 1 1 0 1 1 0 0 ; % PI 13
                                          1 1 1 0 1 1 1 0 1 1 1 0 1 1 0 0 1 1 1 0 1 1 1 0 1 1 1 0 1 1 0 0 ; % PI 14
                                          1 1 1 0 1 1 1 0 1 1 1 0 1 1 1 0 1 1 1 0 1 1 1 0 1 1 1 0 1 1 0 0 ; % PI 15
                                          1 1 1 0 1 1 1 0 1 1 1 0 1 1 1 0 1 1 1 0 1 1 1 0 1 1 1 0 1 1 1 0 ; % PI 16
                                          1 1 1 1 1 1 1 0 1 1 1 0 1 1 1 0 1 1 1 0 1 1 1 0 1 1 1 0 1 1 1 0 ; % PI 17
                                          1 1 1 1 1 1 1 0 1 1 1 0 1 1 1 0 1 1 1 1 1 1 1 0 1 1 1 0 1 1 1 0 ; % PI 18
                                          1 1 1 1 1 1 1 0 1 1 1 1 1 1 1 0 1 1 1 1 1 1 1 0 1 1 1 0 1 1 1 0 ; % PI 19
                                          1 1 1 1 1 1 1 0 1 1 1 1 1 1 1 0 1 1 1 1 1 1 1 0 1 1 1 1 1 1 1 0 ; % PI 20
                                          1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1 1 1 1 0 1 1 1 1 1 1 1 0 ; % PI 21
                                          1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 ; % PI 22
                                          1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 ; % PI 23
                                          1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 ; % PI 24
                                          ] );


    % Tail puncturing vector for UEP
    fixed_vars.punct_tail = logical ( [1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 ] );

    % To get the audio bit rate for UEP
    fixed_vars.audio_bit_rates = [32 48 56 64 80 96 112 128 160 192 224 256 320 384]; 

    % Tables with the length, puncturing vectors and the padding bits for a
    % given protection level (from Table 36 p.158ff) are defined
    % Scheme: table_protlvl_x = [ L1 L2 L3 L4 PI1 PI2 PI3 PI4 padding] %bitrate
    fixed_vars.table_protlvl_1 = [ 03 05 13 03 24 17 12 17 4; % 32kbps
                                   03 05 25 03 24 18 13 18 0; % 48kbps
                                   00 00 00 00 00 00 00 00 0; % 56kbps
                                   06 11 28 03 24 18 12 18 4; % 64kbps
                                   06 10 41 03 24 17 12 18 4; % 80kbps
                                   06 13 50 03 24 18 13 19 0; % 96kbps
                                   00 00 00 00 00 00 00 00 0; % 112kbps
                                   11 20 62 03 24 17 13 19 8; % 128kbps
                                   11 22 84 03 24 18 12 19 0; % 160kbps
                                   11 21 109 3 24 20 13 24 0; % 192kbps
                                   11 24 130 3 24 20 12 20 4; % 224kbps
                                   11 26 152 3 24 19 14 18 4; % 256kbps
                                   00 00 00 00 00 00 00 00 0; % 320kbps
                                   12 28 245 3 24 20 14 23 8; % 384kbps
                                 ]; 

    fixed_vars.table_protlvl_2 = [ 03 04 14 03 22 13 08 13 0; % 32kbps
                                   03 04 26 03 24 14 08 15 0; % 48kbps
                                   06 10 23 03 23 13 08 13 8; % 56kbps
                                   06 10 29 03 23 13 08 13 8; % 64kbps
                                   06 10 41 03 23 13 08 13 8; % 80kbps
                                   06 10 53 03 22 12 09 12 0; % 96kbps
                                   11 21 49 03 23 12 09 14 4; % 112kbps
                                   11 21 61 03 22 12 09 14 0; % 128kbps
                                   11 21 85 03 22 11 09 13 0; % 160kbps
                                   11 20 110 3 22 13 09 13 8; % 192kbps
                                   11 22 132 3 24 16 10 15 0; % 224kbps
                                   11 22 156 3 24 14 10 13 8; % 256kbps
                                   11 26 200 3 24 17 09 17 0; % 320kbps
                                   00 00 00 00 00 00 00 00 0; % 384kbps
                               ]; 

    fixed_vars.table_protlvl_3 = [ 03 04 14 03 15 09 06 08 0; % 32kbps
                                   03 04 26 03 15 10 06 09 4; % 48kbps
                                   06 12 21 03 16 07 06 09 0; % 56kbps
                                   06 12 27 03 16 08 06 09 0; % 64kbps
                                   06 11 40 03 16 08 06 07 0; % 80kbps
                                   06 12 51 03 16 09 06 10 4; % 96kbps
                                   11 23 47 03 16 08 06 09 0; % 112kbps
                                   11 22 60 03 16 09 06 10 4; % 128kbps
                                   11 24 82 03 16 08 06 11 0; % 160kbps
                                   11 24 106 3 16 10 06 11 0; % 192kbps
                                   11 20 134 3 16 10 07 09 0; % 224kbps
                                   11 27 151 3 16 10 09 10 0; % 256kbps
                                   00 00 00 00 00 00 00 00 0; % 320kbps
                                   11 24 250 3 16 09 07 10 4; % 384kbps
                                 ]; 

    fixed_vars.table_protlvl_4 = [ 03 03 18 00 11 06 05 00 0; % 32kbps           
                                   03 04 26 03 09 06 04 06 0; % 48kbps
                                   06 10 23 03 09 06 04 05 0; % 56kbps
                                   06 09 33 00 11 06 06 00 0; % 64kbps
                                   06 10 41 03 11 06 05 06 0; % 80kbps
                                   07 10 52 03 09 06 04 06 0; % 96kbps
                                   11 21 49 03 09 06 04 08 0; % 112kbps
                                   11 21 61 03 11 06 05 07 0; % 128kbps
                                   11 23 83 03 11 06 05 09 0; % 160kbps
                                   11 22 108 3 10 06 04 09 0; % 192kbps
                                   12 26 127 3 12 08 04 11 0; % 224kbps
                                   11 24 154 3 12 09 05 10 4; % 256kbps
                                   11 25 201 3 13 09 05 10 8; % 320kbps
                                   00 00 00 00 00 00 00 00 0; % 384kbps
                                 ]; 

    fixed_vars.table_protlvl_5 = [ 03 04 17 00 05 03 02 00 0; % 32kbps
                                   04 03 26 03 05 04 02 03 0; % 48kbps
                                   06 10 23 03 05 04 02 03 0; % 56kbps
                                   06 09 31 02 05 03 02 03 0; % 64kbps
                                   06 10 41 03 06 03 02 03 0; % 80kbps
                                   07 09 53 03 05 04 02 04 0; % 96kbps
                                   14 17 50 03 05 04 02 05 0; % 112kbps
                                   12 19 62 03 05 03 02 04 0; % 128kbps
                                   11 19 87 03 05 04 02 04 0; % 160kbps
                                   11 20 110 3 06 04 02 05 0; % 192kbps
                                   12 22 131 3 08 06 02 06 4; % 224kbps
                                   11 24 154 3 06 05 02 05 0; % 256kbps
                                   11 26 200 3 08 05 02 06 4; % 320kbps
                                   11 27 247 3 08 06 02 07 0; % 384kbps
                                 ];  

    % Table 7
    fixed_vars.table_7 = [ 04 03 02 01 00  
                           09 08 07 06 05
                           00 13 12 11 10
                           18 17 16 15 14
                           23 22 21 20 19
                           28 27 26 25 24
                           00 32 31 30 29
                           37 36 35 34 33
                           42 41 40 39 38
                           47 46 45 44 43 
                           52 51 50 49 48
                           57 56 55 54 53
                           00 60 00 59 58
                           63 00 62 00 61
                         ];
                 

    % Calculation of length of CU for protection level and audio bit rate
	fixed_vars.table7_length = [35  29  24  21  16 ; % 32kbps
                                52  42  35  29  24 ; % 48kbps
                                0   52  42  35  29 ; % 56kbps
                                70  58  48  42  32 ; % 64kbps
                                84  70  58  52  40 ; % 80kbps
                                104 84  70  58  48 ; % 96kbps
                                0   104 84  70  58 ; % 112kbps
                                140 116 96  84  64 ; % 128kbps
                                168 140 116 104 80 ; % 160kbps
                                208 168 140 116 96 ; % 192kbps
                                232 208 168 140 116; % 224kbps
                                280 232 192 168 128; % 256kbps
                                0   280   0 208 160; % 320kbps
                                416   0 280   0 192; % 384kbps
                               ];   

