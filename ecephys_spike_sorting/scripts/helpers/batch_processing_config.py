from collections import namedtuple, OrderedDict

config = {
    'processable_probes': ['D','E','F'],#, 'B', 'C', 'D', 'E'],# 'B', 'C', 'D', 'E', 'F'],#'B','C'],
	'probe_type': 'PXI', #Use PXI here for 1.0 probes, 'Ultra' for ultra probes
    'acq_system': 'PXI',
	'WSE_computer': 'W10DTSM18306',
    'probe_params': namedtuple('probe_params',['probe_letter', 'pxi_slot', 'num_in_slot', 'session','start_module','end_module','backup1','backup2']),
    'slot_params': namedtuple('slot_params',['slot_num', 'recording_dir', 'extracted_drive','backup1','backup2']),
    'lims_upload_drive': r'\\W10DT05501\E', #r'C:\data\temp', 
    'processing_drive': r'D:',#r'C:\data\extraction',#r'\\10.128.54.20\sd8.3\1128517077_565581_20210915', #r'C:\data\extraction',
    'disk_backup': r'\\W10DT9I8QD3D\extraction',#r'D:',
    'network_backup': r'\\allen\programs\mindscope\workgroups\np-exp', #r"C:\Users\svc_neuropix\Desktop\1128517077_565581_20210915_quality_metrics", #r\\10.128.54.19\sd9,
    'start_module': 'extract_from_npx',
    'end_module': 'final_copy_parallel', #'cleanup',
    'json_directory': r'C:\Users\svc_neuropix\Documents\json_files',
    'ctx_surface_min': 80,
    'ctx_surface_max': 240,
    'slot_config':{
    	2:{
    		'acq_drive': r'\\W10DT05501\A',
    		'suffix': 'probeABC',
    	},
    	3:{
    		'acq_drive': r'\\W10DT05501\B',
    		'suffix': 'probeDEF',
    	},
        # 2:{
        #     'acq_drive': r'C:\data',
        #     'suffix': 'probeABC',
        # },
        # 3:{
        #     'acq_drive': r'C:\data',
        #     'suffix': 'probeDEF',
        # },
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