import sentencepiece as spm


class BDTokenizer:
    def __init__(self, model_path="model/lm_model_bn.model"):
        self.sp = spm.SentencePieceProcessor()
        self.sp.load(model_path)

    def tokenize(self, text):
        return self.sp.EncodeAsPieces(text)
