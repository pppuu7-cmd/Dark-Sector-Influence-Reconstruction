#!/usr/bin/env python3
from pathlib import Path
import sys

root = Path(sys.argv[1]).resolve()
pxd = root / "python/cclassy.pxd"
pyx = root / "python/classy.pyx"

p = pxd.read_text()
needle = """        int * k_size\n        int * ic_size\n        int index_md_scalars\n"""
replacement = """        int * k_size\n        int * ic_size\n        int index_md_scalars\n        int index_ic_ad\n        short has_source_delta_m\n        int index_tp_delta_m\n        double ** k\n"""
if needle not in p:
    raise SystemExit("cclassy.pxd perturbs anchor not found")
p = p.replace(needle, replacement, 1)

needle2 = """    int perturb_output_titles(void *pba, void *ppt,  file_format output_format, char titles[_MAXTITLESTRINGLENGTH_])\n\n"""
replacement2 = needle2 + """    int perturb_sources_at_tau(\n        void * ppt,\n        int index_md,\n        int index_ic,\n        int index_tp,\n        double tau,\n        double * psource)\n\n"""
if needle2 not in p:
    raise SystemExit("cclassy.pxd perturb function anchor not found")
p = p.replace(needle2, replacement2, 1)
pxd.write_text(p)

q = pyx.read_text()
anchor = """    def get_transfer(self, z=0., output_format='class'):\n"""
method = r'''    def get_delta_m_source(self, z=0.):
        """Read the already-computed native gauge-invariant total-matter source.

        Returns the scalar/adiabatic ``index_tp_delta_m`` source interpolated by
        CLASS at the requested conformal time.  This diagnostic is deliberately
        read-only: it never calls ``compute`` or any perturbation evolution
        routine and requires the perturbation module to have been initialized by
        the caller already.
        """
        cdef double tau
        cdef int index_md
        cdef int index_ic
        cdef int n
        cdef int i
        cdef np.ndarray[DTYPE_t, ndim=1] source
        cdef np.ndarray[DTYPE_t, ndim=1] kvals

        if "perturb" not in self.ncp:
            raise CosmoSevereError("get_delta_m_source requires precomputed perturbations")
        if not self.pt.has_scalars:
            raise CosmoSevereError("get_delta_m_source requires scalar perturbations")
        if not self.pt.has_source_delta_m:
            raise CosmoSevereError("native index_tp_delta_m source was not computed")

        if background_tau_of_z(&self.ba, <double> z, &tau) == _FAILURE_:
            raise CosmoSevereError(self.ba.error_message)

        index_md = self.pt.index_md_scalars
        index_ic = self.pt.index_ic_ad
        n = self.pt.k_size[index_md]
        if n <= 0:
            raise CosmoSevereError("empty native scalar k grid")

        source = np.zeros(n, dtype=np.double)
        kvals = np.zeros(n, dtype=np.double)

        if perturb_sources_at_tau(
                &self.pt,
                index_md,
                index_ic,
                self.pt.index_tp_delta_m,
                tau,
                <double*> source.data) == _FAILURE_:
            raise CosmoSevereError(self.pt.error_message)

        for i in range(n):
            kvals[i] = self.pt.k[index_md][i]

        return {"k (1/Mpc)": kvals, "D_m": source}

'''
if anchor not in q:
    raise SystemExit("classy.pyx get_transfer anchor not found")
q = q.replace(anchor, method + anchor, 1)
pyx.write_text(q)

print("patched", pxd)
print("patched", pyx)
