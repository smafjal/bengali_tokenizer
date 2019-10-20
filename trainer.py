import os
import pathlib
import sentencepiece as spm


class Trainer:
    def __init__(self, data_dir, model_prefix=None, vocab=300):
        self.data_dir = data_dir
        self.vocab = vocab
        self.model_prefix = model_prefix

    def get_all_files(self, _dir=None):
        if _dir is None:
            _dir = self.data_dir
        pathlist = pathlib.Path(_dir).glob("./*")
        files = [str(x) for x in pathlist if x.is_file()]
        return files

    def train(self):
        if not self.data_dir:
            raise Exception("Data dir not found")

        files = self.get_all_files(self.data_dir)
        if len(files) == 0:
            raise Exception("Not found any files in {}".format(self.data_dir))
        files = ','.join(files)

        model_prefix = "model/lm_model_bn"
        if self.model_prefix:
            model_prefix = self.model_prefix

        _dir = "/".join(model_prefix.split("/")[:-1])
        if not os.path.exists(_dir):
            os.makedirs(_dir)
        params = "--input={} --model_prefix={} --vocab_size={}".format(
            files, model_prefix, self.vocab)

        print("train params: {}".format(params))
        spm.SentencePieceTrainer.Train(params)
