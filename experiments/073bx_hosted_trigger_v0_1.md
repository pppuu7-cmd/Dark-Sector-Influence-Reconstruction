# Exp073BX trigger v0.1

Run the preregistered remote checkpoint failover QA. Home self-hosted runner writes three validated band checkpoints to `checkpoints/exp073bx-v0-1`, printing live percent/elapsed/ETA. A separate GitHub-hosted runner must then restore the remote branch and validate all canonical `<f8` bytes and SHA values without access to the home machine filesystem. Infrastructure QA only; `+0/+0`.

Prereg commit: `5cee2e0d8ec4cc5a3e9649e7bfaa9cedce39f2b7`.
Checkpoint utility commit: `0b0324afb69acb16cbea97bb924b9be48f303dde`.
Sync helper commit: `96886916b41dce7f0a40807622928c841ef5fc58`.
Driver commit: `15809928dbeea082c0bb6921d581085a89ea6e45`.
Workflow creation commit: `f781f72ed61a9c8c25e5225a8b4d64b5a96e099a`.
