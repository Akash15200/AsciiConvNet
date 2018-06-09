In this folder there is a dataset loader and AsciiConvNet implementation.

Symlink dataset as `ln -s ../01-data-collection/dataset dataset`

Run `python3 learner.py`, this creates a `models/model.ckpt` file
Run `python3 predict.py` that loads this models and prints prediction accuracy.
