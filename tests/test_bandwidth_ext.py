import pytest
import av.bandwidth_ext as mod

CASES = [
    ("anti_alias_spectral_shift", (1,)),
    ("hf_envelope_smooth", (1,)),
    ("block_state_carry", (1,)),
    ("resampler_state_reset", (1,)),
    ("content_type_route", (1,)),
    ("denoise_order_contract", (1,)),
    ("load_narrowband", (1,)),
    ("estimate_bandwidth", (1,)),
    ("extend_highband", (1,)),
    ("present_bandwidth", (1,)),
    ("validate_bandwidth", (1,)),
    ("metrics_bandwidth", (1,)),
    ("audit_bandwidth", (1,)),
    ("fallback_bandwidth", (1,)),
    ("determinism_bandwidth", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
