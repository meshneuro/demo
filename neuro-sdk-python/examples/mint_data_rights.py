from neurosdk.data_rights import mint_doc, mint_plid, mint_ndatar_lot

doc = mint_doc("did:robot:emu001", "did:op:alpha", {"vision": True, "tactile": True}, "home:vienna")
plid = mint_plid(["abc", "def", "ghi"])
lot = mint_ndatar_lot(doc, plid, royalty_curve={"base": 0.02, "max": 0.05})
print(doc)
print(plid)
print(lot)