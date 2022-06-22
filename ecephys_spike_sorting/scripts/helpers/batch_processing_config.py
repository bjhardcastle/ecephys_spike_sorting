
from collections import namedtuple, OrderedDict

config = {
    'processable_probes': ['A', 'B', 'C'], #'D', 'E', 'F' #'A', 'C', 'D', 'E'
	'probe_type': 'PXI',
	'WSE_computer': 'w10dtsm18306',
    'probe_params': namedtuple('probe_params',['probe_letter', 'pxi_slot', 'num_in_slot', 'session','start_module','end_module','backup1','backup2']),
    'slot_params': namedtuple('slot_params',['slot_num', 'recording_dir', 'extracted_drive','backup1','backup2']),
    'lims_upload_drive': r'\\W10DT05501\E',
    'processing_drive': r'\\W10DT05501\D',
    'disk_backup': r'\\W10DT05501\J',
    'network_backup': r'\\allen\programs\mindscope\workgroups\np-exp', #r'\\10.128.54.20\sd8.3', # r'\\10.128.54.19\sd9',
    'start_module': 'final_copy_parallel', # 'extract_from_npx',
    'end_module': 'cleanup', 
    'json_directory': r'C:\Users\svc_neuropix\Documents\json_files',
    'ctx_surface_min': 80,
    'ctx_surface_max': 240,
    'slot_config':{
    	2:{
    		'acq_drive': r'\\W10DT05501\A',
    		'suffix': 'probeABC', # ignored if 'opephys_v0_6_0': True
    	},
    	3:{
    		'acq_drive': r'\\W10DT05501\B',
    		'suffix': 'probeDEF', # ignored if 'opephys_v0_6_0': True
    	},
    },
    'skip_verify_backup': True,
    'probe_config':{
    	'A':{
    		'pxi_slot': '2',
    		'num_in_slot': '1',
    	},
    	'B':{
    		'pxi_slot': '2',
    		'num_in_slot': '2',
    	},
    	'C':{
    		'pxi_slot': '2',
    		'num_in_slot': '3',
    	},
    	'D':{
    		'pxi_slot': '3',
    		'num_in_slot': '1',
    	},
    	'E':{
    		'pxi_slot': '3',
    		'num_in_slot': '2',
    	},
    	'F':{
    		'pxi_slot': '3',
    		'num_in_slot': '3',
    	},
    },
}

def get_from_config(field, default=None):
	if field in config:
		return config[field]
	else:
		return default

def get_from_kwargs(field, kwargs, default=None):
	if field in kwargs:
		return kwargs[field]
	else:
		return get_from_config(field, default)