from argschema import ArgSchema, ArgSchemaParser 
from argschema.schemas import DefaultSchema
from argschema.fields import Nested, InputDir, String, Float, Dict, Int, NumpyArray
from ...common.schemas import EphysParams, Directories, CommonFiles

class KilosortParameters(DefaultSchema):

	Nfilt = Int(required=False, default=1024)
	Threshold = String(required=False, default="[4, 10, 10]")
	lam = String(required=False, default="[5, 20, 20]")
	IntitalizeTh = Int(required=False, default=-4)
	InitializeNfilt = Int(required=False, default=10000)
    
class Kilosort2Parameters(DefaultSchema):

    trange = String(required=False, default='[0 Inf]', help='Time range in seconds to process')
    fproc = String(required=False, default="fullfile('C:/data/kilosort', 'temp_wh.dat')", help='Processed data file on a fast ssd')
  
    chanMap = String(required=False, default="'chanMap.mat'", help='path to channel map .mat file')
    fshigh = Int(required=False, default=150, help='frequency for high pass filtering')
    minfr_goodchannels = Float(required=False, default=0.1, help='minimum firing rate on a "good" channel (0 to skip)')
    Th = String(required=False, default='[10 4]', help='threshold (last pass can be lower')
    lam = Int(required=False, default=10, help='how important is the amplitude penalty (like in Kilosort1, 0 means not used, 10 is average, 50 is a lot)')
    AUCsplit = Float(required=False, default=0.9, help='splitting a cluster at the end requires at least this much isolation for each sub-cluster (max = 1)')
    minFR = Float(required=False, default=1/50., help='minimum spike rate (Hz)')
    momentum = String(required=False, default='[20 400]', help='number of samples to average over (annealed)')
    sigmaMask = Int(required=False, default=30, help='spatial constant in um for computing residual variance of spike')
    ThPre = Int(required=False, default=8, help='threshold crossings for pre-clustering (in PCA projection space)')

    spkTh = Int(required=False, default=-6, help='spike threshold is standard deviations')
    reorder = Int(required=False, default=1, help='whether to reorder batches for drift correction')
    nskip = Int(required=False, default=25, help='how many batches to skip for determining spike PCs')
    GPU = Int(required=False, default=1, help='whether to run this code on an Nvidia GPU')
    nfilt_factor = Int(required=False, default=4, help='max number of clusters per good channel (even temporary ones)')
    ntbuff = Int(required=False, default=64, help='samples of symmetrical buffer for whitening and spike detection')
    NT = String(required=False, default='64*1024 + ops.ntbuff', help='this is the batch size; for GPU should be a multiple of 32 + ntbuff)')
    whiteningRange = Int(required=False, default=32)
    nSkipCov = Int(required=False, default=25, help='compute whitening matrix from every Nth batch')
    scaleproc = Int(required=False, default=200, help='int16 scaling of whitenend data')
    nPCs = Int(required=False, default=3, help='how many PCs to project the spikes into')
    useRAM = Int(required=False, default=0, help='must be 0')

class Kilosort3Parameters(DefaultSchema):

    trange = String(required=False, default='[0 Inf]', help='Time range in seconds to process')
    fproc = String(required=False, default="fullfile('D:/data/kilosort', 'temp_wh.dat')", help='Processed data file on a fast ssd')
  
    chanMap = String(required=False, default="'chanMap.mat'", help='path to channel map .mat file')
    fshigh = Int(required=False, default=300, help='frequency for high pass filtering')
    minfr_goodchannels = Float(required=False, default=0.1, help='minimum firing rate on a "good" channel (0 to skip)')
    Th = String(required=False, default='[9 9]', help='threshold (last pass can be lower')
    lam = Int(required=False, default=10, help='how important is the amplitude penalty (like in Kilosort1, 0 means not used, 10 is average, 50 is a lot)')
    AUCsplit = Float(required=False, default=0.8, help='splitting a cluster at the end requires at least this much isolation for each sub-cluster (max = 1)')
    minFR = Float(required=False, default=1/50., help='minimum spike rate (Hz)')
    momentum = String(required=False, default='[20 400]', help='number of samples to average over (annealed)')
    sigmaMask = Int(required=False, default=30, help='spatial constant in um for computing residual variance of spike')
    ThPre = Int(required=False, default=8, help='threshold crossings for pre-clustering (in PCA projection space)')
    sig = Int(required=False, default=20)
    nblocks = Int(required=False, default=5)

    spkTh = Int(required=False, default=-6, help='spike threshold is standard deviations')
    reorder = Int(required=False, default=1, help='whether to reorder batches for drift correction')
    nskip = Int(required=False, default=25, help='how many batches to skip for determining spike PCs')
    GPU = Int(required=False, default=1, help='whether to run this code on an Nvidia GPU')
    nfilt_factor = Int(required=False, default=4, help='max number of clusters per good channel (even temporary ones)')
    ntbuff = Int(required=False, default=64, help='samples of symmetrical buffer for whitening and spike detection')
    NT = String(required=False, default='64*1024 + ops.ntbuff', help='this is the batch size; for GPU should be a multiple of 32 + ntbuff)')
    whiteningRange = Int(required=False, default=32)
    nSkipCov = Int(required=False, default=25, help='compute whitening matrix from every Nth batch')
    scaleproc = Int(required=False, default=200, help='int16 scaling of whitenend data')
    nPCs = Int(required=False, default=3, help='how many PCs to project the spikes into')
    useRAM = Int(required=False, default=0, help='must be 0')

class KilosortUltraParameters(DefaultSchema):

    trange = String(required=False, default='[0 Inf]', help='Time range in seconds to process')
    fproc = String(required=False, default="fullfile('C:/data/kilosort', 'temp_wh.dat')", help='Processed data file on a fast ssd')
  
    chanMap = String(required=False, default="'chanMap.mat'", help='path to channel map .mat file')
    fshigh = Int(required=False, default=300, help='frequency for high pass filtering')
    minfr_goodchannels = Float(required=False, default=0.1, help='minimum firing rate on a "good" channel (0 to skip)')
    Th = String(required=False, default='[9 9]', help='threshold (last pass can be lower')
    lam = Int(required=False, default=10, help='how important is the amplitude penalty (like in Kilosort1, 0 means not used, 10 is average, 50 is a lot)')
    AUCsplit = Float(required=False, default=0.8, help='splitting a cluster at the end requires at least this much isolation for each sub-cluster (max = 1)')
    minFR = Float(required=False, default=1/50., help='minimum spike rate (Hz)')
    momentum = String(required=False, default='[20 400]', help='number of samples to average over (annealed)')
    sigmaMask = Int(required=False, default=30, help='spatial constant in um for computing residual variance of spike')
    ThPre = Int(required=False, default=8, help='threshold crossings for pre-clustering (in PCA projection space)')
    sig = Int(required=False, default=20)
    nblocks = Int(required=False, default=5)

    spkTh = Int(required=False, default=-6, help='spike threshold is standard deviations')
    reorder = Int(required=False, default=1, help='whether to reorder batches for drift correction')
    nskip = Int(required=False, default=25, help='how many batches to skip for determining spike PCs')
    GPU = Int(required=False, default=1, help='whether to run this code on an Nvidia GPU')
    nfilt_factor = Int(required=False, default=4, help='max number of clusters per good channel (even temporary ones)')
    ntbuff = Int(required=False, default=64, help='samples of symmetrical buffer for whitening and spike detection')
    NT = String(required=False, default='64*1024 + ops.ntbuff', help='this is the batch size; for GPU should be a multiple of 32 + ntbuff)')
    whiteningRange = Int(required=False, default=32)
    nSkipCov = Int(required=False, default=25, help='compute whitening matrix from every Nth batch')
    scaleproc = Int(required=False, default=200, help='int16 scaling of whitenend data')
    nPCs = Int(required=False, default=3, help='how many PCs to project the spikes into')
    useRAM = Int(required=False, default=0, help='must be 0')

    nNeighbors = Int(required=False, default=96)


class KilosortHelperParameters(DefaultSchema):

    kilosort_version = Int(required=True, default=2, help='Kilosort version to use (1 or 2)')

    surface_channel_buffer = Int(required=False, default=15, help='Number of channels above brain surface to include in spike sorting')

    matlab_home_directory = InputDir(help='Location from which Matlab files can be copied and run.')
    kilosort_repository = InputDir(help='Local directory for the Kilosort source code repository.')
    
    kilosort_params = Nested(KilosortParameters, required=False, help='Parameters used to auto-generate a Kilosort config file')
    kilosort2_params = Nested(Kilosort2Parameters, required=False, help='Parameters used to auto-generate a Kilosort2 config file')
    kilosort3_params = Nested(Kilosort3Parameters, required=False, help='Parameters used to auto-generate a Kilosort3 config file')
    kilosortUltra_params = Nested(KilosortUltraParameters, required=False, help='Parameters used to auto-generate a KilosortUltra config file')

class InputParameters(ArgSchema):
    
    kilosort_helper_params = Nested(KilosortHelperParameters)

    directories = Nested(Directories)
    ephys_params = Nested(EphysParams)
    common_files = Nested(CommonFiles)
    

class OutputSchema(DefaultSchema): 
    input_parameters = Nested(InputParameters, 
                              description=("Input parameters the module " 
                                           "was run with"), 
                              required=True) 
 
class OutputParameters(OutputSchema): 

    execution_time = Float()
    kilosort_commit_hash = String()
    kilosort_commit_date = String()
    mask_channels = NumpyArray()
    