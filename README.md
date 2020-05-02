# Brazilian Tax Receipt Reader

Read a QR Code from a picture of the brazilian tax receipt.

**Warning:** This only works for BRAZILIAN tax receipt!

## Getting Started

These instructions will guide you to copy the project and running on your local machine.

### Prerequisites

[Python 3.8.1](https://www.python.org/downloads/release/python-381/) or higher must be installed.

### Installing

* Download the project "tax_receipt".
* Install the libraries, use [requirements.txt](requirements.txt) for automatic installation:

```
pip install -r requirements.txt
```

## How to Use
* Put a tax receipt in input folder (```path_in_image```).
* Run the program (```python tax_receipt\tax_receipt.py```).

Obs: You can try the project with files from [sample](sample) folder. This folder contains 3 files, 2 tax receipts ([sample 1](sample/tax_receipt_1.jpg) and [sample 2](sample/tax_receipt_2.jpg)) and 1 similar to tax receipt ([sample 3](sample/not_a_tax_receipt_1.jpeg)).

## How It Works
* Read a picture of the brazilian tax receipt from input folder (```path_in_image```).
* Generate a unique identifier (uuid4) for the operation.
* Try to read QR Code:
    * Success: Write the uuid and information extracted from QR Code in tax_receipt.csv - a text file semicolon separated - on output directory (```path_out_image```).
    * Fail: Do not write the uuid in a CSV file on output directory (```path_out_image```).
* When the process end, it renames the picture with uuid and move to output directory (```path_out_file```).

## Versioning

The project use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/paaarx/tax_receipt/releases).

## Authors

* **Leonardo Cezar** - *Initial work* - [paaarx](https://github.com/paaarx)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Roadmap

* Improve validation from QR Code values
* Let the input and output folders be defined in a Yaml file.
* Create more types of "writers" (default is csv), as json or database.

## Additional Info

* Initially, it was my first idea for the [Dev For a Change](https://dev4change.devpost.com/) hackathon, when donors send pictures of the tax receipt via Whatsapp or Facebook Messenger, this solution automates the extraction of information from the tax receipt to fill out the forms and send it to the government. Unfortunately it was discarded.

## Donations

Toss a coin to your Witcher.

* [Paypal](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=B7T59X8WJ8CWY&currency_code=BRL&source=url)