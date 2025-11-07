from neurosdk.safety import cbc_envelope
print("Safe?", cbc_envelope((0.0, 0.0), ((-1,1),(-1,1))))
print("Unsafe?", cbc_envelope((2.0, 0.0), ((-1,1),(-1,1))))