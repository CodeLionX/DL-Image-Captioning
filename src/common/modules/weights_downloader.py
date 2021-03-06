import urllib.request
import os


# default_data_dir = <project_root>/data
# resnet models: = <project_root>/data/models/resnet/<weights_file>.h5
DEFAULT_DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, os.path.pardir, "data"))


def download_ResNet152_weights_tf(data_dir=DEFAULT_DATA_DIR):
    tf_url = "https://owncloud.hpi.de/index.php/s/sY9WxAf43XRHrjf/download"
    filename = "resnet152_weights_tf.h5"
    file_path = os.path.join(data_dir, "models", "resnet")

    _download_if_not_exist(tf_url, file_path, filename)
    return os.path.join(file_path, filename)


def download_ResNet152_weights_th(data_dir=DEFAULT_DATA_DIR):
    raise NotImplementedError("this backend is currently not supported! Please add link to weights file and remove this error.")
    th_url = "???"
    filename = "resnet152_weights_th.h5"
    file_path = os.path.join(data_dir, "models", "resnet")

    _download_if_not_exist(th_url, file_path, filename)
    return os.path.join(file_path, filename)


def _download_if_not_exist(url, path, name):
    try:
        os.makedirs(path)
    except OSError:
        pass
    file_path = os.path.join(path, name)

    if os.path.isfile(file_path):
        print("{} does already exist, skipping download".format(file_path))
        return

    else:
        print("downloading resnet-152 model weights to {}".format(file_path))
        urllib.request.urlretrieve(url, file_path)
