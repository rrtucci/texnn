texnn (pronounced like "Texan") is a Python script that generates LaTex (tex)
code that draws a Neural Net (nn) as a causal DAG (Bayesian Network).

texnn is capable of reproducing with ease most of the xy-pic generated bnets 
(Bayesian Networks) displayed in my book [Bayesuvius](https://github.com/rrtucci/Bayesuvius).

texnn is a stand-alone app. I wrote it specifically to aid me in writing a 
chapter on transformer architectures (see directory "vanilla_transformer") 
for my free, open source book Bayesuvius. But I soon realized that it could 
be easily converted into a general tool that is independent of the transformer 
topic and of Bayesuvius.

texnn uses the LaTex package xy-pic for drawing. 
In broad terms, texnn can 
be described as a 
Python 
wrapper for the LaTeX package xy-pic.

Gallery:

* [Silly Bnet](https://github.com/rrtucci/texnn/blob/master/silly_bnet/silly-bnet.pdf)

* [Asia](https://github.com/rrtucci/texnn/blob/master/asia/asia.pdf)

* [Expert Archer](https://github.com/rrtucci/texnn/blob/master/expert_archer/expert-archer.pdf)

* Vanilla Transformer
  * [Scaled dot product attention](https://github.com/rrtucci/texnn/blob/master/vanilla_transformer/scaled-dot-prod-att.pdf)
  * [Multi-head Attention](https://github.com/rrtucci/texnn/blob/master/vanilla_transformer/multi-head-att.pdf)
  * [Encoder](https://github.com/rrtucci/texnn/blob/master/vanilla_transformer/encoder.pdf)
  * [Decoder](https://github.com/rrtucci/texnn/blob/master/vanilla_transformer/decoder.pdf)