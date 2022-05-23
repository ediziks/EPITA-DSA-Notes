"""Defines a bidirectional LSTM-CNNs-CRF as described in https://arxiv.org/abs/1603.01354."""

import tensorflow as tf
import opennmt as onmt

def model():
  return onmt.models.SequenceTagger(
      inputter=onmt.inputters.MixedInputter([
          onmt.inputters.WordEmbedder(
              embedding_size=50,
              trainable=True),
          onmt.inputters.CharConvEmbedder(
              embedding_size=50,
              num_outputs=30,
              kernel_size=3,
              stride=1,
              dropout=0.5)],
          dropout=0.5),
      encoder=onmt.encoders.RNNEncoder(
            num_layers=1,
            num_units=400,
            bidirectional=True,
            dropout=0.5,
            residual_connections=False,
            cell_class=tf.keras.layers.LSTMCell),
        crf_decoding=True)
