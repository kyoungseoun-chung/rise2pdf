# rise2pdf

Simple python scrit to convert RISE script to pdf.

## Requirements

You need npm to download decktape.

## Install

```bash
	python3 -m pip install .
```

## Usage

This script requires two inputs.

	1. Output resolution (0000x0000 format)
	2. Name of your notebook without extension

Example:

```bash
	python -m rise2pdf 1920x1080 filename_of_your_notebook
```

To convert slides, you need token.
This script will detect token of your notebook using following command

```bash
	jupyter notebook list
```

Then take only top-most listed notebook as target.
Therefore, make sure you have only one active notebook in your local server or make your target slide at the top-most position in the list.
