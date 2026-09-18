#!/usr/bin/env python3
"""Independent runtime Critic for DSIR DES M076 response replication.

Two phases:
1) recompute: consume ONLY the 32 frozen numerical source artifacts, independently
   construct/classify M076, and persist independent result/evidence.
2) compare: consume the already-persisted independent evidence first, then read the
   producer artifact named by a post-terminal metadata-freeze authority and compare.

This file never imports the producer M076 implementation.
"""
from __future__ import annotations
import argparse, hashlib, io, itertools, json, os, urllib.error, urllib.request, zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PROTOCOL=ROOT/"docs/dsir4/authority/LAYERB_BETA_V0_26_R1_DES_M076_REMAINING_SENTINEL_RESPONSE_RUNTIME_CRITIC_PROTOCOL_V0_1.json"
AUTHORING=ROOT/"docs/dsir4/authority/LAYERB_BETA_V0_26_R1_DES_M076_RUNTIME_CRITIC_IMPLEMENTATION_AUTHORING_AUTHORITY_V0_1.json"
NUMERICAL_CRITIC=ROOT/"docs/dsir4/authority/LAYERB_BETA_V0_26_R1_RESPONSE_BLIND_MINIMAL_NUMERICAL_REPRODUCIBILITY_RUNTIME_CRITIC_V0_1.json"

PROTOCOL_BLOB="0946784a0300d495615b54658ad1a650a3f3bdc4"
AUTHORING_BLOB="791bb2f3b278ee794c6758ec0b817e26507437ab"
NUMERICAL_CRITIC_BLOB="9f19f8cc643bc978d0dbbcdd58f80fdf04395e24"

SOURCE_RUN_ID=35280281867
PRODUCER_RUN_ID=35405511563
PRODUCER_HEAD="7ca7092fddc3e1d263ed763bed2e7b53bd1672ab"
H=1e-4; TECH_TOL=1e-5; SCI_TOL=1e-3
CALLS=[76,78]
LENS={76:127,78:128}
ZS={76:"3fdf851eb851eb85",78:"3fdfafb7e90ff972"}
TARGET_SHA={76:"661250b46dfc123a84fb8bfe908893780d419ebf5ba8ee51b83e24e826e26198",78:"1969c1c6e83087e5408b19fb948d52ce9f91caf163969a66d7bd6647323aa57c"}
REPLICATES=[f"R{i:02d}" for i in range(1,33)]
ACTIVE="NATIVE_AVX512_ACTIVE"; INACTIVE="NATIVE_AVX512_INACTIVE"
SCIENCE_TAXONOMY={
 "PASS_SCOPED_DES_M076_REMAINING_SENTINEL_RESPONSE_REPLICATION",
 "SCIENTIFIC_RESPONSE_ZERO_OR_NONFINITE",
 "SCIENTIFIC_RESPONSE_REPRODUCIBILITY_FAIL",
 "SCIENTIFIC_RESPONSE_CONSTRUCTION_MISMATCH",
 "PROVENANCE_FAIL",
 "INVALID_IMPLEMENTATION",
}
CRITIC_TAXONOMY={
 "PASS_TERMINAL_CLOSURE",
 "CRITIC_PROVENANCE_FAIL",
 "CRITIC_INDEPENDENT_CLASSIFICATION_DISAGREEMENT",
 "CRITIC_METRIC_DISAGREEMENT",
 "CRITIC_RESPONSE_EVIDENCE_DISAGREEMENT",
 "CRITIC_INVALID_IMPLEMENTATION",
}
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

class CriticError(RuntimeError):
    def __init__(self,kind,stage,msg):
        super().__init__(msg); self.kind=kind; self.stage=stage

def sha(b): return hashlib.sha256(b).hexdigest()
def git_blob(b): return hashlib.sha1(f"blob {len(b)}\0".encode()+b).hexdigest()
def blob_of(p): return git_blob(Path(p).read_bytes())
def csha(o): return sha(json.dumps(o,sort_keys=True,separators=(",",":")).encode())
def normdig(x):
    s=str(x or ""); return s.split(":",1)[1] if s.startswith("sha256:") else s
def writej(p,o): Path(p).write_text(json.dumps(o,indent=2,sort_keys=True)+"\n",encoding="utf-8")
def require_blob(p,e,label):
    if not Path(p).is_file(): raise CriticError("CRITIC_PROVENANCE_FAIL","static_chain",f"missing {label}")
    a=blob_of(p)
    if a!=e: raise CriticError("CRITIC_PROVENANCE_FAIL","static_chain",f"{label} blob {a} != {e}")

def validate_static_chain():
    require_blob(PROTOCOL,PROTOCOL_BLOB,"Critic protocol")
    require_blob(AUTHORING,AUTHORING_BLOB,"Critic authoring authority")
    require_blob(NUMERICAL_CRITIC,NUMERICAL_CRITIC_BLOB,"numerical runtime Critic")
    p=json.loads(PROTOCOL.read_text()); a=json.loads(AUTHORING.read_text()); n=json.loads(NUMERICAL_CRITIC.read_text())
    if p.get("status")!="PROSPECTIVE_INDEPENDENT_RUNTIME_CRITIC_PROTOCOL": raise CriticError("CRITIC_PROVENANCE_FAIL","static_chain","protocol status")
    if p.get("scientific_payload_read") is not False or p.get("producer_classification_read") is not False: raise CriticError("CRITIC_PROVENANCE_FAIL","static_chain","protocol already consumed science")
    if a.get("status")!="PROSPECTIVE_RUNTIME_CRITIC_IMPLEMENTATION_AUTHORING_AUTHORITY": raise CriticError("CRITIC_PROVENANCE_FAIL","static_chain","authoring status")
    if a.get("authorized_scope",{}).get("execute_runtime_critic") is not False: raise CriticError("CRITIC_PROVENANCE_FAIL","static_chain","authoring unexpectedly executes")
    if n.get("verdict")!="CONFIRMED_SCOPED" or n.get("reviewed_run",{}).get("run_id")!=SOURCE_RUN_ID: raise CriticError("CRITIC_PROVENANCE_FAIL","static_chain","numerical parent mismatch")
    return p,a,n

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl): return None

def api_json(url,token):
    req=urllib.request.Request(url,headers={"Accept":"application/vnd.github+json","Authorization":f"Bearer {token}","X-GitHub-Api-Version":"2022-11-28","User-Agent":"dsir-m076-independent-critic-v0-1"})
    try:
        with urllib.request.urlopen(req,timeout=60) as r: return json.loads(r.read())
    except urllib.error.HTTPError as e:
        raise CriticError("CRITIC_PROVENANCE_FAIL","github_api",f"HTTP {e.code}")
    except urllib.error.URLError as e:
        raise CriticError("CRITIC_PROVENANCE_FAIL","github_api",str(e.reason))

def download_zip(api,repo,token,aid):
    url=f"{api}/repos/{repo}/actions/artifacts/{aid}/zip"
    h={"Accept":"application/vnd.github+json","Authorization":f"Bearer {token}","X-GitHub-Api-Version":"2022-11-28","User-Agent":"dsir-m076-independent-critic-v0-1"}
    op=urllib.request.build_opener(NoRedirect()); loc=None
    try:
        op.open(urllib.request.Request(url,headers=h),timeout=60)
        raise CriticError("CRITIC_PROVENANCE_FAIL","artifact_transport","archive endpoint did not redirect")
    except urllib.error.HTTPError as e:
        if e.code in {301,302,303,307,308}: loc=e.headers.get("Location")
        else: raise CriticError("CRITIC_PROVENANCE_FAIL","artifact_transport",f"HTTP {e.code}")
    if not loc: raise CriticError("CRITIC_PROVENANCE_FAIL","artifact_transport","missing redirect")
    req=urllib.request.Request(loc,headers={"Accept":"application/octet-stream","User-Agent":"dsir-m076-independent-critic-v0-1"})
    try:
        with urllib.request.urlopen(req,timeout=120) as r: return r.read()
    except Exception as e:
        raise CriticError("CRITIC_PROVENANCE_FAIL","artifact_storage",f"{type(e).__name__}: {e}")

def expected_keys():
    o={}
    for call in CALLS:
        for kind in ("mixed_target","direct_target"):
            for role in ("beta_plus","beta_minus"):
                o[f"{kind}__M076__{role}__call{call:03d}"]=(kind,role,call)
    return o
EXPECTED=expected_keys()

def validate_manifest_meta(m,key,kind,role,call):
    if m.get("kind")!=kind or m.get("selection")!="M076" or m.get("role")!=role or m.get("call_index")!=call:
        raise CriticError("CRITIC_PROVENANCE_FAIL","selected_binding",f"{key} identity")
    if kind=="direct_target" and m.get("direct_batch")!="D50":
        raise CriticError("CRITIC_PROVENANCE_FAIL","selected_binding",f"{key} D50")
    if m.get("z_u64hex")!=ZS[call] or m.get("target_u64hex_sha256")!=TARGET_SHA[call]:
        raise CriticError("CRITIC_PROVENANCE_FAIL","selected_binding",f"{key} target/z")
    if m.get("shape")!=[LENS[call]] or m.get("dtype")!="<f8" or m.get("byte_length")!=LENS[call]*8:
        raise CriticError("CRITIC_PROVENANCE_FAIL","selected_binding",f"{key} shape/dtype/bytes")
    if not isinstance(m.get("sha256"),str) or len(m["sha256"])!=64:
        raise CriticError("CRITIC_PROVENANCE_FAIL","selected_binding",f"{key} sha")

def source_recompute(outdir):
    import numpy as np
    validate_static_chain()
    token=os.environ.get("GITHUB_TOKEN",""); repo=os.environ.get("GITHUB_REPOSITORY",""); api=os.environ.get("GITHUB_API_URL","https://api.github.com").rstrip("/")
    if not token or not repo: raise CriticError("CRITIC_PROVENANCE_FAIL","runtime_environment","missing GitHub env")
    staged={}; records=[]; classes={ACTIVE:0,INACTIVE:0}; arms={"A":0,"B":0}
    for rep in REPLICATES:
        spec=LANE_ARTIFACTS[rep]
        meta=api_json(f"{api}/repos/{repo}/actions/artifacts/{spec['artifact_id']}",token)
        if int(meta.get("id",-1))!=spec["artifact_id"] or meta.get("name")!=spec["name"] or bool(meta.get("expired")) or normdig(meta.get("digest"))!=spec["sha256"]:
            raise CriticError("CRITIC_PROVENANCE_FAIL","artifact_metadata",rep)
        zb=download_zip(api,repo,token,spec["artifact_id"])
        if sha(zb)!=spec["sha256"]: raise CriticError("CRITIC_PROVENANCE_FAIL","artifact_transport",f"{rep} ZIP digest")
        with zipfile.ZipFile(io.BytesIO(zb)) as z:
            rb=z.read(f"receipt_{rep}.json"); wb=z.read(f"witness_{rep}.npz")
        r=json.loads(rb); sr=r.get("solver_receipt",{}); man=sr.get("witness_manifest",{})
        if r.get("replicate")!=rep or r.get("classification")!="LANE_PASS" or r.get("eligible") is not True:
            raise CriticError("CRITIC_PROVENANCE_FAIL","lane_receipt",rep)
        arm="A" if rep<="R16" else "B"; nc=r.get("native_class")
        if r.get("order_arm")!=arm or nc not in {ACTIVE,INACTIVE}: raise CriticError("CRITIC_PROVENANCE_FAIL","lane_population",rep)
        classes[nc]+=1; arms[arm]+=1
        if sha(wb)!=r.get("witness_npz_sha256") or sha(wb)!=sr.get("witness_npz_sha256") or csha(man)!=sr.get("witness_manifest_canonical_sha256"):
            raise CriticError("CRITIC_PROVENANCE_FAIL","witness_binding",rep)
        sel={k for k in man if k.startswith("mixed_target__M076__") or k.startswith("direct_target__M076__")}
        if sel!=set(EXPECTED): raise CriticError("CRITIC_PROVENANCE_FAIL","selected_key_set",rep)
        lane={"native_class":nc,"order_arm":arm,"mixed":{},"direct":{}}
        selected={}
        with np.load(io.BytesIO(wb),allow_pickle=False) as npz:
            for key,(kind,role,call) in EXPECTED.items():
                m=man[key]; validate_manifest_meta(m,key,kind,role,call)
                arr=np.ascontiguousarray(npz[key],dtype="<f8")
                if arr.dtype.str!="<f8" or list(arr.shape)!=[LENS[call]] or sha(arr.tobytes())!=m["sha256"]:
                    raise CriticError("CRITIC_PROVENANCE_FAIL","selected_payload",f"{rep}/{key}")
                (lane["mixed"] if kind=="mixed_target" else lane["direct"])[(role,call)]=arr.copy()
                selected[key]=m["sha256"]
        staged[rep]=lane
        records.append({"replicate":rep,"artifact_id":spec["artifact_id"],"artifact_name":spec["name"],"outer_zip_sha256":spec["sha256"],"receipt_sha256":sha(rb),"witness_npz_sha256":sha(wb),"manifest_sha256":sr.get("witness_manifest_canonical_sha256"),"native_class":nc,"order_arm":arm,"selected_array_sha256":selected})
    if classes!={ACTIVE:10,INACTIVE:22} or arms!={"A":16,"B":16} or len(records)!=32:
        raise CriticError("CRITIC_PROVENANCE_FAIL","population_totals",f"{classes}/{arms}")
    M=[]; D=[]
    for rep in REPLICATES:
        lm=[]; ld=[]; q=staged[rep]
        for call in CALLS:
            lm.append(np.abs((q["mixed"][("beta_plus",call)]-q["mixed"][("beta_minus",call)])/(2.0*H)))
            ld.append(np.abs((q["direct"][("beta_plus",call)]-q["direct"][("beta_minus",call)])/(2.0*H)))
        M.append(np.concatenate(lm)); D.append(np.concatenate(ld))
    M=np.ascontiguousarray(np.stack(M),dtype="<f8"); D=np.ascontiguousarray(np.stack(D),dtype="<f8")
    if M.shape!=(32,255) or D.shape!=(32,255): raise CriticError("CRITIC_INVALID_IMPLEMENTATION","response_shape",f"{M.shape}/{D.shape}")
    def rel(a,b):
        den=np.maximum(np.maximum(np.abs(a),np.abs(b)),np.finfo(np.float64).tiny); return np.abs(a-b)/den
    goodM=np.isfinite(M)&(M>0); goodD=np.isfinite(D)&(D>0); finite=bool(np.all(goodM)&np.all(goodD))
    smallest=None
    if not finite:
        classification="SCIENTIFIC_RESPONSE_ZERO_OR_NONFINITE"
        for ri,rep in enumerate(REPLICATES):
            for ei in range(255):
                if not goodM[ri,ei] or not goodD[ri,ei]:
                    call=76 if ei<127 else 78; idx=ei if ei<127 else ei-127
                    cons="mixed" if not goodM[ri,ei] else "direct"; val=M[ri,ei] if cons=="mixed" else D[ri,ei]
                    smallest={"failure_class":classification,"replicate":rep,"construction":cons,"call":call,"source_entry_index":idx,"value":float(val)}; break
            if smallest: break
    else:
        mm=0.0; dd=0.0
        for i,j in itertools.combinations(range(32),2):
            mm=max(mm,float(rel(M[i],M[j]).max())); dd=max(dd,float(rel(D[i],D[j]).max()))
        ai=[i for i,r in enumerate(REPLICATES) if staged[r]["native_class"]==ACTIVE]
        ii=[i for i,r in enumerate(REPLICATES) if staged[r]["native_class"]==INACTIVE]
        mn=float(rel(M[ai].mean(0),M[ii].mean(0)).max()); dn=float(rel(D[ai].mean(0),D[ii].mean(0)).max())
        om=float(rel(M[:16].mean(0),M[16:].mean(0)).max()); od=float(rel(D[:16].mean(0),D[16:].mean(0)).max())
        mdarr=rel(M,D); md=float(mdarr.max())
        if not all(x<TECH_TOL for x in (mm,dd,mn,dn)):
            classification="SCIENTIFIC_RESPONSE_REPRODUCIBILITY_FAIL"
        elif not md<SCI_TOL:
            classification="SCIENTIFIC_RESPONSE_CONSTRUCTION_MISMATCH"
            ri,ei=map(int,np.argwhere(mdarr>=SCI_TOL)[0]); call=76 if ei<127 else 78; idx=ei if ei<127 else ei-127
            smallest={"failure_class":classification,"replicate":REPLICATES[ri],"call":call,"source_entry_index":idx,"mixed_value":float(M[ri,ei]),"direct_value":float(D[ri,ei]),"relative_difference":float(mdarr[ri,ei])}
        else:
            classification="PASS_SCOPED_DES_M076_REMAINING_SENTINEL_RESPONSE_REPLICATION"
    if classification not in SCIENCE_TAXONOMY: raise CriticError("CRITIC_INVALID_IMPLEMENTATION","taxonomy",classification)
    metrics={
      "mixed_cross_host_max_pairwise_rel":None if not finite else mm,
      "direct_cross_host_max_pairwise_rel":None if not finite else dd,
      "mixed_native_class_mean_rel_separation":None if not finite else mn,
      "direct_native_class_mean_rel_separation":None if not finite else dn,
      "mixed_direct_response_max_rel":None if not finite else md,
      "execution_order_arm_mean_rel_separation_descriptive_mixed":None if not finite else om,
      "execution_order_arm_mean_rel_separation_descriptive_direct":None if not finite else od,
    }
    outdir=Path(outdir); outdir.mkdir(parents=True,exist_ok=True)
    writej(outdir/"independent_provenance.json",{"schema":"DSIR_M076_INDEPENDENT_CRITIC_PROVENANCE_V0_1","source_run_id":SOURCE_RUN_ID,"source_outer_digest_match_count":32,"selected_manifest_entries_verified":256,"native_class_counts":classes,"order_arm_counts":arms,"records":records})
    np.savez_compressed(outdir/"independent_response.npz",R_mixed=M,R_direct=D)
    result={"schema":"DSIR_M076_INDEPENDENT_CRITIC_RECOMPUTE_V0_1","classification":classification,"source_run_id":SOURCE_RUN_ID,"finite_positive_status":finite,"response_shape":[32,255],"atoms_per_construction":8160,"combined_atoms":16320,"mixed_response_min":float(np.min(M)) if np.all(np.isfinite(M)) else None,"mixed_response_max":float(np.max(M)) if np.all(np.isfinite(M)) else None,"direct_response_min":float(np.min(D)) if np.all(np.isfinite(D)) else None,"direct_response_max":float(np.max(D)) if np.all(np.isfinite(D)) else None,"metrics":metrics,"smallest_exact_counterexample":smallest,"independent_response_npz_sha256":sha((outdir/"independent_response.npz").read_bytes()),"independent_provenance_json_sha256":sha((outdir/"independent_provenance.json").read_bytes()),"producer_payload_read":False}
    writej(outdir/"independent_result.json",result)
    return 0

def compare(indir,metadata_freeze,outdir):
    import numpy as np
    validate_static_chain()
    indir=Path(indir); mf=Path(metadata_freeze); outdir=Path(outdir); outdir.mkdir(parents=True,exist_ok=True)
    # Consume independent evidence BEFORE producer metadata/artifact.
    iraw=(indir/"independent_result.json").read_bytes(); praw=(indir/"independent_provenance.json").read_bytes(); nraw=(indir/"independent_response.npz").read_bytes()
    independent=json.loads(iraw)
    if independent.get("producer_payload_read") is not False: raise CriticError("CRITIC_INVALID_IMPLEMENTATION","independence","independent phase read producer")
    if independent.get("classification") not in SCIENCE_TAXONOMY: raise CriticError("CRITIC_INVALID_IMPLEMENTATION","independent_taxonomy","bad classification")
    with np.load(io.BytesIO(nraw),allow_pickle=False) as z:
        im=np.ascontiguousarray(z["R_mixed"],dtype="<f8"); idr=np.ascontiguousarray(z["R_direct"],dtype="<f8")
    if im.shape!=(32,255) or idr.shape!=(32,255): raise CriticError("CRITIC_INVALID_IMPLEMENTATION","independent_shape","bad shape")

    if not mf.is_file(): raise CriticError("CRITIC_PROVENANCE_FAIL","metadata_freeze","missing freeze")
    freeze=json.loads(mf.read_text())
    if freeze.get("status")!="POST_EXECUTION_METADATA_FREEZE_BEFORE_SCIENTIFIC_PAYLOAD_CONSUMPTION": raise CriticError("CRITIC_PROVENANCE_FAIL","metadata_freeze","status")
    r=freeze.get("run",{})
    if r.get("run_id")!=PRODUCER_RUN_ID or r.get("run_number")!=1 or r.get("run_attempt")!=1 or r.get("head_sha")!=PRODUCER_HEAD or r.get("status")!="completed":
        raise CriticError("CRITIC_PROVENANCE_FAIL","metadata_freeze","run identity")
    art=freeze.get("artifact",{})
    aid=art.get("artifact_id"); expected=normdig(art.get("outer_digest"))
    if not isinstance(aid,int) or not isinstance(expected,str) or len(expected)!=64: raise CriticError("CRITIC_PROVENANCE_FAIL","metadata_freeze","artifact identity")

    token=os.environ.get("GITHUB_TOKEN",""); repo=os.environ.get("GITHUB_REPOSITORY",""); api=os.environ.get("GITHUB_API_URL","https://api.github.com").rstrip("/")
    if not token or not repo: raise CriticError("CRITIC_PROVENANCE_FAIL","runtime_environment","missing GitHub env")
    meta=api_json(f"{api}/repos/{repo}/actions/artifacts/{aid}",token)
    if int(meta.get("id",-1))!=aid or bool(meta.get("expired")) or normdig(meta.get("digest"))!=expected: raise CriticError("CRITIC_PROVENANCE_FAIL","producer_artifact_metadata","mismatch")
    zb=download_zip(api,repo,token,aid)
    if sha(zb)!=expected: raise CriticError("CRITIC_PROVENANCE_FAIL","producer_artifact_transport","digest mismatch")
    with zipfile.ZipFile(io.BytesIO(zb)) as z:
        members=sorted(n for n in z.namelist() if not n.endswith("/"))
        required={"result.json","provenance.json","response_evidence.npz","static_contract.json"}
        if set(members)!=required: raise CriticError("CRITIC_PROVENANCE_FAIL","producer_members",str(members))
        producer_result_raw=z.read("result.json"); producer_prov_raw=z.read("provenance.json"); producer_resp_raw=z.read("response_evidence.npz"); static_raw=z.read("static_contract.json")
    producer=json.loads(producer_result_raw); producer_prov=json.loads(producer_prov_raw)
    with np.load(io.BytesIO(producer_resp_raw),allow_pickle=False) as z:
        pm=np.ascontiguousarray(z["R_mixed"],dtype="<f8"); pd=np.ascontiguousarray(z["R_direct"],dtype="<f8")
    verdict="PASS_TERMINAL_CLOSURE"; reason=None
    if producer.get("classification")!=independent.get("classification"):
        verdict="CRITIC_INDEPENDENT_CLASSIFICATION_DISAGREEMENT"; reason="classification"
    elif producer.get("metrics")!=independent.get("metrics"):
        verdict="CRITIC_METRIC_DISAGREEMENT"; reason="metrics"
    elif producer.get("finite_positive_status")!=independent.get("finite_positive_status") or producer.get("smallest_exact_counterexample")!=independent.get("smallest_exact_counterexample"):
        verdict="CRITIC_METRIC_DISAGREEMENT"; reason="decision fields"
    elif pm.shape!=im.shape or pd.shape!=idr.shape or pm.tobytes()!=im.tobytes() or pd.tobytes()!=idr.tobytes():
        verdict="CRITIC_RESPONSE_EVIDENCE_DISAGREEMENT"; reason="response arrays"
    elif producer_prov.get("selected_array_bindings_verified")!=256 or producer_prov.get("exact_lane_count",32)!=32:
        verdict="CRITIC_PROVENANCE_FAIL"; reason="producer provenance summary"
    if verdict not in CRITIC_TAXONOMY: raise CriticError("CRITIC_INVALID_IMPLEMENTATION","critic_taxonomy",verdict)
    decision={"schema":"DSIR_M076_RUNTIME_CRITIC_DECISION_V0_1","verdict":verdict,"reason":reason,"independent_classification":independent.get("classification"),"producer_classification":producer.get("classification"),"classification_match":producer.get("classification")==independent.get("classification"),"metrics_exact_match":producer.get("metrics")==independent.get("metrics"),"response_bitwise_match_mixed":pm.shape==im.shape and pm.tobytes()==im.tobytes(),"response_bitwise_match_direct":pd.shape==idr.shape and pd.tobytes()==idr.tobytes(),"producer_artifact_id":aid,"producer_outer_sha256":expected,"producer_result_sha256":sha(producer_result_raw),"producer_provenance_sha256":sha(producer_prov_raw),"producer_response_npz_sha256":sha(producer_resp_raw),"producer_static_contract_sha256":sha(static_raw),"independent_result_sha256":sha(iraw),"independent_provenance_sha256":sha(praw),"independent_response_npz_sha256":sha(nraw),"full107_authorized":False,"covariance_authorized":False,"nuisance_authorized":False,"statistical_inference_authorized":False,"physical_inference_authorized":False}
    writej(outdir/"critic_decision.json",decision)
    return 0

def static_contract(out):
    validate_static_chain()
    checks={"producer_implementation_import_absent":True,"exact_calls":CALLS==[76,78],"exact_shapes":LENS=={76:127,78:128},"exact_256_bindings":len(EXPECTED)*32==256,"exact_h":H==1e-4,"exact_technical_threshold":TECH_TOL==1e-5,"exact_scientific_threshold":SCI_TOL==1e-3,"critic_verdict_taxonomy_exact":len(CRITIC_TAXONOMY)==6}
    writej(out,{"schema":"DSIR_M076_RUNTIME_CRITIC_STATIC_CONTRACT_V0_1","classification":"PASS_STATIC_CONTRACT","checks":checks,"source_science_read":False,"producer_science_read":False})
    return 0

def main():
    p=argparse.ArgumentParser(); p.add_argument("--mode",choices=["static-contract","recompute","compare"],required=True); p.add_argument("--out"); p.add_argument("--outdir"); p.add_argument("--independent-dir"); p.add_argument("--metadata-freeze"); a=p.parse_args()
    try:
        if a.mode=="static-contract": return static_contract(a.out)
        if a.mode=="recompute": return source_recompute(a.outdir)
        return compare(a.independent_dir,a.metadata_freeze,a.outdir)
    except CriticError as e:
        target=Path(a.outdir or "."); target.mkdir(parents=True,exist_ok=True)
        writej(target/"critic_error.json",{"schema":"DSIR_M076_RUNTIME_CRITIC_ERROR_V0_1","verdict":e.kind if e.kind in CRITIC_TAXONOMY else "CRITIC_INVALID_IMPLEMENTATION","stage":e.stage,"error":str(e)})
        return 0
    except Exception as e:
        target=Path(a.outdir or "."); target.mkdir(parents=True,exist_ok=True)
        writej(target/"critic_error.json",{"schema":"DSIR_M076_RUNTIME_CRITIC_ERROR_V0_1","verdict":"CRITIC_INVALID_IMPLEMENTATION","stage":"unexpected","error":f"{type(e).__name__}: {e}"})
        return 0
if __name__=="__main__": raise SystemExit(main())
