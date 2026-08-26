from tree import deserialize, drawtree, serialize

serial = "[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]"
root = deserialize(serial)
drawtree(root)
round_trip = serialize(root)
print(serial)
print(round_trip)
