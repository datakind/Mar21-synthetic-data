"""
Running the SDV basic tutorial using their example dataset.
"""
from sdv import load_demo
from sdv import SDV

# Grab the demo data
metadata, tables = load_demo(metadata=True)
print(metadata)

# Run the basic fit
sdv = SDV()
sdv.fit(metadata, tables)
print("done fit")
sdv.save('sdv.pkl')


