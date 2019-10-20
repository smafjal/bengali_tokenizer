import argparse

from trainer import Trainer
from tokenizer import BDTokenizer

parser = argparse.ArgumentParser(description='Bengali language tokenizer')

parser.add_argument('--data_dir', type=str, default='/home/smgo/Downloads/MLProHouse/sentencepiece_bn/data',
                    help='location of the data corpus')
parser.add_argument('--model_prefix', type=str, default='model/lm_model_bn', help='model name prefix')
parser.add_argument('--vocab', type=int, default=300, help='vocabulary size')
parser.add_argument('--model', type=str, default="model/lm_model_bn.model", help='Model path')

args = parser.parse_args()


def train_model(data_dir, model_prefix, vocab):
    bn_train = Trainer(data_dir=data_dir, model_prefix=model_prefix, vocab=vocab)
    bn_train.train()


def tokenize(text, model):
    if text is None or len(text) == 0:
        return []
    bn_tokenizer = BDTokenizer(model_path=model)
    return bn_tokenizer.tokenize(text=text)


def main(train=False):
    if train:
        train_model(args.data_dir, args.model_prefix, args.vocab)

    text = "বগুড়ায় জাতীয় লিগে দ্বিতীয় স্তরের ম্যাচে ঢাকা মেট্রোপলিসের হয়ে সেঞ্চুরি পেয়েছেন মাহমুদউল্লাহ।"

    tokens = tokenize(text, model=args.model)
    print("Tokens: ", tokens)


if __name__ == '__main__':
    main(train=False)
