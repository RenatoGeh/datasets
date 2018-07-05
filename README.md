# Datasets: a collection of datasets

**List of datasets:**
- Caltech-101 (subdataset containing only bikes, cars and faces)
- Digits (simple handwritten digits dataset with binary values)
- DigitsX (variation of Digits with multivalued pixels and slight gaussian blur)
- Four-by-four (artificial dataset for testing)
- Olivetti (AT&T Bell Labs faces dataset)
- Olivetti 3-bit (Olivetti dataset downscaled to 3-bit resolution)
- Olivetti Big (AT&T Bell Labs faces with original size)
- Olivetti Padded Uniform (Olivetti dataset with padded left and right borders so that width and height are divisible by four; paddings pixel values are uniformly distributed)
- Olivetti Small (Olivetti dataset smaller size)
- MNIST

Most datasets have their original images split into its categories by a
folder with its name indicating its class.

A compiled [GoSPN](https://github.com/RenatoGeh/gospn) dataset file in `.data` format is included
in every dataset for use in GoSPN.

For MNIST, we use [GoMNIST](https://github.com/petar/GoMNIST) to parse
the dataset. We select only a portion of MNIST such that the selected
digits are uniformly distributed between 0 and 9.

