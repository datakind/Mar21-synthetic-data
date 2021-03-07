# SDV Exploration

This is where all of our SDV code exploration lives! For more 
thoughts on SDV from an analytic perspective, take a look at [this google doc
from Marc](https://docs.google.com/document/d/1I2gIh3zma7Joci5y9d6d0ET-eMQdQrRJ7-t0mL96R1U/edit).

There's a small `.py` file up for folks who want to try running a basic sdv script with
their demo data. For a look at our covid dataset, look at the `ipynb` file -- in that file,
we load the data, grab the first 10000 entries as a sample, and generate a new set of synthetic data.

Note that to run the `ipynb`, you need to download the [covid dataset] and update the dataset path variable to wherever you've downloaded it to.

The first round of synthetic generation uses all default settings and no constraints. That means issues like
not properly connecting city, state and province fields together -- a second round of data generation adds that in as
a constrain to improve the generated data quality.

### SDV Pros
SDV seems like a good option because:
 - you can manually add constraints
 - it's open source so you can get into the implementation details if needed
 - the user interface is relatively friendly
 - the documentation is decent

### SDV Cons
SDV has some issues we'd need to dig into:
 - especially when you add constraints, I'm concerned that run time is getting too slow too quickly
 - it's unclear if the constraints available will give us all the control we want

### SDV Open Questions
Things to tackle in the future:
 - How does imputing the data affect how SDV models it?
 - There are a few different model approaches under the hood as options. Which should we use?
 - Is SDV too slow to be feasible if you have too much data or too many constraints? How does it compare speed-wise to other options?
 - SDV offers an "evaluation metric" that I haven't read enough about to know if it's useful to us. What does it measure, do we want to use it?
