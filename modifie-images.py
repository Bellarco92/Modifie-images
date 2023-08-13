from PIL import Image
from glob import glob
from argparse import ArgumentParser


parser = ArgumentParser(description='Zamiana kolorowych jpgów na czarno-białe.')

parser.add_argument('--input', help='Folder, z którego pobieram obrazy', required=True)
parser.add_argument('--output', help='Folder, do którego zapiszę obrazy', required=True)
args = parser.parse_args()


for path in glob(args.input + '/*'):
    directory, filename = path.split('\\')
    print(path, directory, filename)

    with Image.open(path) as new_image:
        grayscale_image = new_image.convert('L')
        grayscale_image.save(args.output + '/' + filename)
