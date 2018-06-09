In this directory I have files that generate the required dataset.

Steps to generate dataset

0. Create required folders with `mkdir -p dataset/{images,extract}`
1. Run `save-fonts.pde` in Proccessing3 IDE and copy the generated `dataset/images/` folder here.
  The files are named 1.png 2.png etc
2. Use an image viewer and manually pic the file number to delete that don't contain proper fonts.
  Write these in the `clean-dirty.py` file and run it.
3. Run `octave extract-to-csv.m` script to generate `x.csv` and `y.csv` files in `dataset/extract` folder.
4. Load the collected data and plot some images randomly with `python3 plot-random.py`
