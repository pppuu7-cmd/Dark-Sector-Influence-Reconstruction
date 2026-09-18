#!/usr/bin/env python3
"""DSIR DES M076 remaining-sentinel response replication.

Read-only consumer of frozen run 35280281867. No CLASS, covariance, nuisance or full107.
All 256 selected source-array bindings pass before response arithmetic.
"""
from __future__ import annotations
import argparse, ast, hashlib, io, itertools, json, os, urllib.error, urllib.parse, urllib.request, zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PREREG=ROOT/"prereg/LAYERB_BETA_V0_26_R1_DES_M076_REMAINING_SENTINEL_RESPONSE_REPLICATION_V0_1.md"
DESIGN=ROOT/"docs/dsir4/authority/LAYERB_BETA_V0_26_R1_DES_M076_REMAINING_SENTINEL_RESPONSE_REPLICATION_DESIGN_AUTHORITY_V0_1.json"
DESIGN_CRITIC=ROOT/"docs/dsir4/authority/LAYERB_BETA_V0_26_R1_DES_M076_REMAINING_SENTINEL_RESPONSE_REPLICATION_DESIGN_STATIC_CRITIC_V0_1.json"
AUTHORING_AUTHORITY=ROOT/"docs/dsir4/authority/LAYERB_BETA_V0_26_R1_DES_M076_REMAINING_SENTINEL_RESPONSE_REPLICATION_IMPLEMENTATION_AUTHORING_AUTHORITY_V0_1.json"
NUMERICAL_RUNTIME_CRITIC=ROOT/"docs/dsir4/authority/LAYERB_BETA_V0_26_R1_RESPONSE_BLIND_MINIMAL_NUMERICAL_REPRODUCIBILITY_RUNTIME_CRITIC_V0_1.json"
IMPLEMENTATION_CRITIC=ROOT/"docs/dsir4/authority/LAYERB_BETA_V0_26_R1_DES_M076_REMAINING_SENTINEL_RESPONSE_REPLICATION_IMPLEMENTATION_STATIC_CRITIC_V0_1.json"
EXECUTION_AUTHORITY=ROOT/"docs/dsir4/authority/LAYERB_BETA_V0_26_R1_DES_M076_REMAINING_SENTINEL_RESPONSE_REPLICATION_EXECUTION_AUTHORITY_V0_1.json"
WORKFLOW=ROOT/".github/workflows/dsir-v026-r1-des-m076-remaining-sentinel-response-replication-v0-1.yml"
LAUNCH_MARKER=ROOT/"docs/dsir4/launch/LAYERB_BETA_V0_26_R1_DES_M076_REMAINING_SENTINEL_RESPONSE_REPLICATION_V0_1.launch.json"

PREREG_BLOB="8817448b4794446a81dad3014e900c6ddf43b884"
DESIGN_BLOB="86046021a9463d6287d1d6854149097a9c769d47"
DESIGN_CRITIC_BLOB="d1598a8c8cdc00da5942af79612d319f472f3859"
AUTHORING_AUTHORITY_BLOB="60980d26c609cf3a6591514f1216ef47407d30b2"
NUMERICAL_RUNTIME_CRITIC_BLOB="9f19f8cc643bc978d0dbbcdd58f80fdf04395e24"

SOURCE_RUN_ID=35280281867
H=1e-4; TECH_TOL=1e-5; SCI_TOL=1e-3
CALLS=[76,78]
LENS={76:127,78:128}
ZS={76:"3fdf851eb851eb85",78:"3fdfafb7e90ff972"}
TARGET_SHA={76:"661250b46dfc123a84fb8bfe908893780d419ebf5ba8ee51b83e24e826e26198",78:"1969c1c6e83087e5408b19fb948d52ce9f91caf163969a66d7bd6647323aa57c"}
UNION_SHA="bc86d3e98ff1e7d79bb8b3057e2a810b9dbaffd82f8c552cf781ffa52fd07df3"
REPLICATES=[f"R{i:02d}" for i in range(1,33)]
ACTIVE="NATIVE_AVX512_ACTIVE"; INACTIVE="NATIVE_AVX512_INACTIVE"
ALLOWED={ACTIVE,INACTIVE}
PASS="PASS_SCOPED_DES_M076_REMAINING_SENTINEL_RESPONSE_REPLICATION"
TAXONOMY={PASS,"SCIENTIFIC_RESPONSE_ZERO_OR_NONFINITE","SCIENTIFIC_RESPONSE_REPRODUCIBILITY_FAIL","SCIENTIFIC_RESPONSE_CONSTRUCTION_MISMATCH","PROVENANCE_FAIL","INVALID_IMPLEMENTATION"}
LANE_ARTIFACTS={
  "R01": {
    "artifact_id": 10523240392,
    "name": "layerb-beta-v026-r1-minimal-numerical-R01-v0-1",
    "sha256": "ee95f22766aad94ecbea4b246b0b52918af3b271174a7021541948e41989ad19"
  },
  "R02": {
    "artifact_id": 10524117130,
    "name": "layerb-beta-v026-r1-minimal-numerical-R02-v0-1",
    "sha256": "5de470b8339f8f82dbf8d04bef727ba12ee15b01b12ef45b86dcc7680b14946a"
  },
  "R03": {
    "artifact_id": 10523105313,
    "name": "layerb-beta-v026-r1-minimal-numerical-R03-v0-1",
    "sha256": "05910abbb7ace4e45354be79502a4b4d7a721a4c4855132e62622edbba72a032"
  },
  "R04": {
    "artifact_id": 10523143744,
    "name": "layerb-beta-v026-r1-minimal-numerical-R04-v0-1",
    "sha256": "af04d485963f95db476eac902a974680bf58052cec391060b300e8eb3360d44e"
  },
  "R05": {
    "artifact_id": 10523060327,
    "name": "layerb-beta-v026-r1-minimal-numerical-R05-v0-1",
    "sha256": "017f2f91ae7a06e1cde8c7522a9cb768ff107df775b57988fb68de7a5717fcd6"
  },
  "R06": {
    "artifact_id": 10522119938,
    "name": "layerb-beta-v026-r1-minimal-numerical-R06-v0-1",
    "sha256": "2bcd0b1ed6c4b3da2ae0001ffc39a3591aed1dc1a376da024f5a6ed72ef80eb8"
  },
  "R07": {
    "artifact_id": 10521889308,
    "name": "layerb-beta-v026-r1-minimal-numerical-R07-v0-1",
    "sha256": "7de18e6a3e38da9e6afa6a3ae31f8b4fa5785a4a2774c00f3706b176b9f29841"
  },
  "R08": {
    "artifact_id": 10523686811,
    "name": "layerb-beta-v026-r1-minimal-numerical-R08-v0-1",
    "sha256": "0b4e3e42a2adfa174c0b766c28a14d9fb0e348abcd05cd13b1133cb95bffb244"
  },
  "R09": {
    "artifact_id": 10523533058,
    "name": "layerb-beta-v026-r1-minimal-numerical-R09-v0-1",
    "sha256": "9e4848945074b47b1e6f2bd1da2b51839a160247ac0b66ea6dc19e6fbe9e0f46"
  },
  "R10": {
    "artifact_id": 10523571519,
    "name": "layerb-beta-v026-r1-minimal-numerical-R10-v0-1",
    "sha256": "c238391b558d89ff82f69c3d2d705142c8bf4c66c7f7b31be5c9cafa9c17abc6"
  },
  "R11": {
    "artifact_id": 10523455046,
    "name": "layerb-beta-v026-r1-minimal-numerical-R11-v0-1",
    "sha256": "d24db04361f00c9ae2f34c36afe5482e982a33c6dcfea78415d8f93d40f0981f"
  },
  "R12": {
    "artifact_id": 10523452556,
    "name": "layerb-beta-v026-r1-minimal-numerical-R12-v0-1",
    "sha256": "d05aaef8e5b643caf340a3d7b7cdc12be71d8b743f84a5fce2e97b8922231a00"
  },
  "R13": {
    "artifact_id": 10523680602,
    "name": "layerb-beta-v026-r1-minimal-numerical-R13-v0-1",
    "sha256": "05fbcdbd9557403e0df611e578e0d5982dec26bca49cd41dd240afad688549d4"
  },
  "R14": {
    "artifact_id": 10523692853,
    "name": "layerb-beta-v026-r1-minimal-numerical-R14-v0-1",
    "sha256": "7b410a3fd4bb8fcd56d0ea22c26dc60387a8444d5387e37ff7b0562fd4180efe"
  },
  "R15": {
    "artifact_id": 10523455059,
    "name": "layerb-beta-v026-r1-minimal-numerical-R15-v0-1",
    "sha256": "03d7e73a5dde118e22effb15b718119a11cbceda9a55dee34a3ee927f9cd5d7b"
  },
  "R16": {
    "artifact_id": 10521988921,
    "name": "layerb-beta-v026-r1-minimal-numerical-R16-v0-1",
    "sha256": "ae640737ac5f0f1f252c08f1a0d5f98bc12d55ad1026b52e224100b4a9cd8b49"
  },
  "R17": {
    "artifact_id": 10523415017,
    "name": "layerb-beta-v026-r1-minimal-numerical-R17-v0-1",
    "sha256": "c6eaa3c2eb3d31b709fcc8fbd583e643c36164c45dc5fdf353095e3c63834473"
  },
  "R18": {
    "artifact_id": 10523295503,
    "name": "layerb-beta-v026-r1-minimal-numerical-R18-v0-1",
    "sha256": "ce9482417ac01b23c50069d67072c54cfa6bac7cbdb91677760ea92087b6c3bc"
  },
  "R19": {
    "artifact_id": 10522783710,
    "name": "layerb-beta-v026-r1-minimal-numerical-R19-v0-1",
    "sha256": "5f367d29309fd137bf47431b891547a798680d4efb19d5143eb23a5f8f1e2286"
  },
  "R20": {
    "artifact_id": 10523767086,
    "name": "layerb-beta-v026-r1-minimal-numerical-R20-v0-1",
    "sha256": "e2d66412d8d1e014ed991752743256a2fc04c17f1711683c23fc174cfaa53811"
  },
  "R21": {
    "artifact_id": 10522839934,
    "name": "layerb-beta-v026-r1-minimal-numerical-R21-v0-1",
    "sha256": "21723f39486d483018a137475846c5e70f93d06b32334adacab54218aa56b79e"
  },
  "R22": {
    "artifact_id": 10523352424,
    "name": "layerb-beta-v026-r1-minimal-numerical-R22-v0-1",
    "sha256": "0951c25939d49b149956be4d5f2f728e237887d7b72fc711b2d486bcb3481403"
  },
  "R23": {
    "artifact_id": 10524042336,
    "name": "layerb-beta-v026-r1-minimal-numerical-R23-v0-1",
    "sha256": "4a3ff182f934bef832763856b7beab67c9f942c282f69d57dd6a7e9015798d7e"
  },
  "R24": {
    "artifact_id": 10522633290,
    "name": "layerb-beta-v026-r1-minimal-numerical-R24-v0-1",
    "sha256": "27b5b5ea9ad6fa9835551aa7bee52dc824197e5a6641e44a64c927504ff6b930"
  },
  "R25": {
    "artifact_id": 10523550658,
    "name": "layerb-beta-v026-r1-minimal-numerical-R25-v0-1",
    "sha256": "b4f97670abf70aefa18553443a9896b2bffaa65659c7cdf6d64bfebb0d61b324"
  },
  "R26": {
    "artifact_id": 10522813881,
    "name": "layerb-beta-v026-r1-minimal-numerical-R26-v0-1",
    "sha256": "e41cb15f93d6fb44b032d0f2205a53527786fa87594ad8f5a5019920dadbac7a"
  },
  "R27": {
    "artifact_id": 10523740117,
    "name": "layerb-beta-v026-r1-minimal-numerical-R27-v0-1",
    "sha256": "308f23f03e7ebfbc622f6307d4c174a08b720a3f4f84dabf1681e3ba706f13a6"
  },
  "R28": {
    "artifact_id": 10522698898,
    "name": "layerb-beta-v026-r1-minimal-numerical-R28-v0-1",
    "sha256": "d8d35ce3f263ce2bbd265f477e3d544492f7f03f5552992b28eac8a4c62ec80d"
  },
  "R29": {
    "artifact_id": 10523132184,
    "name": "layerb-beta-v026-r1-minimal-numerical-R29-v0-1",
    "sha256": "89035658a7d751b74d21660f5d333c8db9679506118c64ac4106ae09fb42b872"
  },
  "R30": {
    "artifact_id": 10523112892,
    "name": "layerb-beta-v026-r1-minimal-numerical-R30-v0-1",
    "sha256": "474dacd17ad1f4dd7a0e35a76377b271ba3118252a7c7b7fba4d8c2fede17fb8"
  },
  "R31": {
    "artifact_id": 10522938361,
    "name": "layerb-beta-v026-r1-minimal-numerical-R31-v0-1",
    "sha256": "69d4deed0c6201e08022ec1a85e29c87480c03040bb07c993df21c803edad6c8"
  },
  "R32": {
    "artifact_id": 10523743733,
    "name": "layerb-beta-v026-r1-minimal-numerical-R32-v0-1",
    "sha256": "964acae9ceea1c5b53c9d1d5346e63c81dd3a1d6bb9046633b85cfac062fa887"
  }
}

class GateError(RuntimeError):
    def __init__(self,c,s,m): super().__init__(m); self.classification=c; self.stage=s
def fail(c,s,m):
    if c not in TAXONOMY: raise RuntimeError(c)
    raise GateError(c,s,m)
def sha(b): return hashlib.sha256(b).hexdigest()
def git_blob(b): return hashlib.sha1(f"blob {len(b)}\0".encode()+b).hexdigest()
def blob_of(p): return git_blob(Path(p).read_bytes())
def csha(o): return sha(json.dumps(o,sort_keys=True,separators=(",",":")).encode())
def normdig(x):
    s=str(x or ""); return s.split(":",1)[1] if s.startswith("sha256:") else s
def require_blob(p,e,label):
    if not Path(p).is_file(): fail("PROVENANCE_FAIL","authority_binding",f"missing {label}")
    a=blob_of(p)
    if a!=e: fail("PROVENANCE_FAIL","authority_binding",f"{label} blob {a} != {e}")

def expected_keys():
    o={}
    for call in CALLS:
        for kind in ("mixed_target","direct_target"):
            for role in ("beta_plus","beta_minus"):
                o[f"{kind}__M076__{role}__call{call:03d}"]=(kind,role,call)
    return o
EXPECTED=expected_keys()

def validate_static_chain():
    for p,e,l in [(PREREG,PREREG_BLOB,"prereg"),(DESIGN,DESIGN_BLOB,"design"),(DESIGN_CRITIC,DESIGN_CRITIC_BLOB,"design Critic"),(AUTHORING_AUTHORITY,AUTHORING_AUTHORITY_BLOB,"authoring authority"),(NUMERICAL_RUNTIME_CRITIC,NUMERICAL_RUNTIME_CRITIC_BLOB,"numerical Critic")]:
        require_blob(p,e,l)
    d=json.loads(DESIGN.read_text()); c=json.loads(DESIGN_CRITIC.read_text()); a=json.loads(AUTHORING_AUTHORITY.read_text()); n=json.loads(NUMERICAL_RUNTIME_CRITIC.read_text())
    if d.get("status")!="PROSPECTIVE_DESIGN_ONLY_SCOPED_AUTHORITY" or c.get("verdict")!="PASS_SCOPED": fail("PROVENANCE_FAIL","authority_binding","design chain mismatch")
    z=a.get("authorization",{})
    if z.get("implementation_authoring_authorized") is not True or z.get("implementation_execution_authorized") is not False or z.get("M076_response_read_authorized") is not False: fail("PROVENANCE_FAIL","authority_binding","authoring scope mismatch")
    if n.get("verdict")!="CONFIRMED_SCOPED" or n.get("reviewed_run",{}).get("run_id")!=SOURCE_RUN_ID: fail("PROVENANCE_FAIL","authority_binding","numerical parent mismatch")

def validate_execution_chain():
    validate_static_chain()
    for p,l in [(IMPLEMENTATION_CRITIC,"implementation Critic"),(EXECUTION_AUTHORITY,"execution authority"),(WORKFLOW,"workflow"),(LAUNCH_MARKER,"launch marker")]:
        if not p.is_file(): fail("PROVENANCE_FAIL","execution_binding",f"missing {l}")
    c=json.loads(IMPLEMENTATION_CRITIC.read_text()); a=json.loads(EXECUTION_AUTHORITY.read_text()); m=json.loads(LAUNCH_MARKER.read_text())
    if c.get("verdict")!="PASS_SCOPED": fail("PROVENANCE_FAIL","execution_binding","implementation Critic mismatch")
    if a.get("status")!="PROSPECTIVE_ONE_SHOT_EXECUTION_AUTHORITY" or a.get("authorized_run_count")!=1 or a.get("authorized_run_number")!=1 or a.get("authorized_run_attempt")!=1: fail("PROVENANCE_FAIL","execution_binding","execution authority mismatch")
    checks=[("preregistration_git_blob_sha1",PREREG_BLOB),("design_authority_git_blob_sha1",DESIGN_BLOB),("design_static_critic_git_blob_sha1",DESIGN_CRITIC_BLOB),("implementation_authoring_authority_git_blob_sha1",AUTHORING_AUTHORITY_BLOB),("numerical_runtime_critic_git_blob_sha1",NUMERICAL_RUNTIME_CRITIC_BLOB)]
    for k,v in checks:
        if a.get(k)!=v: fail("PROVENANCE_FAIL","execution_binding",f"{k} mismatch")
    if a.get("implementation_git_blob_sha1")!=blob_of(Path(__file__).resolve()) or a.get("workflow_git_blob_sha1")!=blob_of(WORKFLOW) or a.get("implementation_static_critic_git_blob_sha1")!=blob_of(IMPLEMENTATION_CRITIC): fail("PROVENANCE_FAIL","execution_binding","implementation identity mismatch")
    if a.get("terminal_taxonomy")!=sorted(TAXONOMY): fail("PROVENANCE_FAIL","execution_binding","taxonomy mismatch")
    if m.get("execution_authority_git_blob_sha1")!=blob_of(EXECUTION_AUTHORITY) or m.get("launch_once") is not True: fail("PROVENANCE_FAIL","execution_binding","marker mismatch")
    if os.environ.get("GITHUB_RUN_NUMBER") not in {None,"1"} or os.environ.get("GITHUB_RUN_ATTEMPT") not in {None,"1"}: fail("INVALID_IMPLEMENTATION","workflow_identity","not run1 attempt1")

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl): return None

def api_json(url,token):
    req=urllib.request.Request(url,headers={"Accept":"application/vnd.github+json","Authorization":f"Bearer {token}","X-GitHub-Api-Version":"2022-11-28","User-Agent":"dsir-m076-v0-1"})
    try:
        with urllib.request.urlopen(req,timeout=60) as r: return json.loads(r.read())
    except urllib.error.HTTPError as e:
        if e.code in {401,403}: fail("INVALID_IMPLEMENTATION","artifact_metadata_auth",f"HTTP {e.code}")
        fail("PROVENANCE_FAIL","artifact_metadata_transport",f"HTTP {e.code}")

def download_zip(api,repo,token,aid):
    url=f"{api}/repos/{repo}/actions/artifacts/{aid}/zip"; headers={"Accept":"application/vnd.github+json","Authorization":f"Bearer {token}","X-GitHub-Api-Version":"2022-11-28","User-Agent":"dsir-m076-v0-1"}
    op=urllib.request.build_opener(NoRedirect()); loc=None
    try: op.open(urllib.request.Request(url,headers=headers),timeout=60); fail("PROVENANCE_FAIL","artifact_transport","no redirect")
    except urllib.error.HTTPError as e:
        if e.code in {301,302,303,307,308}: loc=e.headers.get("Location")
        elif e.code in {401,403}: fail("INVALID_IMPLEMENTATION","artifact_archive_auth",f"HTTP {e.code}")
        else: fail("PROVENANCE_FAIL","artifact_archive_transport",f"HTTP {e.code}")
    if not loc: fail("PROVENANCE_FAIL","artifact_transport","missing redirect")
    req=urllib.request.Request(loc,headers={"Accept":"application/octet-stream","User-Agent":"dsir-m076-v0-1"})
    with urllib.request.urlopen(req,timeout=120) as r: return r.read()

def validate_meta(m,key,kind,role,call):
    if m.get("kind")!=kind or m.get("selection")!="M076" or m.get("role")!=role or m.get("call_index")!=call: fail("PROVENANCE_FAIL","selected_array_binding",f"{key} identity mismatch")
    if kind=="direct_target" and m.get("direct_batch")!="D50": fail("PROVENANCE_FAIL","selected_array_binding",f"{key} D50 mismatch")
    if m.get("z_u64hex")!=ZS[call] or m.get("target_u64hex_sha256")!=TARGET_SHA[call]: fail("PROVENANCE_FAIL","selected_array_binding",f"{key} target/z mismatch")
    if m.get("shape")!=[LENS[call]] or m.get("dtype")!="<f8" or m.get("byte_length")!=LENS[call]*8: fail("PROVENANCE_FAIL","selected_array_binding",f"{key} shape/dtype mismatch")

def stage_all():
    import numpy as np
    token=os.environ.get("GITHUB_TOKEN",""); repo=os.environ.get("GITHUB_REPOSITORY",""); api=os.environ.get("GITHUB_API_URL","https://api.github.com").rstrip("/")
    if not token or not repo: fail("PROVENANCE_FAIL","runtime_environment","missing GitHub environment")
    staged={}; prov=[]; classes={ACTIVE:0,INACTIVE:0}; arms={"A":0,"B":0}
    for rep in REPLICATES:
        spec=LANE_ARTIFACTS[rep]; meta=api_json(f"{api}/repos/{repo}/actions/artifacts/{spec['artifact_id']}",token)
        if int(meta.get("id",-1))!=spec["artifact_id"] or meta.get("name")!=spec["name"] or bool(meta.get("expired")) or normdig(meta.get("digest"))!=spec["sha256"]: fail("PROVENANCE_FAIL","artifact_metadata",f"{rep} artifact mismatch")
        zb=download_zip(api,repo,token,spec["artifact_id"])
        if sha(zb)!=spec["sha256"]: fail("PROVENANCE_FAIL","artifact_transport",f"{rep} ZIP hash mismatch")
        with zipfile.ZipFile(io.BytesIO(zb)) as z:
            rb=z.read(f"receipt_{rep}.json"); wb=z.read(f"witness_{rep}.npz")
        r=json.loads(rb)
        if r.get("replicate")!=rep or not r.get("eligible") or r.get("classification")!="LANE_PASS": fail("PROVENANCE_FAIL","lane_receipt",f"{rep} lane invalid")
        nc=r.get("native_class"); arm="A" if rep<="R16" else "B"
        if nc not in ALLOWED or r.get("order_arm")!=arm: fail("PROVENANCE_FAIL","lane_receipt",f"{rep} population mismatch")
        classes[nc]+=1; arms[arm]+=1
        sr=r["solver_receipt"]; man=sr["witness_manifest"]
        if sha(wb)!=r["witness_npz_sha256"] or sha(wb)!=sr["witness_npz_sha256"] or csha(man)!=sr["witness_manifest_canonical_sha256"]: fail("PROVENANCE_FAIL","witness_binding",f"{rep} witness mismatch")
        sel={k for k in man if k.startswith("mixed_target__M076__") or k.startswith("direct_target__M076__")}
        if sel!=set(EXPECTED): fail("PROVENANCE_FAIL","selected_array_binding",f"{rep} exact key set mismatch")
        lane={"native_class":nc,"order_arm":arm,"mixed":{},"direct":{}}
        with np.load(io.BytesIO(wb),allow_pickle=False) as npz:
            for key,(kind,role,call) in EXPECTED.items():
                m=man[key]; validate_meta(m,key,kind,role,call)
                a=np.ascontiguousarray(npz[key],dtype="<f8")
                if list(a.shape)!=[LENS[call]] or a.dtype.str!="<f8" or sha(a.tobytes())!=m["sha256"]: fail("PROVENANCE_FAIL","selected_array_binding",f"{rep} {key} payload mismatch")
                (lane["mixed"] if kind=="mixed_target" else lane["direct"])[(role,call)]=a.copy()
        staged[rep]=lane
        prov.append({"replicate":rep,"artifact_id":spec["artifact_id"],"outer_zip_sha256":spec["sha256"],"receipt_sha256":sha(rb),"witness_npz_sha256":sha(wb),"manifest_sha256":sr["witness_manifest_canonical_sha256"],"selected_array_count":8})
    if classes!={ACTIVE:10,INACTIVE:22} or arms!={"A":16,"B":16} or sum(x["selected_array_count"] for x in prov)!=256: fail("PROVENANCE_FAIL","population_binding","population/binding total mismatch")
    return staged,prov

def rel(a,b):
    import numpy as np
    den=np.maximum(np.maximum(np.abs(a),np.abs(b)),np.finfo(np.float64).tiny); return np.abs(a-b)/den
def maxrel(a,b):
    import numpy as np
    q=rel(a,b); idx=np.unravel_index(int(np.argmax(q)),q.shape); return float(q[idx]),tuple(map(int,idx))
def locate(idx):
    return (76,idx) if idx<127 else (78,idx-127)

def construct(staged):
    import numpy as np
    M=[]; D=[]
    for rep in REPLICATES:
        lm=[]; ld=[]
        for call in CALLS:
            q=staged[rep]
            lm.append(np.abs((q["mixed"][("beta_plus",call)]-q["mixed"][("beta_minus",call)])/(2*H)))
            ld.append(np.abs((q["direct"][("beta_plus",call)]-q["direct"][("beta_minus",call)])/(2*H)))
        M.append(np.concatenate(lm)); D.append(np.concatenate(ld))
    M=np.ascontiguousarray(np.stack(M),dtype="<f8"); D=np.ascontiguousarray(np.stack(D),dtype="<f8")
    if M.shape!=(32,255) or D.shape!=(32,255): fail("INVALID_IMPLEMENTATION","response_construction","shape mismatch")
    goodM=np.isfinite(M)&(M>0); goodD=np.isfinite(D)&(D>0); finite=bool(np.all(goodM)&np.all(goodD)); ce=None
    if not finite:
        for ri,rep in enumerate(REPLICATES):
            for ei in range(255):
                if not goodM[ri,ei] or not goodD[ri,ei]:
                    call,idx=locate(ei); cons="mixed" if not goodM[ri,ei] else "direct"; val=M[ri,ei] if cons=="mixed" else D[ri,ei]
                    ce={"failure_class":"SCIENTIFIC_RESPONSE_ZERO_OR_NONFINITE","replicate":rep,"construction":cons,"call":call,"source_entry_index":idx,"value":float(val)}; break
            if ce: break
    metrics={"mixed_cross_host_max_pairwise_rel":None,"direct_cross_host_max_pairwise_rel":None,"mixed_native_class_mean_rel_separation":None,"direct_native_class_mean_rel_separation":None,"mixed_direct_response_max_rel":None,"execution_order_arm_mean_rel_separation_descriptive_mixed":None,"execution_order_arm_mean_rel_separation_descriptive_direct":None}
    if not finite: cls="SCIENTIFIC_RESPONSE_ZERO_OR_NONFINITE"
    else:
        mm=(-1,None); dd=(-1,None)
        for i,j in itertools.combinations(range(32),2):
            q,idx=maxrel(M[i],M[j]); 
            if q>mm[0]: mm=(q,(i,j,idx))
            q,idx=maxrel(D[i],D[j]); 
            if q>dd[0]: dd=(q,(i,j,idx))
        ai=[i for i,r in enumerate(REPLICATES) if staged[r]["native_class"]==ACTIVE]; ii=[i for i,r in enumerate(REPLICATES) if staged[r]["native_class"]==INACTIVE]
        mn,_=maxrel(M[ai].mean(0),M[ii].mean(0)); dn,_=maxrel(D[ai].mean(0),D[ii].mean(0)); om,_=maxrel(M[:16].mean(0),M[16:].mean(0)); od,_=maxrel(D[:16].mean(0),D[16:].mean(0))
        mdarr=rel(M,D); md=float(mdarr.max())
        metrics.update({"mixed_cross_host_max_pairwise_rel":mm[0],"direct_cross_host_max_pairwise_rel":dd[0],"mixed_native_class_mean_rel_separation":mn,"direct_native_class_mean_rel_separation":dn,"mixed_direct_response_max_rel":md,"execution_order_arm_mean_rel_separation_descriptive_mixed":om,"execution_order_arm_mean_rel_separation_descriptive_direct":od})
        if not all(x<TECH_TOL for x in (mm[0],dd[0],mn,dn)):
            cls="SCIENTIFIC_RESPONSE_REPRODUCIBILITY_FAIL"
            # Freeze a deterministic smallest exact technical witness. Cross-host
            # failures are searched first in replicate-pair order, then atom
            # order, mixed before direct. If only native-class means fail,
            # freeze the first atom in call/source-entry order.
            for i,j in itertools.combinations(range(32),2):
                qm=rel(M[i],M[j]); qd=rel(D[i],D[j])
                for ei in range(255):
                    if qm[ei]>=TECH_TOL:
                        call,idx=locate(ei); ce={"failure_class":cls,"metric":"mixed_cross_host","replicate_a":REPLICATES[i],"replicate_b":REPLICATES[j],"call":call,"source_entry_index":idx,"relative_difference":float(qm[ei])}; break
                    if qd[ei]>=TECH_TOL:
                        call,idx=locate(ei); ce={"failure_class":cls,"metric":"direct_cross_host","replicate_a":REPLICATES[i],"replicate_b":REPLICATES[j],"call":call,"source_entry_index":idx,"relative_difference":float(qd[ei])}; break
                if ce: break
            if ce is None:
                qmn=rel(M[ai].mean(0),M[ii].mean(0)); qdn=rel(D[ai].mean(0),D[ii].mean(0))
                for ei in range(255):
                    if qmn[ei]>=TECH_TOL:
                        call,idx=locate(ei); ce={"failure_class":cls,"metric":"mixed_native_class_mean","native_class_a":ACTIVE,"native_class_b":INACTIVE,"call":call,"source_entry_index":idx,"relative_difference":float(qmn[ei])}; break
                    if qdn[ei]>=TECH_TOL:
                        call,idx=locate(ei); ce={"failure_class":cls,"metric":"direct_native_class_mean","native_class_a":ACTIVE,"native_class_b":INACTIVE,"call":call,"source_entry_index":idx,"relative_difference":float(qdn[ei])}; break
            if ce is None:
                fail("INVALID_IMPLEMENTATION","counterexample_capture","technical failure without exact witness")
        elif not md<SCI_TOL:
            cls="SCIENTIFIC_RESPONSE_CONSTRUCTION_MISMATCH"; ri,ei=map(int,np.argwhere(mdarr>=SCI_TOL)[0]); call,idx=locate(ei); ce={"failure_class":cls,"replicate":REPLICATES[ri],"call":call,"source_entry_index":idx,"mixed_value":float(M[ri,ei]),"direct_value":float(D[ri,ei]),"relative_difference":float(mdarr[ri,ei])}
        else: cls=PASS
    return {"schema":"LAYERB_BETA_V0_26_R1_DES_M076_REMAINING_SENTINEL_RESPONSE_DECISION_V0_1","classification":cls,"effect":"+0/+0","source_run_id":SOURCE_RUN_ID,"survey":"DES","mixed_selection":"M076","direct_batch":"D50","calls":CALLS,"response_shape_per_construction":[32,255],"atoms_per_construction":8160,"combined_atoms":16320,"h":H,"finite_positive_status":finite,"mixed_response_min":float(np.min(M)) if np.all(np.isfinite(M)) else None,"mixed_response_max":float(np.max(M)) if np.all(np.isfinite(M)) else None,"direct_response_min":float(np.min(D)) if np.all(np.isfinite(D)) else None,"direct_response_max":float(np.max(D)) if np.all(np.isfinite(D)) else None,"metrics":metrics,"smallest_exact_counterexample":ce,"provenance_complete_before_response_arithmetic":True,"new_CLASS_solves":0,"M076_response_read":True,"scientific_classifier_invoked":True,"covariance_read":False,"nuisance_read":False,"full107_execution":False,"statistical_inference_authorized":False,"physical_inference_authorized":False},M,D

def write_json(p,o): Path(p).write_text(json.dumps(o,indent=2,sort_keys=True)+"\n")
def static_contract(out):
    validate_static_chain(); s=Path(__file__).read_text(); t=ast.parse(s); mods=set()
    for n in ast.walk(t):
        if isinstance(n,ast.Import): mods.update(a.name for a in n.names)
        elif isinstance(n,ast.ImportFrom) and n.module: mods.add(n.module)
    checks={"no_classy":"classy" not in mods,"no_subprocess":"subprocess" not in mods,"calls_exact":CALLS==[76,78],"lens_exact":LENS=={76:127,78:128},"selected_arrays_256":len(EXPECTED)*32==256,"h_exact":H==1e-4,"tech_exact":TECH_TOL==1e-5,"science_exact":SCI_TOL==1e-3,"union_sha_exact":UNION_SHA=="bc86d3e98ff1e7d79bb8b3057e2a810b9dbaffd82f8c552cf781ffa52fd07df3"}
    if not all(checks.values()): fail("INVALID_IMPLEMENTATION","static_contract",str(checks))
    write_json(out,{"schema":"DES_M076_STATIC_CONTRACT_V0_1","classification":"PASS_STATIC_CONTRACT","checks":checks,"M076_response_read":False,"new_CLASS_solves":0}); return 0
def execute(outdir):
    import numpy as np
    outdir=Path(outdir); outdir.mkdir(parents=True,exist_ok=True); base={"schema":"LAYERB_BETA_V0_26_R1_DES_M076_REMAINING_SENTINEL_RESPONSE_DECISION_V0_1","classification":"INVALID_IMPLEMENTATION","effect":"+0/+0","M076_response_read":False,"scientific_classifier_invoked":False,"new_CLASS_solves":0,"provenance_complete_before_response_arithmetic":False}
    try:
        validate_execution_chain(); staged,prov=stage_all(); write_json(outdir/"provenance.json",{"schema":"DES_M076_PROVENANCE_V0_1","source_run_id":SOURCE_RUN_ID,"selected_array_bindings_verified":256,"all_bindings_passed_before_response_arithmetic":True,"records":prov}); r,M,D=construct(staged); np.savez_compressed(outdir/"response_evidence.npz",R_mixed=M,R_direct=D); r["provenance_json_sha256"]=sha((outdir/"provenance.json").read_bytes()); r["response_evidence_npz_sha256"]=sha((outdir/"response_evidence.npz").read_bytes()); write_json(outdir/"result.json",r); return 0
    except GateError as e: base.update({"classification":e.classification,"failure_stage":e.stage,"error":str(e)}); write_json(outdir/"result.json",base); return 0
    except Exception as e: base.update({"classification":"INVALID_IMPLEMENTATION","failure_stage":"unexpected","error":f"{type(e).__name__}: {e}"}); write_json(outdir/"result.json",base); return 0

def main():
    p=argparse.ArgumentParser(); p.add_argument("--mode",choices=["static-contract","execute"],required=True); p.add_argument("--out"); p.add_argument("--outdir"); a=p.parse_args()
    if a.mode=="static-contract": return static_contract(a.out)
    return execute(a.outdir)
if __name__=="__main__": raise SystemExit(main())
