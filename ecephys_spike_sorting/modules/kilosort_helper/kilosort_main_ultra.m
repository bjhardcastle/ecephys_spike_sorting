%% you need to change most of the paths in this block

addpath(genpath('C:\Users\svc_neuropix\Documents\GitHub\KilosortUltra')) % path to kilosort folder
addpath(genpath('C:\Users\svc_neuropix\Documents\GitHub\npy-matlab')) % path to npy-matlab scripts
%rootH = 'C:\data\kilosort'; % path to temporary binary file (same size as data, should be on fast SSD)
pathToYourConfigFile = 'C:\Users\svc_neuropix\Documents\MATLAB'; % take from Github folder and put it somewhere else (together with the master_file)
run(fullfile(pathToYourConfigFile, 'kilosortUltra_config_file.m'))

% find the binary file
rootZ       = ops.rootZ
ops.fbinary = fullfile(ops.datafile)

%% this block runs all the steps of the algorithm
fprintf('Looking for data inside %s \n', rootZ)

% preprocess data to create temp_wh.dat
rez = preprocessDataSub(ops);

% time-reordering as a function of drift
rez = clusterSingleBatches(rez);

% saving here is a good idea, because the rest can be resumed after loading rez
save(fullfile(rootZ, 'rez.mat'), 'rez', '-v7.3');

% main tracking and template matching algorithm
rez = learnAndSolve8b(rez);

% final merges
rez = find_merges(rez, 1);

% final splits by SVD
rez = splitAllClusters(rez, 1);

% final splits by amplitudes
rez = splitAllClusters(rez, 0);

% decide on cutoff
rez = set_cutoff(rez);

fprintf('found %d good units \n', sum(rez.good>0))

% write to Phy
fprintf('Saving results to Phy  \n')
rezToPhy(rez, rootZ);

%% if you want to save the results to a Matlab file...

% discard features in final rez file (too slow to save)
rez.cProj = [];
rez.cProjPC = [];

% final time sorting of spikes, for apps that use st3 directly
[~, isort]   = sortrows(rez.st3);
rez.st3      = rez.st3(isort, :);

% save final results as rez2
fprintf('Saving final results in rez2  \n')
fname = fullfile(rootZ, 'rez2.mat');
save(fname, 'rez', '-v7.3');
