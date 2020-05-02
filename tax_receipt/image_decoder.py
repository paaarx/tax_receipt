import uuid

from PIL import Image
from pyzbar.pyzbar import ZBarSymbol
from pyzbar.pyzbar import decode


class ImageDecoder:

    def decode_qr_code(self, image_file):
        operation_id = str(uuid.uuid4()).replace('-', '_')
        try:
            return decode(Image.open(image_file),
                          symbols=[ZBarSymbol.QRCODE]), operation_id
        except IOError:
            print('Error when trying to open the image file.')
            return None, operation_id

    def get_decoded_value(self, decoded_image, operation_id):
        qr_code_value = {'uuid': operation_id}
        try:
            for decoded in decoded_image:
                if decoded.type == 'QRCODE':
                    decoded_ascii = decoded.data.decode('ascii').split('|')
                    qr_code_value['chaveConsulta'] = int(
                        decoded_ascii[0].strip())
                    qr_code_value['timeStamp'] = int(decoded_ascii[1].strip())
                    qr_code_value['valorTotal'] = float(
                        decoded_ascii[2].strip())
                    if decoded_ascii[3]:
                        qr_code_value['CPFCNPJValue'] = int(
                            decoded_ascii[3].strip())
                    else:
                        qr_code_value['CPFCNPJValue'] = None
                    qr_code_value['assinaturaQRCODE'] = decoded_ascii[4].strip()
                    qr_code_value['QRCODEPolygon'] = decoded.polygon
                    qr_code_value['QRCODERectangle'] = decoded.rect
            if bool(qr_code_value):
                if self.qr_code_validator(qr_code_value):
                    return qr_code_value
            else:
                print('The QR Code is not from Tax Receipt or is corrupted.')
        except IOError:
            print('The QR Code is not from Tax Receipt or is corrupted.')

    def qr_code_validator(self, qr_code_value):
        if type(qr_code_value['chaveConsulta']) is not int:
            print('chaveConsulta value in QR Code is wrong.')
            return False
        elif type(qr_code_value['timeStamp']) is not int:
            print('timeStamp value in QR Code is wrong.')
            return False
        elif type(qr_code_value['valorTotal']) is not float:
            print('valorTotal value in QR Code is wrong.')
            return False
        elif type(qr_code_value['CPFCNPJValue']) is not int and \
                qr_code_value['CPFCNPJValue'] is not None:
            print('CPFCNPJValue value in QR Code is wrong.')
            return False
        elif type(qr_code_value['assinaturaQRCODE']) is not str:
            print('assinaturaQRCODE value in QR Code is wrong.')
            return False
        else:
            return True
