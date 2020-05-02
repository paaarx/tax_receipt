from pathlib import Path

from tax_receipt.directory import Directory
from tax_receipt.exporter import Exporter
from tax_receipt.image_decoder import ImageDecoder


def main():
    base_path = Path(__file__).parents[0]
    path_in_image = (base_path / 'data/input/image').resolve()
    path_out_image = (base_path / 'data/output/image').resolve()
    path_out_file = (base_path / 'data/output/file').resolve()

    directory = Directory(path_in_image, path_out_image, path_out_file)

    decoder = ImageDecoder()
    exporter = Exporter()

    for image in directory.get_images():
        decoded_image, operation_id = decoder.decode_qr_code(image)
        if decoded_image:
            list_to_export = decoder.get_decoded_value(
                decoded_image, operation_id)
            if bool(list_to_export):
                exporter.write_csv(
                    directory.get_path_out_file, 'tax_receipt',
                    list_to_export)
        directory.move_decoded_image(image, operation_id)


if __name__ == "__main__":
    main()
