#!/usr/bin/env python3
from __future__ import annotations

import ast
import json
from pathlib import Path

PASS = 'PASS_EXP073IK_C2_SOURCE_BASIS_OBSERVABLE_ORDER_INVENTORY_V0_1'
EXPECTED_SELECTION = 'zbin_mcal == t AND dec >= -90 AND dec <= -35 AND flags_select == 0'
EXPECTED_MAPPER = {'nside':4096,'ordering':'RING','coords':'C','lonlat':True}
EXPECTED_SOURCE = {
    0:{'selected':7_705_486,'bytes':30_821_944,'record_sha':'5b507215ca961c09b82786e61e681a0178c29e9b593c17b588e366722a021f15','unique':4_305_774,'occupancy_sha':'b6ed74f31540d4041267f94e2f7cdb70b7040d943ba22a4aa7eab62418f8cb32'},
    1:{'selected':7_851_711,'bytes':31_406_844,'record_sha':'752f585125e413c7bd40cc5174cf7ef98e95f970022a351c5d91206f371d2241','unique':4_339_193,'occupancy_sha':'fed1ffdf2ef7a7ae88e42615bd08e207e039239c44fa20b7994258f147a739f1'},
    2:{'selected':8_238_547,'bytes':32_954_188,'record_sha':'259295a1f5a23ad9e5c6b46842bcf612b0eb13dc701ab6d54eb15f0d7bb0105f','unique':4_401_919,'occupancy_sha':'9e2bfb92289ca4a3abb11efabf7ac8d59bb7c68eb63a7104c2b247267733b24d'},
    3:{'selected':4_196_641,'bytes':16_786_564,'record_sha':'3996f2bacf29d46278773530058d4f5666c0d590bf6cebc06459659166bc60ec','unique':2_943_132,'occupancy_sha':'21e3776111de305c108463b02b0e3fd5e138cc97817d37e7b05330132d058094'},
}
EXPECTED_PAIRS = ['S0_S0','S0_S1','S0_S2','S0_S3','S1_S1','S1_S2','S1_S3','S2_S2','S2_S3','S3_S3']
EXPECTED_14 = ['Wm_S0','Wm_S1','Wm_S2','Wm_S3','WW_S0_S0','WW_S0_S1','WW_S0_S2','WW_S0_S3','WW_S1_S1','WW_S1_S2','WW_S1_S3','WW_S2_S2','WW_S2_S3','WW_S3_S3']


def literal_assign(path: Path, name: str):
    tree = ast.parse(path.read_text(encoding='utf-8'), filename=str(path))
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == name:
                    return ast.literal_eval(node.value)
    raise AssertionError(f'missing literal assignment {name} in {path}')


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    prereg = root/'docs/dsir4/prereg/EXP073IK_C2_SOURCE_BASIS_OBSERVABLE_ORDER_INVENTORY_V0_1.md'
    invp = root/'docs/dsir4/contracts/EXP073IK_SOURCE_BASIS_OBSERVABLE_ORDER_INVENTORY_V0_1.json'
    r1p = root/'ci/exp073r1_sequential_wholestream_v0_5.py'
    aap = root/'ci/exp073aa_article3_des_angular_task_runner_v0_1.py'
    angp = root/'docs/dsir4/authority/C2_WW_ANGULAR_AUTHORITY_ADMITTED_V0_1.json'
    for p in (prereg, invp, r1p, aap, angp):
        assert p.is_file(), p

    inv = json.loads(invp.read_text(encoding='utf-8'))
    ang = json.loads(angp.read_text(encoding='utf-8'))

    # Independent source-basis recovery from frozen implementation sources.
    assert literal_assign(r1p, 'SELECTION') == EXPECTED_SELECTION
    assert literal_assign(r1p, 'MAPPER') == EXPECTED_MAPPER
    assert literal_assign(aap, 'SOURCE') == EXPECTED_SOURCE
    assert literal_assign(aap, 'ALL_TASKS') == EXPECTED_14
    assert literal_assign(aap, 'NSIDE') == 4096
    assert literal_assign(aap, 'LMAX_PLUS_ONE') == 12288

    basis = inv['source_basis']
    assert [x['name'] for x in basis] == ['S0','S1','S2','S3']
    assert [x['zbin_mcal'] for x in basis] == [0,1,2,3]
    for b, x in enumerate(basis):
        e = EXPECTED_SOURCE[b]
        assert x == {
            'name':f'S{b}','zbin_mcal':b,'selected':e['selected'],
            'record_bytes':e['bytes'],'record_sha256':e['record_sha'],
            'unique_pixels':e['unique'],'occupancy_sha256':e['occupancy_sha']
        }
    assert inv['r1_source_authority']['selection'] == EXPECTED_SELECTION
    assert inv['r1_source_authority']['mapper'] == EXPECTED_MAPPER
    assert inv['r1_source_authority']['run'] == 33270843577
    assert inv['r1_source_authority']['job'] == 99148916507
    assert inv['r1_source_authority']['artifact_id'] == 9720335366
    assert inv['r1_source_authority']['artifact_digest'] == 'sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd'

    # Independent order recovery: current C2 WW inventory versus historical full angular manifest.
    assert ang['bound_pair_count'] == 10
    assert ang['bound_pairs'] == EXPECTED_PAIRS
    assert inv['c2_required_ww_pair_order'] == EXPECTED_PAIRS
    assert inv['historical_14_angular_task_order'] == EXPECTED_14
    assert ang['common'] == {
        'semantics':'EE<-EE','dtype':'<f8','shape':[39,12288],
        'des_nside':4096,'ell_min':0,'ell_max':12287,'bands':39,
        'mcm_bytes':19327352832,'exact_equality_only':True
    }
    aa = aap.read_text(encoding='utf-8')
    assert "selected_semantics={'output':'TE','input':'TE','full_component_order':['TE','TB']}" in aa
    assert "selected_semantics={'output':'EE','input':'EE','full_component_order':['EE','EB','BE','BB']}" in aa
    assert "selected=np.ascontiguousarray(wins[0,:,0,:],dtype='<f8')" in aa
    assert inv['angular_semantics'] == {
        'nside':4096,'ell_min':0,'ell_max':12287,'bands':39,'dtype':'<f8',
        'shape':[39,12288],'Wm':'TE<-TE','WW':'EE<-EE','exact_equality_only':True
    }

    # Parent gate and fail-closed downstream boundary.
    assert ang['admission']['experiment'] == 'Exp073IJ'
    assert ang['admission']['version'] == 'v0.2'
    assert ang['admission']['run'] == 34255057685
    assert ang['admission']['job'] == 102158621226
    assert ang['admission']['token'] == 'PASS_EXP073IJ_C2_G_ANGULAR_AUTHORITY_V0_2'
    assert ang['admission']['classification'] == 'SCIENTIFIC_GATE_PASS'
    assert ang['status']['G_DOMAIN_MAPPING'] == 'PASS'
    assert ang['status']['G_ANGULAR_AUTHORITY'] == 'PASS'
    assert ang['status']['G_ORDERED_JOIN'] == 'NOT_YET_TESTABLE'
    assert ang['status']['scientific_model_authority_created'] is False

    fw = inv['interpretation_firewall']
    assert fw == {
        'historical_14_manifest_implies_future_c2_join_membership':False,
        'join_equation_defined':False,'scientific_values_read':False,
        'radial_kernel_read':False,'physical_support_evaluated':False,
        'covariance_read':False,'whitening_performed':False,
        'nuisance_geometry_read':False,'relation_null_read':False,
        'scientific_model_authority_created':False
    }
    assert inv['status']['G_DOMAIN_MAPPING'] == 'PASS'
    assert inv['status']['G_ANGULAR_AUTHORITY'] == 'PASS'
    for key in ('G_ORDERED_JOIN','G_RADIAL_SUPPORT','G_PHYSICAL_SUPPORT','G_COV_WHITENING','G_NUISANCE_QUOTIENT','G_RELATION_NULL','G_FINAL_MODEL','overall_status'):
        assert inv['status'][key] == 'NOT_YET_TESTABLE'

    prereg_text = prereg.read_text(encoding='utf-8')
    assert 'must not infer from its existence that the future C2 `G_ORDERED_JOIN` must consume all 14 entries' in prereg_text
    assert 'No redshift-edge values may be invented' in prereg_text

    print(PASS)
    print('classification=SUPPORT_PLUS_0_PLUS_0')
    print('source_basis_inventory_verified=true')
    print('observable_order_inventory_verified=true')
    print('prospective_ordered_join_contract_may_be_defined=true')
    print('G_DOMAIN_MAPPING=PASS')
    print('G_ANGULAR_AUTHORITY=PASS')
    print('G_ORDERED_JOIN=NOT_YET_TESTABLE')
    print('scientific_model_authority_created=false')
    print('overall_status=NOT_YET_TESTABLE')


if __name__ == '__main__':
    main()
