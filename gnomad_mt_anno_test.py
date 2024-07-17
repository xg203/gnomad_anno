import sys
sys.path.append('./gnomad_qc')
sys.path.append('./gnomad_mitochondria')
import hail as hl
from gnomad_mitochondria.utils.annotations import apply_indel_stack_filter 
hl.init()
