import sys
sys.path.append('./gnomad_qc')
sys.path.append('./gnomad-mitochondria')
import hail as hl
from gnomad_mitochondria.utils.annotations import apply_indel_stack_filter 
hl.init()
mt = hl.import_vcf('data/gnomad.genomes.v3.1.sites.chrM.clean.vcf')
mt_annotated = apply_indel_stack_filter(mt)
hl.export_vcf(mt_annotated, "data/text_annotated.vcf")

"""
* error
Traceback (most recent call last):
  File "/workspaces/gnomad_anno/gnomad_mt_anno_test.py", line 8, in <module>
    mt_annotated = apply_indel_stack_filter(mt)
  File "/workspaces/gnomad_anno/./gnomad-mitochondria/gnomad_mitochondria/utils/annotations.py", line 786, in apply_indel_stack_filter
    indel_expr = get_indel_expr(input_mt)
  File "/workspaces/gnomad_anno/./gnomad-mitochondria/gnomad_mitochondria/utils/annotations.py", line 767, in get_indel_expr
    & (input_mt.HL <= 0.95)
  File "/usr/local/python/3.10.13/lib/python3.10/site-packages/hail/table.py", line 171, in __getattr__
    raise AttributeError(get_nice_attr_error(self, item))
AttributeError: MatrixTable instance has no field, method, or property 'HL'
    Hint: use 'describe()' to show the names of all data fields.

* bloop msg
The error message indicates that the MatrixTable object mt does not have a field named HL, which is expected by the 
get_indel_expr
 function within the 
apply_indel_stack_filter
 function.
The HL field is likely expected to contain heteroplasmy levels for each variant in the dataset. If your VCF does not have this field, you will need to ensure that it is computed or exists before calling apply_indel_stack_filter.
"""